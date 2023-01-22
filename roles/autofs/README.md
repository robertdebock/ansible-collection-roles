# [autofs](#autofs)

Install and configure autofs on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-autofs/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-autofs/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-autofs/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-autofs)|[![quality](https://img.shields.io/ansible/quality/51020)](https://galaxy.ansible.com/robertdebock/autofs)|[![downloads](https://img.shields.io/ansible/role/d/51020)](https://galaxy.ansible.com/robertdebock/autofs)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-autofs.svg)](https://github.com/robertdebock/ansible-role-autofs/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-autofs/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.autofs
      autofs_maps:
        - mountpoint: /bind/mnt
          options:
            - "--timeout 60"
          directories:
            - path: mount
              server: ":/mnt"
              options:
                - "fstype=bind"
        - name: direct-mounts
          mountpoint: /-
          options:
            - "--timeout 60"
            - "--ghost"
          directories:
            - path: /bind/direct/mount
              server: ":/mnt"
              options:
                - "fstype=bind"
        - mountpoint: /do_not_exist
          state: absent
      nis_master_map: auto.master
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-autofs/blob/master/molecule/default/prepare.yml):

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

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-autofs/blob/master/defaults/main.yml):

```yaml
---
# defaults file for autofs

# The first slash in a path will be removed, all remaining slashes will be replaced with this character.
#   Example: mountpoint=/bin/mount & slash_replace_char="-"
#   Output file name: /etc/auto.bind-mount (leading slash removed, remaining replaced with "-")
slash_replace_char: ""

# Here you can configure automount mountpoints.
# autofs_maps:
#   - mountpoint: /home
#     directories:
#       - path: "*"
#         server: "server.example.com/&"
#   - mountpoint: /net
#     options:
#       - "--timeout=60"
#     directories:
#       - path: server
#         options:
#           - rw
#           - soft
#           - intr
#           - rsize=8192
#           - wsize=8192
#         server: "server.example.com:/"
#   - name: cifs-mounts  # optionally name the map (for use in files names).
#     mountpoint: /cifs
#     directories:
#       - path: data
#         options:
#           - fstype=cifs
#         server: "://server.example.com/sharename/"
#   - mountpoint: /fuse
#     directories:
#       - path: ftpserver
#         options:
#           - fstype=curl
#           - rw
#           - allow_others
#           - nodev
#           - nonempty
#           - noatime
#         server: ':ftp\://username\:password\@ftp.example.com'
#   - mountpoint: /do_not_exist
#     state: absent

# Set the nis_master_map.
# nis_master_map: auto.master
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-autofs/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-autofs/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|bullseye|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-autofs/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-autofs/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
