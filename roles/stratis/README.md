# [stratis](#stratis)

Install stratis and carves pools and filesystems.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-stratis/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-stratis/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-stratis/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-stratis)|[![quality](https://img.shields.io/ansible/quality/40309)](https://galaxy.ansible.com/robertdebock/stratis)|[![downloads](https://img.shields.io/ansible/role/d/40309)](https://galaxy.ansible.com/robertdebock/stratis)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-stratis.svg)](https://github.com/robertdebock/ansible-role-stratis/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.stratis
  # It's not easy to test block-devices in CI. That's why the next block
  # of variables is commented, but left here as an example.
  #    stratis_pools:
  #      - name: my_pool
  #        devices:
  #          - /dev/vdb
  #          - /dev/vdc
  #    stratis_filesystems:
  #      - name: my_filesystem
  #        pool: my_pool
  #    stratis_mounts:
  #      - mountpoint: /mnt/my_mountpoint
  #        device: /stratis/my_pool/my_filesystem
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  vars:
    devices:
      - name: vdc
        major: 252
        minor: 2
      - name: vdd
        major: 252
        minor: 3

  roles:
    - role: robertdebock.bootstrap

  tasks:
    - name: create storage file
      command: dd if=/dev/zero of=/{{ item.name }} bs=1M count=1K
      args:
        creates: "/{{ item.name }}"
      loop: "{{ devices }}"
      notify:
        - create loopback device
        - loopback device to storage file
      loop_control:
        label: "/{{ item.name }}"

  handlers:
    - name: create loopback device
      command: mknod /dev/{{ item.name }} b {{ item.major }} {{ item.minor }}
      loop: "{{ devices }}"
      loop_control:
        label: "/dev/{{ item.name }}"
      changed_when: no

    - name: loopback device to storage file
      command: losetup /dev/{{ item.name }} /{{ item.name }}
      loop: "{{ devices }}"
      failed_when: no
      loop_control:
        label: "/dev/{{ item.name }} to /{{ item.name }}"
      changed_when: no
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.


## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-stratis/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-stratis/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|fedora|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-stratis/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
