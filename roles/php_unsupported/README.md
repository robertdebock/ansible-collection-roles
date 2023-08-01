# [php_unsupported](#php_unsupported)

Install an unsupported version of php on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-php_unsupported/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-php_unsupported/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-php_unsupported/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-php_unsupported)|[![quality](https://img.shields.io/ansible/quality/)](https://galaxy.ansible.com/robertdebock/php_unsupported)|[![downloads](https://img.shields.io/ansible/role/d/)](https://galaxy.ansible.com/robertdebock/php_unsupported)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-php_unsupported.svg)](https://github.com/robertdebock/ansible-role-php_unsupported/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-php_unsupported/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.php_unsupported
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-php_unsupported/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-php_unsupported/blob/master/defaults/main.yml):

```yaml
---
# defaults file for php_unsupported

# The version of PHP to install. (string)
# Either 5.6, 7.0, 7.1, 7.2, 7.3, 7.4, 8.0, 8.1 or 8.2
php_version: "5.6"

# The extra packages to install. (list)
php_packages:
  - php{{ php_version }}-cli
  - php{{ php_version }}-common
  - php{{ php_version }}-curl
  - php{{ php_version }}-dev
  - php{{ php_version }}-gd
  - php{{ php_version }}-intl
  - php{{ php_version }}-json
  - php{{ php_version }}-mbstring
  - php{{ php_version }}-mcrypt
  - php{{ php_version }}-mysql
  - php{{ php_version }}-opcache
  - php{{ php_version }}-readline
  - php{{ php_version }}-soap
  - php{{ php_version }}-xml
  - php{{ php_version }}-xmlrpc
  - php{{ php_version }}-zip
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-php_unsupported/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-php_unsupported/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-php_unsupported/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-php_unsupported/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
