# [Ansible role vault](#vault)

Install Hashicorp Vault, either a package or a binary.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vault/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/vault)](https://galaxy.ansible.com/robertdebock/vault)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault.svg)](https://github.com/robertdebock/ansible-role-vault/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vault/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.vault
      vault_hardening_disable_swap: false
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vault/blob/master/molecule/default/prepare.yml):

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
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-vault/blob/master/defaults/main.yml):

```yaml
---
# defaults file for vault

# Select the type of Vault to install. Either "oss", "ent" or "hsm".
# `oss` means Vault Open Source/community edition.
# `ent` means Vault Enterprise.
# `hsm` means Vault Enterprise with HSM support.
vault_type: oss

# Set the version of the package to install.
vault_version: "1.20.2"

# For package installations, a "release" is required. The package would for example be called `vault-1.12.2-1`.
vault_package_release: "1"

# Select the way to intall Vault. Either "package" or "binary".
vault_installation_method: "package"

# When `vault_installation_method` is set to "binary", set the path where to (temporarily) download Vault.
vault_download_path: "/tmp/vault-{{ vault_version }}"

# When `vault_installation_method` is set to "binary", set the (base) path where to install Vault. This can be "" or "/opt" for example.
vault_path: ""

# When `vault_installation_method` is set to "binary", set the user Vault will run under. The user "root" is not allowed.
vault_user: vault

# When `vault_installation_method` is set to "binary", set the group Vault will run under. The group "root" is not allowed.
vault_group: vault

# When `vault_installation_method` is set to "binary", set the shell for the vault_user.
vault_user_shell: /bin/false

# Where to store data. That's Raft data and TLS material.
vault_data_directory: /opt/vault

# Hardening advices to disable swap.
vault_hardening_disable_swap: true

# Hardening advices to disable core dumps.
vault_hardening_disable_core_dumps: true

# Hardening advices to disable shell command history.
vault_hardening_disable_shell_command_history: true

# Hardening advices to configure SELinux / AppArmor.
vault_hardening_configure_selinux_apparmor: true

# You can place variables that Vault listens to in this list.
# For example:
# vault_environment_settings:
#   - name: VAULT_API_ADDR
#     value: "http://127.0.0.1:8200"
#   - name: VAULT_CLUSTER_ADDR
#     value: "http://127.0.0.1:8201"
#   - name: HTTP_PROXY
#     value: "http://proxy.example.com:8080"
#   - name: HTTPS_PROXY
#     value: "https://proxy.example.com:8080"
#   - name: NO_PROXY
#     value: "*.example.com,1.2.3.4:80,1.2.3.4/8"
vault_environment_settings: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.hashicorp](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-hashicorp)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vault/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|41|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|noble, jammy|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vault/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
