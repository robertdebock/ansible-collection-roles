# [Ansible role openssh](#openssh)

Install and configure openssh on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-openssh/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssh/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-openssh/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-openssh)|[![downloads](https://img.shields.io/ansible/role/d/24557)](https://galaxy.ansible.com/robertdebock/openssh)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-openssh.svg)](https://github.com/robertdebock/ansible-role-openssh/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-openssh/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.openssh
      openssh_allow_users:
        - root
      openssh_allow_groups:
        - root
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-openssh/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.selinux
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-openssh/blob/master/defaults/main.yml):

```yaml
---
# defaults file for openssh

# The tcp port ssh should listen on.
openssh_port: 22

openssh_address_family: any

openssh_listen_addresses:
  - "0.0.0.0"
  - "::"

openssh_host_keys:
  - /etc/ssh/ssh_host_rsa_key
  - /etc/ssh/ssh_host_ecdsa_key
  - /etc/ssh/ssh_host_ed25519_key

openssh_rekey_limit: default none

openssh_syslog_facility: AUTH

openssh_loglevel: INFO

openssh_login_grace_time: 2m
openssh_permit_root_login: "yes"
openssh_strict_modes: "yes"
openssh_max_auth_tries: 6
openssh_max_sessions: 10

openssh_pub_key_authentication: "yes"

openssh_authorized_key_file: ".ssh/authorized_keys"

openssh_authorized_prinicpals_file: none
openssh_authorized_keys_command: none
openssh_authorized_keys_command_user: nobody

openssh_host_based_authentication: "no"
openssh_ignore_user_known_hosts: "no"
openssh_ignore_rhosts: "yes"

openssh_permit_empty_passwords: "no"
openssh_password_authentication: "yes"

openssh_challenge_response_authentication: "no"

openssh_gssapi_authentication: "yes"
openssh_gssapi_cleanup_credentials: "no"
openssh_gssapi_strict_acceptor_check: "yes"
openssh_gssapi_key_exchange: "no"
openssh_gssaip_enable_k5_users: "no"

openssh_use_pam: "yes"

openssh_allow_agent_forwarding: "yes"
openssh_allow_tcp_forwarding: "yes"
openssh_gateway_ports: "no"
openssh_x11_forwarding: "yes"
openssh_x11_display_offset: 10
openssh_x11_use_localhost: "yes"
openssh_permit_tty: "yes"

openssh_print_motd: "no"

openssh_print_last_log: "yes"
openssh_tcp_keep_alive: "yes"
openssh_permit_user_environment: "no"
openssh_compression: delayed
openssh_client_alive_interval: 30
openssh_client_alive_count_max: 3
openssh_show_patch_level: "no"
openssh_use_dns: "no"
openssh_pid_file: /var/run/sshd.pid
openssh_max_startups: "10:30:100"
openssh_permit_tunnel: "no"
openssh_chroot_directory: none
openssh_version_addendum: none

openssh_banner: none

openssh_accept_envs:
  - LANG
  - LANGUAGE
  - LC_ADDRESS
  - LC_ALL
  - LC_COLLATE
  - LC_CTYPE
  - LC_IDENTIFICATION
  - LC_MEASUREMENT
  - LC_MESSAGES
  - LC_MONETARY
  - LC_NAME
  - LC_NUMERIC
  - LC_PAPER
  - LC_TELEPHONE
  - LC_TIME
  - XMODIFIERS

openssh_subsystem: sftp {{ openssh_sftp_server }}

# Specifies a file containing public keys of certificate authorities that are
# trusted to sign user certificates for authentication, or none to not use one.
openssh_trusted_user_ca_keys: none

# Restrict access to this (space separated list) of users or groups.
# For example: "openssh_allow_users: root my_user"
# openssh_allow_users:
#  - root

# openssh_allow_groups:
#  - wheel
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-openssh/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-selinux)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-openssh/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
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

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-openssh/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-openssh/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
