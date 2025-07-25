# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------

FEATURE_MANAGEMENT_KEY = "feature_management"
FEATURE_FLAG_KEY = "feature_flags"
FEATURE_FLAG_PREFIX = ".appconfig.featureflag/"

NULL_CHAR = "\0"

REQUEST_TRACING_DISABLED_ENVIRONMENT_VARIABLE = "AZURE_APP_CONFIGURATION_TRACING_DISABLED"
AzureFunctionEnvironmentVariable = "FUNCTIONS_EXTENSION_VERSION"
AzureWebAppEnvironmentVariable = "WEBSITE_SITE_NAME"
ContainerAppEnvironmentVariable = "CONTAINER_APP_NAME"
KubernetesEnvironmentVariable = "KUBERNETES_PORT"
ServiceFabricEnvironmentVariable = "Fabric_NodeName"  # cspell:disable-line

TELEMETRY_KEY = "telemetry"
METADATA_KEY = "metadata"

ALLOCATION_ID_KEY = "AllocationId"
ETAG_KEY = "ETag"
FEATURE_FLAG_REFERENCE_KEY = "FeatureFlagReference"

PERCENTAGE_FILTER_NAMES = ["Percentage", "PercentageFilter", "Microsoft.Percentage", "Microsoft.PercentageFilter"]
TIME_WINDOW_FILTER_NAMES = ["TimeWindow", "TimeWindowFilter", "Microsoft.TimeWindow", "Microsoft.TimeWindowFilter"]
TARGETING_FILTER_NAMES = ["Targeting", "TargetingFilter", "Microsoft.Targeting", "Microsoft.TargetingFilter"]

CUSTOM_FILTER_KEY = "CSTM"  # cspell:disable-line
PERCENTAGE_FILTER_KEY = "PRCNT"  # cspell:disable-line
TIME_WINDOW_FILTER_KEY = "TIME"
TARGETING_FILTER_KEY = "TRGT"  # cspell:disable-line

# Mime profiles
APP_CONFIG_AI_MIME_PROFILE = "https://azconfig.io/mime-profiles/ai/"
APP_CONFIG_AICC_MIME_PROFILE = "https://azconfig.io/mime-profiles/ai/chat-completion"
