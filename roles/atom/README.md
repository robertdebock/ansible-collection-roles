# [atom](#atom)

Install atom on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-atom/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-atom/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-atom/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-atom)|[![quality](https://img.shields.io/ansible/quality/36572)](https://galaxy.ansible.com/robertdebock/atom)|[![downloads](https://img.shields.io/ansible/role/d/36572)](https://galaxy.ansible.com/robertdebock/atom)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-atom.svg)](https://github.com/robertdebock/ansible-role-atom/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.atom
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for atom

# What apm packages (https://atom.io/packages) to install.
atom_apm_packages:
  - linter
  - platformio-ide-terminal
  - teletype
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-atom/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-atom/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|all|
|fedora|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| amazonlinux:1 | Package: atom ... Requires: libsecret-1.so.0 ... and ... polkit |
| debian:bullseye | An error occurred during the test sequence action: 'idempotence'. Cleaning up. |
| centos:7 | /lib64/libstdc++.so.6: version `CXXABI_1.3.9' not found |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-atom/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
