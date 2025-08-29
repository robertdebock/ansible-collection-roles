# [Ansible role openbao](#openbao)

Install and configure openbao on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-openbao/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openbao/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-openbao/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-openbao)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/openbao)](https://galaxy.ansible.com/robertdebock/openbao)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-openbao.svg)](https://github.com/robertdebock/ansible-role-openbao/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-openbao/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.openbao
      openbao_storage:
        type: raft
        path: /opt/openbao/data
        node_id: node1
        retry_join:
          - leader_api_addr: "http://127.0.0.2:8200"
      openbao_cluster_addr: "https://127.0.0.1:8201"
      openbao_api_addr: "https://127.0.0.1:8200"
      openbao_listeners:
        - name: tcp
          address: "127.0.0.1:8200"
          tls_disable: true
      openbao_telemetry:
        prometheus_retention_time: "30s"
        disable_hostname: true
      openbao_log_requests_level: "info"
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-openbao/blob/master/molecule/default/prepare.yml):

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

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-openbao/blob/master/defaults/main.yml):

```yaml
---
# defaults file for openbao

## Version of OpenBao to install. The role will automatically determine
## the appropriate package URL based on your operating system and architecture.
## Example: "1.0.0"
openbao_version: "2.3.2"

## Directory to store the downloaded package before installation.
openbao_download_dir: "/tmp"

## Whether to validate SSL certificates when downloading the GPG key.
## Set to false to handle older Ubuntu versions with outdated CA certificates.
openbao_validate_gpg_ssl: false

## Enable or disable the OpenBao web UI. When true, the UI will be
## accessible at the configured listener address.
openbao_ui: true

## Storage backend configuration for OpenBao.
## Supported types: file, inmem, raft, postgresql
## Example for file storage:
## openbao_storage:
##   type: file
##   path: /opt/openbao/data
##
## Example for in-memory storage:
## openbao_storage:
##   type: inmem
##
## Example for raft storage:
## openbao_storage:
##   type: raft
##   path: /opt/openbao/raft
##   node_id: node1
##   performance_multiplier: 1
##   trailing_logs: 10000
##   snapshot_threshold: 8192
##   snapshot_interval: 120
##   max_entry_size: 1048576
##   max_transaction_size: 8388608
##   autopilot_reconcile_interval: "10s"
##   autopilot_update_interval: "2s"
##   retry_join_as_non_voter: false
##   retry_join:
##     - leader_api_addr: "https://127.0.0.2:8200"
##       leader_ca_cert_file: "/path/to/ca1"
##       leader_client_cert_file: "/path/to/client/cert1"
##       leader_client_key_file: "/path/to/client/key1"
##     - auto_join: "provider=aws region=eu-west-1 tag_key=openbao tag_value=..."
## openbao_cluster_addr: "https://127.0.0.1:8201"
##
## Example for PostgreSQL storage:
## openbao_storage:
##   type: postgresql
##   connection_url: postgresql://user:pass@localhost:5432/openbao
openbao_storage:
  type: file
  path: /opt/openbao/data

## Listener configuration for OpenBao.
## Each listener can have different parameters based on its type.
## Example for HTTP listener:
## openbao_listeners:
##   - name: tcp
##     address: "127.0.0.1:8200"
##     tls_disable: true
##
## Example for HTTPS listener:
## openbao_listeners:
##   - name: tcp
##     address: "0.0.0.0:8200"
##     tls_cert_file: "/opt/openbao/tls/tls.crt"
##     tls_key_file: "/opt/openbao/tls/tls.key"
##
## Example for multiple listeners:
## openbao_listeners:
##   - name: tcp
##     address: "127.0.0.1:8200"
##     tls_disable: true
##   - name: tcp
##     address: "0.0.0.0:8200"
##     tls_cert_file: "/opt/openbao/tls/tls.crt"
##     tls_key_file: "/opt/openbao/tls/tls.key"
openbao_listeners:
  - name: tcp
    address: "0.0.0.0:8200"
    tls_cert_file: "/opt/openbao/tls/tls.crt"
    tls_key_file: "/opt/openbao/tls/tls.key"

## Cluster address for OpenBao. Required when using raft storage.
## This is the address that other nodes in the cluster will use to communicate.
openbao_cluster_addr: ""

## API address for OpenBao. This is the address that other nodes will use
## to communicate with this node's API. Required when using raft storage.
openbao_api_addr: ""

## Seal configuration for OpenBao.
## Currently OpenBao supports only one seal method, but this structure
## allows for future extensibility.
## Example for AWS KMS:
## openbao_seal:
##   - name: awskms
##     region: us-east-1
##     access_key: "XYZ"
##     secret_key: "ZYX"
##     kms_key_id: "1-2-3"
##
## Example for AliCloud KMS:
## openbao_seal:
##   - name: alicloudkms
##     region: cn-hangzhou
##     access_key: "XYZ"
##     secret_key: "ZYX"
##     key_id: "1-2-3"
##
## Example for Azure Key Vault:
## openbao_seal:
##   - name: azurekeyvault
##     tenant_id: "tenant-id"
##     client_id: "client-id"
##     client_secret: "client-secret"
##     vault_name: "vault-name"
##     key_name: "key-name"
##
## Example for GCP Cloud KMS:
## openbao_seal:
##   - name: gcpckms
##     credentials: "/path/to/credentials.json"
##     project: "project-id"
##     region: "global"
##     key_ring: "keyring"
##     crypto_key: "key"
##
## Example for KMIP:
## openbao_seal:
##   - name: kmip
##     server: "server:5696"
##     certificate: "/path/to/cert.pem"
##     key: "/path/to/key.pem"
##     ca_cert: "/path/to/ca.pem"
##
## Example for OCI KMS:
## openbao_seal:
##   - name: ocikms
##     auth_type: "user_principal"
##     key_id: "ocid1.key.region1.tenant1.xyz"
##     crypto_endpoint: "https://crypto.kms.us-ashburn-1.oraclecloud.com"
##
## Example for PKCS#11:
## openbao_seal:
##   - name: pkcs11
##     lib: "/usr/lib/libpkcs11.so"
##     slot: "0"
##     pin: "1234"
##     key_label: "label"
##

##
## Example for Transit:
## openbao_seal:
##   - name: transit
##     address: "http://127.0.0.1:8200"
##     token: "s.xyz123"
##     key_name: "autounseal"
##
## Example for no seal (Shamir's Secret Sharing):
## openbao_seal: []
openbao_seal: []

## Telemetry configuration for OpenBao.
## Example for Prometheus:
## openbao_telemetry:
##   prometheus_retention_time: "30s"
##   disable_hostname: true
##
## Example for StatsD:
## openbao_telemetry:
##   statsd_address: "statsd.company.local:8125"
##   metrics_prefix: "openbao"
##
## Example for DogStatsD:
## openbao_telemetry:
##   dogstatsd_addr: "localhost:8125"
##   dogstatsd_tags:
##     - "env:production"
##     - "service:openbao"
##
## Example for Stackdriver:
## openbao_telemetry:
##   stackdriver_project_id: "my-test-project"
##   stackdriver_location: "us-east1-a"
##   stackdriver_namespace: "openbao-cluster-a"
##   disable_hostname: true
##   enable_hostname_label: true
openbao_telemetry: {}

## Logging configuration for OpenBao.
## Example for debug level logging:
## openbao_log_requests_level: "debug"
##
## Example for info level logging:
## openbao_log_requests_level: "info"
##
## Example for disabling request logging:
## openbao_log_requests_level: "off"
##
## Valid levels: error, warn, info, debug, trace, off
openbao_log_requests_level: "off"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-openbao/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-openbao/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|jammy, noble|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-openbao/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-openbao/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
