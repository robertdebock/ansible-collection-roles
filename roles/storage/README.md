# [Ansible role storage](#storage)

Create partitions, volume groups, volumes, filesystems and mounts

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-storage/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-storage/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-storage/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-storage)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/storage)](https://galaxy.ansible.com/robertdebock/storage)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-storage.svg)](https://github.com/robertdebock/ansible-role-storage/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-storage/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  pre_tasks:
    # For testing in containers, a loopback device is created in `prepare.yml`.
    # The device created in `prepare.yml` is picked up here.
    # Normally you would point to /dev/sd*.
    - name: Read loop device from disk
      ansible.builtin.slurp:
        src: /loopback-devicename.txt
      register: loopback_devicename

  roles:
    - role: robertdebock.roles.storage
      # Partitioning a loopback device is not supported by parted.
      # storage_partitions:
      #   - name: "{{ loopback_devicename.content | b64decode }}"
      #     number: 1
      #     part_end: 100%
      #     label: gpt
      storage_volumegroups:
        - name: data
          devices:
            - "{{ loopback_devicename.content | b64decode }}"
          size: 4
      storage_volumes:
        - name: test1
          vg: data
          size: 1G
          opts: --zero n
      storage_filesystems:
        - name: /dev/data/test1
          fstype: xfs
      # Mounting is not idempotent for:
      # - debian:bullseye
      # - ubuntu:focal
      # - ubuntu:bionic
      # storage_mounts:
      #   - name: /mnt/test
      #     src: /dev/data/test1
      #     fstype: xfs
      #     owner: root
      #     group: root
      #     mode: "0755"
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-storage/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap

  tasks:
    # These are "cleanup" tasks, to make sure the test is run in a non-biased environment.
    - name: Unmount /mnt/test
      ansible.posix.mount:
        path: /mnt/test
        state: absent

    - name: Install lvm2
      ansible.builtin.package:
        name: lvm2

    - name: Remove lv
      community.general.lvol:
        vg: data
        lv: test1
        state: absent
        force: true

    - name: Remove all loop devices
      ansible.builtin.command:
        cmd: losetup -D
      changed_when: true
      when:
        - ansible_distribution != "Alpine"

    - name: Remove loop_device on Alpine
      when:
        - ansible_distribution == "Alpine"
      block:
        - name: Find loop devices
          ansible.builtin.command:
            cmd: losetup -a
          register: loop_devices
          changed_when: false

        - name: Remove loop device
          ansible.builtin.command:
            cmd: "losetup -d {{ item | split(':') | first }}"
          changed_when: true
          loop: "{{ loop_devices.stdout_lines }}"

    # Since we're in a container, let's create a file.
    # Normally you would not require this, as `/dev/sd*` (or so) would be used.
    - name: Create a 4GB file
      community.general.filesize:
        path: /blockdevice.img
        size: 4G
        owner: root
        group: root
        mode: "0644"

    - name: Find first unused loop device
      ansible.builtin.command:
        cmd: losetup -f
      register: loop_device
      changed_when: false

    - name: Store loop device on disk
      ansible.builtin.copy:
        content: "{{ loop_device.stdout }}"
        dest: /loopback-devicename.txt
        owner: root
        group: root
        mode: "0644"

    - name: Create loop device
      ansible.builtin.command:
        cmd: losetup {{ loop_device.stdout }} /blockdevice.img
      changed_when: true
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-storage/blob/master/defaults/main.yml):

```yaml
---
# defaults file for storage

storage_default_fstype: ext4

# storage_partitions:
#   - name: /dev/sdb
#     number: 1
#     part_end: 4GiB
#     label: gpt
#   - name: /dev/sdb
#     number: 2
#     flags:
#       - lvm
#     part_start: 4GiB
#     part_end: 8GiB

# storage_volumegroups:
#   - name: group1
#     devices:
#       - /dev/sdb2
#     size: 8
#   - name: group2
#     devices:
#       - /dev/sdb2
#     size: 128M

# storage_volumes:
#   - name: var1
#     vg: group1
#     size: 16

# storage_filesystems:
#   - name: /dev/group1/var
#     fstype: ext4

# storage_mounts:
#   - name: /var
#     src: /dev/group1/var1
#     owner: root
#     group: root
#     mode: "0755"
#     opts: defaults
#     boot: true
#     dump: 0
#     passno: 2
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-storage/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-storage/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-storage/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-storage/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
