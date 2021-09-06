# [consul](#consul)

Install and configure consul on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-consul/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-consul/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-consul/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-consul)|[![quality](https://img.shields.io/ansible/quality/54812)](https://galaxy.ansible.com/robertdebock/consul)|[![downloads](https://img.shields.io/ansible/role/d/54812)](https://galaxy.ansible.com/robertdebock/consul)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-consul.svg)](https://github.com/robertdebock/ansible-role-consul/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.consul
      consul_bootstrap_expect: 1
```

The machine needs to be prepared in CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.hashicorp
      hashicorp_products:
        - name: consul
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for consul

# This flag controls the datacenter in which the agent is running.
consul_datacenter: dc1

# This flag provides a data directory for the agent to store state.
consul_data_dir: /opt/consul

# The address to which Consul will bind client interfaces, including the HTTP and DNS servers
consul_client_addr: 0.0.0.0

# Enables the built-in web UI server and the required HTTP routes.
consul_ui: yes

# This flag is used to control if an agent is in server or client mode.
consul_server: yes

# This flag provides the number of expected servers in the datacenter.
# consul_bootstrap_expect: 3

# Specifies the secret key to use for encryption of Consul network traffic.
# consul_encrypt: "GEZzRM+2P+FiUcyrx9Fte8NbwtTlX3NA"

# Similar to -join but allows retrying a join until it is successful.
# consul_retry_join:
#   - consul.domain.internal

# The address that should be bound to for internal cluster communications.
# consul_bind_addr: "{{ ansible_default_ipv4.address }}"

# The advertise address is used to change the address that we advertise to other nodes in the cluster.
# consul_advertise_addr: "{{ ansible_default_ipv4.address }}"

# You can define service that Consul should manage.
# consul_services:
#   - name: web
#     tags:
#       - rails
#     port: 80
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-consul/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.hashicorp](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-hashicorp)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-consul/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|amazon|Candidate|
|debian|buster|
|el|7, 8|
|fedora|33, 34|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.9, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-consul/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
