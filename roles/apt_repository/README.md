# [Ansible role apt_repository](#apt_repository)

Manage apt repositor(y|ies).

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-apt_repository/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-apt_repository/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-apt_repository/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-apt_repository)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/apt_repository)](https://galaxy.ansible.com/robertdebock/apt_repository)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-apt_repository.svg)](https://github.com/robertdebock/ansible-role-apt_repository/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-apt_repository/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.apt_repository
      apt_repositories:
        - repo: "deb https://dl.yarnpkg.com/debian/ stable main"
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-apt_repository/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap

  tasks:
    - name: Install apt-transport-https ca-certificates
      ansible.builtin.package:
        name: "{{ item }}"
      loop:
        - apt-transport-https
        - ca-certificates

    - name: Install yarn public key
      ansible.builtin.apt_key:
        url: "https://dl.yarnpkg.com/debian/pubkey.gpg"
        validate_certs: false
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-apt_repository/blob/master/defaults/main.yml):

```yaml
---
# defaults file for apt_repositories

# You can add or remove repositories:
# apt_repositories:
#   - repo: "ppa:rabbitvcs/ppa"
#   - repo: "ppa:something/ppa"
#     state: absent

apt_repositories: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-apt_repository/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-apt_repository/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-apt_repository/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-apt_repository/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
