# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.containerorchestratorruntime import ContainerOrchestratorRuntimeMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContainerOrchestratorRuntimeMgmtBgpPeersOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ContainerOrchestratorRuntimeMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_bgp_peers_get(self, resource_group):
        response = self.client.bgp_peers.get(
            resource_uri="str",
            bgp_peer_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_bgp_peers_begin_create_or_update(self, resource_group):
        response = self.client.bgp_peers.begin_create_or_update(
            resource_uri="str",
            bgp_peer_name="str",
            resource={
                "id": "str",
                "name": "str",
                "properties": {"myAsn": 0, "peerAddress": "str", "peerAsn": 0, "provisioningState": "str"},
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
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_bgp_peers_delete(self, resource_group):
        response = self.client.bgp_peers.delete(
            resource_uri="str",
            bgp_peer_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_bgp_peers_list(self, resource_group):
        response = self.client.bgp_peers.list(
            resource_uri="str",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
