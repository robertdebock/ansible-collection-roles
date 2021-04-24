# [snort](#snort)

THIS ROLE HAS BEEN ARCHIVED AND IS NOT MAINTAINED.

Install and configure snort on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-snort/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-snort/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-snort/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-snort)|[![quality](https://img.shields.io/ansible/quality/32397)](https://galaxy.ansible.com/robertdebock/snort)|[![downloads](https://img.shields.io/ansible/role/d/32397)](https://galaxy.ansible.com/robertdebock/snort)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-snort.svg)](https://github.com/robertdebock/ansible-role-snort/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.snort
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.epel
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for snort

snort_version: 2.9.17
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-snort/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-snort/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|fedora|32|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| Alpine | Could not allocate space to store a copy of the filter string |
| Archlinux | fatal error: rpc/rpc.h: No such file or directory |
| CentOS latest | ERROR! Libpcap library version >= 1.0.0 not found. |
| fedora:rawhide | ./sf_ip.h:231:31: warning: taking address of packed member of struct _sfaddr may result in an unaligned pointer value [-Waddress-of-packed-member] |

## [Included version(s)](#included-versions)

This role [refers to a version](https://github.com/robertdebock/ansible-role-snort/blob/master/vars/main.yml) released by Snort. Check the released version(s) here:
- [snort](https://www.snort.org/downloads).

This version reference means a role may get outdated. Monthly tests occur to see if [bit-rot](https://en.wikipedia.org/wiki/Software_rot) occured. If you however find a problem, please create an issue, I'll get on it as soon as possible.
If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-snort/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
