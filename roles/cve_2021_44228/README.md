# [cve_2021_44228](#cve_2021_44228)

Check and report for cve_2021_44228 (log4shell) on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-cve_2021_44228/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cve_2021_44228/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-cve_2021_44228/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cve_2021_44228)|[![quality](https://img.shields.io/ansible/quality/57278)](https://galaxy.ansible.com/robertdebock/cve_2021_44228)|[![downloads](https://img.shields.io/ansible/role/d/57278)](https://galaxy.ansible.com/robertdebock/cve_2021_44228)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-cve_2021_44228.svg)](https://github.com/robertdebock/ansible-role-cve_2021_44228/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.cve_2021_44228
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

  # The role is prepared to install extra software and also remove when
  # the role is done. This is not idempotent, so in this playbook, the
  # required software is already installed.
  vars_files:
    - ../../vars/main.yml

  post_tasks:
    - name: install required software
      ansible.builtin.package:
        name: ["{{ cve_2021_44228_ps_package }}", unzip]
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for cve_2021_44228

# You can disable certain checks using these variables.

# Check suspicous processes.
cve_2021_44228_check_processes: yes

# Check suspicous packages.
cve_2021_44228_check_packages: yes

# This check uses `find`, which may use the disk intensively.
# Check suspicous files.
cve_2021_44228_check_files: yes

# This check uses `find`, which may use the disk intensively.
# Check suspicous jars
cve_2021_44228_check_archives: yes

# Add your own paths if you want to. The more paths you add, the more
# the disk will be used, but not having enough paths poses a risk of
# not finding vulnerable files.
# Paths to find files and jars in.
cve_2021_44228_paths_to_check:
  - /var
  - /etc
  - /usr
  - /opt
  - /lib64

# The types of archives to scan.
cve_2021_44228_archive_patterns:
  - "*.jar"
  - "*.war"
  - "*.ear"
  - "*.aar"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-cve_2021_44228/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-cve_2021_44228/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|all|
|debian|all|
|el|all|
|fedora|all|
|opensuse|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-cve_2021_44228/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
