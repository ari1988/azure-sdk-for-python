# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING

from .._utils import serialization as _serialization

if TYPE_CHECKING:
    from .. import models as _models


class ChangeAttributes(_serialization.Model):
    """Details about the change resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar correlation_id: The ARM correlation ID of the change resource.
    :vartype correlation_id: str
    :ivar timestamp: The time the change(s) on the target resource ocurred.
    :vartype timestamp: str
    :ivar changes_count: The number of changes this resource captures.
    :vartype changes_count: int
    :ivar previous_resource_snapshot_id: The GUID of the previous snapshot.
    :vartype previous_resource_snapshot_id: str
    :ivar new_resource_snapshot_id: The GUID of the new snapshot.
    :vartype new_resource_snapshot_id: str
    """

    _validation = {
        "correlation_id": {"readonly": True},
        "timestamp": {"readonly": True},
        "changes_count": {"readonly": True},
        "previous_resource_snapshot_id": {"readonly": True},
        "new_resource_snapshot_id": {"readonly": True},
    }

    _attribute_map = {
        "correlation_id": {"key": "correlationId", "type": "str"},
        "timestamp": {"key": "timestamp", "type": "str"},
        "changes_count": {"key": "changesCount", "type": "int"},
        "previous_resource_snapshot_id": {"key": "previousResourceSnapshotId", "type": "str"},
        "new_resource_snapshot_id": {"key": "newResourceSnapshotId", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.correlation_id: Optional[str] = None
        self.timestamp: Optional[str] = None
        self.changes_count: Optional[int] = None
        self.previous_resource_snapshot_id: Optional[str] = None
        self.new_resource_snapshot_id: Optional[str] = None


class ChangeBase(_serialization.Model):
    """An individual change on the target resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar property_change_type: The type of change that occurred. Known values are: "Update",
     "Insert", and "Remove".
    :vartype property_change_type: str or ~azure.mgmt.resource.changes.models.PropertyChangeType
    :ivar change_category: The entity that made the change. Known values are: "User" and "System".
    :vartype change_category: str or ~azure.mgmt.resource.changes.models.ChangeCategory
    :ivar previous_value: The target resource property value before the change.
    :vartype previous_value: str
    :ivar new_value: The target resource property value after the change.
    :vartype new_value: str
    """

    _validation = {
        "property_change_type": {"readonly": True},
        "change_category": {"readonly": True},
        "previous_value": {"readonly": True},
        "new_value": {"readonly": True},
    }

    _attribute_map = {
        "property_change_type": {"key": "propertyChangeType", "type": "str"},
        "change_category": {"key": "changeCategory", "type": "str"},
        "previous_value": {"key": "previousValue", "type": "str"},
        "new_value": {"key": "newValue", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.property_change_type: Optional[Union[str, "_models.PropertyChangeType"]] = None
        self.change_category: Optional[Union[str, "_models.ChangeCategory"]] = None
        self.previous_value: Optional[str] = None
        self.new_value: Optional[str] = None


class ChangeProperties(_serialization.Model):
    """The properties of a change.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar target_resource_id: The fully qualified ID of the target resource that was changed.
    :vartype target_resource_id: str
    :ivar target_resource_type: The namespace and type of the resource.
    :vartype target_resource_type: str
    :ivar change_type: The type of change that was captured in the resource. Known values are:
     "Update", "Delete", and "Create".
    :vartype change_type: str or ~azure.mgmt.resource.changes.models.ChangeType
    :ivar change_attributes: Details about the change resource.
    :vartype change_attributes: ~azure.mgmt.resource.changes.models.ChangeAttributes
    :ivar changes: A dictionary with changed property name as a key and the change details as the
     value.
    :vartype changes: dict[str, ~azure.mgmt.resource.changes.models.ChangeBase]
    """

    _validation = {
        "target_resource_id": {"readonly": True},
        "target_resource_type": {"readonly": True},
        "change_type": {"readonly": True},
    }

    _attribute_map = {
        "target_resource_id": {"key": "targetResourceId", "type": "str"},
        "target_resource_type": {"key": "targetResourceType", "type": "str"},
        "change_type": {"key": "changeType", "type": "str"},
        "change_attributes": {"key": "changeAttributes", "type": "ChangeAttributes"},
        "changes": {"key": "changes", "type": "{ChangeBase}"},
    }

    def __init__(
        self,
        *,
        change_attributes: Optional["_models.ChangeAttributes"] = None,
        changes: Optional[Dict[str, "_models.ChangeBase"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword change_attributes: Details about the change resource.
        :paramtype change_attributes: ~azure.mgmt.resource.changes.models.ChangeAttributes
        :keyword changes: A dictionary with changed property name as a key and the change details as
         the value.
        :paramtype changes: dict[str, ~azure.mgmt.resource.changes.models.ChangeBase]
        """
        super().__init__(**kwargs)
        self.target_resource_id: Optional[str] = None
        self.target_resource_type: Optional[str] = None
        self.change_type: Optional[Union[str, "_models.ChangeType"]] = None
        self.change_attributes = change_attributes
        self.changes = changes


class ChangeResourceListResult(_serialization.Model):
    """The list of resources.

    :ivar next_link: The link used to get the next page of Change Resources.
    :vartype next_link: str
    :ivar value: The list of resources.
    :vartype value: list[~azure.mgmt.resource.changes.models.ChangeResourceResult]
    """

    _attribute_map = {
        "next_link": {"key": "nextLink", "type": "str"},
        "value": {"key": "value", "type": "[ChangeResourceResult]"},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        value: Optional[List["_models.ChangeResourceResult"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword next_link: The link used to get the next page of Change Resources.
        :paramtype next_link: str
        :keyword value: The list of resources.
        :paramtype value: list[~azure.mgmt.resource.changes.models.ChangeResourceResult]
        """
        super().__init__(**kwargs)
        self.next_link = next_link
        self.value = value


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id: Optional[str] = None
        self.name: Optional[str] = None
        self.type: Optional[str] = None


class ChangeResourceResult(Resource):
    """Change Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar properties: The properties of a change.
    :vartype properties: ~azure.mgmt.resource.changes.models.ChangeProperties
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "properties": {"key": "properties", "type": "ChangeProperties"},
    }

    def __init__(self, *, properties: Optional["_models.ChangeProperties"] = None, **kwargs: Any) -> None:
        """
        :keyword properties: The properties of a change.
        :paramtype properties: ~azure.mgmt.resource.changes.models.ChangeProperties
        """
        super().__init__(**kwargs)
        self.properties = properties


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type: Optional[str] = None
        self.info: Optional[JSON] = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.resource.changes.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.resource.changes.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code: Optional[str] = None
        self.message: Optional[str] = None
        self.target: Optional[str] = None
        self.details: Optional[List["_models.ErrorDetail"]] = None
        self.additional_info: Optional[List["_models.ErrorAdditionalInfo"]] = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.resource.changes.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.resource.changes.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error
