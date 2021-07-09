# [snmpd](#snmpd)

Install and configure snmpd on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-snmpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-snmpd/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-snmpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-snmpd)|[![quality](https://img.shields.io/ansible/quality/55193)](https://galaxy.ansible.com/robertdebock/snmpd)|[![downloads](https://img.shields.io/ansible/role/d/55193)](https://galaxy.ansible.com/robertdebock/snmpd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-snmpd.svg)](https://github.com/robertdebock/ansible-role-snmpd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.snmpd
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
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for snmpd

snmpd_security_names:
  - name: notConfigUser
    source: default
    community: public

snmpd_groups:
  - name: notConfigGroup
    security_model: v1
    security_name: notConfigUser
  - name: NotConfigGroup
    security_model: v2c
    security_name: NotConfigUser

snmpd_views:
  - name: systemview
    type: included
    subtree: .1.3.6.1.2.1.1
  - name: systemview
    type: included
    subtree: .1.3.6.1.2.1.25.1.1

snmpd_accesses:
  - group: notConfigGroup
    context: ""
    security_model: any
    security_level: noauth
    prefix: exact
    read: systemview
    write: none
    notif: none

snmpd_syslocation: Unknown
snmpd_syscontact: Root <root@localhost>

snmpd_dontlogtcpwrappersconnects: "yes"

# snmpd_processes:
#   - name: mountd
#   - name: ntalkd
#     maximum: 4
#   - name: sendmail
#     minimum: 1
#     maximum: 10
#
# snmpd_scripts:
#   - name: shelltest
#     program: /bin/sh
#     arguments: /tmp/shtest

snmpd_disks:
  - path: /
    minimum: 10000

snmpd_load:
  one_minute_average: 12
  five_minute_average: 14
  fifteen_minute_average: 14
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-snmpd/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-snmpd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|all|
|debian|all|
|el|8|
|fedora|all|
|opensuse|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.9, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-snmpd/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
