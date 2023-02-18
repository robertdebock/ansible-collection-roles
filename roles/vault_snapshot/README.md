# [vault_snapshot](#vault_snapshot)

Configure vault_snapshot on Vault.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault_snapshot/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_snapshot/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vault_snapshot/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault_snapshot)|[![quality](https://img.shields.io/ansible/quality/)](https://galaxy.ansible.com/robertdebock/vault_snapshot)|[![downloads](https://img.shields.io/ansible/role/d/)](https://galaxy.ansible.com/robertdebock/vault_snapshot)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault_snapshot.svg)](https://github.com/robertdebock/ansible-role-vault_snapshot/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vault_snapshot/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  pre_tasks:
    - name: Read token from remote machine
      ansible.builtin.slurp:
        src: /root/.vault-token
      register: token_raw

  roles:
    - role: robertdebock.roles.vault_snapshot
      vault_snapshot_token: "{{ token_raw['content'] | b64decode }}"
      vault_snapshot_schedules:
        - name: hourly
          interval_seconds: 3600
          retain: 24
          path_prefix: /opt/vault/snapshots/
          storage_type: local
          local_max_space: 1073741824
        - name: hourly-aws
          interval_seconds: 3600
          retain: 24
          path_prefix: /hourly
          storage_type: aws-s3
          aws_s3_bucket: my-bucket
          aws_s3_region: eu-central-1
          aws_access_key_id: some_key
          aws_secret_access_key: some_secret
          aws_s3_enable_kms: false
        - name: hourly-azure
          interval_seconds: 3600
          retain: 24
          path_prefix: /hourly/
          storage_type: azure-blob
          azure_container_name: my-blob
          azure_account_name: some_account
          azure_account_key: some_key
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vault_snapshot/blob/master/molecule/default/prepare.yml):

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
      vault_type: ent
    - role: robertdebock.roles.vault_configuration
      vault_configuration_license: "{{ lookup('ansible.builtin.env', 'VAULT_LICENSE') }}"
      vault_configuration_listener_tcp:
        address: "127.0.0.1:8200"
        cluster_address: "127.0.0.1:8201"
        tls_disable: yes
      vault_configuration_storage_raft:
        path: "/opt/vault/data"
        node_id: "{{ ansible_hostname }}"

  tasks:
    - name: Flush handlers
      ansible.builtin.meta: flush_handlers

    - name: Initialize Vault
      ansible.builtin.command:
        cmd: vault operator init -format=yaml
      register: vault_init_raw
      environment:
        VAULT_ADDR: "http://localhost:8200"

    - name: Store vault_init_raw output as YAML
      ansible.builtin.set_fact:
        vault_init: "{{ vault_init_raw.stdout | from_yaml }}"

    - name: Store root_token
      ansible.builtin.copy:
        content: "{{ vault_init.root_token }}"
        dest: /root/.vault-token
        owner: root
        group: root
        mode: "0640"

    - name: Unseal Vault
      ansible.builtin.command:
        cmd: vault operator unseal {{ item }}
      loop: "{{ vault_init.unseal_keys_b64 }}"
      environment:
        VAULT_ADDR: "http://localhost:8200"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-vault_snapshot/blob/master/defaults/main.yml):

```yaml
---
# defaults file for vault_snapshot

# Set the vault instance address. Similar to `VAULT_ADDR`.
vault_snapshot_address: "http://localhost:8200"

# Set a token to connect to Vault. Similar to `VAULT_TOKEN`.
vault_snapshot_token: "simple"

# A list of snapshots to configure. Please have look in `molecule/default/converge.yml` for a complete example.
vault_snapshot_schedules: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault_snapshot/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.hashicorp](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp)|
|[robertdebock.vault](https://galaxy.ansible.com/robertdebock/vault)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-vault/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-vault/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault)|
|[robertdebock.vault_configuration](https://galaxy.ansible.com/robertdebock/vault_configuration)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-vault_configuration/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-vault_configuration/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault_configuration)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vault_snapshot/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/repository/docker/robertdebock/amazonlinux/general)|all|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|all|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|
|[Fedora](https://hub.docker.com/repository/docker/robertdebock/fedora/general)|36, 37|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault_snapshot/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vault_snapshot/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
