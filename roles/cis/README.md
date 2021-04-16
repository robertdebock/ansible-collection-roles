# [cis](#cis)

Apply and/or check recommendations from the CIS benchmarks.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-cis/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cis/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-cis/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cis)|[![quality](https://img.shields.io/ansible/quality/49856)](https://galaxy.ansible.com/robertdebock/cis)|[![downloads](https://img.shields.io/ansible/role/d/49856)](https://galaxy.ansible.com/robertdebock/cis)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-cis.svg)](https://github.com/robertdebock/ansible-role-cis/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.cis

      # 1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored)
      # Modprobe does not work in containers.
      cis_cramfs_disabled: no

      # 1.1.1.2 Ensure mounting of vFAT filesystems is limited (Not Scored)
      # Modprobe does not work in containers.
      cis_vfat_disabled: no

      # 1.1.1.3 Ensure mounting of squashfs filesystems is disabled (Scored)
      # Modprobe does not work in containers.
      cis_squashfs_disabled: no

      # 1.1.1.4 Ensure mounting of udf filesystems is disabled (Scored)
      # Modprobe does not work in containers.
      cis_udf_disabled: no

      # 1.1.5 Ensure noexec option set on /tmp partition (Scored)
      # `noexec` can't be set in a container.
      cis_tmp_noexec: no

      # 1.1.6 Ensure separate partition exists for /var (Scored)
      # Can't create a partition in CI.
      cis_var_partition: no

      # 1.1.7 Ensure separate partition exists for /var/tmp (Scored)
      # Can't create a partition in CI.
      cis_var_tmp_partition: no

      # 1.1.11 Ensure separate partition exists for /var/log (Scored)
      # Can't create a partition in CI.
      cis_var_log_partition: no

      # 1.1.12 Ensure separate partition exists for /var/log/audit (Scored)
      # Can't create a partition in CI.
      cis_var_log_audit_partition: no

      # 1.1.13 Ensure separate partition exists for /home (Scored)
      # Can't create a partition in CI.
      cis_home_partition: no

      # 1.1.23 Disable USB Storage (Scored)
      # Modprobe does not work in containers.
      cis_usb_storage_disabled: no

      # 1.5.1 Ensure permissions on bootloader config are configured (Scored)
      # No bootloaders in a container.
      cis_permissions_bootloader: no

      # 1.5.2 Ensure bootloader password is set (Scored)
      # No bootloaders in a container.
      cis_bootloader_password_set: no

      # 1.7.1.2 Ensure SELinux is not disabled in bootloader configuration (Scored)
      # No bootloaders in a container.
      cis_selinux_not_disabled: no

      # 1.7.1.3 Ensure SELinux policy is configured (Scored)
      # Can't change an SELinux policy in a container.
      cis_selinux_policy_configured: no

      # 1.7.1.4 Ensure the SELinux state is enforcing (Scored)
      # Can't change an SELinux state in a container.
      cis_selinux_state_enforcing: no

      # 3.3.1 Ensure DCCP is disabled (Scored)
      # can't load modules in a container.
      cis_dccp_disabled: no

      # 3.3.2 Ensure SCTP is disabled (Scored)
      # can't load modules in a container.
      cis_sctp_disabled: no

      # 3.3.3 Ensure RDS is disabled (Scored)
      # can't load modules in a container.
      cis_rds_disabled: no

      # 3.3.4 Ensure TIPC is disabled (Scored)
      # can't load modules in a container.
      cis_tipc_disabled: no

      # 3.5 Ensure wireless interfaces are disabled (Scored)
      # No NetworkManager in a container.
      cis_wireless_interface_disabled: no

      # 3.6 Disable IPv6 (Not Scored)
      # No grub in containers.
      cis_disable_ipv6: no

      # 4.1.1.2 Ensure auditd service is enabled (Scored)
      # For some reason auditd does not start.
      cis_auditd_service_enabled: no

      # 4.1.1.3 Ensure auditing for processes that start prior to auditd is enabled (Scored)
      # No grub in containers.
      cis_auditing_processes_prior_start: no

      # 4.1.1.4 Ensure audit_backlog_limit is sufficient (Scored)
      # No grub in containers.
      cis_audit_backlog_limit_sufficient: no
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.cron
    - role: robertdebock.update
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for cis

# The CIS guidelines determines many settings of a system. The values used in
# this file will make a system compliant to the CIS specifications.
# There are many reasons why you do not want to adhere to one or more specific
# rules. You can overwrite values in you group_vars, host_vars, inventory or
# playbook.

# 1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored)
cis_cramfs_disabled: yes

# 1.1.1.2 Ensure mounting of vFAT filesystems is limited (Not Scored)
cis_vfat_disabled: yes

# 1.1.1.3 Ensure mounting of squashfs filesystems is disabled (Scored)
cis_squashfs_disabled: yes

# 1.1.1.4 Ensure mounting of udf filesystems is disabled (Scored)
cis_udf_disabled: yes

# 1.1.2 Ensure /tmp is configured (Scored)
cis_tmp_configured: yes

# 1.1.3 Ensure nodev option set on /tmp partition (Scored)
cis_tmp_nodev: yes

# 1.1.4 Ensure nosuid option set on /tmp partition (Scored)
cis_tmp_nosuid: yes

# 1.1.5 Ensure noexec option set on /tmp partition (Scored)
cis_tmp_noexec: yes

# 1.1.6 Ensure separate partition exists for /var (Scored)
cis_var_partition: yes

# 1.1.7 Ensure separate partition exists for /var/tmp (Scored)
cis_var_tmp_partition: yes

# 1.1.8 Ensure nodev option set on /var/tmp partition (Scored)
cis_var_tmp_nodev: yes

# 1.1.9 Ensure nosuid option set on /var/tmp partition (Scored)
cis_var_tmp_nosuid: yes

# 1.1.10 Ensure noexec option set on /var/tmp partition (Scored)
cis_var_tmp_noexec: yes

# 1.1.11 Ensure separate partition exists for /var/log (Scored)
cis_var_log_partition: yes

# 1.1.12 Ensure separate partition exists for /var/log/audit (Scored)
cis_var_log_audit_partition: yes

# 1.1.13 Ensure separate partition exists for /home (Scored)
cis_home_partition: yes

# 1.1.14 Ensure nodev option set on /home partition (Scored)
cis_home_nodev: yes

# 1.1.15 Ensure nodev option set on /dev/shm partition (Scored)
cis_dev_shm_nodev: yes

# 1.1.16 Ensure nosuid option set on /dev/shm partition (Scored)
cis_dev_shm_nosuid: yes

# 1.1.17 Ensure noexec option set on /dev/shm partition (Scored)
cis_dev_shm_noexec: yes

# 1.1.18 Ensure nodev option set on removable media partitions (Not Scored)
cis_removable_media_nodev: yes

# 1.1.19 Ensure nosuid option set on removable media partitions (Not Scored)
cis_removable_media_nosuid: yes

# 1.1.20 Ensure noexec option set on removable media partitions (Not Scored)
cis_removable_media_noexec: yes

# 1.1.21 Ensure sticky bit is set on all world-writable directories (Scored)
cis_fix_sticky_bit: yes

# 1.1.22 Disable Automounting
cis_disable_automount: yes

# 1.1.23 Disable USB Storage (Scored)
cis_usb_storage_disabled: yes

# 1.2.1 Ensure GPG keys are configured (Not Scored)
cis_gpg_keys_configured: yes

# 1.2.2 Ensure gpgcheck is globally activated (Scored)
cis_gpgcheck_enabled: yes

# 1.2.3 Ensure package manager repositories are configured (Not Scored)
cis_repositories_configured: yes

# 1.3.1 Ensure sudo is installed (Scored)
cis_sudo_installed: yes

# 1.3.2 Ensure sudo commands use pty (Scored)
cis_sudo_use_pty: yes

# 1.3.3 Ensure sudo log file exists (Scored)
cis_sudo_logfile: yes

# 1.4.1 Ensure AIDE is installed (Scored)
cis_aide_installed: yes

# 1.4.2 Ensure filesystem integrity is regularly checked (Scored)
cis_filesystem_integrity_checked: yes

# 1.5.1 Ensure permissions on bootloader config are configured (Scored)
cis_permissions_bootloader: yes

# 1.5.2 Ensure bootloader password is set (Scored)
cis_bootloader_password_set: yes
cis_bootloader_password: changeme

# 1.5.3 Ensure authentication required for single user mode (Scored)
cis_authentication_single_user_mode: yes

# 1.6.1 Ensure core dumps are restricted (Scored)
cis_core_dumps_restricted: yes

# 1.6.2 Ensure address space layout randomization (ASLR) is enabled (Scored)
cis_aslr_enabled: yes

# 1.7.1.1 Ensure SELinux is installed (Scored)
cis_selinux_installed: yes

# 1.7.1.2 Ensure SELinux is not disabled in bootloader configuration (Scored)
cis_selinux_not_disabled: yes

# 1.7.1.3 Ensure SELinux policy is configured (Scored)
cis_selinux_policy_configured: yes
cis_selinux_policy: targeted

# 1.7.1.4 Ensure the SELinux state is enforcing (Scored)
cis_selinux_state_enforcing: yes

# 1.7.1.5 Ensure no unconfined services exist (Scored)
cis_no_unconfined_services: yes

# 1.7.1.6 Ensure SETroubleshoot is not installed (Scored)
cis_setroubleshoot_not_installed: yes

# 1.7.1.7 Ensure the MCS Translation Service (mcstrans) is not installed (Scored)
cis_mcs_translation_service_not_installed: yes

# 1.8.1.1 Ensure message of the day is configured properly (Scored)
cis_message_of_the_day_configured: yes
cis_message_of_the_day: |
  UNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED
  You must have explicit, authorized permission to access or configure this device. Unauthorized attempts and actions to access or use this system may result in civil and/or criminal penalties. All activities performed on this device are logged and monitored.

# 1.8.1.2 Ensure local login warning banner is configured properly (Scored)
cis_local_login_banner_configured: yes

# 1.8.1.3 Ensure remote login warning banner is configured properly (Scored)
cis_remote_login_banner_configured: yes

# 1.8.1.4 Ensure permissions on /etc/motd are configured (Scored)
cis_permissions_etc_motd: yes

# 1.8.1.5 Ensure permissions on /etc/issue are configured (Scored)
cis_permissions_etc_issue: yes

# 1.8.1.6 Ensure permissions on /etc/issue.net are configured (Scored)
cis_permissions_etc_issue_net: yes

# 1.8.2 Ensure GDM login banner is configured (Scored)
cis_gdm_login_banner_configured: yes

# 1.9 Ensure updates, patches, and additional security software are installed (Not Scored)
cis_updates_installed: yes

# 1.10 Ensure system-wide crypto policy is not legacy (Scored)
cis_crypto_policy_not_legacy: yes
cis_crypto_policy: FIPS

# 1.11 Ensure system-wide crypto policy is FUTURE or FIPS (Scored)
cis_ensure_crypto_policy: yes

# 2.1.1 Ensure xinetd is not installed (Scored)
cis_xinet_not_installed: yes

# 2.2.1.1 Ensure time synchronization is in use (Not Scored)
cis_time_synchronization: yes

# 2.2.1.2 Ensure chrony is configured (Scored)
cis_chrony_configured: yes
cis_chrony_servers: []
cis_chrony_pools:
  - name: 2.fedora.pool.ntp.org
    options: iburst

# 2.2.2 Ensure X Window System is not installed (Scored)
cis_x_windows_system_not_installed: yes

# 2.2.3 Ensure rsync service is not enabled (Scored)
cis_rsync_service_not_enabled: yes

# 2.2.4 Ensure Avahi Server is not enabled (Scored)
cis_avahi_server_not_enabled: yes

# 2.2.5 Ensure SNMP Server is not enabled (Scored)
cis_snmp_server_not_enabled: yes

# 2.2.6 Ensure HTTP Proxy Server is not enabled (Scored)
cis_http_proxy_server_not_enabled: yes

# 2.2.7 Ensure Samba is not enabled (Scored)
cis_samba_server_not_enabled: yes

# 2.2.8 Ensure IMAP and POP3 server is not enabled (Scored)
cis_imap_and_pop3_server_not_enabled: yes

# 2.2.9 Ensure HTTP server is not enabled (Scored)
cis_http_server_not_enabled: yes

# 2.2.10 Ensure FTP Server is not enabled (Scored)
cis_ftp_server_not_enabled: yes

# 2.2.11 Ensure DNS Server is not enabled (Scored)
cis_dns_server_not_enabled: yes

# 2.2.12 Ensure NFS is not enabled (Scored)
cis_nfs_server_not_enabled: yes

# 2.2.13 Ensure RPC is not enabled (Scored)
cis_rpc_not_enabled: yes

# 2.2.14 Ensure LDAP server is not enabled (Scored)
cis_ldap_server_not_enabled: yes

# 2.2.15 Ensure DHCP Server is not enabled (Scored)
cis_dhcp_server_not_enabled: yes

# 2.2.16 Ensure CUPS is not enabled (Scored)
cis_cups_not_enabled: yes

# 2.2.17 Ensure NIS Server is not enabled (Scored)
cis_nis_server_not_enabled: yes

# 2.2.18 Ensure mail transfer agent is configured for local-only mode (Scored)
cis_mta_local_only_mode: yes

# 2.3.1 Ensure NIS Client is not installed (Scored)
cis_nis_client_not_installed: yes

# 2.3.2 Ensure telnet client is not installed (Scored)
cis_telnet_client_not_installed: yes

# 2.3.3 Ensure LDAP client is not installed (Scored)
cis_ldap_client_not_installed: yes

# 3.1.1 Ensure IP forwarding is disabled (Scored)
cis_ip_forwarding_disabled: yes

# 3.1.2 Ensure packet redirect sending is disabled (Scored)
cis_packet_redirect_sending_disabled: yes

# 3.2.1 Ensure source routed packets are not accepted (Scored)
cis_source_routed_packets_not_accepted: yes

# 3.2.2 Ensure ICMP redirects are not accepted (Scored)
cis_icmp_redirects_not_accepted: yes

# 3.2.3 Ensure secure ICMP redirects are not accepted (Scored)
cis_secure_icmp_redirects_not_accepted: yes

# 3.2.4 Ensure suspicious packets are logged (Scored)
cis_suspicious_packets_logged: yes

# 3.2.5 Ensure broadcast ICMP requests are ignored (Scored)
cis_broadcast_icmp_requests_ignored: yes

# 3.2.6 Ensure bogus ICMP responses are ignored (Scored)
cis_bogus_icmp_responses_ignored: yes

# 3.2.7 Ensure Reverse Path Filtering is enabled (Scored)
cis_reverse_path_filtering: yes

# 3.2.8 Ensure TCP SYN Cookies is enabled (Scored)
cis_tcp_syn_cookies_enabled: yes

# 3.2.9 Ensure IPv6 router advertisements are not accepted (Scored)
cis_ipv6_router_advertisements_not_accepted: yes

# 3.3.1 Ensure DCCP is disabled (Scored)
cis_dccp_disabled: yes

# 3.3.2 Ensure SCTP is disabled (Scored)
cis_sctp_disabled: yes

# 3.3.3 Ensure RDS is disabled (Scored)
cis_rds_disabled: yes

# 3.3.4 Ensure TIPC is disabled (Scored)
cis_tipc_disabled: yes

# 3.4.1.1 Ensure a Firewall package is installed (Scored)
cis_firewall_package_installed: yes
cis_firewall_package: firewalld

# 3.4.2.1 Ensure firewalld service is enabled and running (Scored)
cis_firewalld_enabled_and_running: yes

# 3.4.2.2 Ensure nftables is not enabled (Scored)
cis_nftables_not_enabled: yes

# 3.4.2.3 Ensure default zone is set (Scored)
cis_default_zone_set: yes
cis_default_zone: public

# 3.4.2.4 Ensure network interfaces are assigned to appropriate zone (Not Scored)
cis_firewalld_network_interface_assigned_zones: yes
cis_firewalld_zone_interface_mapping:
  - zone: public
    interface: eth0

# 3.4.2.5 Ensure unnecessary services and ports are not accepted (Not Scored)
cis_unnecessary_services_ports_not_accepted: yes
cis_unnecessary_services:
  - cockpit
cis_unnecessary_ports:
  - 12345/tcp

# 3.4.2.6 Ensure iptables is not enabled (Scored)
cis_iptables_not_enabled: yes

# 3.4.3 Configure nftables
# This section and all the subsection under 3.4.3 is skipped because section
# 3.4.2 (Configure firewalld) and this section 3.4.3 (Configure nftables) are
# mutually exclusive and firewalld is the default, which uses nft as a backend.

# 3.4.4 Configure iptables
# This section and all the subsection under 3.4.4 is skipped because section
# 3.4.2 (Configure firewalld) and this section 3.4.4 (Configure iptables) are
# mutually exclusive and firewalld is the default, which uses nft as a backend.

# 3.5 Ensure wireless interfaces are disabled (Scored)
cis_wireless_interface_disabled: yes

# 3.6 Disable IPv6 (Not Scored)
cis_disable_ipv6: yes

# 4.1.1.1 Ensure auditd is installed (Scored)
cis_auditd_installed: yes

# 4.1.1.2 Ensure auditd service is enabled (Scored)
cis_auditd_service_enabled: yes

# 4.1.1.3 Ensure auditing for processes that start prior to auditd is enabled (Scored)
cis_auditing_processes_prior_start: yes

# 4.1.1.4 Ensure audit_backlog_limit is sufficient (Scored)
cis_audit_backlog_limit_sufficient: yes

# 4.1.2.1 Ensure audit log storage size is configured (Scored)
cis_audit_log_storage_size_configured: yes
cis_audit_log_storage_size: 128

# 4.1.2.2 Ensure audit logs are not automatically deleted (Scored)
cis_audit_logs_no_automatically_deleted: yes

# 4.1.2.3 Ensure system is disabled when audit logs are full (Scored)
cis_system_disabled_audit_logs_full: yes

# 4.1.3 Ensure changes to system administration scope (sudoers) is collected (Scored)
cis_changed_to_system_administrator_scope_collected: yes

# 4.1.4 Ensure login and logout events are collected (Scored)
cis_login_and_login_events_collected: yes

# 4.1.5 Ensure session initiation information is collected (Scored)
cis_session_initiation_information_collected: yes

# 4.1.6 Ensure events that modify date and time information are collected (Scored)
cis_events_modify_time_and_date_collected: yes

# 4.1.7 Ensure events that modify the system's Mandatory Access Controls are collected (Scored)
cis_events_modifying_mac_collected: yes

# 4.1.8 Ensure events that modify the system's network environment are collected (Scored)
cis_events_modifying_systems_network_collected: yes

# 4.1.9 Ensure discretionary access control permission modification events are collected (Scored)
cis_dac_permission_modification_collected: yes

# 4.1.10 Ensure unsuccessful unauthorized file access attempts are collected (Scored)
cis_unsuccessful_files_access_collected: yes

# 4.1.11 Ensure events that modify user/group information are collected (Scored)
cis_events_modifying_user_group_collected: yes

# 4.1.12 Ensure successful file system mounts are collected (Scored)
cis_successful_mounts_collected: yes

# 4.1.13 Ensure use of privileged commands is collected (Scored)
cis_privileged_commands_collected: yes
# A list of partitions that will be checked. Extend this with all partitions
# that could contain executables.
cis_privileged_commands_collected_partitions:
  - /

# 4.1.14 Ensure file deletion events by users are collected (Scored)
cis_file_deletion_users_collected: yes

# 4.1.15 Ensure kernel module loading and unloading is collected (Scored)
cis_kernel_module_loading_unloading_collected: yes

# 4.1.16 Ensure system administrator actions (sudolog) are collected (Scored)
cis_system_administrator_actions_collected: yes

# 4.1.17 Ensure the audit configuration is immutable (Scored)
cis_audit_configuration_immutable: yes

# 4.2.1.1 Ensure rsyslog is installed (Scored)
cis_syslog_installed: yes

# 4.2.1.2 Ensure rsyslog Service is enabled (Scored)
cis_rsyslog_enabled: yes

# 4.2.1.3 Ensure rsyslog default file permissions configured (Scored)
cis_rsyslog_file_permissions_configured: yes

# 4.2.1.4 Ensure logging is configured (Not Scored)
cis_logging_configured: yes

cis_logging_site_policy:
  - rule: |-
      '*.emerg'
    destination: |-
      ':omusrmsg:*'
  - rule: 'auth,authpriv.*'
    destination: '/var/log/secure'
  - rule: |-
      'mail.*'
    destination: '-/var/log/mail'
  - rule: 'mail.info'
    destination: '-/var/log/mail.info'
  - rule: 'mail.warning'
    destination: '-/var/log/mail.warn'
  - rule: 'mail.err'
    destination: '/var/log/mail.err'
  - rule: 'news.crit'
    destination: '-/var/log/news/news.crit'
  - rule: 'news.err'
    destination: '-/var/log/news/news.err'
  - rule: 'news.notice'
    destination: '-/var/log/news/news.notice'
  - rule: |-
      '*.=warning;*.=err'
    destination: '-/var/log/warn'
  - rule: |-
      '*.crit'
    destination: '/var/log/warn'
  - rule: |-
      '*.*;mail.none;news.none'
    destination: '-/var/log/messages'
  - rule: |-
      'local0,local1.*'
    destination: '-/var/log/localmessages'
  - rule: 'local2,local3.*'
    destination: '-/var/log/localmessages'
  - rule: |-
      'local4,local5.*'
    destination: '-/var/log/localmessages'
  - rule: |-
      'local6,local7.*'
    destination: '-/var/log/localmessages'

# 4.2.1.5 Ensure rsyslog is configured to send logs to a remote log host (Scored)
cis_rsyslog_configured_remote_log_host: yes

# 4.2.1.5 Ensure rsyslog is configured to send logs to a remote log host (Scored)
cis_rsyslog_site_policy_host: loghost.example.com

# 4.2.1.6 Ensure remote rsyslog messages are only accepted on designated log hosts. (Not Scored)
# This item is not implemented because it would need to run on another host.

# 4.2.2.1 Ensure journald is configured to send logs to rsyslog (Scored)
cis_journald_send_to_rsyslog: yes

# 4.2.2.2 Ensure journald is configured to compress large log files (Scored)
cis_journald_compless_log_files: yes

# 4.2.2.3 Ensure journald is configured to write logfiles to persistent disk (Scored)
cis_journald_write_logfiles_to_disk: yes

# 4.2.3 Ensure permissions on all logfiles are configured (Scored)
cis_permissions_on_logfiles: yes

# 4.3 Ensure logrotate is configured (Not Scored)
cis_logrotate_configured: yes
cis_logrotate_policy:
  - name: dnf
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-cis/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cron)|
|[robertdebock.update](https://galaxy.ansible.com/robertdebock/update)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-update/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-update/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-update/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-update)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-cis/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|ubuntu|focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-cis/issues)

## [License](#license)

Apache-2.0

## [Contributors](#contributors)

I'd like to thank everybody that made contributions to this repository. It motivates me, improves the code and is just fun to collaborate.

- [arturmartins](https://github.com/arturmartins)

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
