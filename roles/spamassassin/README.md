# [spamassassin](#spamassassin)

Install and configure spamassassin on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-spamassassin/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-spamassassin/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-spamassassin/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-spamassassin)|[![quality](https://img.shields.io/ansible/quality/23093)](https://galaxy.ansible.com/robertdebock/spamassassin)|[![downloads](https://img.shields.io/ansible/role/d/23093)](https://galaxy.ansible.com/robertdebock/spamassassin)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-spamassassin.svg)](https://github.com/robertdebock/ansible-role-spamassassin/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-spamassassin/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.spamassassin
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-spamassassin/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.cron
    - role: robertdebock.roles.logrotate
      logrotate_entries:
        - name: spamassassin
          path: /var/log/spamassassin
          missingok: yes
    - role: robertdebock.roles.rsyslog
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-spamassassin/blob/master/defaults/main.yml):

```yaml
---
# defaults file for spamassassin

# What group and user spamd should run under.
spamassassin_group: spamd
spamassassin_user: spamd
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-spamassassin/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-cron)|
|[robertdebock.logrotate](https://galaxy.ansible.com/robertdebock/logrotate)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-logrotate/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-logrotate/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-logrotate/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-logrotate)|
|[robertdebock.rsyslog](https://galaxy.ansible.com/robertdebock/rsyslog)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-rsyslog/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-rsyslog/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-rsyslog/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-rsyslog)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-spamassassin/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/repository/docker/robertdebock/alpine/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-spamassassin/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-spamassassin/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
