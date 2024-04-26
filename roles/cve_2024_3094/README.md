# [Ansible role cve_2024_3094](#cve_2024_3094)

Check xz vulnerability (cve_2024_3094) on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-cve_2024_3094/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cve_2024_3094/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-cve_2024_3094/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-cve_2024_3094)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/cve_2024_3094)](https://galaxy.ansible.com/robertdebock/cve_2024_3094)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-cve_2024_3094.svg)](https://github.com/robertdebock/ansible-role-cve_2024_3094/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-cve_2024_3094/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.cve_2024_3094
      cve_2024_3094_cleanup: false
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-cve_2024_3094/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.openssh
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-cve_2024_3094/blob/master/defaults/main.yml):

```yaml
---
# defaults file for cve_2024_3094

# If requirements are installed, would you like to remove them after this role ran?
cve_2024_3094_cleanup: true

# Where to look for `sshd`, a list of paths.
cve_2024_3094_sshd_paths:
      - /usr/bin
      - /usr/sbin
      - /usr/local/bin
      - /usr/local/sbin
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-cve_2024_3094/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.openssh](https://galaxy.ansible.com/robertdebock/openssh)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssh/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssh/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-openssh/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-openssh)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-cve_2024_3094/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|all|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-cve_2024_3094/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-cve_2024_3094/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
