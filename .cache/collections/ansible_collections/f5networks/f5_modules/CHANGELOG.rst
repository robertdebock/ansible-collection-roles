==============================================
F5Networks F5_Modules Collection Release Notes
==============================================

.. contents:: Topics


v1.9.0
======

Minor Changes
-------------

- Add token refresh handling to bigiq local client
- Added requirement to install ipaddress package for python versions earlier than 3.5

Deprecated Features
-------------------

- Support for Python versions earlier than 3.5 is being deprecated

Bugfixes
--------

- Added Fix for bigip_config check mode issue
- Fix for bigip_device_license license reactivation
- Fix for documentation bigip_data_group module doesn't check records content
- Fix issue with expired tokens causing module run to fail in bigiq_device_discovery
- Fix lookup plugin support for bigiq_license
- Fixes issues with downloading ASM policies in binary format

v1.8.0
======

Minor Changes
-------------

- Add disable action and appropriate scenarios to bigip_policy_rule module
- Add ends_with_any condition to bigip_policy_rule module
- Add http_header condition type with header_is_any condition to bigip_policy_rule module
- Add insert action and appropriate scenarios to bigip_policy_rule module
- Add path_contains condition to bigip_policy_rule module
- Add path_is_any option to conditions in bigip_policy_rule module
- Add remove action and appropriate scenarios to bigip_policy_rule module
- Add replace action and appropriate scenarios to bigip_policy_rule module
- Event types are now supported with forward type action
- Event types are now supported with reset type action
- Policy support with condition type TCP match with any of address/datagroup

Removed Features (previously deprecated)
----------------------------------------

- Removed TMOS v11 support for bigip_gtm_pool and bigip_gtm_wide_ip modules
- Removed quorum and monitor_type parameters in bigip_node module. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html
- Removed syslog_settings and pool_settings parameters in bigip_log_destination moduke. See porting guides section at https://clouddocs.f5.com/products/orchestration/ansible/devel/usage/porting-guides.html

Bugfixes
--------

- Fix a bug with replace_with_all logic to consider ports in bigip_pool_member module
- Fix control characters causing url encoding errors in bigip_policy module
- Fix issue in bigip_pool_member module invwhere incorrect IF statement in function preveninv ted from reusing FQDN nodes for new pool members
- Fix issue where error messages were replaced by generic error message in bigip_device_policy module
- Fix issue with destination_address and destination_port parameters not being properly returned by bigip_device_info module
- Fix issue with removal action not allowing atomic rule updates in bigip_policy_rule module
- Fix virtual server type value displaying incorrect information in bigip_device_info module

v1.7.0
======

Major Changes
-------------

- Added async_timeout parameter to bigip_ucs_fetch module to allow customization of module wait for async interface
- Changed bigip_ucs_fetch module to use asynchronous interface when generating UCS files

Minor Changes
-------------

- Add better error handling for TEEM telemetry connection
- Changed apm_policy_fetch module to use standard download function

Bugfixes
--------

- Fix AFM firewall address list error
- Fix GTM virtual server depenedncy where path to Iapp resources were incorrectly stripped.
- Fix apm policy existence checks in bigip_apm_policy_fetch module
- Fix asm policy existence checks in bigip_asm_policy_fetch module
- Fix bigip_management_route module not idempotent
- Fix host_begins_with_any, host_is_any, server_name_is_any and host_is_not_any parameters of the bigip_policy_rule module to enforce list as the required parameter type. Change was required since in Ansible a string conversion is applied when the provided argument type is not matching the expected one causing undesired side effects.
- Fix idempotency issue with gateway_address and route domain in bigip_static_route module
- Fix issue with bigip_asm_policy_fetch where existing file would break the module run
- Fix issue with bigip_asm_policy_fetch where similiar policy names would cause wrong policy to be fetched
- Fix issue with bigip_asm_policy_manage where similiar policy names would cause wrong policy id to be selected
- Fix iteration bug in bigiq_device_info module

v1.6.0
======

Major Changes
-------------

- Add phone home Teem integration into all modules, functionality can be disabled by setting up F5_TEEM environment variable or no_f5_teem provider parameter

Minor Changes
-------------

- Add AS3 declaration information to the bigip_device_info module
- Add AS3, TS, CFE, and DO information to the bigip_device_info module
- Add CFE declaration information to the bigip_device_info module
- Add DO declaration information to the bigip_device_info module
- Add TS declaration information to the bigip_device_info module
- Add access policy information to the bigip_device_info module
- Add access profile information to the bigip_device_info module
- Add meaningful error message for the wait_for parameter in the bigip_command module
- Add parent_policies and policies_pending_changes information parameters to obtain when gathering asm-policy-stats
- Add remote_syslog information to the bigip_device_info module.
- Add renewal option to the bigip_device_license module
- Add reuse_objects parameter to the bigip_apm_policy_import module
- Add sync-status information to the bigip_device_info module
- Add the ability to import API Protection policies to the bigip_apm_policy_import module
- Added apply information parameter to indicate if an ASM policy has pending changes that need to be applied.
- Changed the meaning of policies_active and policies_inactive stat information due to changes in TMOS 13.x
- New bigip_ssl_key_cert module to manage SSL certificates and keys with the transaction interface

Removed Features (previously deprecated)
----------------------------------------

- Removed arp_state parameter from the bigip_virtual_address module

Bugfixes
--------

- Changed unicast_failover element type to dictionary
- Fix force parameter set to yes causing list index out of range error
- Fix invalid parameter name in the bigip_config_sync action module
- Fix issue where ASM file download needs to be chunked for larger files.
- Fix issue with retaining package files in the bigip_lx_package module
- Fix key error in list comprehension in the AsmPolicyStatsParameters class
- Fix missing ssh-keyfile parameter causing key error in the bigip action plugin

New Modules
-----------

- bigip_ssl_key_cert - Import/Delete SSL keys and certs from BIG-IP

v1.5.0
======

Bugfixes
--------

- Fix issue with control characters in pool_id in bigiq_regkey_license_assignment module
- Fix the download of an APM policy in bigip_apm_policy_fetch module

v1.4.0
======

Major Changes
-------------

- Remove redundant parameters in f5_provider to fix disparity between documentation and module parameters

Minor Changes
-------------

- Add SSH connection type capability to bigip_wait module
- Add apply option to bigip_asm_policy_manage module
- Add retain_package_file option to bigip_lx_package module
- New bigip_asm_advanced_settings module to manage ASM settings
- New bigip_gtm_dns_listener module to manage DNS listener configuration

Bugfixes
--------

- Fix ASM policy import issue by users with web-application-security-administrator role
- Fix idempotency when using true_names parameter in bigip_profile_client_ssl module

New Modules
-----------

- bigip_asm_advanced_settings - Manages BIG-IP system ASM advanced settings.
- bigip_gtm_dns_listener - Configures the BIG-IP DNS system to answer TCP or UDP DNS requests.

v1.3.0
======

Major Changes
-------------

- Broke apart bigip_device_auth_radius to implement radius server configuration in bigip_device_auth_server module. Refer to module documentation for usage details

Minor Changes
-------------

- Add SSL certificate subject_alternative_name information to bigip_device_info module
- Add ability to install software images on vCMP guests with the bigip_software_install module
- Add cipher_list parameter to bigip_monitor_https
- Add hw_syn_cookie parameter to bigip_vlan module
- Add option to bypass all module validation for bigip_virtual_server
- Add pool order option to bigip_gtm_wide_ip module
- Add pva_acceleration parameter to bigip_profile_fastl4 module
- Add set_variable type to bigip_policy_rule module
- Add time_wait_timeout parameter to bigip_profile_tcp module
- Add use_for_auth parameter to bigip_device_auth_ldap module to allow setting up LDAP as the authentication source
- New bigip_device_auth_radius server module to manage radius server configuration
- New bigip_monitor_mysql module to manage mySQL monitor configuration
- New bigip_monitor_oracle module to manage oracle monitor configuration
- New bigip_ssl_csr_module to create CSR files

Removed Features (previously deprecated)
----------------------------------------

- Remove bigip_appsvcs_extension module

Bugfixes
--------

- Fix invalid data type of partition_access parameter in the bigip_user module

New Modules
-----------

- bigip_device_auth_radius - Manages RADIUS auth configuration on a BIG-IP.
- bigip_device_auth_radius_server - Manages the RADIUS server configuration on a BIG-IP.
- bigip_monitor_mysql - Manages BIG-IP MySQL monitors.
- bigip_monitor_oracle - Manages BIG-IP Oracle monitors.
- bigip_ssl_csr - Creates SSL CSR files on the BIG-IP.

v1.2.0
======

Minor Changes
-------------

- Add ImishConfig class to add duplicate records handling capability
- Add additional dos vectors to bigip_firewall_dos_vector_module
- Add addon_keys parameter to bigip_device_license module
- Add aliases for address and port to bigip_monitor_tcp module
- Add allow_duplicates parameter to bigip_imish_config module
- Add check_profiles parameter to bypass profile verification ability in bigip_virtual_server module
- Add cipher_group parameter to bigip_profile_client_ssl module
- Add dns-oversize DNS protocol security vector to bigip_firewall_doc_vector
- Add forward_node option to bigip_policy_rule module
- Add ipv6-ext-hdr-frames security vector to bigip_firewall_doc_vector
- Add management routes information to bigip_device_info module
- Add support for BIG-IQ 7.0 and above to bigiq_device_info module
- Add virtual server policies information to bigip_device_info
- New bigip_device_auth_radius module to manage RADIUS auth configuration

Bugfixes
--------

- Change bigip_data_group module's records parameter type to 'raw'
- Fix '?' character handling in value for bigip_data_group module
- Fix a bug with using the true_name parameter in the bigip_profile_client_ssl module
- Fix an issue with /32 IPV6 subnets being saved as host rather than a network in bigip_data_group module
- Fix attribute error in bigip_software_install module
- Fix check_profiles boolean parameter conversion in bigip_virtual_server
- Fix handling of duplicate records by the bigip_imish_config module

v1.1.0
======

Minor Changes
-------------

- Add accounting parameter for tacacs type to bigip_device_auth module
- Add fw_enforcement_policy parameter to bigip_selfip module
- Add persist cookie option to bigip_policy_rule module
- Add phase1_lifetime parameter to bigip_ike_peer module
- Add self allow option to bigip_network_globals module
- Add true_names support to bigip_profile_client_ssl modules allowing specifying true filenames of the certificates
- New FTP monitor module for configuring and managing FTP monitors
- New ICMP monitor module for configuring and managing ICMP monitors
- New SMTP monitor module for configuring and managing SMTP monitors
- New universal persistence profile module for configuring and managing universal persistence profiles

Deprecated Features
-------------------

- Deprecated bigip_appsvcs_extension module
- Deprecated bigip_device_facts module name
- Deprecated bigiq_device_facts module name

Removed Features (previously deprecated)
----------------------------------------

- Remove _bigip_iapplx_package alias
- Remove _bigip_security_address_list alias
- Remove _bigip_security_port_list alias
- Remove _bigip_traffic_group alias
- Remove bigip_asm_policy module

Bugfixes
--------

- Fix IPv6 netmask for self IPs in bigip_device_info
- Fix allowing authenticated not authorized users using modules to modify a resource
- Fix save_when parameter not saving the configuration as expected in bigip_imish_config module

New Modules
-----------

- bigip_monitor_ftp - Manages FTP monitors on a BIG-IP.
- bigip_monitor_icmp - Manages F5 BIG-IP LTM ICMP monitors.
- bigip_monitor_smtp - Manages SMTP monitors on a BIG-IP.
- bigip_profile_persistence_universal - Manages universal persistence profiles.

v1.0.0
======

New Plugins
-----------

Lookup
~~~~~~

- bigiq_license - Returns a random license from the list.
- license_hopper - Returns a random license from the list.

New Modules
-----------

- bigip_apm_acl - Manages user-defined APM ACLs.
- bigip_apm_network_access - Manages the APM Network Access resource.
- bigip_apm_policy_fetch - Exports the APM policy or APM access profile from remote nodes.
- bigip_apm_policy_import - Manages BIG-IP APM policy or APM access profile imports.
- bigip_asm_dos_application - Manages application settings for DOS profiles.
- bigip_asm_policy_fetch - Exports the ASM policy from remote nodes.
- bigip_asm_policy_import - Manages BIG-IP ASM policy imports.
- bigip_asm_policy_manage - Manages BIG-IP ASM policies
- bigip_asm_policy_server_technology - Manages the Server Technology on an ASM policy.
- bigip_asm_policy_signature_set - Manages Signature Sets on an ASM policy.
- bigip_cgnat_lsn_pool - Manages CGNAT LSN Pools.
- bigip_cli_alias - Manages CLI aliases on a BIG-IP.
- bigip_cli_script - Manages CLI scripts on a BIG-IP.
- bigip_command - Runs TMSH and BASH commands on F5 devices.
- bigip_config - Manages BIG-IP configuration sections.
- bigip_configsync_action - Performs actions related to configuration synchronization (ConfigSync).
- bigip_data_group - Manages data groups on a BIG-IP.
- bigip_device_auth - Manages system authentication on a BIG-IP.
- bigip_device_auth_ldap - Manages LDAP device authentication settings on BIG-IP.
- bigip_device_certificate - Manages self-signed device certificates.
- bigip_device_connectivity - Manages device IP configuration settings for HA on a BIG-IP.
- bigip_device_dns - Manages BIG-IP device DNS settings.
- bigip_device_group - Manages device groups on a BIG-IP.
- bigip_device_group_member - Manages members in a device group.
- bigip_device_ha_group - Manages HA group settings on a BIG-IP system.
- bigip_device_httpd - Manages HTTPD related settings on BIG-IP.
- bigip_device_info - Collects information from F5 BIG-IP devices.
- bigip_device_license - Manages license installation and activation on BIG-IP devices.
- bigip_device_ntp - Manages NTP servers on a BIG-IP.
- bigip_device_sshd - Manages the SSHD settings of a BIG-IP.
- bigip_device_syslog - Manages system-level syslog settings on BIG-IP.
- bigip_device_traffic_group - Manages traffic groups on BIG-IP.
- bigip_device_trust - Manages the trust relationships between BIG-IPs.
- bigip_dns_cache_resolver - Manages DNS resolver cache configurations on BIG-IP.
- bigip_dns_nameserver - Manages LTM DNS nameservers on a BIG-IP.
- bigip_dns_resolver - Manages DNS resolvers on a BIG-IP.
- bigip_dns_zone - Manages DNS zones on BIG-IP.
- bigip_file_copy - Manages files in datastores on a BIG-IP.
- bigip_firewall_address_list - Manages address lists on BIG-IP AFM.
- bigip_firewall_dos_profile - Manages AFM DoS profiles on a BIG-IP.
- bigip_firewall_dos_vector - Manages the attack vector configuration in an AFM DoS profile.
- bigip_firewall_global_rules - Manages AFM global rule settings on a BIG-IP.
- bigip_firewall_log_profile - Manages AFM logging profiles configured in the system.
- bigip_firewall_log_profile_network - Configures Network Firewall related settings of the log profile.
- bigip_firewall_policy - Manages AFM security firewall policies on a BIG-IP.
- bigip_firewall_port_list - Manages port lists on BIG-IP AFM.
- bigip_firewall_rule - Manages AFM Firewall rules.
- bigip_firewall_rule_list - Manages AFM security firewall policies on a BIG-IP.
- bigip_firewall_schedule - Manages BIG-IP AFM schedule configurations.
- bigip_gtm_datacenter - Manages the Datacenter configuration on a BIG-IP.
- bigip_gtm_global - Manages global GTM settings.
- bigip_gtm_monitor_bigip - Manages F5 BIG-IP GTM BIG-IP monitors.
- bigip_gtm_monitor_external - Manages external GTM monitors on a BIG-IP.
- bigip_gtm_monitor_firepass - Manages F5 BIG-IP GTM FirePass monitors.
- bigip_gtm_monitor_http - Manages F5 BIG-IP GTM HTTP monitors.
- bigip_gtm_monitor_https - Manages F5 BIG-IP GTM HTTPS monitors.
- bigip_gtm_monitor_tcp - Manages F5 BIG-IP GTM TCP monitors.
- bigip_gtm_monitor_tcp_half_open - Manages F5 BIG-IP GTM TCP half-open monitors.
- bigip_gtm_pool - Manages F5 BIG-IP GTM pools.
- bigip_gtm_pool_member - Manages GTM pool member settings.
- bigip_gtm_server - Manages F5 BIG-IP GTM servers.
- bigip_gtm_topology_record - Manages GTM Topology Records.
- bigip_gtm_topology_region - Manages GTM Topology Regions.
- bigip_gtm_virtual_server - Manages F5 BIG-IP GTM virtual servers.
- bigip_gtm_wide_ip - Manages F5 BIG-IP GTM wide IPs.
- bigip_hostname - Manages the hostname of a BIG-IP.
- bigip_iapp_service - Manages TCL iApp services on a BIG-IP.
- bigip_iapp_template - Manages TCL iApp templates on a BIG-IP.
- bigip_ike_peer - Manages IPSec IKE Peer configuration on a BIG-IP.
- bigip_imish_config - Manages the BIG-IP advanced routing configuration sections.
- bigip_interface - Manages BIG-IP physical interfaces.
- bigip_ipsec_policy - Manages IPSec policies on a BIG-IP.
- bigip_irule - Manages iRules across different modules on a BIG-IP.
- bigip_log_destination - Manages log destinations on a BIG-IP.
- bigip_log_publisher - Manages log publishers on a BIG-IP.
- bigip_lx_package - Manages Javascript LX packages on a BIG-IP.
- bigip_management_route - Manages system management routes on a BIG-IP.
- bigip_message_routing_peer - Manages peers for routing generic message protocol messages.
- bigip_message_routing_protocol - Manages generic message parser profiles.
- bigip_message_routing_route - Manages static routes for routing message protocol messages.
- bigip_message_routing_router - Manages router profiles for message-routing protocols.
- bigip_message_routing_transport_config - Manages the configuration for an outgoing connection.
- bigip_monitor_dns - Manages DNS monitors on a BIG-IP.
- bigip_monitor_external - Manages external LTM monitors on a BIG-IP.
- bigip_monitor_gateway_icmp - Manages F5 BIG-IP LTM gateway ICMP monitors.
- bigip_monitor_http - Manages F5 BIG-IP LTM HTTP monitors
- bigip_monitor_https - Manages F5 BIG-IP LTM HTTPS monitors
- bigip_monitor_ldap - Manages BIG-IP LDAP monitors.
- bigip_monitor_snmp_dca - Manages BIG-IP SNMP data collecting agent (DCA) monitors.
- bigip_monitor_tcp_echo - Manages F5 BIG-IP LTM TCP echo monitors.
- bigip_monitor_tcp_half_open - Manages F5 BIG-IP LTM TCP half-open monitors.
- bigip_monitor_udp - Manages F5 BIG-IP LTM UDP monitors.
- bigip_network_globals - Manages network global settings on a BIG-IP.
- bigip_node - Manages F5 BIG-IP LTM nodes.
- bigip_partition - Manages BIG-IP partitions.
- bigip_password_policy - Manages the authentication password policy on a BIG-IP.
- bigip_policy - Manages the general policy configuration on a BIG-IP.
- bigip_policy_rule - Manages LTM policy rules on a BIG-IP.
- bigip_pool_member - Manages F5 BIG-IP LTM pool members.
- bigip_profile_analytics - Manages HTTP analytics profiles on a BIG-IP.
- bigip_profile_client_ssl - Manages client SSL profiles on a BIG-IP.
- bigip_profile_dns - Manages DNS profiles on a BIG-IP.
- bigip_profile_fastl4 - Manages Fast L4 profiles on a BIG-IP.
- bigip_profile_ftp - Manages FTP profiles on a BIG-IP.
- bigip_profile_http - Manages HTTP profiles on a BIG-IP.
- bigip_profile_http2 - Manages HTTP2 profiles on a BIG-IP.
- bigip_profile_http_compression - Manages HTTP compression profiles on a BIG-IP.
- bigip_profile_oneconnect - Manages OneConnect profiles on a BIG-IP.
- bigip_profile_persistence_cookie - Manages cookie persistence profiles on BIG-IP.
- bigip_profile_persistence_src_addr - Manages source address persistence profiles on a BIG-IP.
- bigip_profile_server_ssl - Manages server SSL profiles on a BIG-IP.
- bigip_profile_sip - Manages SIP profiles on a BIG-IP.
- bigip_profile_tcp - Manages TCP profiles on a BIG-IP.
- bigip_profile_udp - Manages UDP profiles on a BIG-IP.
- bigip_provision - Manages BIG-IP module provisioning.
- bigip_qkview - Manages qkviews on the device.
- bigip_remote_role - Manages remote roles on a BIG-IP.
- bigip_remote_syslog - Manipulates remote syslog settings on a BIG-IP.
- bigip_remote_user - Manages the default settings for remote user accounts on a BIG-IP.
- bigip_routedomain - Manages route domains on a BIG-IP.
- bigip_selfip - Manages Self IP addresses on a BIG-IP.
- bigip_service_policy - Manages service policies on a BIG-IP.
- bigip_smtp - Manages SMTP settings on the BIG-IP.
- bigip_snat_pool - Manages SNAT pools on a BIG-IP.
- bigip_snat_translation - Manages SNAT Translations on a BIG-IP.
- bigip_snmp - Manipulates general SNMP settings on a BIG-IP.
- bigip_snmp_community - Manages SNMP communities on a BIG-IP.
- bigip_snmp_trap - Manipulates SNMP trap information on a BIG-IP.
- bigip_software_image - Manages software images on a BIG-IP.
- bigip_software_install - Installs software images on a BIG-IP.
- bigip_software_update - Manages the software update settings of a BIG-IP.
- bigip_ssl_certificate - Imports/Deletes certificates from a BIG-IP.
- bigip_ssl_key - Imports/Deletes SSL keys from a BIG-IP.
- bigip_ssl_ocsp - Manages OCSP configurations on a BIG-IP.
- bigip_static_route - Manipulates static routes on a BIG-IP.
- bigip_sys_daemon_log_tmm - Manages BIG-IP tmm daemon log settings.
- bigip_sys_db - Manages BIG-IP system database variables.
- bigip_sys_global - Manages BIG-IP global settings.
- bigip_timer_policy - Manages timer policies on a BIG-IP.
- bigip_traffic_selector - Manages IPSec Traffic Selectors on a BIG-IP.
- bigip_trunk - Manages trunks on a BIG-IP.
- bigip_tunnel - Manages tunnels on a BIG-IP.
- bigip_ucs - Manages upload, installation, and removal of UCS files.
- bigip_ucs_fetch - Fetches a UCS file from remote nodes.
- bigip_user - Manages user accounts and user attributes on a BIG-IP.
- bigip_vcmp_guest - Manages vCMP guests on a BIG-IP.
- bigip_virtual_address - Manages LTM virtual addresses on a BIG-IP.
- bigip_virtual_server - Manages LTM virtual servers on a BIG-IP.
- bigip_vlan - Manages VLANs on a BIG-IP.
- bigip_wait - Manages the wait time for a BIG-IP condition before continuing.
- bigiq_application_fasthttp - Manages BIG-IQ FastHTTP applications.
- bigiq_application_fastl4_tcp - Manages BIG-IQ FastL4 TCP applications.
- bigiq_application_fastl4_udp - Manages BIG-IQ FastL4 UDP applications.
- bigiq_application_http - Manages BIG-IQ HTTP applications.
- bigiq_application_https_offload - Manages BIG-IQ HTTPS offload applications.
- bigiq_application_https_waf - Manages BIG-IQ HTTPS WAF applications.
- bigiq_device_discovery - Manages BIG-IP devices through BIG-IQ.
- bigiq_device_info - Collects information from F5 BIG-IQ devices.
- bigiq_regkey_license - Manages licenses in a BIG-IQ registration key pool.
- bigiq_regkey_license_assignment - Manages regkey license assignment on BIG-IPs from a BIG-IQ.
- bigiq_regkey_pool - Manages registration key pools on BIG-IQ.
- bigiq_utility_license - Manages utility licenses on a BIG-IQ.
- bigiq_utility_license_assignment - Manages utility license assignment on BIG-IPs from a BIG-IQ.
