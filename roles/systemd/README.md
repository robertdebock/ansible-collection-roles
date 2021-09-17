# [systemd](#systemd)

Set default target and configure systemd.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-systemd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-systemd/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-systemd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-systemd)|[![quality](https://img.shields.io/ansible/quality/49836)](https://galaxy.ansible.com/robertdebock/systemd)|[![downloads](https://img.shields.io/ansible/role/d/49836)](https://galaxy.ansible.com/robertdebock/systemd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-systemd.svg)](https://github.com/robertdebock/ansible-role-systemd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.systemd
      systemd_default_target: multi-user.target
      systemd_coredump:
        - option: Compress
          value: "yes"
      systemd_journald:
        - option: LineMax
          value: 48k
      systemd_logind:
        - option: HandleLidSwitch
          value: ignore
      systemd_resolved:
        - option: DNSOverTLS
          value: "no"
      systemd_system:
        - option: LogLevel
          value: info
      systemd_user:
        - option: DefaultStartLimitBurst
          value: 5
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
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

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for systemd

# Select the target to boot into. Either "multiuser.target",
# "graphical.target" or "rescue.target".
# systemd_default_target: multi-user.target

# Set options in coredump.conf. For example:
# systemd_coredump:
#   - option: Compress
#     value: "yes"

# Set options in journald.conf. For example:
# systemd_journald:
#   - option: LineMax
#     value: 48k

# Set options in logind.conf. For example:
# systemd_logind:
#   - option: HandleLidSwitch
#     value: ignore

# Set options in resolved.conf. For example:
# systemd_resolved:
#   - option: DNSOverTLS
#     value: "no"

# Set options in system.conf. For example:
# systemd_system:
#   - option: LogLevel
#     value: info

# Set options in user.conf. For example:
# systemd_logind:
#   - option: DefaultStartLimitBurst
#     value: 5
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-systemd/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-systemd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|debian|all|
|el|8|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-systemd/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
