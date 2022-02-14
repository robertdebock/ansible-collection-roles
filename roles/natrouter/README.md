# [natrouter](#natrouter)

Install and configure a NAT router on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-natrouter/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-natrouter/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-natrouter/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-natrouter)|[![quality](https://img.shields.io/ansible/quality/21915)](https://galaxy.ansible.com/robertdebock/natrouter)|[![downloads](https://img.shields.io/ansible/role/d/21915)](https://galaxy.ansible.com/robertdebock/natrouter)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-natrouter.svg)](https://github.com/robertdebock/ansible-role-natrouter/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.natrouter
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.sysctl
      sysctl_items:
        - name: net.ipv4.ip_forward
          value: 1
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for natrouter

# The network interface connected to the internet.
natrouter_public_interface: eth0

# The network address to translate.
natrouter_private_network: "192.168.1.0/24"

# The destination.
natrouter_destination: "0.0.0.0/0"

# The protocols to NAT.
natrouter_protocols:
  - tcp
  - udp
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-natrouter/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.sysctl](https://galaxy.ansible.com/robertdebock/sysctl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-sysctl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-sysctl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-sysctl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-sysctl)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-natrouter/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|el|8|
|debian|all|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-natrouter/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
