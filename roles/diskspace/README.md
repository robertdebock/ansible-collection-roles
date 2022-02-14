# [diskspace](#diskspace)

Check diskspace (or inodes) available, fail if too low.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-diskspace/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-diskspace/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-diskspace/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-diskspace)|[![quality](https://img.shields.io/ansible/quality/55585)](https://galaxy.ansible.com/robertdebock/diskspace)|[![downloads](https://img.shields.io/ansible/role/d/55585)](https://galaxy.ansible.com/robertdebock/diskspace)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-diskspace.svg)](https://github.com/robertdebock/ansible-role-diskspace/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.diskspace
      # In a container these mounts should be available.
      diskspace_mounts:
        - name: /etc/resolv.conf
          megabytes_available: 64
        - name: /etc/hostname
          gigabytes_available: 4
        - name: /etc/hosts
          inodes_available: 65536
          gigabytes_available: 1
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for diskspace

# You can pass a list of mountpoint and their minimum required space of inodes.
# diskspace_mounts:
#   - name: /
#     megabytes_available: 64
#   - name: /var
#     gigabytes_available: 4
#   - name: /home
#     inodes_available: 65536
diskspace_mounts: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-diskspace/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-diskspace/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|all|
|debian|all|
|el|8|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-diskspace/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
