# [rundeck](#rundeck)

Install and configure rundeck on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-rundeck/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-rundeck/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-rundeck/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-rundeck)|[![quality](https://img.shields.io/ansible/quality/22886)](https://galaxy.ansible.com/robertdebock/rundeck)|[![downloads](https://img.shields.io/ansible/role/d/22886)](https://galaxy.ansible.com/robertdebock/rundeck)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-rundeck.svg)](https://github.com/robertdebock/ansible-role-rundeck/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-rundeck/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.rundeck
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-rundeck/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.java
    - role: robertdebock.roles.common
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-rundeck/blob/master/defaults/main.yml):

```yaml
---
# defaults file for rundeck

# Rundeck version to install
rundeck_version: "4.8.0"
rundeck_release_date: 20221110

# Where to install rundeck.
rundeck_rdeckbase: /opt/rundeck

# The Xmx memory size in mb. (Stored in: "{{ rundeck_rdeckbase }}/etc/profile".)
rundeck_xmx: 4096
rundeck_xms: 256
rundeck_maxmetaspacesize: 128

# The URL where Rundeck will be served on:
rundeck_port: 4440
rundeck_address: "{{ ansible_all_ipv4_addresses[0] | default('127.0.0.1') }}"

# You can change the context to for example: "/rundeck". An empty value means
# that no specific context is added.
rundeck_server_web_context: ""

rundeck_config:
  - parameter: server.address
    value: "{{ rundeck_address }}"
  - parameter: grails.serverURL
    value: "{{ rundeck_url }}"
  - parameter: dataSource.url
    value: "jdbc:h2:file:/opt/rundeck/server/data/grailsdb;MVCC=true"
#   To connect to MySQL, use these settings. (Database has to be prepared.)
#   - parameter: dataSource.url
#     value: "jdbc:mysql://myserver/rundeck?autoReconnect=true&useSSL=false"
#   - parameter: dataSource.username
#     value: rundeck
#   - parameter: dataSource.password
#     value: rundeck
#   - parameter: dataSource.driverClassName
#     value: com.mysql.jdbc.Driver

# The settings for Rundeck. (Stored in: "{{ rundeck_rdeckbase }}/etc/framework.properties".)
rundeck_framework:
  - parameter: framework.server.hostname
    value: "{{ ansible_fqdn }}"
  - parameter: framework.server.name
    value: "{{ ansible_hostname }}"
  - parameter: framework.projects.dir
    value: "{{ rundeck_rdeckbase }}/projects"
  - parameter: framework.var.dir
    value: "{{ rundeck_rdeckbase }}/var"
  - parameter: framework.logs.dir
    value: "{{ rundeck_rdeckbase }}/var/logs"
  # - parameter: "framework.server.username"
  #   value: unset
  # - parameter: "framework.server.password"
  #   value: unset
  - parameter: framework.rundeck.url
    value: "{{ rundeck_url }}"
  # - parameter: "framework.ssh.keypath"
  #   value: unset
  # - parameter: "framework.ssh.user"
  #   value: unset
  - parameter: framework.ssh-connect-timeout
    value: 0
  - parameter: framework.ssh-command-timeout
    value: 0
  # - parameter: "framework.log.dispatch.console.format"
  #   value: unset
  - parameter: framework.rundeck.execution.script.tokenexpansion.enabled
    value: yes

# default users stored in {{ rundeck_rdeckbase }}/server/config/realm.properties
rundeck_users:
  - username: "admin"
    password: "admin"
    roles: "user,admin"
  - username: "user"
    password: "user"
    roles: "user"

# Rundeck plugins to install
rundeck_plugins: []
# - "https://github.com/Batix/rundeck-ansible-plugin/releases/download/3.1.1/ansible-plugin-3.1.1.jar"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-rundeck/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.common](https://galaxy.ansible.com/robertdebock/common)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-common/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-common/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-common/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-common)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.java](https://galaxy.ansible.com/robertdebock/java)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-java/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-java/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-java/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-java)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-service)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-rundeck/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|8|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|all|
|[opensuse](https://hub.docker.com/repository/docker/robertdebock/opensuse/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-rundeck/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-rundeck/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
