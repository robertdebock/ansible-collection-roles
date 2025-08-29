# [Ansible role prosody](#prosody)

Install and configure prosody on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-prosody/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-prosody/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-prosody/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-prosody)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/prosody)](https://galaxy.ansible.com/robertdebock/prosody)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-prosody.svg)](https://github.com/robertdebock/ansible-role-prosody/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-prosody/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.prosody
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-prosody/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-prosody/blob/master/defaults/main.yml):

```yaml
---
# defaults file for prosody

# The domain to use for this XMPP server
prosody_domain: "{{ ansible_fqdn }}"

# External addresses for this server (optional)
# List of IP addresses that this server is reachable on from the internet
# Example: ["192.0.2.34", "2001:db8::abcd:1234"]
prosody_external_addresses: []

# The port to use for XMPP client connections
prosody_port: 5222

# The port to use for XMPP server-to-server connections
prosody_s2s_port: 5269

# The port to use for HTTP/HTTPS (for admin interface, BOSH, etc.)
prosody_http_port: 5280

# Enable HTTPS for the HTTP interface
prosody_https_enable: false

# The port to use for HTTPS
prosody_https_port: 5281

# SSL Certificate for HTTPS
prosody_ssl_cert: "{{ prosody_ssl_cert_directory }}/prosody.crt"

# SSL Key for HTTPS
prosody_ssl_key: "{{ prosody_ssl_key_directory }}/prosody.key"

# SSL Certificate and key directories (platform-specific paths are defined in vars/main.yml)

# SSL Certificate generation settings
prosody_ssl_common_name: "{{ prosody_domain }}"
prosody_ssl_organization: "Example Organization"
prosody_ssl_country: "US"
prosody_ssl_state: "Example State"
prosody_ssl_locality: "Example City"
prosody_ssl_email: "admin@{{ prosody_domain }}"
prosody_ssl_days: 365

# Enable server-to-server connections
prosody_s2s_enable: true

# Enable component connections
prosody_components_enable: false

# Enable admin interface
prosody_admin_enable: true

# Enable BOSH (Bidirectional-streams Over Synchronous HTTP)
prosody_bosh_enable: false

# Enable WebSocket support
prosody_websocket_enable: false

# Enable MUC (Multi-User Chat)
prosody_muc_enable: true

# Enable PubSub (Publish-Subscribe)
prosody_pubsub_enable: true

# Enable PEP (Personal Eventing Protocol)
prosody_pep_enable: true

# Enable offline message storage
prosody_offline_enable: true

# Enable user registration
prosody_registration_enable: false

# Enable anonymous authentication
prosody_anonymous_enable: false

# Enable SASL authentication
prosody_sasl_enable: true

# Enable TLS/SSL for client connections
prosody_tls_enable: true

# Enable TLS/SSL for server-to-server connections
prosody_s2s_tls_enable: true

# Enable compression
prosody_compression_enable: false

# Enable logging
prosody_logging_enable: true

# Log level (debug, info, warn, error)
prosody_log_level: info

# Enable daemon mode
prosody_daemon_enable: true

# User to run prosody as
prosody_user: prosody

# Group to run prosody as
prosody_group: prosody

# Prosody packages to install (platform-specific packages are defined in vars/main.yml)

# Data directory for prosody
prosody_data_directory: /var/lib/prosody

# Log directory for prosody
prosody_log_directory: /var/log/prosody

# Configuration directory for prosody
prosody_config_directory: /etc/prosody

# Additional modules to enable
prosody_additional_modules: []

# Custom configuration options (key-value pairs)
prosody_custom_config: {}

# Virtual hosts configuration
prosody_vhosts: []

# Component configurations
prosody_components: []

# MUC room configurations
prosody_muc_rooms: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-prosody/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-prosody/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-prosody/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-prosody/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
