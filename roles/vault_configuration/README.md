# [Ansible role vault_configuration](#vault_configuration)

Configure HashiCorp Vault on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault_configuration/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vault_configuration/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault_configuration)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/vault_configuration)](https://galaxy.ansible.com/robertdebock/vault_configuration)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault_configuration.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.vault_configuration
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.hashicorp
    - role: robertdebock.roles.vault
      vault_hardening_disable_swap: false
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

# Set the license. Required when Vault enterprise is being used.
# The role `robertdebock.vault` can install Vault enterprise by setting:
# - `vault_type` to `"ent"` or `"hsm"`.
# vault_configuration_license: "XYZABC"

# Specify the location where TLS material should be placed. This is typically `/opt/vault/tls`.
vault_configuration_tls_directory: "/opt/vault/tls"

#
# GLOBAL SETTINGS
#

# These are "global" settings.
# Values used below are taken from: https://developer.hashicorp.com/vault/docs/configuration
vault_configuration_max_lease_ttl: "768h"
vault_configuration_default_lease_ttl: "768h"
vault_configuration_api_addr: "https://{{ ansible_fqdn }}:8200"
vault_configuration_cluster_addr: "https://{{ ansible_fqdn }}:8201"
vault_configuration_disable_cache: false
vault_configuration_disable_mlock: true
vault_configuration_disable_clustering: false
vault_configuration_plugin_directory: ""
vault_configuration_ui: false
vault_configuration_log_level: ""

#
# LISTENER SETTINGS
#

# These are "listener" settings, there can be multiple listeners.
vault_configuration_listeners:
  - type: "tcp"
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
    tls_disable: false
    # You can specify a file (`tls_cert_file`) OR the content of the file (`tls_cert`).
    # tls_cert_file: "/opt/vault/tls/vault.crt"
    tls_cert: |
      -----BEGIN CERTIFICATE-----
      MIIDlDCCAnwCCQDKshDt/N9YbTANBgkqhkiG9w0BAQsFADCBiTELMAkGA1UEBhMC
      TkwxEDAOBgNVBAgMB1VUUkVDSFQxEjAQBgNVBAcMCUJyZXVrZWxlbjEXMBUGA1UE
      CgwOUm9iZXJ0IGRlIEJvY2sxGjAYBgNVBAMMEUNBIFJvYmVydCBkZSBCb2NrMR8w
      HQYJKoZIhvcNAQkBFhByb2JlcnRAbWVpbml0Lm5sMB4XDTIzMDIxMzA4NTg1MloX
      DTIzMDMxNTA4NTg1MlowgY0xCzAJBgNVBAYTAk5MMRAwDgYDVQQIDAdVVFJFQ0hU
      MRIwEAYDVQQHDAlCcmV1a2VsZW4xFzAVBgNVBAoMDlJvYmVydCBkZSBCb2NrMR4w
      HAYDVQQDDBV2YXVsdC5yb2JlcnRkZWJvY2submwxHzAdBgkqhkiG9w0BCQEWEHJv
      YmVydEBtZWluaXQubmwwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDN
      LeDgfuElvJL+EPY6zaPx/lF8nblytGvxIy/8BBpsu9wyvI0Ty9XXxk7alwdTM+mE
      LYA1Nznnk0ekC9gaQTLRUGqTOJ92la0Z6M4/yVxe9gvN5yNsUjU01dXXiFzgx0e4
      usdnrqkZchi5Ib0SunHm1sE0O3uEYdW9mJrqWb25HLLmQwtrztr9bE5PBUH8CzlX
      fqM6+6e2e1pnmPmt533GtIJcwfBg+pUkc01EfhKzLjtILgAijfx+m+XjpKShGLUg
      QTL4V9fmXCmPBP0IYjw8I5k64aBLTQ/oj1sw4EzkaVKxTtluiAENDf2x9yPaoH3x
      PkPG36D5/4JK90THTihlAgMBAAEwDQYJKoZIhvcNAQELBQADggEBAAdPO8l+ww5p
      YJKZ3COyzz/RWHQ4R1fH3KQE53Jk4kjARoEcuh34YQJ3uWbiyrMMorHUrKStWrEO
      297pMizrA45bFm79gwoZ1yI/2WdejnC86JFdAbHRWLkEKs40Fy9JhEU0ouHLk7ya
      Gr9hGKWNVJmnNpk+xpmIY1hi5L4Opb8/hRe16MzhpVivyenyekEpu4S0muZXvUKt
      igLKDsMemBMADA1xS05IJ8PVfSpsGxhB9cga1DL94Bpq+p1ZSSbupQUNEIObi8BK
      vIciVdKVLy30rGn2JGKSEQ9fnULuZUWxjOv0awqKRpFE5WVnav2iwF4pzvRxFw7Y
      ba0Ft217IrI=
      -----END CERTIFICATE-----
    # You can specify a file (`tls_file_key`) OR the content of the file (`tls_key`).
    # tls_key_file: "/opt/vault/tls/vault.key"
    tls_key: |
      -----BEGIN PRIVATE KEY-----
      MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDNLeDgfuElvJL+
      EPY6zaPx/lF8nblytGvxIy/8BBpsu9wyvI0Ty9XXxk7alwdTM+mELYA1Nznnk0ek
      C9gaQTLRUGqTOJ92la0Z6M4/yVxe9gvN5yNsUjU01dXXiFzgx0e4usdnrqkZchi5
      Ib0SunHm1sE0O3uEYdW9mJrqWb25HLLmQwtrztr9bE5PBUH8CzlXfqM6+6e2e1pn
      mPmt533GtIJcwfBg+pUkc01EfhKzLjtILgAijfx+m+XjpKShGLUgQTL4V9fmXCmP
      BP0IYjw8I5k64aBLTQ/oj1sw4EzkaVKxTtluiAENDf2x9yPaoH3xPkPG36D5/4JK
      90THTihlAgMBAAECggEBAL0sxL8YHOyXPowkBXLYMYWob2dPYTHiKfft8osRGXAR
      kYfyEr0i3iqRPBkM0QMkxPRKo3/tSGU8hPw6s2gZnwogc/MDbPuAK1bNMITdWl5v
      yxhwOVfhQA9T7VNI9iGFe5pWFA6DmoPMkAD5m4NOBkDI1uAay9qV/eVOc98JGQU3
      Scc5H9gMvxe2J0njyUv+W4p5y8oMz0iVxqDvbQEduUuVZ7xKp1YysitfKViss2ej
      Ug3VcsPltuUrARfC/vO5PYJ2BXt9tHxPfu+nykGi42zAM6ex4xJyFiXnpZBOvjk1
      XIklhN9CoelxoECAxl7YgtweRwlbKf7belYd61HkmS0CgYEA9/zlX/BjIgmQjG7T
      odbb36pw9qW5M8ZVIIPQj5hndtPlGoESjcmHeogV1zAmsKvnQ6BuRUB4ZUh/nEpf
      HMPY1UaJ1L9jR8GjXh9mlVMAStYVwOxU2iILYditQ+BzLbr4ChNriI/Zo1/wIhxZ
      fk/cyutSF4z+RJ3C3+wPCk1n7H8CgYEA087pobuaiF5vSlnbjHIbb4zxPrxT1rW3
      k5KTC6RyMVW92yoOr6Gwgizzyq+qW4YSs3lePfN9oHxkkFJ9SU1/uV2ta64fnsxI
      HqbbgsMTKX1BbtkxNDYOCWvduJmC83LBYPVblPDvSr4G7zqxWyo3PQm9O/MrbtlW
      zrjGJrEYSRsCgYAINB2CZvlgjuBxRNlLaUgsxf6mqiTOSalXQgUMOwZxL+FMVyi9
      +AS7UPUoATfGcGleG1iKge95qkROb0dmNDRgGc1FdG9cWFOHMZK7Ldu8nghqMWc9
      MBMgUYKp1Cr7QEwkSTAtfFS+ytWuyzFKtGmhbNdyX/+pVW606aI1vQnLEQKBgQC0
      jXtHLR7sBGQmIzcuH88XZjP34J4vNzRIDfhfQk09lPOEsfNW8CQAs8UWEGzOHBow
      99LISJnchm1LQaYfKHsqTpqYYhP+T/Fif6Y7b4MUKPvwPCDfevy4N0UIKYQhdr81
      obHx4vh45EgRAh1Rs0jnNTgktINfuNFw4r23Gduz5QKBgD1qGo2Yjtk9blNV5v4Z
      oEKp5NQ+2Fbkpwl9k+nyA9CaSs98uf7C7Br7vrt/JBjAu447p/myeT9GiJSao6xj
      g8DTnnIvFuiLS9NKJMH4S2sd7P73j9djdV8J0qpxiEE6PMGjXrz455G6vowdKldu
      xWZvV9q5Ouxf7iRPf3o2cfKw
      -----END PRIVATE KEY-----
    tls_min_version: "tls12"
    tls_cipher_suites: ""
    tls_require_and_verify_client_cert: false
    tls_client_ca_file: ""
    tls_disable_client_certs: false
    x_forwarded_for_authorized_addrs: ""
    x_forwarded_for_hop_skips: 0
    x_forwarded_for_reject_not_authorized: true
    x_forwardesd_for_reject_not_present: true
    telemetry:
      unauthenticated_metrics_access: false
    profiling:
      unauthenticated_pprof_access: false
      unauthenticated_in_flight_request_access: false
  - type: "unix"
    address: "/run/vault/vault.sock"
    socket_mode: "666"
    socket_user: "vault"
    socket_group: "vault"

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
      # You can specify a file (`leader_ca_cert_file`) OR the content of the file (`leader_ca_cert`).
      # leader_ca_cert_file: "/opt/vault/tls/ca.crt"
      leader_ca_cert: |
        -----BEGIN CERTIFICATE-----
        MIIDkDCCAngCCQCDSFQRyRuDWDANBgkqhkiG9w0BAQsFADCBiTELMAkGA1UEBhMC
        TkwxEDAOBgNVBAgMB1VUUkVDSFQxEjAQBgNVBAcMCUJyZXVrZWxlbjEXMBUGA1UE
        CgwOUm9iZXJ0IGRlIEJvY2sxGjAYBgNVBAMMEUNBIFJvYmVydCBkZSBCb2NrMR8w
        HQYJKoZIhvcNAQkBFhByb2JlcnRAbWVpbml0Lm5sMB4XDTIzMDIxMzA4NTg1MVoX
        DTIzMDMxNTA4NTg1MVowgYkxCzAJBgNVBAYTAk5MMRAwDgYDVQQIDAdVVFJFQ0hU
        MRIwEAYDVQQHDAlCcmV1a2VsZW4xFzAVBgNVBAoMDlJvYmVydCBkZSBCb2NrMRow
        GAYDVQQDDBFDQSBSb2JlcnQgZGUgQm9jazEfMB0GCSqGSIb3DQEJARYQcm9iZXJ0
        QG1laW5pdC5ubDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALSXuMkY
        ROOcKbZBb63oWoDE26I3MNLsCvTY7vqMAZU0Mshe7rv+TfIw8RIYV8vXS9fBo11U
        ICG8q+q3vaDrFJR1Vfdk2GMrk/sTL+E4VzJirqLmaAAEzWAnQ+woGvYNXuGl9x3I
        /B0CJcrRQOJi0lL7NKKQmMXwhdw/m5eZDjekfp+JyHt7vuhKlLaOcY2d6An4Pmc6
        MxdQIFWy89HRU604uFFoExDNFZkEWr8a/bVGb8lRiG+AnxW0cuus1kgbl9/avW9d
        kDDi7hE7FO9apr0GfF0nva6C39zaiUxG/ZB0IPWaAOsEHXhRtMUUJM6J9FT3LhPS
        GGVV+bK5PEs/ekMCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEAYJ1D2h7nEQoXC8Ka
        w87hNP37oYDLgkXZoxNK+h5UBmYjMATGcZPbbeGsppdi3qRb3pEqNwCWlzETSJqG
        0HzUSEeRjLp2mxLZuMHSlq+wRj2vtsN/IV5Gz/hs23LSxVXMEF7DLRSWY++sOPC9
        /2bN3eJGhjMoDP4Pgr/h/7Kk2dqOrxR4Etgli7nxIKiUNpCAwhv+yodGz3qDBSj1
        KWn9KbjlX/IIRakY9Gh7X+UDUWFJU30vU0so5hKKtrq0ZQoDCPhfYV9T0SLd5N3y
        JHufLAJw5yK8WMpBOhqmnoGco48nnsRJ55qK8xeTiVGgsewhjyeHNMUP7RDDptua
        mo3kZQ==
        -----END CERTIFICATE-----
      leader_client_cert_file: ""
      leader_client_key_file: ""
      leader_client_cert: ""
      leader_client_key: ""
  retry_join_as_non_voter: false
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
#   disable_registration: false
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
# vault_configuration_storage_inmem: true

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
#   disabled: false

# AWS KMS can be used to unseal Vault.
# Values used below are taken from https://developer.hashicorp.com/vault/docs/configuration/seal/awskms
# vault_configuration_seal_awskms:
#   region: "us-east-1"
#   access_key: ""
#   session_token: ""
#   secret_key: ""
#   kms_key_id: ""
#   disabled: false
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
#   disabled: false

# Goole GCP KMS can be used to unseal Vault.
# NOT IMPLEMENTED.
#  vault_configuration_seal_gcpckms:
#   credentials:
#   project:
#   region:
#   key_ring:
#   crypto_key:
#   disabled: false

# OCI KMS can be used to unseal Vault.
# vault_configuration_seal_ocikms:
#   key_id: "ocid1.key.oc1.iad.afnxza26aag4s.abzwkljsbapzb2nrha5nt3s7s7p42ctcrcj72vn3kq5qx"
#   crypto_endpoint: "https://afnxza26aag4s-crypto.kms.us-ashburn-1.oraclecloud.com"
#   management_endpoint:  "https://afnxza26aag4s-management.kms.us-ashburn-1.oraclecloud.com"
#   auth_type_api_key: false
#   disabled: false

# An HSM supporting PKCS11 can be used to unseal Vault.
# vault_configuration_seal_pkcs11:
#   lib: "/usr/vault/lib/libCryptoki2_64.so"
#   slot: "2305843009213693953"
#   # token_label: ""
#   pin: "AAAA-BBBB-CCCC-DDDD"
#   key_label: "vault-hsm-key"
#   # default_key_label: ""
#   # key_id: ""
#   hmac_key_label: "vault-hsm-hmac-key"
#   # default_hmac_key_label: ""
#   # hmac_key_id: ""
#   # mechanism: ""
#   # hmac_mechanism: ""
#   # generate_key: ""
#   # force_rw_session: ""
#   disabled: false

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
#   disabled: false
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

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
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|38, 39|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault_configuration/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
