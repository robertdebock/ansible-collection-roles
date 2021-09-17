# [zabbix_web](#zabbix_web)

Install and configure zabbix_web on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-zabbix_web/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_web/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-zabbix_web/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-zabbix_web)|[![quality](https://img.shields.io/ansible/quality/35789)](https://galaxy.ansible.com/robertdebock/zabbix_web)|[![downloads](https://img.shields.io/ansible/role/d/35789)](https://galaxy.ansible.com/robertdebock/zabbix_web)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-zabbix_web.svg)](https://github.com/robertdebock/ansible-role-zabbix_web/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.zabbix_web
      # You can provision Zabbix groups.
      # Most options map directly to the documentation:
      # https://docs.ansible.com/ansible/latest/modules/zabbix_group_module.html
      zabbix_web_groups:
        - name: Linux servers
      # Add hosts to Zabbix.
      # Most options map directly to the documentation:
      # https://docs.ansible.com/ansible/latest/modules/zabbix_host_module.html
      zabbix_web_hosts:
        - name: Example server 1
          interface_ip: 192.168.127.127
          interface_dns: server1.example.com
          visible_name: Example server 1 name
          description: Example server 1 description
          groups:
            - Linux servers
          link_templates:
            - Template OS Linux by Zabbix agent
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
    - role: robertdebock.buildtools
    - role: robertdebock.epel
    - role: robertdebock.python_pip
    - role: robertdebock.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
    - role: robertdebock.mysql
      mysql_databases:
        - name: zabbix
          encoding: utf8
          collation: utf8_bin
      mysql_users:
        - name: zabbix
          password: zabbix
          priv: "zabbix.*:ALL"
    - role: robertdebock.php
    - role: robertdebock.httpd
    - role: robertdebock.ca_certificates
    - role: robertdebock.zabbix_repository
    - role: robertdebock.core_dependencies
    - role: robertdebock.zabbix_server
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for zabbix_web

# How to connect to the mysql database, either `socket` or `network`.
zabbix_web_mysql_connection: socket

# Details to connect to the database.
zabbix_web_database_name: zabbix
zabbix_web_database_user: zabbix
zabbix_web_database_pass: zabbix

# When `zabbix_web_mysql_connection` is set to `network` this role needs
# these extra setting.
# zabbix_web_database_host: localhost
# zabbix_web_database_port: 3306

# Details to connect to Zabbix.
zabbix_web_server: "{{ ansible_fqdn }}"
zabbix_web_server_port: 10051
zabbix_web_server_name: zabbix

# Details to connect to the Zabbix API.
zabbix_web_username: Admin
zabbix_web_password: zabbix
zabbix_web_validate_certs: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-zabbix_web/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.container_docs](https://galaxy.ansible.com/robertdebock/container_docs)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-container_docs/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-container_docs/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-container_docs/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-container_docs)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ca_certificates)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-httpd)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-mysql)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-openssl)|
|[robertdebock.php](https://galaxy.ansible.com/robertdebock/php)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-php/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-php/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-php)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-selinux)|
|[robertdebock.zabbix_repository](https://galaxy.ansible.com/robertdebock/zabbix_repository)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-zabbix_repository/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_repository/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-zabbix_repository/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-zabbix_repository)|
|[robertdebock.zabbix_server](https://galaxy.ansible.com/robertdebock/zabbix_server)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-zabbix_server/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-zabbix_server/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-zabbix_server/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-zabbix_server)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-zabbix_web/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|bullseye|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| Alpine | Zabbix has [limited OS support](https://www.zabbix.com/download). |
| amazonlinux | Zabbix has [limited OS support](https://www.zabbix.com/download). |
| Archlinux | Zabbix has [limited OS support](https://www.zabbix.com/download). |
| CentOS 7 | Zabbix (5) requires php 7, not available on CentOS 7. |
| Debian | Zabbix has [limited OS support](https://www.zabbix.com/download). |
| Fedora | Zabbix has [limited OS support](https://www.zabbix.com/download). |
| openSUSE | Zabbix has [limited OS support](https://www.zabbix.com/download). |
| Ubuntu rolling | Zabbix has [limited OS support](https://www.zabbix.com/download). |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-zabbix_web/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
