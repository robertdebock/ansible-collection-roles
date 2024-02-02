# [Ansible role mount_options](#mount_options)

Install and configure mount_options on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-mount_options/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mount_options/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-mount_options/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-mount_options)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/mount_options)](https://galaxy.ansible.com/robertdebock/mount_options)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-mount_options.svg)](https://github.com/robertdebock/ansible-role-mount_options/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-mount_options/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.mount_options
      # CI runs in a container, where no mounts are available to change, disable this test.
      # mount_options:
      #   - path: /
      #     add_options:
      #       - noexec
      #     remove_options:
      #       - noatime
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-mount_options/blob/master/molecule/default/prepare.yml):

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

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-mount_options/blob/master/defaults/main.yml):

```yaml
---
# defaults file for mount_options

# Creating mountpoints can be done with [this role](https://galaxy.ansible.com/robertdebock/mount).

# You can add or remove mount options for an existing mount point.
# mount_options:
#   - path: /boot/efi
#     add_options:
#       - noexec
#     remove_options:
#       - noatime

# Here is a set used in may compliancy frameworks.
# mount_options:
#   - path: /dev/shm
#     add_options:
#       - nodev
#       - noexec
#       - nosuid
#   - path: /var/log
#     add_options:
#       - nodev
#       - noexec
#       - nosuid
#   - path: /home
#     add_options:
#       - nodev
#       - nosuid
#   - path: /boot
#     add_options:
#       - nodev
#       - nosuid
#   - path: /tmp
#     add_options:
#       - nodev
#       - noexec
#       - nosuid
#   - path: /var/tmp
#     add_options:
#       - nodev
#       - noexec
#       - nosuid
#   - path: /var/log/audit
#     add_options:
#       - nodev
#       - noexec
#       - nosuid
#   - path: /var
#     add_options:
#       - nodev

mount_options: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-mount_options/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-mount_options/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|all|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora/)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-mount_options/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-mount_options/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
