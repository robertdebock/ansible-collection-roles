# [Ansible role phpmyadmin](#phpmyadmin)

Install and configure phpmyadmin on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-phpmyadmin/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-phpmyadmin/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-phpmyadmin/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-phpmyadmin)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/phpmyadmin)](https://galaxy.ansible.com/robertdebock/phpmyadmin)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-phpmyadmin.svg)](https://github.com/robertdebock/ansible-role-phpmyadmin/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-phpmyadmin/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.httpd
    - role: robertdebock.roles.phpmyadmin
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-phpmyadmin/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.epel
    - role: robertdebock.roles.python_pip
    - role: robertdebock.roles.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
    - role: robertdebock.roles.selinux
    - role: robertdebock.roles.httpd
    - role: robertdebock.roles.mysql
      mysql_users:
        - name: admin
          password: P@s5-W0rd
          priv: "*.*:ALL"
    - role: robertdebock.roles.php
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-phpmyadmin/blob/master/defaults/main.yml):

```yaml
---
# defaults file for phpmyadmin

# The version of PHPMyAdmin to install
phpmyadmin_version: "5.2.1"

# Where to connect to for the database.
phpmyadmin_database_host: localhost

# To authenticate to the database using a user/pass requested in the browser,
# ensure you set phpmyadmin_blowfish_secret.
phpmyadmin_blowfish_secret: "x7GD9DBEE32bAWd2sTHKBfYiqOfnj82neaPD3wrDTs0K"

# Only set these (and unset phpmyadmin_blowfish_secret) to save the login
# credentials in the configuration file.
# This role does not setup a MySQL user and/or password, it just uses these
# settings.
phpmyadmin_database_user: admin
phpmyadmin_database_pass: "P@s5-W0rd"

phpmyadmin_database_compress: false
phpmyadmin_database_allownopassword: false
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-phpmyadmin/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-buildtools)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-httpd)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-mysql)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-openssl)|
|[robertdebock.php](https://galaxy.ansible.com/robertdebock/php)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-php/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-php/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-php)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-python_pip)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-selinux)|

## [Dependencies](#dependencies)

Most roles require some kind of preparation, this is done in `molecule/default/prepare.yml`. This role has a "hard" dependency on the following roles:

- {'role': 'robertdebock.httpd'}

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-phpmyadmin/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-phpmyadmin/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-phpmyadmin/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
