# [jenkins](#jenkins)

Install and configure jenkins on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-jenkins/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-jenkins/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-jenkins/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-jenkins)|[![quality](https://img.shields.io/ansible/quality/29474)](https://galaxy.ansible.com/robertdebock/jenkins)|[![downloads](https://img.shields.io/ansible/role/d/29474)](https://galaxy.ansible.com/robertdebock/jenkins)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-jenkins.svg)](https://github.com/robertdebock/ansible-role-jenkins/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-jenkins/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.jenkins
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-jenkins/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.epel
    - role: robertdebock.roles.java
      java_default_version: 11
    - role: robertdebock.roles.locale
    - role: robertdebock.roles.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-jenkins/blob/master/defaults/main.yml):

```yaml
---
# defaults file for jenkins

# What tcp port Jenkins should listen to.
jenkins_port: 8080

# What address Jenkins should bind to.
jenkins_listen_address: "0.0.0.0"

# The version of Jenkins to install. Not specifying a version, will install the latest available.
# jenkins_version: "2.399.1"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-jenkins/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.java](https://galaxy.ansible.com/robertdebock/java)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-java/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-java/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-java/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-java)|
|[robertdebock.locale](https://galaxy.ansible.com/robertdebock/locale)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-locale/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-locale/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-locale/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-locale)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-jenkins/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|bullseye|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-jenkins/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-jenkins/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
