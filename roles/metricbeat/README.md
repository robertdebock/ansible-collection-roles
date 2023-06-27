# [metricbeat](#metricbeat)

Install and configure Metricbeat, manage Metricbeat modules.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-metricbeat/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-metricbeat/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-metricbeat/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-metricbeat)|[![quality](https://img.shields.io/ansible/quality/56439)](https://galaxy.ansible.com/robertdebock/metricbeat)|[![downloads](https://img.shields.io/ansible/role/d/56439)](https://galaxy.ansible.com/robertdebock/metricbeat)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-metricbeat.svg)](https://github.com/robertdebock/ansible-role-metricbeat/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-metricbeat/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.metricbeat
      metricbeat_elasticsearch_password: "My-P@s5w0rd."
      metricbeat_modules:
        - name: system
          state: enabled
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-metricbeat/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.elastic_repo
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-metricbeat/blob/master/defaults/main.yml):

```yaml
---
# defaults file for metricbeat

# The version of metricbeat to install.
metricbeat_version: "7.15.2"

# A list of modules to enable.
metricbeat_modules: []

# A list of elasticsearch hosts.
metricbeat_elasticsearch_hosts:
  - "http://localhost:9200"

# The username for elasticsearch.
metricbeat_elasticsearch_username: elastic

# The password for elasticsearch.
metricbeat_elasticsearch_password: ""

# The URL for Kibana.
metricbeat_kibana_host: "http://localhost:5601"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-metricbeat/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.elastic_repo](https://galaxy.ansible.com/robertdebock/elastic_repo)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-elastic_repo/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-elastic_repo/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-elastic_repo/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-elastic_repo)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-metricbeat/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|all|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|focal, bionic|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-metricbeat/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-metricbeat/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
