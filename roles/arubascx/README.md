# [arubascx](#arubascx)

Install and configure arubascx on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-arubascx/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-arubascx/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-arubascx/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-arubascx)|[![quality](https://img.shields.io/ansible/quality/)](https://galaxy.ansible.com/robertdebock/arubascx)|[![downloads](https://img.shields.io/ansible/role/d/)](https://galaxy.ansible.com/robertdebock/arubascx)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-arubascx.svg)](https://github.com/robertdebock/ansible-role-arubascx/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-arubascx/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.arubascx
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-arubascx/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-arubascx/blob/master/defaults/main.yml):

```yaml
---
# defaults file for arubascx

arubascx_banner: "Aruba Rocks!"

arubascx_dns:
  primary: "10.10.2.10"
  secondary: "10.10.3.10"
  dns_domain_name: "hpe.com"
  dns_domain_list:
    0: "hp.com"
    1: "aru.com"
    2: "sea.com"
  dns_name_servers:
    0: "4.4.4.8"
    1: "4.4.4.10"
  dns_host_v4_address_mapping:
    host1: "5.5.44.5"
    host2: "2.2.44.2"
  vrf: "green"

arubascx_vlans:
  - vlan_id: 300
    name: UPLINK_VLAN
    description: This is VLAN 300

arubascx_interfaces:
  - name: 1/1/1
  - name: 1/1/2
    duplex: full
    speeds:
      - '1000'
    enabled: true
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-arubascx/blob/master/requirements.txt).


## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-arubascx/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/repository/docker/robertdebock/alpine/general)|all|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|all|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-arubascx/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-arubascx/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
