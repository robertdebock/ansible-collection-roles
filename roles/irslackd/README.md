# [irslackd](#irslackd)

Install and configure irslackd on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-irslackd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-irslackd/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-irslackd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-irslackd)|[![quality](https://img.shields.io/ansible/quality/30532)](https://galaxy.ansible.com/robertdebock/irslackd)|[![downloads](https://img.shields.io/ansible/role/d/30532)](https://galaxy.ansible.com/robertdebock/irslackd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-irslackd.svg)](https://github.com/robertdebock/ansible-role-irslackd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.irslackd
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.epel
    - role: robertdebock.git
    - role: robertdebock.ca_certificates
    - role: robertdebock.npm
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for irslackd

# The tcp port that irslackd should listen on.
irslackd_port: 6697

# The address that irslackd should bind to.
irslackd_address: "0.0.0.0"

# Where to install irslackd.
irslackd_dest: /opt/irslackd

# The version of irslackd to install.
irslackd_version: b8ab630c877819d8b4bac9ab808b408e06cdb350

# These settings are used for the SSL certificate.
irslackd_country: NL
irslackd_state: Utrecht
irslackd_location: Breukelen
irslackd_organization: Very little
irslackd_organizational_unit: IT Department
irslackd_common_name: "{{ ansible_fqdn }}"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-irslackd/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ca_certificates)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.git](https://galaxy.ansible.com/robertdebock/git)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-git/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-git/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-git/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-git)|
|[robertdebock.npm](https://galaxy.ansible.com/robertdebock/npm)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-npm/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-npm/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-npm/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-npm)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-service)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-irslackd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|bullseye|
|fedora|all|
|ubuntu|focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-irslackd/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
