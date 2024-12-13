# [Ansible role oracle_instant_client](#oracle_instant_client)

Install oracle_instant_client on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-oracle_instant_client/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-oracle_instant_client/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-oracle_instant_client/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-oracle_instant_client)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/oracle_instant_client)](https://galaxy.ansible.com/robertdebock/oracle_instant_client)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-oracle_instant_client.svg)](https://github.com/robertdebock/ansible-role-oracle_instant_client/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-oracle_instant_client/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.oracle_instant_client
      oracle_instant_client_version: "19.17.0.0.0"
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-oracle_instant_client/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-oracle_instant_client/blob/master/defaults/main.yml):

```yaml
---
# defaults file for oracle_instant_client

# What type of package to install, either "basic", "devel", or "all".
oracle_instant_client_type: "all"

# The version of the client to install. Versions can be found here: https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html
oracle_instant_client_version: "21.15.0.0.0"

# Set the installation package type, either: "package" or "zip".
# The `oracle_instant_client_selected_type` is detected in `vars/main.yml`, but can be overridden here.
oracle_instant_client_installation_type: "{{ oracle_instant_client_selected_type }}"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-oracle_instant_client/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-oracle_instant_client/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|jammy, focal|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-oracle_instant_client/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-oracle_instant_client/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
