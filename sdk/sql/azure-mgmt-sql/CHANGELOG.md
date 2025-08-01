# Release History

## 4.0.0b22 (2025-07-30)

### Features Added

  - Added operation LongTermRetentionBackupsOperations.begin_lock_time_based_immutability
  - Added operation LongTermRetentionBackupsOperations.begin_lock_time_based_immutability_by_resource_group
  - Added operation LongTermRetentionBackupsOperations.begin_remove_legal_hold_immutability
  - Added operation LongTermRetentionBackupsOperations.begin_remove_legal_hold_immutability_by_resource_group
  - Added operation LongTermRetentionBackupsOperations.begin_remove_time_based_immutability
  - Added operation LongTermRetentionBackupsOperations.begin_remove_time_based_immutability_by_resource_group
  - Added operation LongTermRetentionBackupsOperations.begin_set_legal_hold_immutability
  - Added operation LongTermRetentionBackupsOperations.begin_set_legal_hold_immutability_by_resource_group
  - Added operation ManagedDatabasesOperations.begin_reevaluate_inaccessible_database_state
  - Added operation ManagedInstancesOperations.begin_reevaluate_inaccessible_database_state
  - Added operation ManagedInstancesOperations.begin_validate_azure_key_vault_encryption_key
  - Added operation TransparentDataEncryptionsOperations.begin_resume
  - Added operation TransparentDataEncryptionsOperations.begin_suspend
  - Added operation VirtualClustersOperations.begin_create_or_update
  - Model DatabaseKey has a new parameter key_version
  - Model EncryptionProtector has a new parameter key_version
  - Model LocationCapabilities has a new parameter is_zone_resilient_provisioning_allowed
  - Model LogicalDatabaseTransparentDataEncryption has a new parameter scan_state
  - Model LongTermRetentionBackup has a new parameter legal_hold_immutability
  - Model LongTermRetentionBackup has a new parameter time_based_immutability
  - Model LongTermRetentionBackup has a new parameter time_based_immutability_mode
  - Model LongTermRetentionPolicy has a new parameter time_based_immutability
  - Model LongTermRetentionPolicy has a new parameter time_based_immutability_mode
  - Model ManagedDatabase has a new parameter extended_accessibility_info
  - Model ManagedDatabaseUpdate has a new parameter extended_accessibility_info
  - Model ManagedInstance has a new parameter memory_size_in_gb
  - Model ManagedInstance has a new parameter requested_logical_availability_zone
  - Model ManagedInstanceUpdate has a new parameter memory_size_in_gb
  - Model ManagedInstanceUpdate has a new parameter requested_logical_availability_zone
  - Model ManagedInstanceVcoresCapability has a new parameter supported_memory_sizes_in_gb
  - Model Server has a new parameter create_mode
  - Model Server has a new parameter retention_days
  - Model ServerKey has a new parameter key_version
  - Model ServerUpdate has a new parameter create_mode
  - Model ServerUpdate has a new parameter retention_days

### Breaking Changes

  - Model ManagedInstance no longer has parameter total_memory_mb
  - Model ManagedInstanceUpdate no longer has parameter total_memory_mb
  - Model ManagedInstanceVcoresCapability no longer has parameter supported_memory_limits_mb

## 4.0.0b21 (2025-03-23)

### Features Added

  - Added operation GeoBackupPoliciesOperations.list
  - Added operation ManagedDatabaseSensitivityLabelsOperations.list_by_database
  - Added operation ManagedInstanceLongTermRetentionPoliciesOperations.begin_delete
  - Added operation SensitivityLabelsOperations.list_by_database
  - Added operation group InstancePoolOperationsOperations
  - Added operation group NetworkSecurityPerimeterConfigurationsOperations
  - Model DataMaskingRuleListResult has a new parameter next_link
  - Model DatabaseExtensions has a new parameter administrator_login
  - Model DatabaseExtensions has a new parameter administrator_login_password
  - Model DatabaseExtensions has a new parameter authentication_type
  - Model DatabaseExtensions has a new parameter database_edition
  - Model DatabaseExtensions has a new parameter max_size_bytes
  - Model DatabaseExtensions has a new parameter network_isolation
  - Model DatabaseExtensions has a new parameter service_objective_name
  - Model EditionCapability has a new parameter zone_pinning
  - Model ElasticPool has a new parameter auto_pause_delay
  - Model ElasticPoolEditionCapability has a new parameter zone_pinning
  - Model ElasticPoolPerDatabaseSettings has a new parameter auto_pause_delay
  - Model ElasticPoolPerformanceLevelCapability has a new parameter supported_auto_pause_delay
  - Model ElasticPoolPerformanceLevelCapability has a new parameter supported_min_capacities
  - Model ElasticPoolPerformanceLevelCapability has a new parameter supported_per_database_auto_pause_delay
  - Model ElasticPoolPerformanceLevelCapability has a new parameter supported_zones
  - Model ElasticPoolUpdate has a new parameter auto_pause_delay
  - Model GeoBackupPolicyListResult has a new parameter next_link
  - Model ImportExportExtensionsOperationResult has a new parameter blob_uri
  - Model ImportExportExtensionsOperationResult has a new parameter private_endpoint_connections
  - Model ImportExportExtensionsOperationResult has a new parameter queued_time
  - Model JobAgent has a new parameter identity
  - Model JobAgentUpdate has a new parameter identity
  - Model JobAgentUpdate has a new parameter sku
  - Model LocationCapabilities has a new parameter supported_job_agent_versions
  - Model ManagedInstance has a new parameter total_memory_mb
  - Model ManagedInstanceEditionCapability has a new parameter is_general_purpose_v2
  - Model ManagedInstanceFamilyCapability has a new parameter zone_redundant
  - Model ManagedInstanceLongTermRetentionBackup has a new parameter backup_storage_access_tier
  - Model ManagedInstanceLongTermRetentionPolicy has a new parameter backup_storage_access_tier
  - Model ManagedInstancePrivateLinkProperties has a new parameter required_zone_names
  - Model ManagedInstanceUpdate has a new parameter total_memory_mb
  - Model ManagedInstanceVcoresCapability has a new parameter included_storage_i_ops
  - Model ManagedInstanceVcoresCapability has a new parameter included_storage_throughput_m_bps
  - Model ManagedInstanceVcoresCapability has a new parameter iops_included_value_override_factor_per_selected_storage_gb
  - Model ManagedInstanceVcoresCapability has a new parameter iops_min_value_override_factor_per_selected_storage_gb
  - Model ManagedInstanceVcoresCapability has a new parameter supported_memory_limits_mb
  - Model ManagedInstanceVcoresCapability has a new parameter supported_storage_i_ops
  - Model ManagedInstanceVcoresCapability has a new parameter supported_storage_throughput_m_bps
  - Model ManagedInstanceVcoresCapability has a new parameter throughput_m_bps_included_value_override_factor_per_selected_storage_gb
  - Model ManagedInstanceVcoresCapability has a new parameter throughput_m_bps_min_value_override_factor_per_selected_storage_gb
  - Model SensitivityLabel has a new parameter client_classification_source
  - Model ServerUsage has a new parameter id
  - Model ServerUsage has a new parameter type
  - Model ServerUsageListResult has a new parameter next_link
  - Model ServiceObjectiveCapability has a new parameter supported_free_limit_exhaustion_behaviors
  - Model ServiceObjectiveCapability has a new parameter supported_zones
  - Model ServiceObjectiveCapability has a new parameter zone_pinning
  - Operation LongTermRetentionManagedInstanceBackupsOperations.list_by_location has a new optional parameter filter
  - Operation LongTermRetentionManagedInstanceBackupsOperations.list_by_location has a new optional parameter skip
  - Operation LongTermRetentionManagedInstanceBackupsOperations.list_by_location has a new optional parameter top
  - Operation LongTermRetentionManagedInstanceBackupsOperations.list_by_resource_group_location has a new optional parameter filter
  - Operation LongTermRetentionManagedInstanceBackupsOperations.list_by_resource_group_location has a new optional parameter skip
  - Operation LongTermRetentionManagedInstanceBackupsOperations.list_by_resource_group_location has a new optional parameter top

### Breaking Changes

  - Model LongTermRetentionPolicy no longer has parameter backup_storage_access_tier
  - Model LongTermRetentionPolicy no longer has parameter make_backups_immutable
  - Model ManagedInstanceEditionCapability no longer has parameter zone_redundant
  - Model ServerUsage no longer has parameter next_reset_time
  - Model ServerUsage no longer has parameter resource_name
  - Operation DataMaskingPoliciesOperations.create_or_update has a new required parameter data_masking_policy_name
  - Operation DataMaskingPoliciesOperations.get has a new required parameter data_masking_policy_name
  - Operation DataMaskingRulesOperations.create_or_update has a new required parameter data_masking_policy_name
  - Operation DataMaskingRulesOperations.list_by_database has a new required parameter data_masking_policy_name
  - Operation OutboundFirewallRulesOperations.begin_create_or_update no longer has parameter parameters
  - Removed operation DatabasesOperations.list_metric_definitions
  - Removed operation DatabasesOperations.list_metrics
  - Removed operation ElasticPoolsOperations.list_metric_definitions
  - Removed operation ElasticPoolsOperations.list_metrics
  - Removed operation GeoBackupPoliciesOperations.list_by_database
  - Removed operation group ElasticPoolActivitiesOperations
  - Removed operation group ElasticPoolDatabaseActivitiesOperations
  - Removed operation group ServerCommunicationLinksOperations
  - Removed operation group ServiceObjectivesOperations

## 4.0.0b20 (2024-11-04)

### Features Added

  - Model `DistributedAvailabilityGroup` added property `distributed_availability_group_name`
  - Model `DistributedAvailabilityGroup` added property `partner_link_role`
  - Model `DistributedAvailabilityGroup` added property `partner_availability_group_name`
  - Model `DistributedAvailabilityGroup` added property `partner_endpoint`
  - Model `DistributedAvailabilityGroup` added property `instance_link_role`
  - Model `DistributedAvailabilityGroup` added property `instance_availability_group_name`
  - Model `DistributedAvailabilityGroup` added property `failover_mode`
  - Model `DistributedAvailabilityGroup` added property `seeding_mode`
  - Model `DistributedAvailabilityGroup` added property `databases`
  - Added model `CertificateInfo`
  - Added model `DistributedAvailabilityGroupDatabase`
  - Added model `DistributedAvailabilityGroupSetRole`
  - Added model `DistributedAvailabilityGroupsFailoverRequest`
  - Added enum `FailoverModeType`
  - Added enum `FailoverType`
  - Added enum `InstanceRole`
  - Added enum `LinkRole`
  - Added enum `ReplicaConnectedState`
  - Added enum `ReplicaSynchronizationHealth`
  - Added enum `ReplicationModeType`
  - Added enum `RoleChangeType`
  - Added enum `SeedingModeType`
  - Operation group `DistributedAvailabilityGroupsOperations` added method `begin_failover`
  - Operation group `DistributedAvailabilityGroupsOperations` added method `begin_set_role`

### Breaking Changes

  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `target_database`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `source_endpoint`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `primary_availability_group_name`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `secondary_availability_group_name`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `source_replica_id`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `target_replica_id`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `link_state`
  - Model `DistributedAvailabilityGroup` deleted or renamed its instance variable `last_hardened_lsn`
  - Deleted or renamed model `ReplicationMode`

## 4.0.0b19 (2024-09-09)

### Features Added

  - The 'ReplicationLinksOperations' method 'begin_create_or_update' was added in the current version
  - The 'ReplicationLinksOperations' method 'begin_update' was added in the current version
  - The model or publicly exposed class 'ColumnDataType' had property 'INT' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'target_database' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'source_endpoint' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'primary_availability_group_name' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'secondary_availability_group_name' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'source_replica_id' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'target_replica_id' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'link_state' added in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had property 'last_hardened_lsn' added in the current version
  - The model or publicly exposed class 'FailoverGroup' had property 'secondary_type' added in the current version
  - The model or publicly exposed class 'FailoverGroupUpdate' had property 'secondary_type' added in the current version
  - The model or publicly exposed class 'ManagedInstance' had property 'storage_iops' added in the current version
  - The model or publicly exposed class 'ManagedInstance' had property 'storage_throughput_mbps' added in the current version
  - The model or publicly exposed class 'ManagedInstanceUpdate' had property 'storage_iops' added in the current version
  - The model or publicly exposed class 'ManagedInstanceUpdate' had property 'storage_throughput_mbps' added in the current version
  - The model or publicly exposed class 'ReplicationLink' had property 'partner_database_id' added in the current version
  - The model or publicly exposed class 'FailoverGroupDatabasesSecondaryType' was added in the current version
  - The model or publicly exposed class 'ReplicationLinkUpdate' was added in the current version
  - The model or publicly exposed class 'ReplicationMode' was added in the current version
  - The 'ReplicationLinksOperations' method 'begin_create_or_update' was added in the current version
  - The 'ReplicationLinksOperations' method 'begin_update' was added in the current version

### Breaking Changes

  - The 'DistributedAvailabilityGroupsOperations' method 'begin_failover' was deleted or renamed in the current version
  - The 'DistributedAvailabilityGroupsOperations' method 'begin_set_role' was deleted or renamed in the current version
  - The 'ColumnDataType' enum had its value 'INT_ENUM' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'distributed_availability_group_name' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'partner_link_role' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'partner_availability_group_name' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'partner_endpoint' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'instance_link_role' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'instance_availability_group_name' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'failover_mode' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'seeding_mode' deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroup' had its instance variable 'databases' deleted or renamed in the current version
  - The model or publicly exposed class 'ManagedInstance' had its instance variable 'storage_i_ops' deleted or renamed in the current version
  - The model or publicly exposed class 'ManagedInstance' had its instance variable 'storage_throughput_m_bps' deleted or renamed in the current version
  - The model or publicly exposed class 'ManagedInstanceUpdate' had its instance variable 'storage_i_ops' deleted or renamed in the current version
  - The model or publicly exposed class 'ManagedInstanceUpdate' had its instance variable 'storage_throughput_m_bps' deleted or renamed in the current version
  - The model or publicly exposed class 'CertificateInfo' was deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroupDatabase' was deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroupSetRole' was deleted or renamed in the current version
  - The model or publicly exposed class 'DistributedAvailabilityGroupsFailoverRequest' was deleted or renamed in the current version
  - The model or publicly exposed class 'FailoverModeType' was deleted or renamed in the current version
  - The model or publicly exposed class 'FailoverType' was deleted or renamed in the current version
  - The model or publicly exposed class 'InstanceRole' was deleted or renamed in the current version
  - The model or publicly exposed class 'LinkRole' was deleted or renamed in the current version
  - The model or publicly exposed class 'ReplicaConnectedState' was deleted or renamed in the current version
  - The model or publicly exposed class 'ReplicaSynchronizationHealth' was deleted or renamed in the current version
  - The model or publicly exposed class 'ReplicationModeType' was deleted or renamed in the current version
  - The model or publicly exposed class 'RoleChangeType' was deleted or renamed in the current version
  - The model or publicly exposed class 'SeedingModeType' was deleted or renamed in the current version
  - The 'DistributedAvailabilityGroupsOperations' method 'begin_failover' was deleted or renamed in the current version
  - The 'DistributedAvailabilityGroupsOperations' method 'begin_set_role' was deleted or renamed in the current version

## 4.0.0b18 (2024-07-11)

### Bugs Fixed

  - Fix import error when import from azure.mgmt.sql.aio

## 4.0.0b17 (2024-05-20)

### Features Added

  - Model DatabaseOperation has a new parameter operation_phase_details

## 4.0.0b16 (2024-04-07)

### Features Added

  - Added operation DistributedAvailabilityGroupsOperations.begin_failover
  - Added operation DistributedAvailabilityGroupsOperations.begin_set_role
  - Model DistributedAvailabilityGroup has a new parameter databases
  - Model DistributedAvailabilityGroup has a new parameter distributed_availability_group_name
  - Model DistributedAvailabilityGroup has a new parameter failover_mode
  - Model DistributedAvailabilityGroup has a new parameter instance_availability_group_name
  - Model DistributedAvailabilityGroup has a new parameter instance_link_role
  - Model DistributedAvailabilityGroup has a new parameter partner_availability_group_name
  - Model DistributedAvailabilityGroup has a new parameter partner_endpoint
  - Model DistributedAvailabilityGroup has a new parameter partner_link_role
  - Model DistributedAvailabilityGroup has a new parameter seeding_mode

### Breaking Changes

  - Model DistributedAvailabilityGroup no longer has parameter last_hardened_lsn
  - Model DistributedAvailabilityGroup no longer has parameter link_state
  - Model DistributedAvailabilityGroup no longer has parameter primary_availability_group_name
  - Model DistributedAvailabilityGroup no longer has parameter secondary_availability_group_name
  - Model DistributedAvailabilityGroup no longer has parameter source_endpoint
  - Model DistributedAvailabilityGroup no longer has parameter source_replica_id
  - Model DistributedAvailabilityGroup no longer has parameter target_database
  - Model DistributedAvailabilityGroup no longer has parameter target_replica_id

## 4.0.0b15 (2024-01-11)

### Features Added

  - Added operation ManagedInstancesOperations.begin_refresh_status
  - Model ManagedInstance has a new parameter authentication_metadata
  - Model ManagedInstance has a new parameter create_time
  - Model ManagedInstance has a new parameter database_format
  - Model ManagedInstance has a new parameter external_governance_status
  - Model ManagedInstance has a new parameter hybrid_secondary_usage
  - Model ManagedInstance has a new parameter hybrid_secondary_usage_detected
  - Model ManagedInstance has a new parameter is_general_purpose_v2
  - Model ManagedInstance has a new parameter pricing_model
  - Model ManagedInstance has a new parameter storage_i_ops
  - Model ManagedInstance has a new parameter storage_throughput_m_bps
  - Model ManagedInstance has a new parameter virtual_cluster_id
  - Model ManagedInstanceUpdate has a new parameter authentication_metadata
  - Model ManagedInstanceUpdate has a new parameter create_time
  - Model ManagedInstanceUpdate has a new parameter database_format
  - Model ManagedInstanceUpdate has a new parameter external_governance_status
  - Model ManagedInstanceUpdate has a new parameter hybrid_secondary_usage
  - Model ManagedInstanceUpdate has a new parameter hybrid_secondary_usage_detected
  - Model ManagedInstanceUpdate has a new parameter is_general_purpose_v2
  - Model ManagedInstanceUpdate has a new parameter pricing_model
  - Model ManagedInstanceUpdate has a new parameter storage_i_ops
  - Model ManagedInstanceUpdate has a new parameter storage_throughput_m_bps
  - Model ManagedInstanceUpdate has a new parameter virtual_cluster_id

## 4.0.0b14 (2023-12-18)

### Features Added

  - Added operation LongTermRetentionBackupsOperations.begin_change_access_tier
  - Added operation LongTermRetentionBackupsOperations.begin_change_access_tier_by_resource_group
  - Model LongTermRetentionBackup has a new parameter backup_storage_access_tier
  - Model LongTermRetentionBackup has a new parameter is_backup_immutable
  - Model LongTermRetentionPolicy has a new parameter backup_storage_access_tier
  - Model LongTermRetentionPolicy has a new parameter make_backups_immutable

## 4.0.0b13 (2023-11-17)

### Features Added

  - Added operation group JobPrivateEndpointsOperations
  - Model FailoverGroupReadOnlyEndpoint has a new parameter target_server
  - Model FailoverGroupUpdate has a new parameter partner_servers
  - Model InstancePool has a new parameter dns_zone
  - Model InstancePool has a new parameter maintenance_configuration_id
  - Model InstancePoolUpdate has a new parameter dns_zone
  - Model InstancePoolUpdate has a new parameter license_type
  - Model InstancePoolUpdate has a new parameter maintenance_configuration_id
  - Model InstancePoolUpdate has a new parameter sku
  - Model InstancePoolUpdate has a new parameter subnet_id
  - Model InstancePoolUpdate has a new parameter v_cores
  - Model Server has a new parameter is_i_pv6_enabled
  - Model ServerUpdate has a new parameter is_i_pv6_enabled

## 4.0.0b12 (2023-08-30)

### Features Added

  - Model Database has a new parameter encryption_protector_auto_rotation
  - Model Database has a new parameter free_limit_exhaustion_behavior
  - Model Database has a new parameter use_free_limit
  - Model DatabaseUpdate has a new parameter encryption_protector_auto_rotation
  - Model DatabaseUpdate has a new parameter free_limit_exhaustion_behavior
  - Model DatabaseUpdate has a new parameter use_free_limit

## 4.0.0b11 (2023-07-28)

### Features Added

  - Added operation FailoverGroupsOperations.begin_try_planned_before_forced_failover
  - Model PrivateEndpointConnection has a new parameter group_ids
  - Model SqlVulnerabilityAssessmentScanRecord has a new parameter last_scan_time

## 4.0.0b10 (2023-04-11)

### Features Added

  - Model ManagedDatabase has a new parameter is_ledger_on
  - Model ManagedDatabaseUpdate has a new parameter is_ledger_on

## 4.0.0b9 (2023-03-24)

### Features Added

  - Model ElasticPool has a new parameter availability_zone
  - Model ElasticPool has a new parameter min_capacity
  - Model ElasticPool has a new parameter preferred_enclave_type
  - Model ElasticPoolUpdate has a new parameter availability_zone
  - Model ElasticPoolUpdate has a new parameter min_capacity
  - Model ElasticPoolUpdate has a new parameter preferred_enclave_type

## 4.0.0b8 (2023-02-17)

### Features Added

  - Added operation ManagedInstancesOperations.begin_start
  - Added operation ManagedInstancesOperations.begin_stop
  - Added operation ManagedInstancesOperations.list_outbound_network_dependencies_by_managed_instance
  - Added operation ServersOperations.begin_refresh_status
  - Added operation group DatabaseEncryptionProtectorsOperations
  - Added operation group ManagedLedgerDigestUploadsOperations
  - Added operation group ServerConfigurationOptionsOperations
  - Added operation group StartStopManagedInstanceSchedulesOperations
  - Model Database has a new parameter availability_zone
  - Model Database has a new parameter encryption_protector
  - Model Database has a new parameter keys
  - Model Database has a new parameter manual_cutover
  - Model Database has a new parameter perform_cutover
  - Model DatabaseUpdate has a new parameter encryption_protector
  - Model DatabaseUpdate has a new parameter keys
  - Model DatabaseUpdate has a new parameter manual_cutover
  - Model DatabaseUpdate has a new parameter perform_cutover
  - Model PrivateEndpointConnectionProperties has a new parameter group_ids
  - Model RecoverableDatabase has a new parameter keys
  - Model RecoverableDatabaseListResult has a new parameter next_link
  - Model RestorableDroppedDatabase has a new parameter keys
  - Model Server has a new parameter external_governance_status
  - Model ServerUpdate has a new parameter external_governance_status
  - Operation DatabasesOperations.get has a new optional parameter expand
  - Operation DatabasesOperations.get has a new optional parameter filter
  - Operation RecoverableDatabasesOperations.get has a new optional parameter expand
  - Operation RecoverableDatabasesOperations.get has a new optional parameter filter
  - Operation RestorableDroppedDatabasesOperations.get has a new optional parameter expand
  - Operation RestorableDroppedDatabasesOperations.get has a new optional parameter filter

### Breaking Changes

  - Renamed operation TransparentDataEncryptionsOperations.create_or_update to TransparentDataEncryptionsOperations.begin_create_or_update

## 4.0.0b7 (2023-01-29)

### Features Added

  - Model InstanceFailoverGroup has a new parameter secondary_type
  - Model ManagedDatabase has a new parameter cross_subscription_restorable_dropped_database_id
  - Model ManagedDatabase has a new parameter cross_subscription_source_database_id
  - Model ManagedDatabase has a new parameter cross_subscription_target_managed_instance_id
  - Model ManagedDatabaseUpdate has a new parameter cross_subscription_restorable_dropped_database_id
  - Model ManagedDatabaseUpdate has a new parameter cross_subscription_source_database_id
  - Model ManagedDatabaseUpdate has a new parameter cross_subscription_target_managed_instance_id

## 4.0.0b6 (2022-12-30)

### Features Added

  - Model Database has a new parameter preferred_enclave_type
  - Model DatabaseUpdate has a new parameter preferred_enclave_type

## 4.0.0b5 (2022-11-10)

### Features Added

  - Model ServerDevOpsAuditingSettings has a new parameter is_managed_identity_in_use

## 4.0.0b4 (2022-09-29)

### Features Added

  - Added operation ManagedDatabasesOperations.begin_cancel_move
  - Added operation ManagedDatabasesOperations.begin_complete_move
  - Added operation ManagedDatabasesOperations.begin_start_move
  - Added operation group DatabaseSqlVulnerabilityAssessmentBaselinesOperations
  - Added operation group DatabaseSqlVulnerabilityAssessmentExecuteScanOperations
  - Added operation group DatabaseSqlVulnerabilityAssessmentRuleBaselinesOperations
  - Added operation group DatabaseSqlVulnerabilityAssessmentScanResultOperations
  - Added operation group DatabaseSqlVulnerabilityAssessmentScansOperations
  - Added operation group DatabaseSqlVulnerabilityAssessmentsSettingsOperations
  - Added operation group ManagedDatabaseAdvancedThreatProtectionSettingsOperations
  - Added operation group ManagedDatabaseMoveOperationsOperations
  - Added operation group ManagedInstanceAdvancedThreatProtectionSettingsOperations
  - Added operation group ManagedInstanceDtcsOperations
  - Added operation group SqlVulnerabilityAssessmentBaselineOperations
  - Added operation group SqlVulnerabilityAssessmentBaselinesOperations
  - Added operation group SqlVulnerabilityAssessmentExecuteScanOperations
  - Added operation group SqlVulnerabilityAssessmentRuleBaselineOperations
  - Added operation group SqlVulnerabilityAssessmentRuleBaselinesOperations
  - Added operation group SqlVulnerabilityAssessmentScanResultOperations
  - Added operation group SqlVulnerabilityAssessmentScansOperations
  - Added operation group SqlVulnerabilityAssessmentsOperations
  - Added operation group SqlVulnerabilityAssessmentsSettingsOperations
  - Added operation group SynapseLinkWorkspacesOperations
  - Model ManagedDatabase has a new parameter storage_container_identity
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter current_backup_type
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter current_restore_plan_size_mb
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter current_restored_size_mb
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter diff_backup_sets
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter full_backup_sets
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter log_backup_sets
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter number_of_files_queued
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter number_of_files_restored
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter number_of_files_restoring
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter number_of_files_skipped
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter number_of_files_unrestorable
  - Model ManagedDatabaseRestoreDetailsResult has a new parameter type_properties_type
  - Model ManagedDatabaseUpdate has a new parameter storage_container_identity
  - Model VirtualCluster has a new parameter version
  - Model VirtualClusterUpdate has a new parameter version

### Breaking Changes

  - Model VirtualCluster no longer has parameter family
  - Model VirtualCluster no longer has parameter maintenance_configuration_id
  - Model VirtualClusterUpdate no longer has parameter family
  - Model VirtualClusterUpdate no longer has parameter maintenance_configuration_id
  - Renamed operation ReplicationLinksOperations.delete to ReplicationLinksOperations.begin_delete
  - Renamed operation VirtualClustersOperations.update_dns_servers to VirtualClustersOperations.begin_update_dns_servers

## 4.0.0b3 (2022-07-06)

**Features**

  - Added operation group DatabaseAdvancedThreatProtectionSettingsOperations
  - Added operation group EndpointCertificatesOperations
  - Added operation group ManagedServerDnsAliasesOperations
  - Added operation group ServerAdvancedThreatProtectionSettingsOperations
  - Model Database has a new parameter source_resource_id
  - Model DatabaseBlobAuditingPolicy has a new parameter is_managed_identity_in_use
  - Model ExtendedDatabaseBlobAuditingPolicy has a new parameter is_managed_identity_in_use
  - Model ExtendedServerBlobAuditingPolicy has a new parameter is_managed_identity_in_use
  - Model ServerBlobAuditingPolicy has a new parameter is_managed_identity_in_use

**Breaking changes**

  - Model Database no longer has parameter primary_delegated_identity_client_id
  - Model DatabaseIdentity no longer has parameter delegated_resources
  - Model DatabaseUpdate no longer has parameter primary_delegated_identity_client_id
  - Removed operation ReplicationLinksOperations.begin_unlink

## 4.0.0b2 (2022-03-08)

**Features**

  - Added operation group DistributedAvailabilityGroupsOperations
  - Added operation group IPv6FirewallRulesOperations
  - Added operation group ServerTrustCertificatesOperations
  - Model ElasticPool has a new parameter high_availability_replica_count
  - Model ElasticPoolUpdate has a new parameter high_availability_replica_count

**Breaking changes**

  - Removed operation group OperationsHealthOperations

## 4.0.0b1 (2021-12-21)

**Features**

  - Model ManagedInstanceUpdate has a new parameter current_backup_storage_redundancy
  - Model ManagedInstanceUpdate has a new parameter requested_backup_storage_redundancy
  - Model ManagedInstanceUpdate has a new parameter service_principal
  - Model Database has a new parameter identity
  - Model Database has a new parameter primary_delegated_identity_client_id
  - Model Database has a new parameter federated_client_id
  - Model ManagedInstance has a new parameter current_backup_storage_redundancy
  - Model ManagedInstance has a new parameter requested_backup_storage_redundancy
  - Model ManagedInstance has a new parameter service_principal
  - Model DatabaseUpdate has a new parameter identity
  - Model DatabaseUpdate has a new parameter primary_delegated_identity_client_id
  - Model DatabaseUpdate has a new parameter federated_client_id
  - Added operation TransparentDataEncryptionsOperations.list_by_database
  - Added operation LedgerDigestUploadsOperations.begin_create_or_update
  - Added operation LedgerDigestUploadsOperations.begin_disable
  - Added operation ServerConnectionPoliciesOperations.list_by_server
  - Added operation ServerConnectionPoliciesOperations.begin_create_or_update

**Breaking changes**

  - Operation TransparentDataEncryptionsOperations.create_or_update has a new signature
  - Operation TransparentDataEncryptionsOperations.get has a new signature
  - Model ManagedInstanceUpdate no longer has parameter storage_account_type
  - Model ManagedInstance no longer has parameter storage_account_type
  - Model RestorableDroppedDatabase no longer has parameter elastic_pool_id
  - Removed operation LedgerDigestUploadsOperations.create_or_update
  - Removed operation LedgerDigestUploadsOperations.disable
  - Removed operation ServerConnectionPoliciesOperations.create_or_update
  - Removed operation group TransparentDataEncryptionActivitiesOperations

## 3.0.1 (2021-07-15)

**Bugfixes**

  - Fix default setting for blob_auditing_policy_name

## 3.0.0 (2021-06-18)

**Features**

  - Model Server has a new parameter federated_client_id
  - Model Server has a new parameter restrict_outbound_network_access
  - Model ServerUpdate has a new parameter federated_client_id
  - Model ServerUpdate has a new parameter restrict_outbound_network_access
  - Model BackupShortTermRetentionPolicy has a new parameter diff_backup_interval_in_hours

**Breaking changes**

  - Operation ReplicationLinksOperations.get has a new signature

## 2.1.0 (2021-05-24)

 - Add resource identity

## 2.0.0 (2021-05-13)

**Features**

  - Model LongTermRetentionBackup has a new parameter requested_backup_storage_redundancy
  - Model LongTermRetentionBackup has a new parameter backup_storage_redundancy
  - Model ManagedInstanceKey has a new parameter auto_rotation_enabled
  - Model ManagedInstanceEncryptionProtector has a new parameter auto_rotation_enabled
  - Model Database has a new parameter is_infra_encryption_enabled
  - Model Database has a new parameter is_ledger_on
  - Model Database has a new parameter secondary_type
  - Model Database has a new parameter current_backup_storage_redundancy
  - Model Database has a new parameter high_availability_replica_count
  - Model Database has a new parameter maintenance_configuration_id
  - Model Database has a new parameter requested_backup_storage_redundancy
  - Model ReplicationLink has a new parameter link_type
  - Model ServerUpdate has a new parameter primary_user_assigned_identity_id
  - Model ServerUpdate has a new parameter administrators
  - Model ServerUpdate has a new parameter identity
  - Model ServerUpdate has a new parameter key_id
  - Model ServerUpdate has a new parameter workspace_feature
  - Model DatabaseUpdate has a new parameter is_infra_encryption_enabled
  - Model DatabaseUpdate has a new parameter is_ledger_on
  - Model DatabaseUpdate has a new parameter secondary_type
  - Model DatabaseUpdate has a new parameter current_backup_storage_redundancy
  - Model DatabaseUpdate has a new parameter high_availability_replica_count
  - Model DatabaseUpdate has a new parameter maintenance_configuration_id
  - Model DatabaseUpdate has a new parameter requested_backup_storage_redundancy
  - Model ManagedInstance has a new parameter primary_user_assigned_identity_id
  - Model ManagedInstance has a new parameter administrators
  - Model ManagedInstance has a new parameter key_id
  - Model ManagedInstance has a new parameter zone_redundant
  - Model ManagedInstance has a new parameter private_endpoint_connections
  - Model ServerKey has a new parameter auto_rotation_enabled
  - Model ExtendedServerBlobAuditingPolicy has a new parameter is_devops_audit_enabled
  - Model ServiceObjectiveCapability has a new parameter supported_maintenance_configurations
  - Model EncryptionProtector has a new parameter auto_rotation_enabled
  - Model FirewallRuleListResult has a new parameter next_link
  - Model ManagedInstanceUpdate has a new parameter primary_user_assigned_identity_id
  - Model ManagedInstanceUpdate has a new parameter administrators
  - Model ManagedInstanceUpdate has a new parameter identity
  - Model ManagedInstanceUpdate has a new parameter key_id
  - Model ManagedInstanceUpdate has a new parameter private_endpoint_connections
  - Model ManagedInstanceUpdate has a new parameter zone_redundant
  - Model ElasticPoolUpdate has a new parameter maintenance_configuration_id
  - Model SyncMember has a new parameter private_endpoint_name
  - Model ElasticPool has a new parameter maintenance_configuration_id
  - Model ManagedInstanceVcoresCapability has a new parameter supported_maintenance_configurations
  - Model ManagedInstanceLongTermRetentionBackup has a new parameter backup_storage_redundancy
  - Model ServerSecurityAlertPolicy has a new parameter system_data
  - Model ManagedInstanceEditionCapability has a new parameter supported_storage_capabilities
  - Model ManagedInstanceEditionCapability has a new parameter zone_redundant
  - Model ServerBlobAuditingPolicy has a new parameter is_devops_audit_enabled
  - Model ElasticPoolPerformanceLevelCapability has a new parameter supported_maintenance_configurations
  - Model RestorableDroppedDatabase has a new parameter backup_storage_redundancy
  - Model RestorableDroppedDatabase has a new parameter tags
  - Model RestorableDroppedDatabase has a new parameter sku
  - Model RestorableDroppedDatabase has a new parameter elastic_pool_id
  - Model DatabaseSecurityAlertPolicy has a new parameter creation_time
  - Model DatabaseSecurityAlertPolicy has a new parameter system_data
  - Model SyncGroup has a new parameter conflict_logging_retention_in_days
  - Model SyncGroup has a new parameter private_endpoint_name
  - Model SyncGroup has a new parameter sku
  - Model SyncGroup has a new parameter enable_conflict_logging
  - Model VirtualClusterUpdate has a new parameter maintenance_configuration_id
  - Model PrivateLinkResourceProperties has a new parameter required_zone_names
  - Model VirtualCluster has a new parameter maintenance_configuration_id
  - Model ManagedServerSecurityAlertPolicy has a new parameter system_data
  - Model DatabaseUsage has a new parameter type
  - Model DatabaseUsage has a new parameter id
  - Model Server has a new parameter primary_user_assigned_identity_id
  - Model Server has a new parameter key_id
  - Model Server has a new parameter administrators
  - Model Server has a new parameter workspace_feature
  - Model SensitivityLabel has a new parameter column_name
  - Model SensitivityLabel has a new parameter schema_name
  - Model SensitivityLabel has a new parameter managed_by
  - Model SensitivityLabel has a new parameter table_name
  - Added operation VirtualClustersOperations.update_dns_servers
  - Added operation ServersOperations.begin_import_database
  - Added operation DatabasesOperations.list_inaccessible_by_server
  - Added operation FirewallRulesOperations.replace
  - Added operation ReplicationLinksOperations.list_by_server
  - Added operation SensitivityLabelsOperations.update
  - Added operation ManagedInstancesOperations.list_by_managed_instance
  - Added operation ManagedDatabaseSensitivityLabelsOperations.update
  - Added operation LongTermRetentionBackupsOperations.begin_update
  - Added operation LongTermRetentionBackupsOperations.begin_copy
  - Added operation LongTermRetentionBackupsOperations.begin_copy_by_resource_group
  - Added operation LongTermRetentionBackupsOperations.begin_update_by_resource_group
  - Added operation group DatabaseSchemasOperations
  - Added operation group DatabaseExtensionsOperations
  - Added operation group ManagedInstancePrivateEndpointConnectionsOperations
  - Added operation group DeletedServersOperations
  - Added operation group ManagedDatabaseTablesOperations
  - Added operation group MaintenanceWindowOptionsOperations
  - Added operation group DatabaseSecurityAlertPoliciesOperations
  - Added operation group ServerTrustGroupsOperations
  - Added operation group ManagedInstanceAzureADOnlyAuthenticationsOperations
  - Added operation group SqlAgentOperations
  - Added operation group TimeZonesOperations
  - Added operation group ManagedInstancePrivateLinkResourcesOperations
  - Added operation group RecommendedSensitivityLabelsOperations
  - Added operation group DatabaseTablesOperations
  - Added operation group ServerAdvisorsOperations
  - Added operation group ManagedDatabaseSecurityEventsOperations
  - Added operation group ServerOperationsOperations
  - Added operation group DatabaseAdvisorsOperations
  - Added operation group DatabaseColumnsOperations
  - Added operation group DataWarehouseUserActivitiesOperations
  - Added operation group OutboundFirewallRulesOperations
  - Added operation group ManagedDatabaseSchemasOperations
  - Added operation group DatabaseRecommendedActionsOperations
  - Added operation group LongTermRetentionPoliciesOperations
  - Added operation group ManagedDatabaseQueriesOperations
  - Added operation group ManagedDatabaseRecommendedSensitivityLabelsOperations
  - Added operation group ManagedDatabaseTransparentDataEncryptionOperations
  - Added operation group ServerDevOpsAuditSettingsOperations
  - Added operation group OperationsHealthOperations
  - Added operation group LedgerDigestUploadsOperations
  - Added operation group MaintenanceWindowsOperations
  - Added operation group ManagedDatabaseColumnsOperations

**Breaking changes**

  - Operation RestorableDroppedDatabasesOperations.get has a new signature
  - Operation ReplicationLinksOperations.get has a new signature
  - Parameter old_server_dns_alias_id of model ServerDnsAliasAcquisition is now required
  - Operation SensitivityLabelsOperations.list_recommended_by_database has a new signature
  - Operation ManagedDatabaseSensitivityLabelsOperations.list_recommended_by_database has a new signature
  - Operation DatabasesOperations.begin_import_method has a new signature
  - Operation DatabasesOperations.list_by_server has a new signature
  - Operation ManagedDatabaseSensitivityLabelsOperations.list_current_by_database has a new signature
  - Operation ManagedDatabaseSensitivityLabelsOperations.list_current_by_database has a new signature
  - Operation ManagedDatabaseSensitivityLabelsOperations.list_recommended_by_database has a new signature
  - Operation ManagedInstanceAdministratorsOperations.begin_create_or_update has a new signature
  - Operation ManagedInstanceAdministratorsOperations.begin_delete has a new signature
  - Operation ManagedInstanceAdministratorsOperations.get has a new signature
  - Operation ManagedInstancesOperations.get has a new signature
  - Operation ManagedInstancesOperations.list has a new signature
  - Operation ManagedInstancesOperations.list_by_instance_pool has a new signature
  - Operation ManagedInstancesOperations.list_by_resource_group has a new signature
  - Operation SensitivityLabelsOperations.list_current_by_database has a new signature
  - Operation SensitivityLabelsOperations.list_current_by_database has a new signature
  - Operation SensitivityLabelsOperations.list_recommended_by_database has a new signature
  - Operation ServersOperations.get has a new signature
  - Operation ServersOperations.list has a new signature
  - Operation ServersOperations.list_by_resource_group has a new signature
  - Model BackupShortTermRetentionPolicy no longer has parameter diff_backup_interval_in_hours
  - Model Database no longer has parameter read_replica_count
  - Model ReplicationLink no longer has parameter location
  - Model DatabaseUpdate no longer has parameter read_replica_count
  - Model FirewallRule no longer has parameter kind
  - Model FirewallRule no longer has parameter location
  - Model RestorableDroppedDatabase no longer has parameter service_level_objective
  - Model RestorableDroppedDatabase no longer has parameter edition
  - Model RestorableDroppedDatabase no longer has parameter elastic_pool_name
  - Model DatabaseSecurityAlertPolicy no longer has parameter use_server_default
  - Model DatabaseSecurityAlertPolicy no longer has parameter kind
  - Model DatabaseSecurityAlertPolicy no longer has parameter location
  - Model DatabaseUsage no longer has parameter resource_name
  - Model DatabaseUsage no longer has parameter next_reset_time
  - Removed operation DatabasesOperations.begin_create_import_operation
  - Model DatabaseUsageListResult has a new signature
  - Model RestorableDroppedDatabaseListResult has a new signature
  - Removed operation group RecommendedElasticPoolsOperations
  - Removed operation group BackupLongTermRetentionPoliciesOperations
  - Removed operation group DatabaseThreatDetectionPoliciesOperations
  - Removed operation group ServiceTierAdvisorsOperations

## 1.0.0 (2020-11-24)

- GA release

## 1.0.0b1 (2020-10-13)

This is beta preview version.

This version uses a next-generation code generator that introduces important breaking changes, but also important new features (like unified authentication and async programming).

**General breaking changes**

- Credential system has been completly revamped:

  - `azure.common.credentials` or `msrestazure.azure_active_directory` instances are no longer supported, use the `azure-identity` classes instead: https://pypi.org/project/azure-identity/
  - `credentials` parameter has been renamed `credential`

- The `config` attribute no longer exists on a client, configuration should be passed as kwarg. Example: `MyClient(credential, subscription_id, enable_logging=True)`. For a complete set of
  supported options, see the [parameters accept in init documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)
- You can't import a `version` module anymore, use `__version__` instead
- Operations that used to return a `msrest.polling.LROPoller` now returns a `azure.core.polling.LROPoller` and are prefixed with `begin_`.
- Exceptions tree have been simplified and most exceptions are now `azure.core.exceptions.HttpResponseError` (`CloudError` has been removed).
- Most of the operation kwarg have changed. Some of the most noticeable:

  - `raw` has been removed. Equivalent feature can be found using `cls`, a callback that will give access to internal HTTP response for advanced user
  - For a complete set of
  supported options, see the [parameters accept in Request documentation of azure-core](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/core/azure-core/CLIENT_LIBRARY_DEVELOPER.md#available-policies)

**General new features**

- Type annotations support using `typing`. SDKs are mypy ready.
- This client has now stable and official support for async. Check the `aio` namespace of your package to find the async client.
- This client now support natively tracing library like OpenCensus or OpenTelemetry. See this [tracing quickstart](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/core/azure-core-tracing-opentelemetry) for an overview.

## 0.21.0 (2020-09-03)

**Features**

  - Model DatabaseUpdate has a new parameter storage_account_type
  - Model Database has a new parameter storage_account_type
  - Model BackupShortTermRetentionPolicy has a new parameter diff_backup_interval_in_hours
  - Model ManagedInstance has a new parameter storage_account_type
  - Model ManagedInstance has a new parameter provisioning_state
  - Model ManagedInstanceUpdate has a new parameter storage_account_type
  - Model ManagedInstanceUpdate has a new parameter provisioning_state
  - Added operation DatabasesOperations.list_inaccessible_by_server
  - Added operation ServersOperations.import_database
  - Added operation group ImportExportOperations
  - Added operation group ServerAzureADOnlyAuthenticationsOperations
  - Added operation group ManagedInstanceAzureADOnlyAuthenticationsOperations

**Breaking changes**

  - Operation BackupShortTermRetentionPoliciesOperations.create_or_update has a new signature
  - Operation BackupShortTermRetentionPoliciesOperations.update has a new signature
  - Removed operation DatabasesOperations.import_method
  - Removed operation DatabasesOperations.create_import_operation
  - Removed operation ServerAzureADAdministratorsOperations.disable_azure_ad_only_authentication

## 0.20.0 (2020-06-22)

**Features**

  - Model ManagedDatabase has a new parameter last_backup_name
  - Model ManagedDatabase has a new parameter auto_complete_restore
  - Model ManagedDatabaseUpdate has a new parameter last_backup_name
  - Model ManagedDatabaseUpdate has a new parameter auto_complete_restore
  - Model ManagedInstanceOperation has a new parameter operation_parameters
  - Model ManagedInstanceOperation has a new parameter operation_steps

## 0.19.0 (2020-06-22)

**Features**

  - Model SyncGroup has a new parameter use_private_link_connection
  - Model ManagedInstanceUpdate has a new parameter maintenance_configuration_id
  - Model SyncMember has a new parameter use_private_link_connection
  - Model SyncMember has a new parameter sync_member_azure_database_resource_id
  - Model ManagedInstance has a new parameter maintenance_configuration_id
  - Added operation ExtendedDatabaseBlobAuditingPoliciesOperations.list_by_database
  - Added operation ManagedInstancesOperations.failover
  - Added operation ReplicationLinksOperations.unlink
  - Added operation ExtendedServerBlobAuditingPoliciesOperations.list_by_server

# 0.18.0 (2020-03-23)

**Features**

  - Added operation group ManagedInstanceOperations

# 0.17.0 (2020-03-02)

**Features**

  - Model ManagedInstanceUpdate has a new parameter minimal_tls_version
  - Model ServerAzureADAdministrator has a new parameter azure_ad_only_authentication
  - Model ManagedDatabase has a new parameter long_term_retention_backup_resource_id
  - Model ManagedDatabaseUpdate has a new parameter long_term_retention_backup_resource_id
  - Model SensitivityLabel has a new parameter rank
  - Model ServerUpdate has a new parameter private_endpoint_connections
  - Model ServerUpdate has a new parameter minimal_tls_version
  - Model ServerUpdate has a new parameter public_network_access
  - Model Server has a new parameter private_endpoint_connections
  - Model Server has a new parameter minimal_tls_version
  - Model Server has a new parameter public_network_access
  - Model ManagedInstance has a new parameter minimal_tls_version
  - Added operation ServerAzureADAdministratorsOperations.disable_azure_ad_only_authentication
  - Added operation ManagedDatabasesOperations.list_inaccessible_by_instance
  - Added operation group ManagedInstanceLongTermRetentionPoliciesOperations
  - Added operation group LongTermRetentionManagedInstanceBackupsOperations

## 0.16.0 (2019-12-17)

**Features**

  - Model ExtendedServerBlobAuditingPolicy has a new parameter
    queue_delay_ms
  - Model EditionCapability has a new parameter read_scale
  - Model EditionCapability has a new parameter
    supported_storage_capabilities
  - Model ServiceObjectiveCapability has a new parameter compute_model
  - Model ServiceObjectiveCapability has a new parameter
    supported_auto_pause_delay
  - Model ServiceObjectiveCapability has a new parameter zone_redundant
  - Model ServiceObjectiveCapability has a new parameter
    supported_min_capacities
  - Model ManagedInstanceVersionCapability has a new parameter
    supported_instance_pool_editions
  - Model DatabaseBlobAuditingPolicy has a new parameter
    queue_delay_ms
  - Model ExtendedDatabaseBlobAuditingPolicy has a new parameter
    queue_delay_ms
  - Model ManagedInstanceVcoresCapability has a new parameter
    supported_storage_sizes
  - Model ManagedInstanceVcoresCapability has a new parameter
    instance_pool_supported
  - Model ManagedInstanceVcoresCapability has a new parameter
    standalone_supported
  - Model ManagedInstanceVcoresCapability has a new parameter
    included_max_size
  - Model ServerBlobAuditingPolicy has a new parameter queue_delay_ms
  - Model ElasticPoolPerformanceLevelCapability has a new parameter
    zone_redundant
  - Added operation group WorkloadGroupsOperations
  - Added operation group WorkloadClassifiersOperations

**Breaking changes**

  - Operation ServerAzureADAdministratorsOperations.create_or_update
    has a new signature
  - Model ManagedInstanceFamilyCapability no longer has parameter
    supported_storage_sizes
  - Model ManagedInstanceFamilyCapability no longer has parameter
    included_max_size

## 0.15.0 (2019-11-12)

**Breaking changes**

  - Operation DatabasesOperations.failover has a new signature
  - Operation ManagedInstanceAdministratorsOperations.get has a new
    signature
  - Operation ManagedInstanceAdministratorsOperations.delete has a new
    signature
  - Operation ManagedInstanceAdministratorsOperations.create_or_update
    has a new signature

## 0.14.0 (2019-10-04)

**Features**

  - Added operation
    ServerBlobAuditingPoliciesOperations.list_by_server
  - Added operation ManagedDatabasesOperations.complete_restore
  - Added operation
    DatabaseBlobAuditingPoliciesOperations.list_by_database
  - Added operation group ManagedDatabaseRestoreDetailsOperations

## 0.13.0 (2019-09-03)

**Features**

  - Model ManagedInstanceUpdate has a new parameter
    source_managed_instance_id
  - Model ManagedInstanceUpdate has a new parameter instance_pool_id
  - Model ManagedInstanceUpdate has a new parameter
    restore_point_in_time
  - Model ManagedInstanceUpdate has a new parameter
    managed_instance_create_mode
  - Model SensitivityLabel has a new parameter is_disabled
  - Model Database has a new parameter paused_date
  - Model Database has a new parameter read_replica_count
  - Model Database has a new parameter resumed_date
  - Model Database has a new parameter auto_pause_delay
  - Model Database has a new parameter min_capacity
  - Model ManagedInstance has a new parameter
    source_managed_instance_id
  - Model ManagedInstance has a new parameter instance_pool_id
  - Model ManagedInstance has a new parameter restore_point_in_time
  - Model ManagedInstance has a new parameter
    managed_instance_create_mode
  - Model DatabaseUpdate has a new parameter paused_date
  - Model DatabaseUpdate has a new parameter read_replica_count
  - Model DatabaseUpdate has a new parameter resumed_date
  - Model DatabaseUpdate has a new parameter auto_pause_delay
  - Model DatabaseUpdate has a new parameter min_capacity
  - Added operation
    ManagedInstanceEncryptionProtectorsOperations.revalidate
  - Added operation
    ManagedDatabaseSensitivityLabelsOperations.enable_recommendation
  - Added operation
    ManagedDatabaseSensitivityLabelsOperations.disable_recommendation
  - Added operation ElasticPoolsOperations.failover
  - Added operation ManagedInstancesOperations.list_by_instance_pool
  - Added operation DatabasesOperations.failover
  - Added operation
    LongTermRetentionBackupsOperations.get_by_resource_group
  - Added operation
    LongTermRetentionBackupsOperations.list_by_resource_group_server
  - Added operation
    LongTermRetentionBackupsOperations.delete_by_resource_group
  - Added operation
    LongTermRetentionBackupsOperations.list_by_resource_group_location
  - Added operation
    LongTermRetentionBackupsOperations.list_by_resource_group_database
  - Added operation SensitivityLabelsOperations.enable_recommendation
  - Added operation SensitivityLabelsOperations.disable_recommendation
  - Added operation EncryptionProtectorsOperations.revalidate
  - Added operation group InstancePoolsOperations
  - Added operation group ManagedInstanceAdministratorsOperations
  - Added operation group UsagesOperations
  - Added operation group PrivateLinkResourcesOperations
  - Added operation group PrivateEndpointConnectionsOperations

**Breaking changes**

  - Operation
    ManagedDatabaseSensitivityLabelsOperations.list_recommended_by_database
    has a new signature
  - Operation
    SensitivityLabelsOperations.list_recommended_by_database has a
    new signature
  - Operation EncryptionProtectorsOperations.create_or_update has a
    new signature

**General breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes if from some import. In summary, some modules
were incorrectly visible/importable and have been renamed. This fixed
several issues caused by usage of classes that were not supposed to be
used in the first place.

  - SqlManagementClient cannot be imported from
    `azure.mgmt.sql.sql_management_client` anymore (import from
    `azure.mgmt.sqlmanagement` works like before)
  - SqlManagementClientConfiguration import has been moved from
    `azure.mgmt.sqlmanagement.sql_management_client` to
    `azure.mgmt.sqlmanagement`
  - A model `MyClass` from a "models" sub-module cannot be imported
    anymore using `azure.mgmt.sqlmanagement.models.my_class` (import
    from `azure.mgmt.sqlmanagement.models` works like before)
  - An operation class `MyClassOperations` from an `operations`
    sub-module cannot be imported anymore using
    `azure.mgmt.sqlmanagement.operations.my_class_operations`
    (import from `azure.mgmt.sqlmanagement.operations` works like
    before)

Last but not least, HTTP connection pooling is now enabled by default.
You should always use a client as a context manager, or call close(), or
use no more than one client per process.

## 0.12.0 (2019-03-28)

**Features**

  - Model ManagedDatabase has a new parameter recoverable_database_id
  - Model ManagedDatabase has a new parameter
    restorable_dropped_database_id
  - Model ServerSecurityAlertPolicy has a new parameter creation_time
  - Model ManagedInstanceUpdate has a new parameter
    public_data_endpoint_enabled
  - Model ManagedInstanceUpdate has a new parameter proxy_override
  - Model ManagedInstanceUpdate has a new parameter timezone_id
  - Model ManagedDatabaseUpdate has a new parameter
    recoverable_database_id
  - Model ManagedDatabaseUpdate has a new parameter
    restorable_dropped_database_id
  - Model ManagedInstance has a new parameter
    public_data_endpoint_enabled
  - Model ManagedInstance has a new parameter proxy_override
  - Model ManagedInstance has a new parameter timezone_id
  - Added operation group ManagedServerSecurityAlertPoliciesOperations
  - Added operation group VirtualClustersOperations
  - Added operation group
    ManagedRestorableDroppedDatabaseBackupShortTermRetentionPoliciesOperations
  - Added operation group RestorableDroppedManagedDatabasesOperations
  - Added operation group ManagedDatabaseSensitivityLabelsOperations
  - Added operation group RecoverableManagedDatabasesOperations
  - Added operation group ServerVulnerabilityAssessmentsOperations
  - Added operation group
    ManagedInstanceVulnerabilityAssessmentsOperations
  - Added operation group ManagedDatabaseSecurityAlertPoliciesOperations
  - Added operation group SensitivityLabelsOperations

## 0.11.0 (2018-11-08)

**Features**

  - Model ServerBlobAuditingPolicy has a new parameter
    is_azure_monitor_target_enabled
  - Model ExtendedServerBlobAuditingPolicy has a new parameter
    is_azure_monitor_target_enabled
  - Model DatabaseBlobAuditingPolicy has a new parameter
    is_azure_monitor_target_enabled
  - Model ExtendedDatabaseBlobAuditingPolicy has a new parameter
    is_azure_monitor_target_enabled
  - Added operation
    DatabaseVulnerabilityAssessmentsOperations.list_by_database
  - Added operation
    ManagedDatabaseVulnerabilityAssessmentsOperations.list_by_database
  - Added operation group
    ManagedBackupShortTermRetentionPoliciesOperations

## 0.10.0 (2018-10-18)

**Features**

  - Model DatabaseVulnerabilityAssessment has a new parameter
    storage_account_access_key
  - Model ManagedInstanceUpdate has a new parameter dns_zone_partner
  - Model ManagedInstanceUpdate has a new parameter collation
  - Model ManagedInstanceUpdate has a new parameter dns_zone
  - Model ManagedInstance has a new parameter dns_zone_partner
  - Model ManagedInstance has a new parameter collation
  - Model ManagedInstance has a new parameter dns_zone
  - Added operation
    BackupShortTermRetentionPoliciesOperations.list_by_database
  - Added operation group
    ManagedDatabaseVulnerabilityAssessmentsOperations
  - Added operation group ExtendedDatabaseBlobAuditingPoliciesOperations
  - Added operation group TdeCertificatesOperations
  - Added operation group ManagedInstanceKeysOperations
  - Added operation group ServerBlobAuditingPoliciesOperations
  - Added operation group ManagedInstanceEncryptionProtectorsOperations
  - Added operation group ExtendedServerBlobAuditingPoliciesOperations
  - Added operation group ServerSecurityAlertPoliciesOperations
  - Added operation group
    ManagedDatabaseVulnerabilityAssessmentScansOperations
  - Added operation group ManagedInstanceTdeCertificatesOperations
  - Added operation group
    ManagedDatabaseVulnerabilityAssessmentRuleBaselinesOperations

**Breaking changes**

  - Operation
    DatabaseVulnerabilityAssessmentRuleBaselinesOperations.delete has a
    new signature
  - Operation DatabaseVulnerabilityAssessmentRuleBaselinesOperations.get
    has a new signature
  - Operation
    DatabaseVulnerabilityAssessmentRuleBaselinesOperations.create_or_update
    has a new signature

**Note**

  - azure-mgmt-nspkg is not installed anymore on Python 3 (PEP420-based
    namespace package)

## 0.9.1 (2018-05-24)

**Features**

  - Managed instances, databases, and failover groups
  - Vulnerability assessments
  - Backup short term retention policies
  - Elastic Jobs

## 0.9.0 (2018-04-25)

**General Breaking changes**

This version uses a next-generation code generator that *might*
introduce breaking changes.

  - Model signatures now use only keyword-argument syntax. All
    positional arguments must be re-written as keyword-arguments. To
    keep auto-completion in most cases, models are now generated for
    Python 2 and Python 3. Python 3 uses the "*" syntax for
    keyword-only arguments.
  - Enum types now use the "str" mixin (class AzureEnum(str, Enum)) to
    improve the behavior when unrecognized enum values are encountered.
    While this is not a breaking change, the distinctions are important,
    and are documented here:
    <https://docs.python.org/3/library/enum.html#others> At a glance:
      - "is" should not be used at all.
      - "format" will return the string value, where "%s" string
        formatting will return `NameOfEnum.stringvalue`. Format syntax
        should be prefered.
  - New Long Running Operation:
      - Return type changes from
        `msrestazure.azure_operation.AzureOperationPoller` to
        `msrest.polling.LROPoller`. External API is the same.
      - Return type is now **always** a `msrest.polling.LROPoller`,
        regardless of the optional parameters used.
      - The behavior has changed when using `raw=True`. Instead of
        returning the initial call result as `ClientRawResponse`,
        without polling, now this returns an LROPoller. After polling,
        the final resource will be returned as a `ClientRawResponse`.
      - New `polling` parameter. The default behavior is
        `Polling=True` which will poll using ARM algorithm. When
        `Polling=False`, the response of the initial call will be
        returned without polling.
      - `polling` parameter accepts instances of subclasses of
        `msrest.polling.PollingMethod`.
      - `add_done_callback` will no longer raise if called after
        polling is finished, but will instead execute the callback right
        away.

**SQL Breaking changes**

  -   - Database and ElasticPool now use Sku property for scale and
        tier-related properties. We have made this change in order to
        allow future support of autoscale, and to allow for new
        vCore-based editions.

          - Database.sku has replaced
            Database.requested_service_objective_name and
            Database.edition. Database scale can be set by setting
            Sku.name to the requested service objective name (e.g. S0,
            P1, or GP_Gen4_1), or by setting Sku.name to the sku name
            (e.g. Standard, Premium, or GP_Gen4) and set Sku.capacity
            to the scale measured in DTU or vCores.
          - Database.current_sku has replaced
            Database.service_level_objetive.
          - Database.current_service_objective_id and
            Database.requested_service_objective_id have been
            removed.
          - ElasticPool.sku has replaced ElasticPool.dtu. Elastic pool
            scale can be set by setting Sku.name to the requested sku
            name (e.g. StandardPool, PremiumPool, or GP_Gen4) and
            setting Sku.capacity to the scale measured in DTU or vCores.
          - ElasticPool.per_database_settings has replaced
            ElasticPool.database_dtu_min and
            ElasticPool.database_dtu_max.

  - Database.max_size_bytes is now an integer instead of string.

  - LocationCapabilities tree has been changed in order to support
    capabilities of new vCore-based database and elastic pool editions.

**Features**

  - Added support for List and Cancel operation on Azure database and
    elastic pool REST API
  - Added Long Term Retention V2 commands, including getting backups,
    deleting backups, setting the V2 policies, and getting the V2
    policies
      - Removed support for managing Vaults used for Long Term Retention
        V1
      - Changed BackupLongTermRetentionPolicy class, removing the Long
        Term Retention V1 properties and adding the Long Term Retention
        V2 properties
      - Removed BackupLongTermRetentionPolicyState

## 0.8.6 (2018-03-22)

**Features**

  - Added support for List and Cancel operation on Azure database and
    elastic pool REST API
  - Added support for Auto-tuning REST API

## 0.8.5 (2018-01-18)

**Features**

  - Added support for renaming databases
  - Added missing database editions and service objectives
  - Added ability to list long term retention vaults & policies

## 0.8.4 (2017-11-14)

**Features**

  - Added support for subscription usages

## 0.8.3 (2017-10-24)

**Features**

  - Added support for database zone redundant property
  - Added support for server dns aliases

## 0.8.2 (2017-10-18)

**Features**

  - Added support for state and migration flag properties for SQL Vnet
    rules

## 0.8.1 (2017-10-04)

**Features**

  - Add database.cancel operation
  - Add database.list_by_database

## 0.8.0 (2017-09-07)

**Disclaimer**

We were using a slightly unorthodox convention for some operation ids.
Some resource operations were "nested" inside others, e.g. blob auditing
policies was nested inside databases as in
client.databases.get_blob_auditing_policies(..) instead of the
flattened ARM standard
client.database_blob_auditing_policies.get(...).

This convention has lead to some inconsistencies, makes some APIs
difficult to find, and is at odds with future APIs. For example if we
wanted to implement listing db audit policies by server, continuing the
current convention would be
client.databases.list_blob_auditing_policies_by_server(..) which
makes much less sense than the ARM standard which would
beclient.database_blob_auditing_policies.list_by_server(...)`.

In order to resolve this and provide a good path moving forward, we have
renamed the inconsistent operations to follow the ARM standard. This is
an unfortunate breaking change, but it's best to do now while the SDK is
still in preview and since most of these operations were only recently
added.

**Breaking changes**

  - client.database.get_backup_long_term_retention_policy ->
    client.backup_long_term_retention_policies.get
  - client.database.create_or_update_backup_long_term_retention_policy
    ->
    client.backup_long_term_retention_policies.create_or_update
  - client.servers.create_backup_long_term_retention_vault ->
    client.backup_long_term_retention_vaults.create_or_update
  - client.servers.get_backup_long_term_retention_vault ->
    client.backup_long_term_retention_vaults.get
  - client.database.list_restore_points ->
    client.restore_points.list_by_database
  - client.servers.create_or_update_connection_policy ->
    client.server_connection_policies.create_or_update
  - client.servers.get_connection_policy ->
    client.server_connection_policies.get
  - client.databases.create_or_update_data_masking_policy ->
    client.data_masking_policies.create_or_update
  - client.databases.get_data_masking_policy ->
    client.data_masking_policies.get
  - client.databases.create_or_update_data_masking_rule ->
    client.data_masking_rules.create_or_update
  - client.databases.get_data_masking_rule ->
    client.data_masking_rules.get
  - client.databases.list_data_masking_rules ->
    client.data_masking_rules.list_by_database
  - client.databases.get_threat_detection_policy ->
    client.database_threat_detection_policies.get
  - client.databases.create_or_update_threat_detection_policy ->
    client.database_threat_detection_policies.create_or_update
  - client.databases.create_or_update_geo_backup_policy ->
    client.geo_backup_policies.create_or_update
  - client.databases.get_geo_backup_policy ->
    client.geo_backup_policies.get
  - client.databases.list_geo_backup_policies ->
    client.geo_backup_policies.list_by_database
  - client.databases.delete_replication_link ->
    client.replication_links.delete
  - client.databases.get_replication_link ->
    client.replication_links.get
  - client.databases.failover_replication_link ->
    client.replication_links.failover
  - client.databases.failover_replication_link_allow_data_loss ->
    client.replication_links.failover_allow_data_loss
  - client.databases.list_replication_links ->
    client.replication_links.list_by_database
  - client.server_azure_ad_administrators.list ->
    client.server_azure_ad_administrators.list_by_server
  - client.servers.get_service_objective ->
    client.service_objectives.get
  - client.servers.list_service_objectives ->
    client.service_objectives.list_by_server
  - client.elastic_pools.list_activity ->
    client.elastic_pool_activities.list_by_elastic_pool
  - client.elastic_pools.list_database_activity ->
    client.elastic_pool_database_activities.list_by_elastic_pool
  - client.elastic_pools.get_database ->
    client.databases.get_by_elastic_pool
  - client.elastic_pools.list_databases ->
    client.databases.list_by_elastic_pool
  - client.recommended_elastic_pools.get_databases ->
    client.databases.get_by_recommended_elastic_pool
  - client.recommended_elastic_pools.list_databases ->
    client.databases.list_by_recommended_elastic_pool
  - client.databases.get_service_tier_advisor ->
    client.service_tier_advisors.get
  - client.databases.list_service_tier_advisors ->
    client.service_tier_advisors.list_by_database
  - client.databases.create_or_update_transparent_data_encryption_configuration
    -> client.transparent_data_encryptions.create_or_update
  - client.databases.get_transparent_data_encryption_configuration
    -> client.transparent_data_encryptions.get
  - client.databases.list_transparent_data_encryption_activity ->
    client.transparent_data_encryption_activities.list_by_configuration
  - client.servers.list_usages ->
    client.server_usages.list_by_server
  - client.databases.list_usages ->
    client.database_usages.list_by_database
  - client.databases.get_blob_auditing_policy ->
    client.database_blob_auditing_policies.get
  - client.databases.create_or_update_blob_auditing_policy ->
    client.database_blob_auditing_policies.create_or_update
  - client.servers.list_encryption_protectors, ->
    client.encryption_protectors.list_by_server
  - client.servers.get_encryption_protector ->
    client.encryption_protectors.get
  - client.servers.create_or_update_encryption_protector ->
    client.encryption_protectors.create_or_update
  - Database blob auditing policy state is required
  - Failover group resource now has required properties defined

**Features**

  - Add SQL DB, server, and pool PATCH operations
  - client.operations.list now returnes a full list of operations and
    not a limited subset (2014-04-01 to 2015-05-01-preview)

**Fixed bugs**

  - Fixed KeyError in server_azure_ad_administrators_operations.get

## 0.7.1 (2017-06-30)

  - Added support for server connection policies
  - Fixed error in
    databases_operations.create_or_update_threat_detection_policy

## 0.7.0 (2017-06-28)

**Features**

  - Backup/Restore related: RecoverableDatabase,
    RestorableDroppedDatabase, BackupLongTermRetentionVault,
    BackupLongTermRetentionPolicy, and GeoBackupPolicy
  - Data Masking rules and policies
  - Server communication links

**Breaking changes**

  - Renamed enum RestorePointTypes to RestorePointType
  - Renamed VnetFirewallRule and related operations to
    VirtualNetworkRule

## 0.6.0 (2017-06-13)

  - Updated Servers api version from 2014-04-01 to 2015-05-01-preview,
    which is SDK compatible and includes support for server managed
    identity
  - Added support for server keys and encryption protectors
  - Added support for check server name availability
  - Added support for virtual network firewall rules
  - Updated server azure ad admin from swagger
  - Minor nonfunctional updates to database blob auditing
  - Breaking changes DatabaseMetrics and ServerMetrics renamed to
    DatabaseUsage and ServerUsage. These were misleadingly named because
    metrics is a different API.
  - Added database metrics and elastic pool metrics

## 0.5.3 (2017-06-01)

  - Update minimal dependency to msrestazure 0.4.8

## 0.5.2 (2017-05-31)

**Features**

  - Added support for server active directory administrator, failover
    groups, and virtual network rules
  - Minor changes to database auditing support

## 0.5.1 (2017-04-28)

**Bugfixes**

  - Fix return exception in import/export

## 0.5.0 (2017-04-19)

**Breaking changes**

  - `SqlManagementClient.list_operations` is now
    `SqlManagementClient.operations.list`

**New features**

  - Added elastic pool capabilities to capabilities API.

**Notes**

  - This wheel package is now built with the azure wheel extension

## 0.4.0 (2017-03-22)

Capabilities and security policy features.

Also renamed several types and operations for improved clarify and
consistency.

Additions:

  - BlobAuditingPolicy APIs (e.g.
    databases.create_or_update_blob_auditing_policy)
  - ThreatDetectionPolicy APIs (e.g.
    databases.create_or_update_threat_detection_policy)
  - databases.list_by_server now supports $expand parameter
  - Capabilities APIs (e.g. capabilities.list_by_location)

Classes and enums renamed:

  - ServerFirewallRule -> FirewallRule
  - DatabaseEditions -> DatabaseEdition
  - ElasticPoolEditions -> ElasticPoolEdition
  - ImportRequestParameters -> ImportRequest
  - ExportRequestParameters -> ExportRequest
  - ImportExportOperationResponse -> ImportExportResponse
  - OperationMode -> ImportOperationMode
  - TransparentDataEncryptionStates -> TransparentDataEncryptionStatus

Classes removed:

  - Unused types: UpgradeHint, Schema, Table, Column

Operations renamed:

  - servers.get_by_resource_group -> servers.get
  - servers.create_or_update_firewall_rule ->
    firewall_rules.create_or_update, and similar for get, list, and
    delete
  - databases.import -> databases.create_import_operation
  - servers.import -> databases.import
  - databases.pause_data_warehouse -> databases.pause
  - databases.resume_data_warehouse -> databases.resume
  - recommended_elastic_pools.list ->
    recommended_elastic_pools.list_by_server

Operations removed:

  - Removed ImportExport operation results APIs since these are handled
    automatically by Azure async pattern.

## 0.3.3 (2017-03-14)

  - Add database blob auditing and threat detection operations

## 0.3.2 (2017-03-08)

  - Add import/export operations
  - Expanded documentation of create modes

## 0.3.1 (2017-03-01)

  - Added ‘filter’ param to list databases

## 0.3.0 (2017-02-27)

**Breaking changes**

  - Enums:
      - createMode renamed to CreateMode
      - Added ReadScale, SampleName, ServerState
  - Added missing Database properties (failover_group_id,
    restore_point_in_time, read_scale, sample_name)
  - Added missing ElasticPoolActivity properties ([requested](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/sql/azure-mgmt-sql)*)
  - Added missing ReplicationLink properties (is_termination_allowed,
    replication_mode)
  - Added missing Server properties ([external_administrator](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/sql/azure-mgmt-sql)*,
    state)
  - Added operations APIs
  - Removed unused Database.upgrade_hint property
  - Removed unused RecommendedDatabaseProperties class
  - Renamed incorrect RecommendedElasticPool.databases_property to
    databases
  - Made firewall rule start/end ip address required
  - Added missing kind property to many resources
  - Many doc clarifications

## 0.2.0 (2016-12-12)

**Breaking changes**

  - Parameters re-ordering (list_database_activity)
  - Flatten create_or_update_firewall_rule from "parameters" to
    "start_ip_address" and "end_ip_address"

## 0.1.0 (2016-11-02)

  - Initial Release
