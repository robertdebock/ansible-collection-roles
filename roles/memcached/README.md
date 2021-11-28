# [memcached](#memcached)

Install and configure Memcached on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-memcached/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-memcached/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-memcached/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-memcached)|[![quality](https://img.shields.io/ansible/quality/30009)](https://galaxy.ansible.com/robertdebock/memcached)|[![downloads](https://img.shields.io/ansible/role/d/30009)](https://galaxy.ansible.com/robertdebock/memcached)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-memcached.svg)](https://github.com/robertdebock/ansible-role-memcached/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.memcached
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
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for memcached

# The tcp port memcached should listen on.
memcached_port: 11211

# The address memcached should bind on.
memcached_listenon: "127.0.0.1"

# The maximum connections memcached.
memcached_maxconn: 1024

# The cachesize.
memcached_cachesize: 64
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-memcached/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-memcached/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|debian|all|
|el|8|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| amazonlinux | /etc/init.d/memcached: line 26: /etc/sysconfig/network: No such file or directory |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-memcached/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
