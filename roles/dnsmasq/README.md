# [dnsmasq](#dnsmasq)

Install and configure dnsmasq on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-dnsmasq/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-dnsmasq/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-dnsmasq/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-dnsmasq)|[![quality](https://img.shields.io/ansible/quality/50704)](https://galaxy.ansible.com/robertdebock/dnsmasq)|[![downloads](https://img.shields.io/ansible/role/d/50704)](https://galaxy.ansible.com/robertdebock/dnsmasq)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-dnsmasq.svg)](https://github.com/robertdebock/ansible-role-dnsmasq/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.dnsmasq
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:

```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:

```yaml
---
# defaults file for dnsmasq

# dnsmasq_port: 5353

dnsmasq_domain_needed: no
dnsmasq_bogus_priv: no
dnsmasq_conf_file: "{{ dnsmasq_documentation_path }}/trust-anchors.conf"
dnsmasq_dnssec: no
dnsmasq_dnssec_check_unsigned: no
dnsmasq_filterwin2k: no
# dnsmasq_resolv_file: /etc/resolv.conf
dnsmasq_strict_order: no
dnsmasq_no_resolv: no
dnsmasq_no_poll: no
# dnsmasq_servers:
#   - domain: localnet
#     nameserver: "192.168.0.1"
#   - domain: "3.168.192.in-addr.arpa"
#     nameserver: "10.1.2.3"
#   - domain: "10.1.2.3"
#     interface: eth1
#   - destination: "10.2.3.4"
#     nameserver: "192.168.1.1"
#     interface: "192.168.1.1"
#     port: 55
# dnsmasq_locals:
#   - domain: localnet
# dnsmasq_addresses:
#   - domain: double-click.net
#     address: "127.0.0.1"
#   - domain: www.thekelleys.org.uk
#     address: "fe80::20d:60ff:fe36:f83"
# dnsmasq_ipsets:
#   - domains:
#       - name: yahoo.com
#       - name: google.com
#     destination: vpn
#     option: search
dnsmasq_user: "{{ dnsmasq_set_user }}"
dnsmasq_group: "{{ dnsmasq_set_group }}"
# dnsmasq_interfaces:
#   - name: lo
#   - name: eth0
# dnsmasq_except_interface: eth0
# dnsmasq_listen_addresses:
#   - name: "127.0.0.1"
dnsmasq_no_dhcp_interface: ""
dnsmasq_local_service: no
dnsmasq_bind_interfaces: no
dnsmasq_no_hosts: no
# dnsmasq_addn_hosts: /etc/banner_add_hosts
dnsmasq_expand_hosts: no
# dnsmasq_domains:
#   - name: thekelleys.org.uk
#   - name: wireless.thekelleys.org.uk
#     subnet: "192.168.2.0/24"
#   - name: reserved.thekelleys.org.uk
#     from: "192.68.3.100"
#     until: "192.168.3.200"
# dnsmasq_dhcp_ranges:
#   - from: "192.168.0.50"
#     until: "192.168.0.150"
#     leasetime: 12h
#   - from: "192.168.0.50"
#     until: "192.168.0.150"
#     subnet: "255.255.255.0"
#     leasetime: 12h
#   - from: "192.168.0.50"
#     until: "192.168.0.150"
#     sets:
#       - name: red
#   - from: "192.168.0.50"
#     until: "192.168.0.150"
#     leasetime: 12h
#     tags:
#       - name: green
#   - from: "192.168.0.0"
#     options:
#       - name: static
#     static: yes
#   - from: "1234::2"
#     until: "1234::500"
#     prefix: 64
#     leasetime: 12h
#   - from: "1234::"
#     options:
#       - name: ra-only
#   - from: "1234::"
#     options:
#       - name: ra-names
#   - from: "1234::"
#     options:
#       - name: ra-only
#     leasetime: 48hA
#   - from: "1234::2"
#     until: "1234::500"
#     options:
#       - name: slaac
#   - from: "1234::"
#     options:
#        - name: ra-stateless
#   - from: "1234::"
#     options:
#       - name: ra-stateless
#       - name: ra-names
dnsmasq_enable_ra: no
# dnsmasq_hosts:
#   - name: "11:22:33:44:55:66"
#     value: "192.168.0.60"
#   - name: "11:22:33:44:55:66"
#     value: fred
#   - name: "11:22:33:44:55:66"
#     value: "fred,192.168.0.60,45m"
#   - name: "11:22:33:44:55:66,12:34:56:78:90:12"
#     value: "192.168.0.60"
#   - name: bert
#     value: "192.168.0.70,infinite"
#   - name: "id:01:02:02:04"
#     value: "192.168.0.60"
#   - name: "id:ff:00:00:00:00:00:02:00:00:02:c9:00:f4:52:14:03:00:28:05:81"
#     value: "192.168.0.61"
# dnsmasq_dhcp_ignore: "tag:!known"
# dnsmasq_dhcp_vendorclass: "set:red,Linux"
# dnsmasq_dhcp_userclass: "set:red,accounts"
dnsmasq_dhcp_mac: "set:red,00:60:8C:*:*:*"
dnsmasq_read_ethers: no
# dnsmasq_dhcp_options:
#   - name: 3
#     value: "1.2.3.4"
#   - name: "option:router"
#     value: "1.2.3.4"
#   - name: 3
#   - name: "option:ntp-server"
#     value: "192.168.0.4,10.10.0.5"
#   - name: "option6:dns-server"
#     value: "[1234::77],[1234::88]"
#   - name: "option6:dns-server"
#     value: "[::],[1234::88]"
#   - name: "option6:information-refresh-time"
#     value: 6h
#   - name: "option:T1"
#     value: 1m
#   - name: "option:T2"
#     value: 2m
#   - name: 42
#     value: "0.0.0.0"
#   - name: 40
#     value: welly
#   - name: 23
#     value: 50
#   - name: 27
#     value: 1
#   - name: 128
#     value: "e4:45:74:68:00:00"
#   - name: 129
#     value: NIC=eepro100
#   - name: "option:ntp-server"
#     tag: red
#     value: "192.168.1.1"
#   - name: 19
#     value: 0
#   - name: 44
#     value: "0.0.0.0"
#   - name: 45
#     value: "0.0.0.0"
#   - name: 46
#     value: 8
#   - name: 252
#     value: "\n"
#   - name: "option:domain-search"
#     value: eng.apple.com,marketing.apple.com
#   - name: 121
#     value: "192.168.1.0/24,1.2.3.4,10.0.0.0/8,5.6.7.8"
#   - name: "vendor:PXEClient"
#     value: "1,0.0.0.0"
#   - name: "vendor:MSFT"
#     value: 2,1i
#   - name: "vendor:Etherboot"
#     value: 60,"Etherboot"
# dnsmasq_dhcp_option_force:
#   - name: 208
#     value: "f1:00:74:7e"
#   - name: 209
#     value: configs/common
#   - name: 210
#     value: /tftpboot/pxelinux/files/
#   - name: 211
#     value: 30i
# dnsmasq_dhcp_boot: pxelinux.0
# dnsmasq_dhcp_boot: "pxelinux.0,server.name,192.168.1.100"
dnsmasq_enable_tftp: no
# dnsmasq_tftp_root: /var/ftpd
dnsmasq_tftp_no_fail: no
dnsmasq_tftp_secure: no
dnsmasq_tftp_no_blocksize: no
# dnsmasq_dhcp_lease_max: 150
# dnsmasq_dhcp_leasefile: /var/lib/dnsmasq/dnsmasq.leases
dnsmasq_dhcp_authoritative: no
dnsmasq_dhcp_rapid_commit: no
dnsmasq_dhcp_script: /bin/echo
# dnsmasq_cache_size: 150
dnsmasq_no_negcache: no
# dnsmasq_local_ttl: 3600
# dnsmasq_bogus_nxdomain: "64.94.110.11"
# dnsmasq_aliases:
#   - from: "1.2.3.4"
#     until: "4.5.6.7"
#   - from: "1.2.3.0"
#     until: "5.6.7.0"
#     subnet: "255.255.255.0"
#   - from: "192.168.0.10-192.168.0.40"
#     until: "10.0.0.0"
#     subnet: "255.255.255.0"
# dnsmasq_mx_hosts:
#   - domain: maildomain.com
#     host: servermacine.com
#     priority: 50
#   - domain: servermachine.com
dnsmasq_localmx: no
dnsmasq_selfmx: no
# dnsmasq_src_hosts:
#   - record: _ldap._tcp.example.com
#     destination: ldapserver.example.com
#     port: 389
#   - record: _ldap._tcp.example.com
#     destination: ldapserver.example.com
#     port: 389
#     priority: 1
#   - record: _ldap._tcp.example.com
#     destination: ldapserver.example.com
#     port: 389
#     priority: 2
#   - record: _ldap._tcp.example.com
dnsmasq_log_queries: no
dnsmasq_log_dhcp: no
# dnsmasq_conf_dir: /etc/dnsmasq.d
# dnsmasq_dhcp_name_match: "set:wpad-ignore,wpad"
# dnsmasq_ignore_names: "tag:wpad-ignore"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-dnsmasq/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-dnsmasq/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|debian|all|
|el|8|
|fedora|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-dnsmasq/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
