# [etherpad](#etherpad)

Install and configure Etherpad on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-etherpad/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-etherpad/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-etherpad/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-etherpad)|[![quality](https://img.shields.io/ansible/quality/38333)](https://galaxy.ansible.com/robertdebock/etherpad)|[![downloads](https://img.shields.io/ansible/role/d/38333)](https://galaxy.ansible.com/robertdebock/etherpad)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-etherpad.svg)](https://github.com/robertdebock/ansible-role-etherpad/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-etherpad/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  vars:
    etherpad_port: 9002

  roles:
    - role: robertdebock.roles.etherpad
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-etherpad/blob/master/molecule/default/prepare.yml):

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
    - role: robertdebock.roles.npm
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-etherpad/blob/master/defaults/main.yml):

```yaml
---
# defaults file for etherpad

etherpad_version: "1.8.16"

etherpad_installation_destination: /opt

etherpad_port: 9001
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-etherpad/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.npm](https://galaxy.ansible.com/robertdebock/npm)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-npm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-npm/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-npm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-npm)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-service)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-etherpad/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|bullseye|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-etherpad/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-etherpad/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
