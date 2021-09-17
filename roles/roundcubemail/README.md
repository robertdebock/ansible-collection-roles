# [roundcubemail](#roundcubemail)

Install and configure roundcubemail on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-roundcubemail/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-roundcubemail/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-roundcubemail/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-roundcubemail)|[![quality](https://img.shields.io/ansible/quality/24815)](https://galaxy.ansible.com/robertdebock/roundcubemail)|[![downloads](https://img.shields.io/ansible/role/d/24815)](https://galaxy.ansible.com/robertdebock/roundcubemail)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-roundcubemail.svg)](https://github.com/robertdebock/ansible-role-roundcubemail/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  vars_files:
    ../../vars/main.yml

  roles:
    - role: robertdebock.httpd
      httpd_vhosts:
        - name: docroot
          servername: roundcubemail.example.com
          documentroot: "{{ roundcubemail_install_directory }}"
    - role: robertdebock.roundcubemail
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
    - role: robertdebock.epel
    - role: robertdebock.buildtools
    - role: robertdebock.python_pip
    - role: robertdebock.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
    - role: robertdebock.selinux
    - role: robertdebock.httpd
    - role: robertdebock.php
      php_upload_max_filesize: 5M
      php_post_max_size: 6M
      php_date_timezone: Europe/Amsterdam
      php_extension:
        - mcrypt.so
    - role: robertdebock.mysql
      mysql_databases:
        - name: roundcube
      mysql_users:
        - name: roundcube
          password: roundcube
          priv: "roundcube.*:ALL"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for roundcubemail

roundcubemail_database_host: localhost
roundcubemail_database_user: roundcube
roundcubemail_database_password: roundcube
roundcubemail_database_name: roundcube

# A URL to get support.
roundcubemail_support_url: "{{ ansible_fqdn }}/support"

# A key to encrypt sensitive data.
roundcubemail_des_key: 964af56991531a805bd55085

# The spellchecker to use. Either: 'google', 'pspell', 'enchant' or 'atd'.
roundcubemail_spellcheck_engine: pspell
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-roundcubemail/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-httpd)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-mysql)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-openssl)|
|[robertdebock.php](https://galaxy.ansible.com/robertdebock/php)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-php/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-php/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-php)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|
|[robertdebock.reboot](https://galaxy.ansible.com/robertdebock/reboot)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-reboot/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-reboot/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-reboot/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-reboot)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-selinux)|

## [Dependencies](#dependencies)

Most roles require some kind of preparation, this is done in `molecule/default/prepare.yml`. This role has a "hard" dependency on the following roles:

- robertdebock.httpd
## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-roundcubemail/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|debian|all|
|fedora|all|
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
| centos:8 | No package roundcubemail available. |
| amazonlinux:1 | No package matching 'python3-pip' found available, installed or updated |
| amazonlinux:latest | The error was: ImportError: No module named pkg_resources (openssl role) |
| alpine | failed to install mariadb py-mysqldb (mysql role) |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-roundcubemail/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
