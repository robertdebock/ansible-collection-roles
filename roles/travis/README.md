# [travis](#travis)

Installs travis on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-travis/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-travis/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-travis/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-travis)|[![quality](https://img.shields.io/ansible/quality/35947)](https://galaxy.ansible.com/robertdebock/travis)|[![downloads](https://img.shields.io/ansible/role/d/35947)](https://galaxy.ansible.com/robertdebock/travis)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-travis.svg)](https://github.com/robertdebock/ansible-role-travis/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.travis
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
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.ruby
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.


## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-travis/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.ruby](https://galaxy.ansible.com/robertdebock/ruby)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ruby/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ruby/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ruby/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ruby)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-travis/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|el|8|
|debian|all|
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
| centos:7 | Dependency faraday requires Ruby version >= 2.3 |
| fedora | extconf failed, exit code 1 |
| ubuntu:xenial | faraday requires Ruby version >= 2.4. |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-travis/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
