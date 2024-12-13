# [Ansible role grub](#grub)

Configure grub on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-grub/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-grub/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-grub/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-grub)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/grub)](https://galaxy.ansible.com/robertdebock/grub)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-grub.svg)](https://github.com/robertdebock/ansible-role-grub/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-grub/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.grub
      grub_options:
        - option: cgroup_enable
          value: memory
        - option: systemd.unified_cgroup_hierarchy
          value: 0
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-grub/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap

  tasks:
    - name: Make /etc/default
      ansible.builtin.file:
        path: /etc/default
        state: directory
        mode: "0755"

    - name: Place bogus /etc/default/grub
      ansible.builtin.copy:
        content: 'GRUB_CMDLINE_LINUX="a=1"'
        dest: /etc/default/grub
        mode: "0664"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-grub/blob/master/defaults/main.yml):

```yaml
---
# defaults file for grub

grub_timeout: 5

grub_recordfail_timeout: "{{ grub_timeout }}"

grub_set_password: false
grub_user: root
# grub_password = changeme
grub_password: grub.pbkdf2.sha512.10000.6CE338C69BC5180354034EEA28BB34BF6D50993A0AEAAE3F001F7CF8078BC3FBCB7968A4BE641AEB00D822FE55E0739ABF4D5F853AECA77958AC90A3DEC7132A.222738FE51C9A000ED1ECB77FA1A28C64AF1DE58D14F397DBF611343D7DC3443E38240663B8690F26F8F1A30BB58A88CCA9EDC4525F4DA0D93D8F2E7FB4623F0
grub_password_unrestricted: true
grub_password_unrestricted_files:
  - /etc/grub.d/10_linux
  - /etc/grub.d/20_linux_xen

# Add options here, for example:
# grub_options:
#   - option: cgroup_enable
#     value: memory
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-grub/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-grub/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-grub/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-grub/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
