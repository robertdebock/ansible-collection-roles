# [mediawiki](#mediawiki)

Install and configure mediawiki on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-mediawiki/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mediawiki/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-mediawiki/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-mediawiki)|[![quality](https://img.shields.io/ansible/quality/29572)](https://galaxy.ansible.com/robertdebock/mediawiki)|[![downloads](https://img.shields.io/ansible/role/d/29572)](https://galaxy.ansible.com/robertdebock/mediawiki)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-mediawiki.svg)](https://github.com/robertdebock/ansible-role-mediawiki/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-mediawiki/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.mediawiki
      mediawiki_destination: /opt
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-mediawiki/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.epel
    - role: robertdebock.roles.python_pip
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
    - role: robertdebock.roles.httpd
    - role: robertdebock.roles.php
    - role: robertdebock.roles.mysql
      mysql_databases:
        - name: mediawiki
      mysql_users:
        - name: mediawiki
          password: m3d14w1k1
          priv: "mediawiki.*:ALL"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-mediawiki/blob/master/defaults/main.yml):

```yaml
---
# defaults file for mediawiki

# The version (major.minor.release) to install.
mediawiki_major: 1
mediawiki_minor: 37
mediawiki_release: 1

mediawiki_version: "{{ mediawiki_major }}.{{ mediawiki_minor }}.{{ mediawiki_release }}"

# Where to install mediawiki. You can use this pattern to install to a default
# location that differs per distribution, see `vars/main.yml`:
# "{{ _mediawiki_destination[ansible_distribution] | default(_mediawiki_destination['default'] ) }}"
# Change this to a simple string that refers to a path, for example:
# "/data/mediawiki".

mediawiki_destination: "{{ _mediawiki_destination[ansible_distribution] | default(_mediawiki_destination['default']) }}"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-mediawiki/blob/master/requirements.txt).

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

## [Dependencies](#dependencies)

Most roles require some kind of preparation, this is done in `molecule/default/prepare.yml`. This role has a "hard" dependency on the following roles:

- {'role': 'robertdebock.httpd'}

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-mediawiki/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|focal|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-mediawiki/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-mediawiki/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
