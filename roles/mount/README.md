# [mount](#mount)

Configure mounts

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-mount/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mount/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-mount/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-mount)|[![quality](https://img.shields.io/ansible/quality/51485)](https://galaxy.ansible.com/robertdebock/mount)|[![downloads](https://img.shields.io/ansible/role/d/51485)](https://galaxy.ansible.com/robertdebock/mount)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-mount.svg)](https://github.com/robertdebock/ansible-role-mount/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.mount
      mount_requests:
        - path: /mnt/tmp
          src: /tmp
          opts: bind
          fstype: none
          mode: "1777"
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
# defaults file for mount

# The `mode`, `owner` and `group` can be set in the `mount_requests` list, but
# when not specified, these defaults are used.
mount_default_mode: "0750"
mount_default_owner: root
mount_default_group: root

# You can define mounts as variables. All parameters for the `mount` module are
# supported.

# mount_requests:
#   - path: /mnt/tmp
#     src: /tmp
#     opts: bind
#     fstype: none
#   - path: swap
#     src: /dev/data/swap
#     fstype: swap
#     opts: sw
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-mount/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-mount/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|debian|all|
|el|8|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-mount/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
