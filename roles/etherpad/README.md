# [etherpad](#etherpad)

Install and configure Etherpad on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-etherpad/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-etherpad/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-etherpad/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-etherpad)|[![quality](https://img.shields.io/ansible/quality/38333)](https://galaxy.ansible.com/robertdebock/etherpad)|[![downloads](https://img.shields.io/ansible/role/d/38333)](https://galaxy.ansible.com/robertdebock/etherpad)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-etherpad.svg)](https://github.com/robertdebock/ansible-role-etherpad/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  vars:
    etherpad_port: 9002

  roles:
    - role: robertdebock.etherpad
```

The machine needs to be prepared in CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.epel
    - role: robertdebock.npm
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for etherpad

etherpad_version: 1.7.5

etherpad_installation_destination: /opt

etherpad_port: 9001
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-etherpad/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.npm](https://galaxy.ansible.com/robertdebock/npm)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-npm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-npm/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-npm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-npm)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-service)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-etherpad/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|buster|
|fedora|all|
|ubuntu|focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| alpine | Not idempotent on starting the service. |
| ubuntu | Your npm version "3.5.2" is too old. npm 3.10.x or higher is required. |
| amazonlinux | Failed to set execute bit on remote files |
| debian:testing | The repository 'https://deb.nodesource.com/node_10.x bullseye Release' does not have a Release file. |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-etherpad/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
