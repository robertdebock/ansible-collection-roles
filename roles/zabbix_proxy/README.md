# [Ansible role zabbix_proxy](#zabbix_proxy)

Install and configure zabbix-proxy on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-zabbix_proxy/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_proxy/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-zabbix_proxy/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-zabbix_proxy)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/zabbix_proxy)](https://galaxy.ansible.com/robertdebock/zabbix_proxy)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-zabbix_proxy.svg)](https://github.com/robertdebock/ansible-role-zabbix_proxy/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-zabbix_proxy/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.zabbix_proxy
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-zabbix_proxy/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.ca_certificates
    - role: robertdebock.roles.zabbix_repository
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-zabbix_proxy/blob/master/defaults/main.yml):

```yaml
---
# defaults file for zabbix_proxy

# The mode to operate in, 0 is active, 1 is passive.
zabbix_proxy_mode: "0"

zabbix_proxy_server: "127.0.0.1"

zabbix_proxy_server_port: 10051

zabbix_proxy_hostname: "{{ ansible_fqdn }}"

zabbix_proxy_database_hostname: localhost
zabbix_proxy_database_name: zabbix_proxy
zabbix_proxy_database_user: zabbix
zabbix_proxy_database_password: zabbix
zabbix_proxy_database_port: 3306
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-zabbix_proxy/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-ca_certificates)|
|[robertdebock.zabbix_repository](https://galaxy.ansible.com/robertdebock/zabbix_repository)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-zabbix_repository/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_repository/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-zabbix_repository/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-zabbix_repository)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-zabbix_proxy/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|bullseye|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|focal|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-zabbix_proxy/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-zabbix_proxy/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
