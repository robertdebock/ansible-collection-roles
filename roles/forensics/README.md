# [Ansible role forensics](#forensics)

Install and configure forensics on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-forensics/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-forensics/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-forensics/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-forensics)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/forensics)](https://galaxy.ansible.com/robertdebock/forensics)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-forensics.svg)](https://github.com/robertdebock/ansible-role-forensics/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-forensics/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.forensics
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-forensics/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-forensics/blob/master/defaults/main.yml):

```yaml
---
# defaults file for forensics

# A directory where collected data can be stored locally.
forensics_local_storage_path: /tmp/forensics

# A list of commands to run.
forensics_command_list:
  - "journalctl -xe"
  - "ps -ef"
  - "lsof"
  - "systemctl status"
  - "netstat -an"
  - "netstat -tulpen"

# A list of directories to collect all files from.
forensics_directory_list:
  - "/var/log"
  - "/tmp"
  - "/var/tmp"
  - "/var/spool/cron"
  - "/var/spool/anacron"
  - "/etc/cron.d"
  - "/etc/cron.daily"
  - "/etc/cron.hourly"
  - "/etc/cron.monthly"
  - "/etc/cron.weekly"
  - "/var/spool/at"

# A list of files to collect.
forensics_file_list:
  - "/etc/passwd"
  - "/etc/group"
  - "/etc/shadow"

# A list of directories and patterns to collect.
forensics_specific_file_list:
  - path: "/root"
    pattern: ".authorized_keys"
  - path: "/root"
    pattern: ".bash_history"
  - path: "/root"
    pattern: ".history"
  - path: "/home"
    pattern: ".authorized_keys"
  - path: "/home"
    pattern: ".bash_history"
  - path: "/home"
    pattern: ".history"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-forensics/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-forensics/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-forensics/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-forensics/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
