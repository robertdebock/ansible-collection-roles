# [openssl](#openssl)

Make openssl certificates.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-openssl)|[![quality](https://img.shields.io/ansible/quality/48939)](https://galaxy.ansible.com/robertdebock/openssl)|[![downloads](https://img.shields.io/ansible/role/d/48939)](https://galaxy.ansible.com/robertdebock/openssl)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-openssl.svg)](https://github.com/robertdebock/ansible-role-openssl/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.openssl
      openssl_items:
        - name: my_openssl_key
          common_name: my.example.com
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
    - role: robertdebock.buildtools
    - role: robertdebock.epel
    - role: robertdebock.python_pip
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for openssl

# You can pass a list of ssl key/csr/crt/p12's to generate:
# openssl_items:
#   - name: my_openssl_key
#     common_name: my.example.com

# You can change the paths where to store each type of object (key, csr, crt,
# p12 and pkcs12). This is not required, by default the distributions regular
# location is set in `vars/main.yml`.

# This directory stores sensitive objects. (key, p12 and pkcs12)
openssl_key_directory: "{{ _openssl_key_directory[ansible_os_family] | default(_openssl_key_directory['default'] ) }}"

# This directory stores public, non-persistent objects. (csr)
openssl_csr_directory: "{{ _openssl_csr_directory[ansible_os_family] | default(_openssl_csr_directory['default'] ) }}"

# This directory stores public, persistent objects. (crt)
openssl_crt_directory: "{{ _openssl_crt_directory[ansible_os_family] | default(_openssl_crt_directory['default'] ) }}"

# You can change the owner and group of file created by this role.
openssl_file_owner: root
openssl_file_group: root
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-openssl/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-openssl/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|el|8|
|debian|all|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-openssl/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
