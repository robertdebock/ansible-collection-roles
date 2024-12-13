# [Ansible role cisco_anyconnect](#cisco_anyconnect)

Install and configure Cisco AnyConnect Secure Mobility Client.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-cisco_anyconnect/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cisco_anyconnect/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-cisco_anyconnect/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-cisco_anyconnect)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/cisco_anyconnect)](https://galaxy.ansible.com/robertdebock/cisco_anyconnect)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-cisco_anyconnect.svg)](https://github.com/robertdebock/ansible-role-cisco_anyconnect/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-cisco_anyconnect/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.cisco_anyconnect
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-cisco_anyconnect/blob/master/molecule/default/prepare.yml):

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

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-cisco_anyconnect/blob/master/defaults/main.yml):

```yaml
---
# defaults file for cisco_anyconnect

# The directory where temporary files will be stored during installation
cisco_anyconnect_tmp_dir: /tmp/cisco-anyconnect

# The URL where the Cisco Anyconnect package can be downloaded from
cisco_anyconnect_download_url: ""
# Since this package is not typically available from a public URL, you can host your own copy and reference it here.
# cisco_anyconnect_download_url: "https://example.com/downloads/cisco-secure-client-linux64-5.1.3.62-predeploy-k9.tar.gz"

# The directory where Cisco Anyconnect will be installed
cisco_anyconnect_install_dir: /opt
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-cisco_anyconnect/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-cisco_anyconnect/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-cisco_anyconnect/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-cisco_anyconnect/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
