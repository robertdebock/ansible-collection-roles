# [cups](#cups)

Install and configure CUPS, the Common Unix Printing System.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-cups/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cups/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-cups/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cups)|[![quality](https://img.shields.io/ansible/quality/51946)](https://galaxy.ansible.com/robertdebock/cups)|[![downloads](https://img.shields.io/ansible/role/d/51946)](https://galaxy.ansible.com/robertdebock/cups)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-cups.svg)](https://github.com/robertdebock/ansible-role-cups/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.cups
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
# defaults file for cups

# Allow remote access
cups_listen: "localhost:631"
cups_serveralias: "*"

# Share local printers on the local network.
cups_browsing: "Off"

# Allow access to the server...
cups_locations:
  - name: /
    order: allow,deny
    allow: "@LOCAL"
  - name: /admin
    order: allow,deny
    allow: "@LOCAL"
  - name: /admin/conf
    authtype: Default
    require: user @SYSTEM
    order: allow,deny
    allow: "@LOCAL"
  - name: /admin/log
    authtype: Default
    require: user @SYSTEM
    order: allow,deny

# Cups can save a job history. Choose from "No" or "Yes".
cups_preserve_job_history: "Yes"

# Cups can offer a web-interface. Choose from "No" or "Yes".
cups_web_interface: "Yes"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-cups/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-cups/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|Candidate|
|el|8|
|debian|all|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-cups/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
