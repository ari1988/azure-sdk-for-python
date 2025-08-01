# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.resource.policy.aio import PolicyClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPolicyPolicyExemptionsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(PolicyClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_delete(self, resource_group):
        response = await self.client.policy_exemptions.delete(
            scope="str",
            policy_exemption_name="str",
            api_version="2022-07-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_create_or_update(self, resource_group):
        response = await self.client.policy_exemptions.create_or_update(
            scope="str",
            policy_exemption_name="str",
            parameters={
                "exemptionCategory": "str",
                "policyAssignmentId": "str",
                "assignmentScopeValidation": "str",
                "description": "str",
                "displayName": "str",
                "expiresOn": "2020-02-20 00:00:00",
                "id": "str",
                "metadata": {},
                "name": "str",
                "policyDefinitionReferenceIds": ["str"],
                "resourceSelectors": [{"name": "str", "selectors": [{"in": ["str"], "kind": "str", "notIn": ["str"]}]}],
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2022-07-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_get(self, resource_group):
        response = await self.client.policy_exemptions.get(
            scope="str",
            policy_exemption_name="str",
            api_version="2022-07-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_update(self, resource_group):
        response = await self.client.policy_exemptions.update(
            scope="str",
            policy_exemption_name="str",
            parameters={
                "assignmentScopeValidation": "str",
                "resourceSelectors": [{"name": "str", "selectors": [{"in": ["str"], "kind": "str", "notIn": ["str"]}]}],
            },
            api_version="2022-07-01-preview",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_list(self, resource_group):
        response = self.client.policy_exemptions.list(
            api_version="2022-07-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_list_for_resource_group(self, resource_group):
        response = self.client.policy_exemptions.list_for_resource_group(
            resource_group_name=resource_group.name,
            api_version="2022-07-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_list_for_resource(self, resource_group):
        response = self.client.policy_exemptions.list_for_resource(
            resource_group_name=resource_group.name,
            resource_provider_namespace="str",
            parent_resource_path="str",
            resource_type="str",
            resource_name="str",
            api_version="2022-07-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_policy_exemptions_list_for_management_group(self, resource_group):
        response = self.client.policy_exemptions.list_for_management_group(
            management_group_id="str",
            api_version="2022-07-01-preview",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
