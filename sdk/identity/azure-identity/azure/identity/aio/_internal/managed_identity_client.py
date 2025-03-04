# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import time
from typing import TypeVar

from azure.core.credentials import AccessTokenInfo
from azure.core.pipeline import AsyncPipeline
from .._internal import AsyncContextManager
from ..._internal import _scopes_to_resource
from ..._internal.managed_identity_client import ManagedIdentityClientBase
from ..._internal.pipeline import build_async_pipeline

T = TypeVar("T", bound="AsyncManagedIdentityClient")


# pylint:disable=async-client-bad-name
class AsyncManagedIdentityClient(AsyncContextManager, ManagedIdentityClientBase):
    async def __aenter__(self: T) -> T:
        await self._pipeline.__aenter__()
        return self

    async def close(self) -> None:
        await self._pipeline.__aexit__()

    async def request_token(self, *scopes: str, **kwargs) -> AccessTokenInfo:
        # pylint:disable=invalid-overridden-method
        resource = _scopes_to_resource(*scopes)
        request = self._request_factory(resource, self._identity_config)
        kwargs.pop("tenant_id", None)
        kwargs.pop("claims", None)
        request_time = int(time.time())
        response = await self._pipeline.run(request, retry_on_methods=[request.method], **kwargs)
        token = self._process_response(response, request_time)
        return token

    def _build_pipeline(self, **kwargs) -> AsyncPipeline:
        return build_async_pipeline(**kwargs)
