# [glusterfs](#glusterfs)

Install and configure glusterfs on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-glusterfs/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-glusterfs/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-glusterfs/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-glusterfs)|[![quality](https://img.shields.io/ansible/quality/29310)](https://galaxy.ansible.com/robertdebock/glusterfs)|[![downloads](https://img.shields.io/ansible/role/d/29310)](https://galaxy.ansible.com/robertdebock/glusterfs)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-glusterfs.svg)](https://github.com/robertdebock/ansible-role-glusterfs/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.glusterfs
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.apt_autostart
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for glusterfs

# A list of bricks and their properties.
# glusterfs_bricks:
#   - name: brick1
#     device: /dev/vdb
#     mountpoint: /data/brick1

# A list of volumes and their properties.
# glusterfs_volumes:
#   - name: gv0
#     bricks: /data/brick1/gv0
#     replicas: 3
#     mountpoint: /mnt/gv0
#     rebalance: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-glusterfs/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.apt_autostart](https://galaxy.ansible.com/robertdebock/apt_autostart)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-apt_autostart/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-apt_autostart/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-apt_autostart/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-apt_autostart)|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-glusterfs/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|debian|bullseye|
|fedora|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| Alpine | glusterfs (missing) |
| EL | No package glusterfs available. |
| opensuse | The package glusterfs requires python2... |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-glusterfs/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
