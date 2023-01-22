# [git](#git)

Install and configure git on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-git/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-git/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-git/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-git)|[![quality](https://img.shields.io/ansible/quality/34950)](https://galaxy.ansible.com/robertdebock/git)|[![downloads](https://img.shields.io/ansible/role/d/34950)](https://galaxy.ansible.com/robertdebock/git)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-git.svg)](https://github.com/robertdebock/ansible-role-git/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-git/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  vars:
    git_username: root
    git_groupname: root
    git_repository_destination: /root
    git_repositories:
      - repo: "https://github.com/robertdebock/robertdebock.bootstrap"
        dest: bootstrap
      - repo: "https://github.com/robertdebock/robertdebock.bootstrap"
        dest: bootstrap-force
        force: yes
      - repo: "https://github.com/robertdebock/robertdebock.bootstrap"
        dest: bootstrap-version
        version: "2.11.1"

  roles:
    - role: robertdebock.roles.git
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-git/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes
  serial: 30%

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-git/blob/master/defaults/main.yml):

```yaml
---
# defaults file for git

# The system username in /home where to place the gitconfig file.
# git_username: johndoe

# The group to own directories.
# git_groupname: "{{ git_username }}"

# Settings for git configuration.
# git_user_email: johndoe@example.com
# git_user_name: John Doe

# Where to place the copies of the repositories.
git_repository_destination: /home/{{ git_username | default('unset') }}/Documents/github.com/{{ git_username | default('unset') }}

# Should git force (overwrite locally changed) clone? (Can also be controlled
# per repository, see below.
git_force: no

# The repositories to check out, bootstrap is pinned to a version, java will get HEAD/latest.
# git_repositories:
#   - repo: "https://github.com/robertdebock/ansible-role-bootstrap.git"
#     dest: bootstrap
#     version: "2.2.4"
#   - repo: "ssh://git@github.com/robertdebock/ansible-role-java.git"
#     dest: java
#   - repo: "ssh://git@github.com/robertdebock/ansible-role-tomcat.git"
#     dest: tomcat
#     force: yes
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-git/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-git/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/repository/docker/robertdebock/alpine/general)|all|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|Candidate|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-git/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-git/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
