# [Ansible role tailscale](#tailscale)

Install and configure tailscale on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-tailscale/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-tailscale/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-tailscale/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-tailscale)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/tailscale)](https://galaxy.ansible.com/robertdebock/tailscale)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-tailscale.svg)](https://github.com/robertdebock/ansible-role-tailscale/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-tailscale/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.tailscale
      # When setting the `tailscale_authkey`, a node can join automatically.
      # In case the `tailscale_authkey` is unset, registration of the node is manual.
      # tailscale_authkey: "tskey-auth-KEY_IDENTITY-KEY_SERET_KEY_SERET_KEY_SERET_KE"
      #
      # You can request the node to publish itself as an exit node.
      # tailscale_exit_node: true
      #
      # You can advertise certain routes to the Tailscale network.
      # tailscale_advertise_routes:
      #   - 10.0.0.0/24
      #   - 10.0.1.0/24
      #
      # You can give hosts a specific name:
      # tailscale_hostname: some_hostname
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-tailscale/blob/master/molecule/default/prepare.yml):

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

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-tailscale/blob/master/defaults/main.yml):

```yaml
---
# defaults file for tailscale

# You can configure your tailscale node to act as an exit node.
# Enabling this, sets the required sysctl settings and adds a firewalld rule.
tailscale_exit_node: false

# To route traffice for certain subnets through tailscale, add them here.
tailscale_advertise_routes: []

# Nodes can authenticate with the tailscale service using an authkey.
# These keys can be created here: https://login.tailscale.com/admin/settings/keys
tailscale_authkey: ""

# You can specify a hostname.
tailscale_hostname: "{{ ansible_hostname }}"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-tailscale/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-tailscale/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-tailscale/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-tailscale/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
