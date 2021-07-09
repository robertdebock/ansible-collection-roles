# [packer](#packer)

Install and configure packer on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-packer/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-packer/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-packer/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-packer)|[![quality](https://img.shields.io/ansible/quality/27497)](https://galaxy.ansible.com/robertdebock/packer)|[![downloads](https://img.shields.io/ansible/role/d/27497)](https://galaxy.ansible.com/robertdebock/packer)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-packer.svg)](https://github.com/robertdebock/ansible-role-packer/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.packer
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for packer

# The version of Packer to install.
packer_version: 1.4.5
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-packer/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-packer/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|Candidate|
|el|8|
|debian|buster, bullseye|
|fedora|all|
|opensuse|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


## [Included version(s)](#included-versions)

This role [refers to a version](https://github.com/robertdebock/ansible-role-packer/blob/master/defaults/main.yml) released by HashiCorp. Check the released version(s) here:
- [packer](https://www.packer.io/).

This version reference means a role may get outdated. Monthly tests occur to see if [bit-rot](https://en.wikipedia.org/wiki/Software_rot) occured. If you however find a problem, please create an issue, I'll get on it as soon as possible.
If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-packer/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
