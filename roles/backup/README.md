# [Ansible role backup](#backup)

The purpose of this role is to make backups of your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-backup/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-backup/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-backup/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-backup)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/backup)](https://galaxy.ansible.com/robertdebock/backup)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-backup.svg)](https://github.com/robertdebock/ansible-role-backup/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-backup/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.backup
      backup_cleanup: no
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-backup/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.mysql
      mysql_databases:
        - name: test_db
          encoding: utf8
          collation: utf8_bin
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.epel
    - role: robertdebock.roles.python_pip
    - role: robertdebock.roles.postgres
      postgres_databases:
        - name: test_db
          state: present
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-backup/blob/master/defaults/main.yml):

```yaml
---
# defaults file for backup

# The directory on the Ansible controller where to store backups.
backup_directory: backups

# The directory on the Ansible managed node where to temporarily store backups.
backup_remote_directory: /tmp

# Cleanup files created on the {{ backup_remote_directory }} when done?
backup_cleanup: yes

# What timestamp format to use when saving files.
backup_timestamp: "{{ ansible_date_time.date }}"

# What compression type to use, choose from bz2, tar, xz or zip
backup_format: zip

backup_objects:
  - name: varspool
    type: directory
    source: /var/spool
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-backup/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.mysql](https://galaxy.ansible.com/robertdebock/mysql)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-mysql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mysql/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-mysql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-mysql)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-buildtools)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-python_pip)|
|[robertdebock.postgres](https://galaxy.ansible.com/robertdebock/postgres)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-postgres/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-postgres/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-postgres/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-postgres)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-backup/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora/)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-backup/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-backup/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
