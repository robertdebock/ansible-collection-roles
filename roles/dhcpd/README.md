# [dhcpd](#dhcpd)

Install and configure dhcpd on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-dhcpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-dhcpd/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-dhcpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-dhcpd)|[![quality](https://img.shields.io/ansible/quality/21853)](https://galaxy.ansible.com/robertdebock/dhcpd)|[![downloads](https://img.shields.io/ansible/role/d/21853)](https://galaxy.ansible.com/robertdebock/dhcpd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-dhcpd.svg)](https://github.com/robertdebock/ansible-role-dhcpd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-dhcpd/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  vars:
    dhcpd_subnets:
      - network: "{{ ansible_default_ipv4.network }}"
        netmask: "255.255.255.0"

  roles:
    - role: robertdebock.roles.dhcpd
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-dhcpd/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.apt_autostart
    - role: robertdebock.roles.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-dhcpd/blob/master/defaults/main.yml):

```yaml
---
# defaults file for dhcpd

# Configuration settings for the daemon.
dhcpd_ipv4_interface: "{{ ansible_default_ipv4.interface | default('eth0') }}"

# Setting applicable for the global scope.
dhcpd_default_lease_time: 600
dhcpd_max_lease_time: 7200
dhcpd_subnet_mask: "255.255.255.0"
dhcpd_broadcast_address: "10.0.2.255"
dhcpd_routers: "10.0.2.254"
dhcpd_domain_name_servers:
  - "192.168.1.1"
  - "192.168.1.2"
dhcpd_domain_search: example.com

# The image to serve for PXE booting.
dhcpd_filename: "pxelinux.0"
# Where the image can be downloaded from.
dhcpd_next_server: "10.0.2.254"

# DHCP works with subnets, a list containing properties per subnet.
dhcpd_subnets:
  - network: "10.0.2.0"
    netmask: "255.255.255.0"
    range_start: "10.0.2.200"
    range_end: "10.0.2.210"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-dhcpd/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.apt_autostart](https://galaxy.ansible.com/robertdebock/apt_autostart)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-apt_autostart/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-apt_autostart/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-apt_autostart/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-apt_autostart)|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-dhcpd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/repository/docker/robertdebock/alpine/general)|all|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|Candidate|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-dhcpd/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-dhcpd/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
