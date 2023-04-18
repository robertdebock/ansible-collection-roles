# [cntlm](#cntlm)

Install and configure cntlm on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-cntlm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cntlm/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-cntlm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-cntlm)|[![quality](https://img.shields.io/ansible/quality/25457)](https://galaxy.ansible.com/robertdebock/cntlm)|[![downloads](https://img.shields.io/ansible/role/d/25457)](https://galaxy.ansible.com/robertdebock/cntlm)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-cntlm.svg)](https://github.com/robertdebock/ansible-role-cntlm/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-cntlm/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.cntlm
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-cntlm/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.epel
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-cntlm/blob/master/defaults/main.yml):

```yaml
---
# defaults file for cntlm

# The version of CNTLM to install.
cntlm_version: "0.92.3"

# What release to install.
cntlm_release: 1

# Where to download CNTLM from.
cntlm_download_mirror: netcologne.dl.sourceforge.net

# CNTLM authenticate to the proxy, set a username, password and domain.
cntlm_username: changeme
cntlm_password: changeme
cntlm_domain: example.com
cntlm_proxy: "changeme.example.com:3128"

# To what port should CNTLM listen?
cntlm_listen: 3128

# When you've got a password hash, you may fill it in here.
# cntlm_passntlmv2: 1234567890abcdef
cntlm_auth_ntlm: no

# What hosts to omit in the proxy.
cntlm_noproxy: localhost

# Where to install temporary files
cntlm_tmp: /root

# Which IPs or CIDR subnets CNTLM is accessible from.
# Items other than 127.0.0.1 are only effective if gateway_enabled is set to `yes`.
cntlm_allows:
  - "127.0.0.1"

# If "yes", include the default ansible_default_ipv4 IP in cntlm_allows ([inventory_hostname]['ansible_default_ipv4'] )
cntlm_allows_include_local_ipv4: no

# By default ("0/0"), CNTLM is inaccessible from all other IP addresses.
cntlm_denies:
  - "0/0"

# If yes, access to CNTLM is possible from outside of the local host, subject to cntlm_allows and cntlm_denies:
gateway_enabled: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-cntlm/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-buildtools)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-service)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-cntlm/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-cntlm/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-cntlm/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
