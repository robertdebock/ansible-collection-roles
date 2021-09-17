# [logwatch](#logwatch)

Install and configure logwatch on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-logwatch/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-logwatch/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-logwatch/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-logwatch)|[![quality](https://img.shields.io/ansible/quality/39152)](https://galaxy.ansible.com/robertdebock/logwatch)|[![downloads](https://img.shields.io/ansible/role/d/39152)](https://galaxy.ansible.com/robertdebock/logwatch)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-logwatch.svg)](https://github.com/robertdebock/ansible-role-logwatch/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.logwatch
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
      postfix_relayhost: "[relay.example.com]"
      postfix_myhostname: "smtp.example.com"
      postfix_mydomain: "example.com"
      postfix_myorigin: "example.com"
      postfix_aliases:
        - name: root
          destination: test@example.com
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for logwatch

logwatch_mailto: root
logwatch_mailfrom: Logwatch

# The time range for the report, either "all", "today" or "yesterday".
logwatch_range: yesterday

# The detail level for the report, either "Low", "Med" or "High" or a number
# ranging from 0 to 10.
logwatch_detail: Low

# A name of a defined service in "/usr/share/logwatch/scripts/services/" or
# "All".
logwatch_service: All
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-logwatch/blob/master/requirements.txt).

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
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-logwatch/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
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

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| Alpine | logwatch (missing) |
| EL | No package logwatch available. |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-logwatch/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
