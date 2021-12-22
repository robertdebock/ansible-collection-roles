# [gitlab](#gitlab)

Install and configure GitLab on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-gitlab/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-gitlab/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-gitlab/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-gitlab)|[![quality](https://img.shields.io/ansible/quality/)](https://galaxy.ansible.com/robertdebock/gitlab)|[![downloads](https://img.shields.io/ansible/role/d/)](https://galaxy.ansible.com/robertdebock/gitlab)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-gitlab.svg)](https://github.com/robertdebock/ansible-role-gitlab/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.gitlab
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
    - role: robertdebock.postfix
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for gitlab

# Specify a specific version for GitLab to install.
# Please have a look at this repository for available package version:
# community: https://packages.gitlab.com/gitlab/gitlab-ce
# enterprise: https://packages.gitlab.com/gitlab/gitlab-ee
# gitlab_version: 14.5.2
gitlab_version: 14.1.8

# A part of the version is the "release", mostly "0". See repositories above.
gitlab_release: 0

# The URL where the gitlab installation will be made available on.
# For "https", let's encrypt will be used.
gitlab_external_url: "http://localhost"

# Choose to install "enterprise" or "community".
gitlab_distribution: community
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-gitlab/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.postfix](https://galaxy.ansible.com/robertdebock/postfix)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-postfix/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-postfix/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-postfix/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-postfix)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-gitlab/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|7, 8|
|ubuntu|focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-gitlab/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
