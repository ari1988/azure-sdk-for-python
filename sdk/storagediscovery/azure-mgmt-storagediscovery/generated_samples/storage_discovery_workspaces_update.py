# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.storagediscovery import StorageDiscoveryMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storagediscovery
# USAGE
    python storage_discovery_workspaces_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageDiscoveryMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.storage_discovery_workspaces.update(
        resource_group_name="sample-rg",
        storage_discovery_workspace_name="Sample-Storage-Workspace",
        properties={
            "properties": {
                "description": "Updated Sample Storage Discovery Workspace",
                "scopes": [
                    {
                        "displayName": "Updated-Sample-Collection",
                        "resourceTypes": [
                            "/subscriptions/b79cb3ba-745e-5d9a-8903-4a02327a7e09/resourceGroups/sample-rg/providers/Microsoft.Storage/storageAccounts/updated-sample-storageAccount"
                        ],
                        "tagKeysOnly": ["updated-filtertag1", "updated-filtertag2"],
                        "tags": {"updated-filtertag3": "updated-value3", "updated-filtertag4": "updated-value4"},
                    }
                ],
                "sku": "Premium",
                "workspaceRoots": ["/subscriptions/b79cb3ba-745e-5d9a-8903-4a02327a7e09"],
            }
        },
    )
    print(response)


# x-ms-original-file: 2025-06-01-preview/StorageDiscoveryWorkspaces_Update.json
if __name__ == "__main__":
    main()
