# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._utils.serialization import Deserializer, Serializer
from ...operations._scope_access_review_instance_operations import (
    build_apply_decisions_request,
    build_record_all_decisions_request,
    build_reset_decisions_request,
    build_send_reminders_request,
    build_stop_request,
)
from .._configuration import AuthorizationManagementClientConfiguration

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ScopeAccessReviewInstanceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.aio.AuthorizationManagementClient`'s
        :attr:`scope_access_review_instance` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: AuthorizationManagementClientConfiguration = (
            input_args.pop(0) if input_args else kwargs.pop("config")
        )
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def stop(self, scope: str, schedule_definition_id: str, id: str, **kwargs: Any) -> None:
        """An action to stop an access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_stop_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def record_all_decisions(
        self,
        scope: str,
        schedule_definition_id: str,
        id: str,
        properties: _models.RecordAllDecisionsProperties,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """An action to approve/deny all decisions for a review with certain filters.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param properties: Record all decisions payload. Required.
        :type properties: ~azure.mgmt.authorization.models.RecordAllDecisionsProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def record_all_decisions(
        self,
        scope: str,
        schedule_definition_id: str,
        id: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """An action to approve/deny all decisions for a review with certain filters.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param properties: Record all decisions payload. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def record_all_decisions(
        self,
        scope: str,
        schedule_definition_id: str,
        id: str,
        properties: Union[_models.RecordAllDecisionsProperties, IO[bytes]],
        **kwargs: Any
    ) -> None:
        """An action to approve/deny all decisions for a review with certain filters.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :param properties: Record all decisions payload. Is either a RecordAllDecisionsProperties type
         or a IO[bytes] type. Required.
        :type properties: ~azure.mgmt.authorization.models.RecordAllDecisionsProperties or IO[bytes]
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "RecordAllDecisionsProperties")

        _request = build_record_all_decisions_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def reset_decisions(self, scope: str, schedule_definition_id: str, id: str, **kwargs: Any) -> None:
        """An action to reset all decisions for an access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_reset_decisions_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def apply_decisions(self, scope: str, schedule_definition_id: str, id: str, **kwargs: Any) -> None:
        """An action to apply all decisions for an access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_apply_decisions_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def send_reminders(self, scope: str, schedule_definition_id: str, id: str, **kwargs: Any) -> None:
        """An action to send reminders for an access review instance.

        :param scope: The scope of the resource. Required.
        :type scope: str
        :param schedule_definition_id: The id of the access review schedule definition. Required.
        :type schedule_definition_id: str
        :param id: The id of the access review instance. Required.
        :type id: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-12-01-preview"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_send_reminders_request(
            scope=scope,
            schedule_definition_id=schedule_definition_id,
            id=id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorDefinition, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
