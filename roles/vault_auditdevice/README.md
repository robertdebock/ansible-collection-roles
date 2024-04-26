# [Ansible role vault_auditdevice](#vault_auditdevice)

Install and configure vault_auditdevice on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vault_auditdevice/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vault_auditdevice/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vault_auditdevice/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vault_auditdevice)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/vault_auditdevice)](https://galaxy.ansible.com/robertdebock/vault_auditdevice)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vault_auditdevice.svg)](https://github.com/robertdebock/ansible-role-vault_auditdevice/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vault_auditdevice/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: false

  pre_tasks:
    - name: Read /root/.vault-token
      ansible.builtin.slurp:
        src: /root/.vault-token
      register: vault_auditdevice_token_slurped

  roles:
    - role: robertdebock.roles.vault_auditdevice
      vault_auditdevice_ssl_verify: false
      vault_auditdevice_token: "{{ vault_auditdevice_token_slurped['content'] | b64decode }}"
      vault_auditdevice_list:
        - name: local_file/  # Make sure the value is trailed by a `/`.
          type: file
          description: File Audit Device
          options:
            file_path: /opt/vault/vault_audit.log
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vault_auditdevice/blob/master/molecule/default/prepare.yml):

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


  tasks:
    - name: Flush handlers
      ansible.builtin.meta: flush_handlers

    - name: Initialize vault
      ansible.builtin.command:
        cmd: vault operator init -format=yaml
      register: vault_auditdevice_init
      changed_when: true
      environment:
        VAULT_SKIP_VERIFY: true
      notify:
        - Unseal vault

    - name: Format vault_auditdevice_init_yaml
      ansible.builtin.set_fact:
        vault_auditdevice_init_yaml: "{{ vault_auditdevice_init.stdout | from_yaml }}"
      when:
        - vault_auditdevice_init is defined

    - name: Store vault token
      ansible.builtin.copy:
        content: "{{ vault_auditdevice_init_yaml['root_token'] }}"
        dest: /root/.vault-token
        owner: root
        group: root
        mode: 0600
      when:
        - vault_auditdevice_init is defined

  handlers:
    - name: Unseal vault
      ansible.builtin.command:
        cmd: vault operator unseal "{{ item }}"
      changed_when: true
      loop: "{{ vault_auditdevice_init_yaml['unseal_keys_b64'] }}"
      environment:
        VAULT_SKIP_VERIFY: true
      when:
        - vault_auditdevice_init is defined
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-vault_auditdevice/blob/master/defaults/main.yml):

```yaml
---
# defaults file for vault_auditdevice

# Set the vault instance address. Similar to `VAULT_ADDR`.
vault_auditdevice_address: "https://localhost:8200"

# Set a token to connect to Vault. Similar to `VAULT_TOKEN`.
vault_auditdevice_token: "simple"

# A list of audit devices to configure. Please have look in `molecule/default/converge.yml` for a complete example.
vault_auditdevice_list: []

# Should SSL certificate verification be disabled?
vault_auditdevice_ssl_verify: true
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vault_auditdevice/blob/master/requirements.txt).

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
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vault_auditdevice/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|bullseye|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|8, 9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|39|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vault_auditdevice/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vault_auditdevice/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
