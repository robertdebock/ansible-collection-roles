# [omsagent](#omsagent)

Install Microsoft omsagent (Log Analytics agent) on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-omsagent/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-omsagent/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-omsagent/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-omsagent)|[![quality](https://img.shields.io/ansible/quality/43607)](https://galaxy.ansible.com/robertdebock/omsagent)|[![downloads](https://img.shields.io/ansible/role/d/43607)](https://galaxy.ansible.com/robertdebock/omsagent)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-omsagent.svg)](https://github.com/robertdebock/ansible-role-omsagent/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.omsagent
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.users
      users_group_list:
        - name: omiusers
      users_user_list:
        - name: omsagent
          group: omiusers
    - role: robertdebock.auditd
      auditd_local_events: "no"
    - role: robertdebock.cron
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for omsagent

# Extra documentation on Log Analytic Agent is available on:
# https://docs.microsoft.com/en-us/azure/azure-monitor/platfrom/logs-analytics-agent

omsagent_version: 1.13.35-0

# omsagent_tmp directory is where the installer script is placed.
# The installer downloads a large file (125MB) to this directory.
omsagent_tmp: /tmp

# Set the user and group owning the directory.
omsagent_owner: omsagent
omsagent_group: omiusers

# Use as the OMS domain for onboarding.
# For azure monitoring log Analytics workspace in Goverment cloud use:
# omsagent_domain: opinsights.azure.command
# leave emapy to use scripts default (omsagent_domain: opinsights.azure.com).
omsagent_domain: ""

# Use [protocol://][user:password@]proxyhost[:port] as the proxy configuration.
# omsagent_proxy: "https://username:password@proxyserver:proxyport"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-omsagent/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.auditd](https://galaxy.ansible.com/robertdebock/auditd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-auditd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-auditd/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-auditd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-auditd)|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.cron](https://galaxy.ansible.com/robertdebock/cron)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-cron/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-cron/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-cron/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-cron)|
|[robertdebock.users](https://galaxy.ansible.com/robertdebock/users)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-users/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-users/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-users/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-users)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-omsagent/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|opensuse|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| alpine | Only RPM and DPKG is supported by Microsoft. |
| amazonlinux | Dependency not available: ansible-role-auditd |
| archlinux | Only RPM and DPKG is supported by Microsoft. |
| ubuntu | Python is not configured or Python does not support ctypes on this system, installation cannot continue. |
| debian | Python is not configured or Python does not support ctypes on this system, installation cannot continue. |

## [Included version(s)](#included-versions)

This role [refers to a version](https://github.com/robertdebock/ansible-role-omsagent/blob/master/defaults/main.yml) released by Microsoft. Check the released version(s) here:
- [OMS Agent for Linux GA](https://github.com/microsoft/OMS-Agent-for-Linux/releases).

This version reference means a role may get outdated. Monthly tests occur to see if [bit-rot](https://en.wikipedia.org/wiki/Software_rot) occured. If you however find a problem, please create an issue, I'll get on it as soon as possible.
If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-omsagent/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
