# [mssql](#mssql)

Install and configure mssql on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-mssql/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-mssql/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-mssql/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-mssql)|[![quality](https://img.shields.io/ansible/quality/24094)](https://galaxy.ansible.com/robertdebock/mssql)|[![downloads](https://img.shields.io/ansible/role/d/24094)](https://galaxy.ansible.com/robertdebock/mssql)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-mssql.svg)](https://github.com/robertdebock/ansible-role-mssql/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-mssql/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.roles.mssql
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-mssql/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.roles.bootstrap
    - role: robertdebock.roles.roles.core_dependencies
    - role: robertdebock.roles.roles.ca_certificates
    - role: robertdebock.roles.roles.microsoft_repository_keys
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-mssql/blob/master/defaults/main.yml):

```yaml
---
# defaults file for mssql

# mssql_add_repositories can be used to select if you want the repositories installed by this role.
# See vars/main.yml for the location of the repositories. Can be: yes, true or 1.
mssql_add_repositories: yes

# What version to use, currently either 2017 or 2019.
# `2017` is the only working version now, `2019` lacks the required
# mssql-server-agent package.
mssql_version: "2017"

# Select the version of server and server_agent to install.
mssql_server_version: "14.0.3294.2-27"
mssql_server_agent_version: "14.0.3015.40-1"

# mssql_sa_password contains the password for a system administrator.
# The password must be at least 8 characters long and contain characters from
# three of the following four sets:
# - uppercase letters
# - lowercase letters
# - numbers
# - and symbols
mssql_sa_password: "StR0nGp4ss."

# mssql_pid refers to the product key to use. Either:
# - Evaluation
# - Developer
# - Express
# - Web
# - Standard
# - Enterprise
# - A product key (Format: #####-#####-#####-#####-#####)
mssql_pid: Evaluation

# To enable full text search, set this value to yes.
mssql_fts: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-mssql/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-ca_certificates)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.microsoft_repository_keys](https://galaxy.ansible.com/robertdebock/microsoft_repository_keys)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-microsoft_repository_keys/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-microsoft_repository_keys/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-microsoft_repository_keys/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-microsoft_repository_keys)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-mssql/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|Candidate|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|7|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-mssql/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-mssql/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
