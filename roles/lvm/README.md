# [lvm](#lvm)

Configure Logical Volumes Management (lvm), group and volumes.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-lvm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-lvm/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-lvm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-lvm)|[![quality](https://img.shields.io/ansible/quality/52783)](https://galaxy.ansible.com/robertdebock/lvm)|[![downloads](https://img.shields.io/ansible/role/d/52783)](https://galaxy.ansible.com/robertdebock/lvm)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-lvm.svg)](https://github.com/robertdebock/ansible-role-lvm/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-lvm/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.lvm
      # It's difficult to test this in CI.
      # lvm_volume_groups:
      #   - name: first
      #     pvs:
      #       - /dev/loop0

      # There is no device mapper in containers.
      # lvm_logical_volumes:
      #   - name: first
      #     vg: first
      #     size: 100%FREE
      #     opts: --type cache-pool
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-lvm/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap

  # tasks:
  #   - name: create disk.img
  #     command: dd if=/dev/zero of=/disk.img bs=1M count=100
  #     args:
  #       creates: /disk.img

  #   - name: create /dev/loop0
  #     command: mknod /dev/loop0 b 7 8
  #     args:
  #       creates: /dev/loop0
  #     notify:
  #       - link disk.img to /dev/loop0

  # handlers:
  #   - name: link disk.img to /dev/loop0
  #     command: losetup /dev/loop0 /disk.img
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-lvm/blob/master/defaults/main.yml):

```yaml
---
# defaults file for lvm

# Per lvm a size can be set, if it's not set, use this value.
lvm_default_pesize: 32

# A list of volume groups.
# lvm_volume_groups:
#   - name: first
#     pvs:
#       - /dev/sdb1
#   - name: second
#     pvs:
#       - /dev/sdb2
#     pesize: 128K
#   - name: third
#     pvs:
#       - /dev/sdb3
#       - /dev/sdb4

# A list of volumes.
# lvm_logical_volumes:
#   - name: first
#     vg: first
#     size: 512
#     opts: --type cache-pool
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-lvm/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-lvm/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/repository/docker/robertdebock/alpine/general)|all|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-lvm/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-lvm/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
