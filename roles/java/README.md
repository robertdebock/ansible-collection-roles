# [java](#java)

Install and configure java on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-java/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-java/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-java/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-java)|[![quality](https://img.shields.io/ansible/quality/22732)](https://galaxy.ansible.com/robertdebock/java)|[![downloads](https://img.shields.io/ansible/role/d/22732)](https://galaxy.ansible.com/robertdebock/java)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-java.svg)](https://github.com/robertdebock/ansible-role-java/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.java
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Default
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
# defaults file for java

# Set the vendor of java, valid values are "openjdk" and "oracle".
java_vendor: openjdk

# Set the variable to install the type, valid values are "jre" and "jdk".
java_type: jre

# Set the version of java, valid values are "6", 7", "8", "9", "10", "11",
# "12" or "13".
# By default, a distibution default is used, mapped in `vars/main.yml`.
# By setting java_version, you overwrite this default to your selected
# version.
java_version: "{{ java_default_version }}"

# Set the format of the installation source, valid values are "targz" and
# "rpm". This is only valid with "java_vendor == oracle"
java_format: targz

# Where do the RPMs come from when installing Oracle RPMs?
# Either "local" or "repository".
# Valid for "java_vendor == oracle" and "java_format" == "rpm"
java_rpm_source: local

# Choose if you can JCE installed. Only applicable for (both):
# - java_vendor == "oracle"
# - java_version == "8"
java_jce: yes

# In case of "java_vendor == oracle" and "java_format == targz", a directory
# as to be set where to install.
java_install_directory: /opt
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-java/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-java/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|amazon|Candidate|
|el|8|
|debian|all|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


## [Included version(s)](#included-versions)

This role [refers to a version](https://github.com/robertdebock/ansible-role-java/blob/master/vars/main.yml) released by Oracle. Check the released version(s) here:
- [java](https://www.oracle.com/technetwork/java/javaseproducts/downloads/index.html).

This version reference means a role may get outdated. Monthly tests occur to see if [bit-rot](https://en.wikipedia.org/wiki/Software_rot) occured. If you however find a problem, please create an issue, I'll get on it as soon as possible.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-java/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
