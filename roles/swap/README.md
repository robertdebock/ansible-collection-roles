# [swap](#swap)

Configure swap files on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-swap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-swap/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-swap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-swap)|[![quality](https://img.shields.io/ansible/quality/46284)](https://galaxy.ansible.com/robertdebock/swap)|[![downloads](https://img.shields.io/ansible/role/d/46284)](https://galaxy.ansible.com/robertdebock/swap)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-swap.svg)](https://github.com/robertdebock/ansible-role-swap/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-swap/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.roles.swap
      swap_files:
        - path: /my.swap
          size: 1024
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-swap/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.roles.bootstrap
    - role: robertdebock.roles.roles.sysctl
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-swap/blob/master/defaults/main.yml):

```yaml
---
# defaults file for swap

# Set the swappiness, 60 is default for Fedora 31.
swap_swappiness: 60

# A list of swap files to add. The list must container **path** (an absolute path to a file) and **size** (an integer in megabytes).
# swap_files:
#   - path: /my.swap
#     size: 1024

# You can disable swap if required.
swap_enabled: yes
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-swap/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.sysctl](https://galaxy.ansible.com/robertdebock/sysctl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-sysctl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-sysctl/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-sysctl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-sysctl)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-swap/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8, 9|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-swap/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-swap/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
