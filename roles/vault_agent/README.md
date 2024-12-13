# [Ansible role vault_agent](#vault_agent)

Install and configure HashiCorp Vault Agent on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault_agent/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_agent/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vault_agent/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault_agent)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/vault_agent)](https://galaxy.ansible.com/robertdebock/vault_agent)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault_agent.svg)](https://github.com/robertdebock/ansible-role-vault_agent/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vault_agent/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.vault_agent
      vault_agent_address: "http://vault.example.com:8200"
      vault_agent_auto_auth:
        methods:
          - name: "approle"
            config:
              role_id_file_path: "/etc/vault-agent/role_id"
              secret_id_file_path: "/etc/vault-agent/secret_id"
        #   - name: "aws"
        #     mount_path: "auth/aws-subaccount"
        #     config:
        #       type: "iam"
        #       role: "foobar"
        sinks:
          - name: file
            config:
              path: "/tmp/file-foo"
          - name: "file"
            wrap_ttl: "5m"
            aad_env_var: "Test_AAD_ENV"
            dh_type: "curve25519"
            dh_path: "/tmp/file-foo-dhpath2"
            config:
              path: "/tmp/file-bar"
      vault_agent_listeners:
        # - name: "unix"
        #   address: "/path/to/socket"
        #   tls_disable: true
        #   agent_api:
        #     enable_quit: true
        - name: "tcp"
          address: "127.0.0.1:8100"
          tls_disable: true
      # vault_agent_templates:
      #   - source: "/etc/vault-agent/server.key.ctmpl"
      #     destination: "/tmp/server.key"
      #   - source: "/etc/vault-agent/server.crt.ctmpl"
      #     destination: "/tmp/server.crt"
      vault_agent_env_templates:
        - name: "USERNAME"
          contents: "{{ '{{ with secret \\\"secret/data/foo\\\" }}{{ .Data.data.password }}{{ end }}' }}"
          error_on_missing_key: true
        - name: "PASSWORD"
          contents: "{{ '{{ with secret \\\"secret/data/foo\\\" }}{{ .Data.data.user }}{{ end }}' }}"
          error_on_missing_key: true
      vault_agent_exec:
        command: ["/path/to/my-app", "arg1", "arg2"]
        restart_on_secret_changes: "always"
        restart_stop_signal: "SIGTERM"
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vault_agent/blob/master/molecule/default/prepare.yml):

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

  tasks:
    - name: Create /etc/vault-agent directory
      ansible.builtin.file:
        path: /etc/vault-agent
        state: directory
        owner: root
        group: root
        mode: 0755

    - name: Place fake approle id and secret
      ansible.builtin.copy:
        content: "FAKE"
        dest: "{{ item }}"
        owner: root
        group: root
        mode: 0644
      loop:
        - /etc/vault-agent/role_id
        - /etc/vault-agent/secret_id

    - name: Pleace Vault agent templates
      ansible.builtin.copy:
        content: "FAKE"
        dest: "{{ item }}"
        owner: root
        group: root
        mode: 0644
      loop:
        - /etc/vault-agent/server.key.ctmpl
        - /etc/vault-agent/server.crt.ctmpl
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-vault_agent/blob/master/defaults/main.yml):

```yaml
---
# defaults file for vault_agent

# The user that owns the Vault configuration files.
vault_agent_user: "vault"

# The group that owns the Vault configuration files.
vault_agent_group: "vault"

# The PID file for the Vault agent.
# vault_agent_pid_file: "./pidfile"

# The Vault address where the agent can connect to.
# vault_agent_address: "http://vault.example.com:8200"

# The number of times to retry connecting to Vault.
vault_agent_retries: 5

# The authentication method to use.
# vault_agent_auto_auth:
#   methods:
#     - name: "aws"
#       mount_path: "auth/aws-subaccount"
#       config:
#         type: "iam"
#         role: "foobar"
#   sinks:
#     - name: file
#       config:
#         path: "/tmp/file-foo"
#     - name: "file"
#       wrap_ttl: "5m"
#       aad_env_var: "Test_AAD_ENV"
#       dh_type: "curve25519"
#       dh_path: "/tmp/file-foo-dhpath2"
#       config:
#         path: "/tmp/file-bar"

# By specifying (an empty cache configuration), the agent will store the token in the cache.
vault_agent_cache: {}

# Should this Vault offer proxy capabilties?
# vault_agent_api_proxy:
#   use_auto_auth_token: true

# A list of listeners to configure.
# vault_agent_listeners:
#   - name: "tcp"
#     address: "/path/to/socket"
#     tls_disable: true
#     agent_api:
#       enable_quit: true
#   - name: "tcp"
#     address: "127.0.0.1:8100"
#     tls_disable: true

# A list of templates to render. The files mentioned in the source will not be placed by this role.
# vault_agent_templates:
#   - source: "/etc/vault/server.key.ctmpl"
#     destination: "/etc/vault/server.key"
#   - source: "/etc/vault/server.crt.ctmpl"
#     destination: "/etc/vault/server.crt"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault_agent/blob/master/requirements.txt).

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
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vault_agent/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|39, 40|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault_agent/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vault_agent/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
