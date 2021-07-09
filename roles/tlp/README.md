# [tlp](#tlp)

Save laptop battery power using TLP

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-tlp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-tlp/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-tlp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-tlp)|[![quality](https://img.shields.io/ansible/quality/49809)](https://galaxy.ansible.com/robertdebock/tlp)|[![downloads](https://img.shields.io/ansible/role/d/49809)](https://galaxy.ansible.com/robertdebock/tlp)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-tlp.svg)](https://github.com/robertdebock/ansible-role-tlp/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.tlp
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
    - role: robertdebock.epel
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for tlp

# You can configure start and stop thresholds per battery.
# In CI there are not batteries, so disabling this list by default.

# tlp_batteries:
#   - name: BAT0
#     start_threshold: 70
#     stop_threshold: 90
#   - name: BAT1
#     start_threshold: 70
#     stop_threshold: 90
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-tlp/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-tlp/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|debian|buster|
|el|8|
|fedora|all|
|opensuse|all|
|ubuntu|bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| ubuntu:latest | Can't locate Tie/Hash/NamedCapture.pm in @INC |
| debian:bullseye | Can't locate Tie/Hash/NamedCapture.pm in @INC |
| alpine | Starting TLP is not idempotent. |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-tlp/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
