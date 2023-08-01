# [sosreport](#sosreport)

Install, run and collect sosreports from your systems.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-sosreport/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-sosreport/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-sosreport/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-sosreport)|[![quality](https://img.shields.io/ansible/quality/38477)](https://galaxy.ansible.com/robertdebock/sosreport)|[![downloads](https://img.shields.io/ansible/role/d/38477)](https://galaxy.ansible.com/robertdebock/sosreport)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-sosreport.svg)](https://github.com/robertdebock/ansible-role-sosreport/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-sosreport/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.roles.sosreport
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-sosreport/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no
  serial: 30%

  roles:
    - role: robertdebock.roles.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-sosreport/blob/master/defaults/main.yml):

```yaml
---
# defaults file for sosreport

# Where to store the sosreport on the managed node.
sosreport_remote_location: /tmp/sosreport

# Where to store the sosreport(s) on the controller.
sosreport_local_location: /tmp/sosreports
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-sosreport/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-sosreport/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8, 9|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-sosreport/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-sosreport/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
