# [vault_configuration](#vault_configuration)

Configure HashiCorp Vault on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault_configuration/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vault_configuration/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault_configuration)|[![quality](https://img.shields.io/ansible/quality/61422)](https://galaxy.ansible.com/robertdebock/vault_configuration)|[![downloads](https://img.shields.io/ansible/role/d/61422)](https://galaxy.ansible.com/robertdebock/vault_configuration)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault_configuration.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.vault_configuration
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.hashicorp
    - role: robertdebock.roles.vault

- name: Create TLS material on localhost
  hosts: localhost
  become: no
  gather_facts: no

  tasks:
    - name: Install openssl
      ansible.builtin.package:
        name: openssl

    - name: Generate a private key for the CA
      ansible.builtin.command:
        cmd: openssl genpkey -algorithm RSA -out ca.key

    - name: Create the root CA certificate
      ansible.builtin.command:
        cmd: openssl req -new -x509 -key ca.key -out ca.crt -subj "/C=NL/ST=UTRECHT/L=Breukelen/O=Robert de Bock/CN=CA Robert de Bock/emailAddress=robert@meinit.nl"

    - name: Generate a private key for the server
      ansible.builtin.command:
        cmd: openssl genpkey -algorithm RSA -out vault.key

    - name: Create a certificate signing request (CSR) for the server
      ansible.builtin.command:
        cmd: openssl req -new -key vault.key -out vault.csr -subj "/C=NL/ST=UTRECHT/L=Breukelen/O=Robert de Bock/CN=vault.robertdebock.nl/emailAddress=robert@meinit.nl"

    - name: Sign the server certificate with the CA
      ansible.builtin.command:
        cmd: openssl x509 -req -in vault.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out vault.crt
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/defaults/main.yml):

```yaml
---
# defaults file for vault_configuration

# The owner and group owning files and directories managed by this role.
vault_configuration_owner: vault
vault_configuration_group: vault

# Set the license. Rquired when `vault_type` is `"ent"` or `"hsm"`.
# vault_configuration_license: "XYZABC"

# Environment variables can be saved to /etc/vault.d.vault.env. These are loaded when starting Vault.
# vault_configuration_environment:
#   - name: http_proxy
#     value: "http://proxy.example.com:3128"
#   - name: HTTP_PROXY
#     value: "http://proxy.example.com:3128"
#   - name: no_proxy
#     value: "direct.example.com,other.example.com"

#
# GLOBAL SETTINGS
#

# These are "global" settings.
# Values used below are taken from: https://developer.hashicorp.com/vault/docs/configuration
vault_configuration_max_lease_ttl: "768h"
vault_configuration_default_lease_ttl: "768h"
vault_configuration_api_addr: "https://{{ ansible_fqdn }}:8200"
vault_configuration_cluster_addr: "https://{{ ansible_fqdn }}:8201"
vault_configuration_disable_cache: no
vault_configuration_disable_mlock: yes
vault_configuration_disable_clustering: no
vault_configuration_plugin_directory: ""
vault_configuration_ui: no
vault_configuration_log_level: ""

#
# LISTENER SETTINGS
#

# These are settings for the listener. The only current valid listener is "tcp".
# Values used below are taken from https://developer.hashicorp.com/vault/docs/configuration/listener/tcp
vault_configuration_listener_tcp:
  address: "127.0.0.1:8200"
  cluster_address: "127.0.0.1:8201"
  http_idle_timeout: "5m"
  http_read_header_timeout: "10s"
  http_read_timeout: "30s"
  http_write_timeout: "0"
  max_request_size: 33554432
  max_request_duration: "90s"
  proxy_protocol_behavior: ""
  proxy_protocol_authorized_addrs: ""
  tls_disable: no
  tls_cert_file: "/opt/vault/tls/vault.crt"
  tls_key_file: "/opt/vault/tls/vault.key"
  tls_min_version: "tls12"
  tls_cipher_suites: ""
  tls_require_and_verify_client_cert: no
  tls_client_ca_file: ""
  tls_disable_client_certs: no
  x_forwarded_for_authorized_addrs: ""
  x_forwarded_for_hop_skips: 0
  x_forwarded_for_reject_not_authorized: yes
  x_forwarded_for_reject_not_present: yes
  telemetry:
    unauthenticated_metrics_access: no
  profiling:
    unauthenticated_pprof_access: no
    unauthenticated_in_flight_request_access: no

#
# STORAGE SETTINGS
#

# The "storage" stanza supports many types: https://developer.hashicorp.com/vault/docs/configuration/storage
# Select on of the "storage" options by uncommenting the one you need. You can only use one of the `vault_configuration_storage_*` maps.

# These are "raft" settings.
# Values used below are taken from: https://developer.hashicorp.com/vault/docs/configuration/storage/raft
vault_configuration_storage_raft:
  path: "/opt/vault/data"
  node_id: "{{ ansible_hostname }}"
  performance_multiplier: 0
  trailing_logs: 10000
  snapshot_threshold: 8192
  retry_join:
    - leader_api_addr: "https://127.0.0.1:8200"
      auto_join: ""
      auto_join_scheme: "https"
      auto_join_port: 8200
      leader_tls_servername: ""
      leader_ca_cert_file: "/opt/vault/tls/ca.crt"
      leader_client_cert_file: ""
      leader_client_key_file: ""
      leader_ca_cert: ""
      leader_client_cert: ""
      leader_client_key: ""
  retry_join_as_non_voter: no
  max_entry_size: 1048576
  autopilot_reconcile_interval: "10s"
  autopilot_update_interval: "2s"
  autopilot_upgrade_version: ""
  autopilot_redundancy_zone: ""

# The Consul storage backend uses a Consul cluster to store data.
# NOT IMPLEMENTED.
# vault_configuration_storage_consul:
#   address: "127.0.0.1:8500"
#   check_timeout: "5s"
#   consistency_mode: "default"
#   disable_registration: no
#   max_parallel: 128
#   path: "vault/"
#   scheme: "http"
#   service: "vault"
#   service_tags: []
#   service_address: ""
#   token: ""
#   session_ttl: "15s"
#   lock_wait_time: "15s"

# The "inmem" (Memory) storage stanza has no parameters. Use it by setting it to 'yes'.
# NOT IMPLEMENTED.
# vault_configuration_storage_inmem: yes

#
# (UN)SEAL SETTINGS
#

# You can configure Vault to automatically unseal. Each type has a unique set of parameters.
# You can only use one of the `vault_configuration_seal_*` maps.

# AliCloud KMS can be used to unseal Vault.
# NOT IMPLEMENTED.
# vault_configuration_seal_alicloudkm:
#   region:
#   domain:
#   access_key:
#   secret_key:
#   kms_key_id:
#   disabled: no

# AWS KMS can be used to unseal Vault.
# Values used below are taken from https://developer.hashicorp.com/vault/docs/configuration/seal/awskms
# vault_configuration_seal_awskms:
#   region: "us-east-1"
#   access_key: ""
#   session_token: ""
#   secret_key: ""
#   kms_key_id: ""
#   disabled: no
#   endpoint: ""

# Azure KeyVault can be used to unseal Vault.
# vault_configuration_seal_azurekeyvault:
#   tenant_id: "46646709-b63e-4747-be42-516edeaf1e14"
#   client_id: "03dc33fc-16d9-4b77-8152-3ec568f8af6e"
#   client_secret: "DUJDS3..."
#   environment: ""
#   vault_name: "hc-vault"
#   key_name: "vault_key"
#   resource: ""
#   disabled: no

# Goole GCP KMS can be used to unseal Vault.
# NOT IMPLEMENTED.
#  vault_configuration_seal_gcpckms:
#   credentials:
#   project:
#   region:
#   key_ring:
#   crypto_key:
#   disabled: no

# OCI KMS can be used to unseal Vault.
# NOT IMPLEMENTED.
# vault_configuration_seal_ocikms:
#   key_id:
#   crypto_endpoint:
#   management_endpoint:
#   auth_type_api_key:
#   disabled: no

# An HSM supporting PKCS11 can be used to unseal Vault.
# NOT IMPLEMENTED.
# vault_configuration_seal_pkcs11:
#   lib:
#   slot:
#   token_label:
#   pin:
#   key_label:
#   default_key_label:
#   key_id:
#   hmac_key_label:
#   default_hmac_key_label:
#   hmac_key_id:
#   mechanism:
#   hmac_mechanism:
#   generate_key:
#   force_rw_session:
#   disabled: no

# Another Vault (with the Transit secrets engine) can be used to unseal Vault.
# NOT IMPLEMENTED.
# vault_configuration_seal_transit:
#   address:
#   token:
#   key_name:
#   mount_path:
#   namespace:
#   disable_renewal:
#   tls_ca_cert:
#   tls_client_cert:
#   tls_client_key:
#   tls_server_name:
#   tls_skip_verify:
#   disabled: no
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.hashicorp](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp)|
|[robertdebock.vault](https://galaxy.ansible.com/robertdebock/vault)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-vault/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-vault/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vault_configuration/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|Candidate|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|36, 37|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault_configuration/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
