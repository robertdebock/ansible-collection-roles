# [f5_ltm](#f5_ltm)

Configure an F5 LTMs nodes, pool, pool members and virtual servers.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-f5_ltm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-f5_ltm/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-f5_ltm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-f5_ltm)|[![quality](https://img.shields.io/ansible/quality/43521)](https://galaxy.ansible.com/robertdebock/f5_ltm)|[![downloads](https://img.shields.io/ansible/role/d/43521)](https://galaxy.ansible.com/robertdebock/f5_ltm)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-f5_ltm.svg)](https://github.com/robertdebock/ansible-role-f5_ltm/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.f5_ltm
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for f5_ltm

# Connection details for the F5 LTM.
# f5_ltm_provider:
#   server: "192.168.1.254"
#   user: root
#   password: password
#   server_port: 8443
#   validate_certs: no

# General settings for the F5 LTM.
f5_ltm_partition: Common
f5_ltm_hostname: f5.example.com
f5_ltm_timezone: "Europe/Amsterdam"
f5_ltm_ntp_servers:
  - "1.1.1.1"
  - "8.8.8.8"

# The list of nodes.
# f5_ltm_nodes:
#   - name: node1.example.com
#     host: "192.168.1.1"
#   - name: node2.example.com
#     host: "192.168.1.2"

# The list of pools.
# f5_ltm_pools:
#   - name: pool1.example.com
#     lb_method: http_pool
#     monitors: /Common/http
#     monitor_type: and_list

# The list of pools and their members.
# f5_ltm_pool_members:
#   - name: pool1.example.com
#     members:
#       - name: node1.example.com
#         port: 80
#       - name: node2.example.com
#         port: 80

# The list of virtual_servers.
# f5_ltm_virtual_servers:
#   - name: virtual_server1.example.com
#     pool: pool1.example.com
#     destination: "192.168.1.254"
#     port: 443
#     enable_vlans: all
#     all_profiles:
#       - http
#       - clientssl
#       - oneconnect
#     snat: Automap
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-f5_ltm/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-f5_ltm/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|Candidate|
|el|8|
|debian|all|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-f5_ltm/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
