# [moodle](#moodle)

Install and configure moodle on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-moodle/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-moodle/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-moodle/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-moodle)|[![quality](https://img.shields.io/ansible/quality/52034)](https://galaxy.ansible.com/robertdebock/moodle)|[![downloads](https://img.shields.io/ansible/role/d/52034)](https://galaxy.ansible.com/robertdebock/moodle)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-moodle.svg)](https://github.com/robertdebock/ansible-role-moodle/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-moodle/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.moodle
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-moodle/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.epel
    - role: robertdebock.roles.mysql
      mysql_databases:
        - name: moodle
          encoding: utf8mb4
          collation: utf8mb4_unicode_ci
      mysql_users:
        - name: moodle
          password: moodle
          priv: "moodle.*:ALL"
    - role: robertdebock.roles.python_pip
    - role: robertdebock.roles.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
    - role: robertdebock.roles.php
    - role: robertdebock.roles.selinux
    - role: robertdebock.roles.httpd
      httpd_vhosts:
        - name: moodle
          servername: moodle.example.com
    - role: robertdebock.roles.cron
    - role: robertdebock.roles.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-moodle/blob/master/defaults/main.yml):

```yaml
---
# defaults file for moodle

# The version of moodle to install.
moodle_version: 401

# A path where to save the data.
moodle_data_directory: /opt/moodledata

# The permissions of the created directories.
moodle_directory_mode: "0750"

# Details to connect to the database.
moodle_database_type: mysqli
moodle_database_hostname: localhost
moodle_database_name: moodle
moodle_database_username: moodle
moodle_database_password: moodle
moodle_database_prefix: ""

# The URL where to serve content.
moodle_wwwroot: "https://{{ ansible_default_ipv4.address }}/moodle"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-moodle/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-buildtools)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-cron)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-httpd)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-mysql)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-openssl)|
|[robertdebock.php](https://galaxy.ansible.com/robertdebock/php)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-php/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-php/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-php)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-python_pip)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-selinux)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-moodle/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8, 9|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-moodle/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-moodle/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
