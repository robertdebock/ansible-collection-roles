# [collabora_online](#collabora_online)

Install and configure Collabora Online CODE on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-collabora_online/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-collabora_online/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-collabora_online/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-collabora_online)|[![quality](https://img.shields.io/ansible/quality/55445)](https://galaxy.ansible.com/robertdebock/collabora_online)|[![downloads](https://img.shields.io/ansible/role/d/55445)](https://galaxy.ansible.com/robertdebock/collabora_online)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-collabora_online.svg)](https://github.com/robertdebock/ansible-role-collabora_online/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.collabora_online
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
    - role: robertdebock.ca_certificates
    - role: robertdebock.users
      users_group_list:
        - name: cool
      users_user_list:
        - name: cool
          group: cool
          home: /opt/cool
          shell: /usr/sbin/nologin
          system: yes
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for collabora_online

# You can set the type of installation; either "code" or "licensed".
collabora_online_type: code

# In case "LICENSED" is set for `collabora_online_type`, a version is required.
collabora_online_version: "6.4"

# When using `collabora_online_type: licensed` and running on RHEL systems, you
# need to set this variable. Get it from https://support.collaboraoffice.com/ .
# collabora_online_secret_key: "abc-def-ghi-jkl-mno"

# The languages allowed.
# collabora_online_allowed_languages: "de_DE en_GB en_US es_ES fr_FR it nl pt_BR pt_PT ru"

# Manage SSL capabilities, either "false" or "true". (As a string.)
collabora_online_ssl_enabled: "false"

# These settings become relevant when `collabora_online_ssl_enabled` is set to
# `yes`.
collabora_online_ssl_cert: /etc/coolwsd/coolwsd.crt
collabora_online_ssl_key: /etc/coolwsd/coolwsd.key
collabora_online_ssl_ca: /etc/coolwsd/coolwsd.keycrt
collabora_online_ciphers: "ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH"

# You can manage the mounting feature. Either "false" or "true". (As a string.)
collabora_online_mount_jail_tree: "true"

# Set the log level. Can be 0 through 8, none or "fatal", "critical", "error",
# "warning", "notice", "information", "debug", "trace".
collabora_online_log_level: warning

# Set the username for the admin console.
collabora_online_admin_username: "admin"

# Set the password for the admin console.
collabora_online_admin_password: "50m3-53cu23-p455w02d."

collabora_online_configuration_template: "coolwsd.xml.j2"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-collabora_online/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-ca_certificates)|
|[robertdebock.users](https://galaxy.ansible.com/robertdebock/users)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-users/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-users/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-users/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-users)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-collabora_online/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|7, 8|
|ubuntu|bionic, focal|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-collabora_online/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
