# [awx_configuration](#awx_configuration)

Configure AWX.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-awx_configuration/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-awx_configuration/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-awx_configuration/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-awx_configuration)|[![quality](https://img.shields.io/ansible/quality/60492)](https://galaxy.ansible.com/robertdebock/awx_configuration)|[![downloads](https://img.shields.io/ansible/role/d/60492)](https://galaxy.ansible.com/robertdebock/awx_configuration)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-awx_configuration.svg)](https://github.com/robertdebock/ansible-role-awx_configuration/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-awx_configuration/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.awx_configuration
      awx_configuration_ci: yes
      awx_configuration_organizations:
        - name: My organization
          description: My organization description
          # galaxy_credentials:
          #   - My Galaxy credential
      awx_configuration_credentials:
        - name: My credential
          description: My credential description
          organization: My organization
          credential_type: Machine
        - name: My Galaxy credential
          description: My Galaxy credential description
          credential_type: Ansible Galaxy/Automation Hub API Token
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-awx_configuration/blob/master/molecule/default/prepare.yml):

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

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-awx_configuration/blob/master/defaults/main.yml):

```yaml
---
# defaults file for awx_configuration

# The hostname (actually URL) of the AWX instance to connect to.
awx_configuration_controller_host: "http://localhost"

# Credentials for AWX.
awx_configuration_controller_password: "My_P@ssw0rd"
awx_configuration_controller_username: admin

# Note: An organization can refer to a credential and a credential can refer to an organization.
# This is basically a cyclic dependency this Ansible role can't fix.
# You may need to run a playbook twice:
# - first to create the credential
# - next to create the organization.
# (Or the other way around.)

# A list of organizations to create in AWX.
awx_configuration_organizations: []

# A list of credentials to create in AWX.
awx_configuration_credentials: []

# It's difficult to test this role in CI, AWX is not available.
awx_configuration_ci: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-awx_configuration/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-awx_configuration/png/requirements.png "Dependencies")

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

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-awx_configuration/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-awx_configuration/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
