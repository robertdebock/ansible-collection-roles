# [luks](#luks)

Create encrypted devices using luks and open them at boot.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-luks/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-luks/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-luks/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-luks)|[![quality](https://img.shields.io/ansible/quality/52794)](https://galaxy.ansible.com/robertdebock/luks)|[![downloads](https://img.shields.io/ansible/role/d/52794)](https://galaxy.ansible.com/robertdebock/luks)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-luks.svg)](https://github.com/robertdebock/ansible-role-luks/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.luks
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap

  # tasks:
  #   - name: create disk0.img
  #     command: dd if=/dev/zero of=/disk0.img bs=1 count=1G
  #     args:
  #       creates: /disk0.img

  #   - name: create /dev/loop0
  #     command: mknod /dev/loop0 b 7 8
  #     args:
  #       creates: /dev/loop0
  #     notify:
  #       - link disk0.img to /dev/loop0

  # handlers:
  #   - name: link disk0.img to /dev/loop0
  #     command: losetup /dev/loop0 /disk0.img
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for luks

# The state of luks devices if not mentioned specifically.
luks_default_state: opened

# A list of devices to encrypt.
luks_devices: []

# For example:
# luks_devices:
#   - device: /dev/loop0
#     name: luksdisk0
#     keyfile: /etc/luksdisk0.keyfile
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-luks/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-luks/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|Candidate|
|el|8|
|debian|all|
|fedora|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-luks/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
