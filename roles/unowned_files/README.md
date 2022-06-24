# [unowned_files](#unowned_files)

Install and configure unowned_files on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-unowned_files/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-unowned_files/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-unowned_files/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-unowned_files)|[![quality](https://img.shields.io/ansible/quality/45318)](https://galaxy.ansible.com/robertdebock/unowned_files)|[![downloads](https://img.shields.io/ansible/role/d/45318)](https://galaxy.ansible.com/robertdebock/unowned_files)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-unowned_files.svg)](https://github.com/robertdebock/ansible-role-unowned_files/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.unowned_files
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
# defaults file for unowned_files

# What to do with files or directories that have no owner. `yes` will detele
# files that have either no owner or group. `no` will change the ownership of
# files to the user and group set with `unowned_files_default_owner` and
# `unowned_files_default_group`.
unowned_files_delete: no

# If files have no owner, but do have a group, change the owner to this
# variable.
unowned_files_default_owner: nodody

# If files have no group, but do have an owner, change the group to this
# variable.
unowned_files_default_group: nodody

# A list of paths to search
unowned_files_directories:
  - /
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-unowned_files/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-unowned_files/png/requirements.png "Dependencies")

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


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-unowned_files/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
