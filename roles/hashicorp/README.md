# [hashicorp](#hashicorp)

Install HashiCorp products using packages.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-hashicorp)|[![quality](https://img.shields.io/ansible/quality/51612)](https://galaxy.ansible.com/robertdebock/hashicorp)|[![downloads](https://img.shields.io/ansible/role/d/51612)](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-hashicorp.svg)](https://github.com/robertdebock/ansible-role-hashicorp/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.hashicorp
      hashicorp_products:
        - name: consul

    - role: robertdebock.hashicorp
      hashicorp_installation_method: manual
      hashicorp_products:
        - name: vault
          version: 1.4.2
          type: ent
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for hashicorp

# You can select how to intall hashicorp products. Choose from `package` or
# `manual`. `manual` means this role wil download from
# "https://releases.hashicorp.com/vault/".
hashicorp_installation_method: package

# You can install hashicorp products using this list.
# hashicorp_products:
#   - name: consul
#   - name: nomad
#   - name: packer
#   - name: terraform
#   - name: vagrant
#   - name: vault

# If you are using `manual` as the `hashicorp_installation_method`, you must
# specify the version to install.
# hashicorp_products:
#   - name: vault
#     version: 1.6.0

# For `vault` you can choose what type you want to install, either:
# `oss` (default), `ent` or `hsm`.
# hashicorp_products:
#   - name: vault
#     type: oss
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-hashicorp/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-hashicorp/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|amazon|Candidate|
|el|7, 8|
|debian|buster|
|fedora|32, 33|
|ubuntu|bionic, focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-hashicorp/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
