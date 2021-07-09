# [aide](#aide)

Install and configure aide on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-aide/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-aide/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-aide/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-aide)|[![quality](https://img.shields.io/ansible/quality/44968)](https://galaxy.ansible.com/robertdebock/aide)|[![downloads](https://img.shields.io/ansible/role/d/44968)](https://galaxy.ansible.com/robertdebock/aide)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-aide.svg)](https://github.com/robertdebock/ansible-role-aide/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.aide
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
    - role: robertdebock.cron
    - role: robertdebock.postfix
      postfix_myhostname: "smtp.example.com"
      postfix_mydomain: "example.com"
      postfix_myorigin: "example.com"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.


## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-aide/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cron)|
|[robertdebock.postfix](https://galaxy.ansible.com/robertdebock/postfix)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-postfix/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-postfix/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-postfix/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-postfix)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-aide/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|amazon|Candidate|
|el|8|
|debian|buster|
|fedora|all|
|opensuse|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| alpine | aide (missing): required by: world[aide] |
| debian:unstable | No package matching 'aide' is available |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-aide/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
