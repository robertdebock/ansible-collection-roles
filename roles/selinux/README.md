# [Ansible role selinux](#selinux)

Install and configure selinux and its required libraries on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-selinux)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/selinux)](https://galaxy.ansible.com/robertdebock/selinux)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-selinux.svg)](https://github.com/robertdebock/ansible-role-selinux/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-selinux/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.selinux
      selinux_reboot: false
      selinux_booleans:
        - name: http_can_network_connect
        - name: abrt_anon_write
          state: false
          persistent: false
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-selinux/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-selinux/blob/master/defaults/main.yml):

```yaml
---
# defaults file for selinux

# The state, either disabled, permissive or enforcing.
selinux_state: enforcing

# The policy, default: see vars/main.yml.
# The policy differs per distribution, mostly because Debian and Ubuntu use 'default' and other distributions use 'targeted'.
selinux_policy: "{{ _selinux_policy[ansible_os_family] | default(_selinux_policy['default']) }}"

# Should the machine be rebooted after changes?
selinux_reboot: true

# You can enable (or disable) booleans by specifying them in this list.
# selinux_booleans:
#   - name: http_can_network_connect
#   - name: abrt_anon_write
#     state: false
#     persistent: false
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-selinux/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-selinux/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-selinux/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-selinux/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
