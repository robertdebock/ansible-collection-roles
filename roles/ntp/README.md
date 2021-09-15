# [ntp](#ntp)

Install and configure ntp on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-ntp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ntp/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-ntp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ntp)|[![quality](https://img.shields.io/ansible/quality/23988)](https://galaxy.ansible.com/robertdebock/ntp)|[![downloads](https://img.shields.io/ansible/role/d/23988)](https://galaxy.ansible.com/robertdebock/ntp)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-ntp.svg)](https://github.com/robertdebock/ansible-role-ntp/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.cron
    - role: robertdebock.ntp
      ntp_state: stopped
```

The machine needs to be prepared in CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for ntp

# The state of the NTP service.
ntp_state: started

# The state of the NTP service at boot.
ntp_enabled: yes

# A list of IP addresses to listen on.
ntp_interfaces:
  - address: 127.0.0.1

# A list of NTP pools and their options.
ntp_pool:
  - name: 0.pool.ntp.org iburst
  - name: 1.pool.ntp.org iburst
  - name: 2.pool.ntp.org iburst
  - name: 3.pool.ntp.org iburst

# A list of NTP servers and their options.
# ntp_server:
#   - name: ntp.example.com
#     options:
#       - iburst

# The timezone.
ntp_timezone: Europe/Amsterdam
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-ntp/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cron)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-ntp/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|amazon|Candidate|
|el|8|
|debian|buster, bullseye|
|fedora|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| alpine | /lib/rc/sh/openrc-run.sh: line 100: can't create /sys/fs/cgroup/systemd/tasks: Read-only file system |
| opensuse | ConditionVirtualization=!container was not met |
| debian:buster | Unable to restart service ntp: Job for ntp.service failed because the control process exited with error code. |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-ntp/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
