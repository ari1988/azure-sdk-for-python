# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import asyncio  # pylint: disable=do-not-import-asyncio
import sys
from typing import Any, cast, List, Optional
from azure.core.credentials import AccessToken, AccessTokenInfo, TokenRequestOptions

from .._internal import AsyncContextManager
from .._internal.decorators import log_get_token_async
from ... import CredentialUnavailableError
from ..._credentials.azure_powershell import (
    AzurePowerShellCredential as _SyncCredential,
    get_command_line,
    get_safe_working_dir,
    raise_for_error,
    parse_token,
)
from ..._internal import resolve_tenant, validate_tenant_id, validate_scope


class AzurePowerShellCredential(AsyncContextManager):
    """Authenticates by requesting a token from Azure PowerShell.

    This requires previously logging in to Azure via "Connect-AzAccount", and will use the currently logged in identity.

    :keyword str tenant_id: Optional tenant to include in the token request.
    :keyword List[str] additionally_allowed_tenants: Specifies tenants in addition to the specified "tenant_id"
        for which the credential may acquire tokens. Add the wildcard value "*" to allow the credential to
        acquire tokens for any tenant the application can access.
    :keyword int process_timeout: Seconds to wait for the Azure PowerShell process to respond. Defaults to 10 seconds.

    .. admonition:: Example:

        .. literalinclude:: ../samples/credential_creation_code_snippets.py
            :start-after: [START create_azure_power_shell_credential_async]
            :end-before: [END create_azure_power_shell_credential_async]
            :language: python
            :dedent: 4
            :caption: Create an AzurePowerShellCredential.
    """

    def __init__(
        self,
        *,
        tenant_id: str = "",
        additionally_allowed_tenants: Optional[List[str]] = None,
        process_timeout: int = 10,
    ) -> None:
        if tenant_id:
            validate_tenant_id(tenant_id)
        self.tenant_id = tenant_id
        self._additionally_allowed_tenants = additionally_allowed_tenants or []
        self._process_timeout = process_timeout

    @log_get_token_async
    async def get_token(
        self,
        *scopes: str,
        claims: Optional[str] = None,  # pylint:disable=unused-argument
        tenant_id: Optional[str] = None,
        **kwargs: Any,
    ) -> AccessToken:
        """Request an access token for `scopes`.

        This method is called automatically by Azure SDK clients. Applications calling this method directly must
        also handle token caching because this credential doesn't cache the tokens it acquires.

        :param str scopes: desired scope for the access token. This credential allows only one scope per request.
            For more information about scopes, see
            https://learn.microsoft.com/entra/identity-platform/scopes-oidc.
        :keyword str claims: not used by this credential; any value provided will be ignored.
        :keyword str tenant_id: optional tenant to include in the token request.

        :return: An access token with the desired scopes.
        :rtype: ~azure.core.credentials.AccessToken
        :raises ~azure.identity.CredentialUnavailableError: the credential was unable to invoke Azure PowerShell, or
          no account is authenticated
        :raises ~azure.core.exceptions.ClientAuthenticationError: the credential invoked Azure PowerShell but didn't
          receive an access token
        """
        # only ProactorEventLoop supports subprocesses on Windows (and it isn't the default loop on Python < 3.8)
        if sys.platform.startswith("win") and not isinstance(asyncio.get_event_loop(), asyncio.ProactorEventLoop):
            return _SyncCredential().get_token(*scopes, tenant_id=tenant_id, **kwargs)

        options: TokenRequestOptions = {}
        if tenant_id:
            options["tenant_id"] = tenant_id

        token_info = await self._get_token_base(*scopes, options=options, **kwargs)
        return AccessToken(token_info.token, token_info.expires_on)

    @log_get_token_async
    async def get_token_info(self, *scopes: str, options: Optional[TokenRequestOptions] = None) -> AccessTokenInfo:
        """Request an access token for `scopes`.

        This is an alternative to `get_token` to enable certain scenarios that require additional properties
        on the token. This method is called automatically by Azure SDK clients. Applications calling this method
        directly must also handle token caching because this credential doesn't cache the tokens it acquires.

        :param str scopes: desired scopes for the access token. TThis credential allows only one scope per request.
            For more information about scopes, see https://learn.microsoft.com/entra/identity-platform/scopes-oidc.
        :keyword options: A dictionary of options for the token request. Unknown options will be ignored. Optional.
        :paramtype options: ~azure.core.credentials.TokenRequestOptions

        :rtype: ~azure.core.credentials.AccessTokenInfo
        :return: An AccessTokenInfo instance containing information about the token.

        :raises ~azure.identity.CredentialUnavailableError: the credential was unable to invoke Azure PowerShell, or
          no account is authenticated
        :raises ~azure.core.exceptions.ClientAuthenticationError: the credential invoked Azure PowerShell but didn't
          receive an access token
        """
        if sys.platform.startswith("win") and not isinstance(asyncio.get_event_loop(), asyncio.ProactorEventLoop):
            return _SyncCredential().get_token_info(*scopes, options=options)
        return await self._get_token_base(*scopes, options=options)

    async def _get_token_base(
        self, *scopes: str, options: Optional[TokenRequestOptions] = None, **kwargs: Any
    ) -> AccessTokenInfo:
        tenant_id = options.get("tenant_id") if options else None
        if tenant_id:
            validate_tenant_id(tenant_id)
        for scope in scopes:
            validate_scope(scope)

        tenant_id = resolve_tenant(
            default_tenant=self.tenant_id,
            tenant_id=tenant_id,
            additionally_allowed_tenants=self._additionally_allowed_tenants,
            **kwargs,
        )
        command_line = get_command_line(scopes, tenant_id)
        output = await run_command_line(command_line, self._process_timeout)
        token = parse_token(output)
        return token

    async def close(self) -> None:
        """Calling this method is unnecessary"""


async def run_command_line(command_line: List[str], timeout: int) -> str:
    try:
        proc = await start_process(command_line)
        stdout, stderr = await asyncio.wait_for(proc.communicate(), 10)
        if sys.platform.startswith("win") and (b"' is not recognized" in stderr or proc.returncode == 9009):
            # pwsh.exe isn't on the path; try powershell.exe
            command_line[-1] = command_line[-1].replace("pwsh", "powershell", 1)
            proc = await start_process(command_line)
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout)

    except asyncio.TimeoutError as ex:
        proc.kill()
        raise CredentialUnavailableError(
            message="Timed out waiting for Azure PowerShell.\n"
            "To mitigate this issue, please refer to the troubleshooting guidelines here at "
            "https://aka.ms/azsdk/python/identity/powershellcredential/troubleshoot."
        ) from ex
    except OSError as ex:
        # failed to execute "cmd" or "/bin/sh"; Azure PowerShell may or may not be installed
        error = CredentialUnavailableError(
            message='Failed to execute "{}".\n'
            "To mitigate this issue, please refer to the troubleshooting guidelines here at "
            "https://aka.ms/azsdk/python/identity/powershellcredential/troubleshoot.".format(command_line[0])
        )
        raise error from ex

    decoded_stdout = stdout.decode()

    # casting because mypy infers Optional[int]; however, when proc.returncode is None,
    # we handled TimeoutError above and therefore don't execute this line
    raise_for_error(cast(int, proc.returncode), decoded_stdout, stderr.decode())
    return decoded_stdout


async def start_process(command_line):
    working_directory = get_safe_working_dir()
    proc = await asyncio.create_subprocess_exec(
        *command_line,
        cwd=working_directory,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.DEVNULL,
    )
    return proc
