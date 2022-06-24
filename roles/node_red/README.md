# [node_red](#node_red)

Install and configure Node RED on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-node_red/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-node_red/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-node_red/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-node_red)|[![quality](https://img.shields.io/ansible/quality/50571)](https://galaxy.ansible.com/robertdebock/node_red)|[![downloads](https://img.shields.io/ansible/role/d/50571)](https://galaxy.ansible.com/robertdebock/node_red)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-node_red.svg)](https://github.com/robertdebock/ansible-role-node_red/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.node_red
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.ca_certificates
    - role: robertdebock.epel
    - role: robertdebock.npm
    - role: robertdebock.users
      users_group_list:
        - name: nodered
      users_user_list:
        - name: nodered
          group: nodered
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for node_red

# The directory where Node RED should be running from.
node_red_working_directory: /opt/node_red

# The user Node RED should be running under.
# This roles does not create users, see `molecule/default/prepare.yml`.
node_red_user_name: nodered

# The group Node RED should be running under.
# This roles does not create groups, see `molecule/default/prepare.yml`.
node_red_group_name: nodered
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-node_red/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ca_certificates)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.npm](https://galaxy.ansible.com/robertdebock/npm)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-npm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-npm/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-npm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-npm)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-service)|
|[robertdebock.users](https://galaxy.ansible.com/robertdebock/users)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-users/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-users/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-users/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-users)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-node_red/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|debian|bullseye|
|el|8|
|fedora|all|
|ubuntu|focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-node_red/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
