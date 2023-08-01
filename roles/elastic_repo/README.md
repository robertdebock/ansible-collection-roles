# [elastic_repo](#elastic_repo)

Install the Elastic repository on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-elastic_repo/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-elastic_repo/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-elastic_repo/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-elastic_repo)|[![quality](https://img.shields.io/ansible/quality/56415)](https://galaxy.ansible.com/robertdebock/elastic_repo)|[![downloads](https://img.shields.io/ansible/role/d/56415)](https://galaxy.ansible.com/robertdebock/elastic_repo)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-elastic_repo.svg)](https://github.com/robertdebock/ansible-role-elastic_repo/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-elastic_repo/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.roles.elastic_repo
      elastic_repo_cleanup_requirements: no
      elastic_repo_revert_crypto_policy: no
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-elastic_repo/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.roles.bootstrap
    - role: robertdebock.roles.roles.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-elastic_repo/blob/master/defaults/main.yml):

```yaml
---
# defaults file for elastic_repo

# The software is free to use under the Elastic license.
# An alternative package which contains only features that are available
# under the Apache 2.0 license is also available.

# Elastic has two versions of the packages:
# - "elastic" using the "Elastic" license.
# - "oss" using the Apache 2.0 license.
elastic_repo_license: oss

# An extra package is required for RHEL9 (`crypto-policies-scripts`).
# This variable determines if it should be removed or not.
elastic_repo_cleanup_requirements: yes

# The crypto policy must be modified on RHEL9. This variable determines if
# the policy should be switched back to the default.
elastic_repo_revert_crypto_policy: yes
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-elastic_repo/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-elastic_repo/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|all|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-elastic_repo/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-elastic_repo/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
