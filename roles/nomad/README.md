# [nomad](#nomad)

Install and configure Nomad.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-nomad/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-nomad/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-nomad/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-nomad)|[![quality](https://img.shields.io/ansible/quality/51615)](https://galaxy.ansible.com/robertdebock/nomad)|[![downloads](https://img.shields.io/ansible/role/d/51615)](https://galaxy.ansible.com/robertdebock/nomad)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-nomad.svg)](https://github.com/robertdebock/ansible-role-nomad/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-nomad/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.roles.nomad
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-nomad/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.roles.bootstrap
    - role: robertdebock.roles.roles.core_dependencies
    - role: robertdebock.roles.roles.hashicorp
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-nomad/blob/master/defaults/main.yml):

```yaml
---
# defaults file for nomad

# You can install nomad using a package in this role. If you have installed
# nomad manually, set this to `no`.
nomad_install_package: yes

# Set this to "yes" for a server.
nomad_server: yes

# Configuration items for the Nomad server
nomad_server_data_dir: /tmp/server
nomad_server_bind_addr: "0.0.0.0"
nomad_server_log_level: INFO

# How many servers and agents are expected?
nomad_server_bootstrap_expect: 1

# This this to "yes" for an agent.
nomad_agent: no

# Configuration items for the Nomad agent
nomad_agent_log_level: INFO
nomad_agent_data_dir: /tmp/agent
nomad_agent_name: "{{ inventory_hostname }}"

nomad_agent_servers:
  - name: "127.0.0.1"
    port: 4647
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-nomad/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.hashicorp](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-nomad/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8, 9|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|bullseye|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|37, 38|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-nomad/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-nomad/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
