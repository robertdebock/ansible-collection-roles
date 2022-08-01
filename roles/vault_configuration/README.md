# [vault_configuration](#vault_configuration)

Configure HashiCorp Vault.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault_configuration/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-vault_configuration/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-vault_configuration)|[![quality](https://img.shields.io/ansible/quality/)](https://galaxy.ansible.com/robertdebock/vault_configuration)|[![downloads](https://img.shields.io/ansible/role/d/)](https://galaxy.ansible.com/robertdebock/vault_configuration)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault_configuration.svg)](https://github.com/robertdebock/ansible-role-vault_configuration/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: no

  pre_tasks:
    - name: read the vault token
      ansible.builtin.slurp:
        src: /root/.vault-token
      register: vault_configuration_token_raw

    - name: set vault_configuration_token
      ansible.builtin.set_fact:
        vault_configuration_token: "{{ vault_configuration_token_raw.content | b64decode }}"

  roles:
    - role: robertdebock.vault_configuration
      vault_configuration_secret_engines:
        - path: kv1
          type: kv
          description: My key-value 1 secret engine.
          options:
            version: 1
          max_versions: 8
          cas_required: yes
          delete_version_after: 1m
        - path: kv2
          type: kv
          description: My key-value 2 secret engine.
          delete_version_after: 0s
        - path: pki
          type: pki
          description: My pki secret engine.
          config:
            common_name: example.com
            default_lease_ttl: 8760h  # 1 year
      vault_configuration_auth_engines:
        - path: users
          type: userpass
          description: My userpass auth engine.
          config:
            default_lease_ttl: 28800  # 1 working day
            max_lease_ttl: 864000  # 1 day
        - path: kubernetes
          type: kubernetes
          description: My kubernetes auth engine.
        - path: approle
          type: approle
          description: My approle auth engine.
        - path: ldap
          type: ldap
          description: My ldap auth engine.
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
    - role: robertdebock.hashicorp
    - role: robertdebock.vault
      vault_store_root_token: yes
      vault_max_lease_ttl: "87600h"  # 10 years.
      vault_default_lease_ttl: "24h"  # 1 day.
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for vault_configuration

# The url to HashiCorp Vault.
vault_configuration_url: "http://localhost:8200"

# The token to authenticate to HashiCorp Vault.
# vault_configuration_token: "s.xyz"

# The namespace in HashiCorp Vault to use. Only fill this in when you have an Enterprise installation of HashiCorp Vault.
# vault_configuration_namespace: "my_namespace"

# A list of secrets engines to configure.
# vault_configuration_secret_engines:
#   - type: kv
#     description: My key-value secret engine.
#     options:
#       version: 2

# TODO: Finish vault_configuration_auth_methods.
# vault_configuration_auth_methods:
#   - name: aws
#     auth_type: ec2
#     acccess_key: xyz
#     secret_key: abc

# TODO: Finish vault_configuration_acls.
# vault_configuration_acls:
#   - path: kv
#     capabilities:
#       - create
#       - update
#       - read
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault_configuration/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.hashicorp](https://galaxy.ansible.com/robertdebock/hashicorp)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hashicorp/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hashicorp/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-hashicorp/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-hashicorp)|
|[robertdebock.vault](https://galaxy.ansible.com/robertdebock/vault)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-vault/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-vault/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-vault)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vault_configuration/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|debian|all|
|el|all|
|fedora|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault_configuration/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
