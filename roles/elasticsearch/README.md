# [elasticsearch](#elasticsearch)

Install and configure Elasticsearch on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-elasticsearch/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-elasticsearch/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-elasticsearch/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-elasticsearch)|[![quality](https://img.shields.io/ansible/quality/56420)](https://galaxy.ansible.com/robertdebock/elasticsearch)|[![downloads](https://img.shields.io/ansible/role/d/56420)](https://galaxy.ansible.com/robertdebock/elasticsearch)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-elasticsearch.svg)](https://github.com/robertdebock/ansible-role-elasticsearch/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.elasticsearch
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
    - role: robertdebock.core_dependencies
    - role: robertdebock.elastic_repo
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for elasticsearch

# Elastic offers both "oss" (Apache 2.0 license) and "elastic"
# (Elastic license). Select the type here. Either "oss" or "elastic"
elasticsearch_type: oss

# The IP address to bind on.
elasticsearch_network_host: "0.0.0.0"

# The port to bind on.
elasticsearch_http_port: 9200

# Provides a list of the addresses of the master-eligible nodes in the cluster
elasticsearch_discovery_seed_hosts: []

# Sets the initial set of master-eligible nodes in a brand-new cluster.
elasticsearch_cluster_initial_master_nodes: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-elasticsearch/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.elastic_repo](https://galaxy.ansible.com/robertdebock/elastic_repo)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-elastic_repo/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-elastic_repo/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-elastic_repo/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-elastic_repo)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-elasticsearch/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|amazon|all|
|debian|all|
|el|7, 8|
|fedora|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-elasticsearch/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
