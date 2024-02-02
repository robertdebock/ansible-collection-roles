# [Ansible role eclipse](#eclipse)

Install eclipse and plugins on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-eclipse/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-eclipse/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-eclipse/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-eclipse)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/eclipse)](https://galaxy.ansible.com/robertdebock/eclipse)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-eclipse.svg)](https://github.com/robertdebock/ansible-role-eclipse/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-eclipse/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.eclipse
    # - role: robertdebock.roles.eclipse
    #   eclipse_release: 2022-09
    #   eclipse_install_path: /opt/eclipse-{{ eclipse_release }}
    #   eclipse_link_paths:
    #     - /opt/eclipse-09
    #     - /opt/eclipse-202209
    # - role: robertdebock.roles.eclipse
    #   eclipse_release: 2022-12
    #   eclipse_install_path: /opt/eclipse-{{ eclipse_release }}
    #   eclipse_link_paths: []
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-eclipse/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.java
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-eclipse/blob/master/defaults/main.yml):

```yaml
---
# defaults file for eclipse

# The release to install.
# See https://www.eclipse.org/downloads/packages/release
eclipse_release: 2023-06

# The release version to install, either: R, RC1, M3, M2 or M1.
eclipse_release_version: R

# The type of installation, either: jee, committers, cpp, dsl, java, javascript, jee, modeling, parallel, php, rcp, rust, scout or testing.
eclipse_release_type: java

# Where to download eclipse to. The installation will later be moved to a versioned path.
eclipse_tmp_path: /tmp

# The path where to install eclipse.
eclipse_install_path: /opt/eclipse-{{ eclipse_release }}

# The mirror to use for downloading eclipse.
# The mirrors keep the 3 last versions.
# eclipse_archive_mirror: "https://ftp.fau.de/eclipse/technology/epp/downloads/release"
# eclipse_archive_mirror: "https://download.eclipse.org/technology/epp/downloads/release"
eclipse_archive_mirror: "http://ftp.snt.utwente.nl/pub/software/eclipse/technology/epp/downloads/release"

# What path(s) would you like to link to the eclipse installation?
eclipse_link_paths:
  - /opt/eclipse

eclipse_plugins: []
# This plugin causes an issue:
# org.eclipse.m2e.logback.configuration:
# The org.eclipse.m2e.logback.configuration bundle was activated before
# the state location was initialized.  Will retry after the state location
# is initialized.
# - name: org.tigris.subversion.subclipse.feature.group
#   repository: "http://subclipse.tigris.org/update_1.10.x"
# - name: org.sonatype.m2e.egit.feature.feature.group
#   repository: "https://repo1.maven.org/maven2/.m2e/connectors/m2eclipse-egit/0.15.1/N/0.15.1.201806191431"

# You can have this role install Lombok into Eclipse.
eclipse_install_lombok: yes
# Also specify the version of lombok.
eclipse_lombok_version: "1.18.22"

# You may install Maven.
eclipse_install_maven: yes
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-eclipse/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.java](https://galaxy.ansible.com/robertdebock/java)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-java/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-java/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-java/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-java)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-eclipse/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora/)|all|
|[opensuse](https://hub.docker.com/r/robertdebock/opensuse)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-eclipse/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-eclipse/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
