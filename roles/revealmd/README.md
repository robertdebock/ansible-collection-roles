# [revealmd](#revealmd)

Install and configure revealmd on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-revealmd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-revealmd/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-revealmd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-revealmd)|[![quality](https://img.shields.io/ansible/quality/21646)](https://galaxy.ansible.com/robertdebock/revealmd)|[![downloads](https://img.shields.io/ansible/role/d/21646)](https://galaxy.ansible.com/robertdebock/revealmd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-revealmd.svg)](https://github.com/robertdebock/ansible-role-revealmd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.revealmd
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.epel
    - role: robertdebock.git
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for revealmd

# The directory where reveal-md should find presentations.
revealmd_directory: /data

# The exact presentation to process
revealmd_presentation: index.md

# The tcp port where reveal-md should listen on.
revealmd_port: 1948

# The theme to use.
# https://github.com/highlightjs/highlight.js/tree/master/src/styles
revealmd_options: --theme black
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-revealmd/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.git](https://galaxy.ansible.com/robertdebock/git)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-git/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-git/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-git/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-git)|
|[robertdebock.npm](https://galaxy.ansible.com/robertdebock/npm)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-npm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-npm/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-npm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-npm)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-service)|

## [Dependencies](#dependencies)

Most roles require some kind of preparation, this is done in `molecule/default/prepare.yml`. This role has a "hard" dependency on the following roles:

- robertdebock.npm
## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-revealmd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|buster|
|fedora|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| centos:7 | /usr/lib/node_modules/reveal-md/bin/reveal-md.js:29 (async () => { |
| redhat:7 | /usr/lib/node_modules/reveal-md/bin/reveal-md.js:29 (async () => { |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-revealmd/issues)

## [License](#license)

Apache-2.0

## [Contributors](#contributors)

I'd like to thank everybody that made contributions to this repository. It motivates me, improves the code and is just fun to collaborate.


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
