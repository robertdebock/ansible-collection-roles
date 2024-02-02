# [Ansible role bareos_repository](#bareos_repository)

Setup the [Bareos](https://www.bareos.com/) repositories.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-bareos_repository/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bareos_repository/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-bareos_repository/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bareos_repository)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/bareos_repository)](https://galaxy.ansible.com/robertdebock/bareos_repository)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-bareos_repository.svg)](https://github.com/robertdebock/ansible-role-bareos_repository/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-bareos_repository/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.bareos_repository
      bareos_repository_enable_tracebacks: yes
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-bareos_repository/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-bareos_repository/blob/master/defaults/main.yml):

```yaml
---
# defaults file for bareos_repository

# What type of Bareos to install, either "community" or "subscription".
bareos_repository_type: community

# The subscription username for the repository.
bareos_repository_username: ""

# The subscription password for the repository.
bareos_repository_password: ""

# What release to use, either "current", "next" or "release".
# When using `bareos_repository_type: community` this can be set to "release" or "testing".
bareos_repository_release: current

# The version of Bareos to install.
# Only affects `bareos_repository_type: subscription`.
bareos_repository_version: 23

# You can enable tracebacks for troubleshooting purposes.
bareos_repository_enable_tracebacks: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-bareos_repository/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-bareos_repository/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|bookworm, bullseye, buster|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|7, 8, 9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora/)|38, 39|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|jammy, focal|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-bareos_repository/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-bareos_repository/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
