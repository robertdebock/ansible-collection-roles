# [Ansible role filesystem](#filesystem)

Make filesystems.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-filesystem/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-filesystem/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-filesystem/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-filesystem)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/filesystem)](https://galaxy.ansible.com/robertdebock/filesystem)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-filesystem.svg)](https://github.com/robertdebock/ansible-role-filesystem/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-filesystem/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.filesystem
      filesystem_list:
        - dev: disk_1
          fstype: ext4
        - dev: disk_2
          fstype: ext3
          opts: -cc
        - dev: disk_3
          state: absent
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-filesystem/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap

  tasks:
    - name: Make disk image
      command: truncate -s 16M "{{ item }}"
      args:
        creates: "{{ item }}"
      loop:
        - disk_1
        - disk_2
        - disk_3
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-filesystem/blob/master/defaults/main.yml):

```yaml
---
# defaults file for filesystem

# If not specified in the `filesystem_list`, use this filesytem type.
filesytem_default_filesystem: ext4

# A list of filesytems to manage.
filesystem_list: []

# For example:
# filesystem_list:
#   - dev: /dev/sdb1
#     fstype: ext4
#   - dev: /dev/sdb2
#     fstype: ext3
#     opts: -cc
#   - dev: /dev/sdb3
#     state: absent
#   - dev /dev/sdb4
#     fstype: swap
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-filesystem/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-filesystem/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-filesystem/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-filesystem/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
