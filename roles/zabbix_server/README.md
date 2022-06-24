# [zabbix_server](#zabbix_server)

Install and configure zabbix_server on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-zabbix_server/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_server/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-zabbix_server/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-zabbix_server)|[![quality](https://img.shields.io/ansible/quality/35783)](https://galaxy.ansible.com/robertdebock/zabbix_server)|[![downloads](https://img.shields.io/ansible/role/d/35783)](https://galaxy.ansible.com/robertdebock/zabbix_server)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-zabbix_server.svg)](https://github.com/robertdebock/ansible-role-zabbix_server/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.zabbix_server
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.selinux
    - role: robertdebock.container_docs
    - role: robertdebock.mysql
      mysql_databases:
        - name: zabbix
          encoding: utf8
          collation: utf8_bin
      mysql_users:
        - name: zabbix
          password: zabbix
          priv: "zabbix.*:ALL"
    - role: robertdebock.ca_certificates
    - role: robertdebock.zabbix_repository
    - role: robertdebock.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for zabbix_server

# The details to connect to the database.
zabbix_server_database_name: zabbix
zabbix_server_database_user: zabbix
zabbix_server_database_password: zabbix
zabbix_server_database_host: localhost
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-zabbix_server/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ca_certificates)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.container_docs](https://galaxy.ansible.com/robertdebock/container_docs)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-container_docs/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-container_docs/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-container_docs/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-container_docs)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-mysql)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-selinux)|
|[robertdebock.zabbix_repository](https://galaxy.ansible.com/robertdebock/zabbix_repository)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-zabbix_repository/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_repository/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-zabbix_repository/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-zabbix_repository)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-zabbix_server/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|bullseye|
|opensuse|all|
|ubuntu|bionic, focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-zabbix_server/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
