# [turn](#turn)

Install and configure a (co) turn server on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-turn/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-turn/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-turn/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-turn)|[![quality](https://img.shields.io/ansible/quality/54410)](https://galaxy.ansible.com/robertdebock/turn)|[![downloads](https://img.shields.io/ansible/role/d/54410)](https://galaxy.ansible.com/robertdebock/turn)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-turn.svg)](https://github.com/robertdebock/ansible-role-turn/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.turn
      turn_listening_ip: "0.0.0.0"
      turn_external_ip: "1.2.3.4"
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
    - role: robertdebock.epel
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for turn

turn_listening_port: 3478
turn_fingerprint: yes
turn_lt_cred_mech: no
turn_use_auth_secret: yes
turn_static_auth_secret: 96ef8dbed1ba36132d9cccfa608d1f90f879d7fb38cb5c18
turn_realm: nextcloud.meinit.nl
turn_total_quota: 100
turn_bps_quota: 0
turn_stale_nonce: 600
turn_no_loopback_peers: yes
turn_no_multicast_peers: yes
turn_simple_log: yes
turn_cli_password: 5S4QtTbkC2tzJj4jRKePZJlmCVU3ljnG
turn_server_name: "{{ ansible_fqdn }}"
turn_listening_ip: "{{ ansible_default_ipv4.address }}"
turn_external_ip: "{{ ansible_default_ipv4.address }}"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-turn/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-turn/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
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


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-turn/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
