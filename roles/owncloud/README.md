# [owncloud](#owncloud)

Install and configure owncloud on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-owncloud/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-owncloud/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-owncloud/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-owncloud)|[![quality](https://img.shields.io/ansible/quality/27060)](https://galaxy.ansible.com/robertdebock/owncloud)|[![downloads](https://img.shields.io/ansible/role/d/27060)](https://galaxy.ansible.com/robertdebock/owncloud)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-owncloud.svg)](https://github.com/robertdebock/ansible-role-owncloud/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.httpd
    - role: robertdebock.owncloud
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.cron
    - role: robertdebock.buildtools
    - role: robertdebock.epel
    - role: robertdebock.python_pip
    - role: robertdebock.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
    - role: robertdebock.selinux
    - role: robertdebock.httpd
    - role: robertdebock.redis
    - role: robertdebock.remi
      remi_enabled_repositories:
        - php73
      when:
        - ansible_distribution != "Fedora"
    - role: robertdebock.php
    - role: robertdebock.php_fpm
    - role: robertdebock.mysql
      mysql_databases:
        - name: owncloud
          encoding: utf8
          collation: utf8_bin
      mysql_users:
        - name: owncloud
          password: 0wnCl0uD
          priv: "owncloud.*:ALL"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for owncloud

# The version of owncloud to install.
owncloud_version: "10.8.0"

# The domain under which this server will be available. For example:
# "localhost" or "owncloud.example.com". Does not include protocol identifier,
# (https://) or directories. (/owncloud)
owncloud_domain_url: "{{ ansible_default_ipv4.address | default(ansible_all_ipv4_addresses[0] ) }}"

# Database connection details.
owncloud_database_name: owncloud
owncloud_database_user: owncloud
owncloud_database_pass: 0wnCl0uD
owncloud_database_host: "127.0.0.1"
owncloud_admin_user: admin
owncloud_admin_pass: OwnCl0uD
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-owncloud/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cron)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-httpd)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-mysql)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-openssl)|
|[robertdebock.php](https://galaxy.ansible.com/robertdebock/php)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-php/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-php/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-php)|
|[robertdebock.php_fpm](https://galaxy.ansible.com/robertdebock/php_fpm)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-php_fpm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php_fpm/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-php_fpm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-php_fpm)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|
|[robertdebock.redis](https://galaxy.ansible.com/robertdebock/redis)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-redis/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-redis/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-redis/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-redis)|
|[robertdebock.remi](https://galaxy.ansible.com/robertdebock/remi)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-remi/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-remi/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-remi/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-remi)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-selinux)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-owncloud/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|bullseye|
|fedora|all|
|opensuse|all|
|ubuntu|bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| centos:latest | No package php73 available. |
| opensuse | This version of ownCloud is not compatible with PHP 7.4 |
| fedora:32 | nothing provides libzip(x86-64) >= 1.7.3 needed by php-pecl-zip-1.19.1-1.fc32.remi.7.4.x86_64 |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-owncloud/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
