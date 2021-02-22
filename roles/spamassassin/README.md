# [spamassassin](#spamassassin)

Install and configure spamassassin on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-spamassassin/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-spamassassin/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-spamassassin/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-spamassassin)|[![quality](https://img.shields.io/ansible/quality/23093)](https://galaxy.ansible.com/robertdebock/spamassassin)|[![downloads](https://img.shields.io/ansible/role/d/23093)](https://galaxy.ansible.com/robertdebock/spamassassin)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-spamassassin.svg)](https://github.com/robertdebock/ansible-role-spamassassin/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.spamassassin
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.cron
    - role: robertdebock.logrotate
    - role: robertdebock.rsyslog
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for spamassassin

# What group and user spamd should run under.
spamassassin_group: spamd
spamassassin_user: spamd
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-spamassassin/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
| [robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)
| [robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)
| [robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cron)
| [robertdebock.logrotate](https://galaxy.ansible.com/robertdebock/logrotate) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-logrotate/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-logrotate/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-logrotate/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-logrotate)
| [robertdebock.rsyslog](https://galaxy.ansible.com/robertdebock/rsyslog) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-rsyslog/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-rsyslog/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-rsyslog/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-rsyslog)
| [robertdebock.spamassassin](https://galaxy.ansible.com/robertdebock/spamassassin) | [![Build Status GitHub](https://github.com/robertdebock/ansible-role-spamassassin/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-spamassassin/actions) | [![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ansible-role-spamassassin/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-spamassassin)

## [Dependencies](#dependencies)

Most roles require some kind of preparation, this is done in `molecule/default/prepare.yml`. This role has a "hard" dependency on the following roles:

- robertdebock.rsyslog
## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-spamassassin/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|el|7, 8|
|debian|buster, bullseye|
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
| Archlinux | target not found: rsyslog |
| amazonlinux:1 | /etc/init.d/spamassassin: line 17: /etc/sysconfig/network: No such file or directory |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-spamassassin/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
