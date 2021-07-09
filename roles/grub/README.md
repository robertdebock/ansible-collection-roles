# [grub](#grub)

Configure grub on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-grub/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-grub/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-grub/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-grub)|[![quality](https://img.shields.io/ansible/quality/48762)](https://galaxy.ansible.com/robertdebock/grub)|[![downloads](https://img.shields.io/ansible/role/d/48762)](https://galaxy.ansible.com/robertdebock/grub)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-grub.svg)](https://github.com/robertdebock/ansible-role-grub/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.grub
      grub_options:
        - option: cgroup_enable
          value: memory
        - option: systemd.unified_cgroup_hierarchy
          value: 0
```

The machine needs to be prepared in CI this is done using `molecule/resources/prepare.yml`:
```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap

  tasks:
    - name: make /etc/default
      ansible.builtin.file:
        path: /etc/default
        state: directory
        mode: "0755"
    - name: place bogus /etc/default/grub
      ansible.builtin.copy:
        content: 'GRUB_CMDLINE_LINUX="a=1"'
        dest: /etc/default/grub
        mode: "0664"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for grub

grub_timeout: 5

grub_recordfail_timeout: "{{ grub_timeout }}"

# Add options here, for example:
# grub_options:
#   - option: cgroup_enable
#     value: memory
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-grub/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-grub/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|alpine|all|
|el|8|
|debian|buster, bullseye|
|fedora|all|
|opensuse|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.



If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-grub/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
