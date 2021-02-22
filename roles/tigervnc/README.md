# [tigervnc](#tigervnc)

Install and configure tigervnc on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-tigervnc/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-tigervnc/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-tigervnc/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-tigervnc)|[![quality](https://img.shields.io/ansible/quality/46981)](https://galaxy.ansible.com/robertdebock/tigervnc)|[![downloads](https://img.shields.io/ansible/role/d/46981)](https://galaxy.ansible.com/robertdebock/tigervnc)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-tigervnc.svg)](https://github.com/robertdebock/ansible-role-tigervnc/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.tigervnc
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.gnome
    - role: robertdebock.users
      users_group_list:
        - name: vncgroup
      users_user_list:
        - name: vncuser
          sudo_options: "ALL=(ALL) NOPASSWD: ALL"
          group: vncgroup
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for tigervnc

# The tigervnc-server runs under a specific user and group. This user is
# created in `molecule/default/prepare.yml`. You can pick an existing
# user or create one using
# [ansible-role-users](https://galaxy.ansible.com/robertdebock/users)
tigervnc_username: vncuser
tigervnc_groupname: vncgroup

# Connecting to tigervnc-server required a password.
tigervnc_password: vncpass
# Use existing user's paswword
tigervnc_user_exists: no

# Desktop session xstartup should connect to e.g. gnome-session, mate-session
tigervnc_desktop_session: gnome-session
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-tigervnc/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
| [robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)
| [robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)
| [robertdebock.gnome](https://galaxy.ansible.com/robertdebock/gnome) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-gnome/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-gnome/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-gnome/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-gnome)
| [robertdebock.users](https://galaxy.ansible.com/robertdebock/users) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-users/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-users/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-users/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-users)

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-tigervnc/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|7|
|debian|buster, bullseye|
|fedora|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-tigervnc/issues)

## [License](#license)

Apache-2.0

## [Contributors](#contributors)

I'd like to thank everybody that made contributions to this repository. It motivates me, improves the code and is just fun to collaborate.

- [jellevandehaterd](https://github.com/jellevandehaterd)
- [aindenko](https://github.com/aindenko)

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
