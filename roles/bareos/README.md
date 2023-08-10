# [bareos](#bareos)

Install and configure bareos on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-bareos/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bareos/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-bareos/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bareos)|[![quality](https://img.shields.io/ansible/quality/)](https://galaxy.ansible.com/robertdebock/bareos)|[![downloads](https://img.shields.io/ansible/role/d/)](https://galaxy.ansible.com/robertdebock/bareos)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-bareos.svg)](https://github.com/robertdebock/ansible-role-bareos/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-bareos/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  # Bareos has three types of roles: fd (File Daemon), sd (Storage Daemon), and dir (Director).
  # We want to test all three roles, so we need to run the role three times, each time with
  # a different value for the variable bareos_role.
  roles:
    - role: robertdebock.roles.bareos
    - role: robertdebock.roles.bareos
      bareos_role: sd
    - role: robertdebock.roles.bareos
      bareos_role: dir
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-bareos/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  # We are going to install all components on one hosts.
  # This is not what is typically done, but works for testing.

  roles:
    - role: robertdebock.roles.bootstrap
    # The roles buildtools, python_pip and postgres are only required for the `bareos_role`: dir.
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.python_pip
    - role: robertdebock.roles.postgres
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-bareos/blob/master/defaults/main.yml):

```yaml
---
# defaults file for bareos

# What type of Bareos to install, either "community" or "subscription".
bareos_type: community

# What release to use, either "current", "next" or "release".
bareos_release: current

# What version to install, either "20", "21" or "22".
bareos_version: 22

# What role should be used, either "fd" (File Daemon)), "sd" (Storage Daemon), or "dir" (Director).
# You can only select one role, so if you want to have mulitple roles on a server,
# you need to run this role multiple times, each time with a different role.
bareos_role: fd
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-bareos/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-buildtools)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-python_pip)|
|[robertdebock.postgres](https://galaxy.ansible.com/robertdebock/postgres)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-postgres/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-postgres/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-postgres/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-postgres)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-bareos/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8, 9|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|37|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|jammy|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-bareos/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-bareos/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
