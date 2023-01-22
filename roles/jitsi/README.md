# [jitsi](#jitsi)

Install and configure jitsi on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-jitsi/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-jitsi/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-jitsi/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-jitsi)|[![quality](https://img.shields.io/ansible/quality/47727)](https://galaxy.ansible.com/robertdebock/jitsi)|[![downloads](https://img.shields.io/ansible/role/d/47727)](https://galaxy.ansible.com/robertdebock/jitsi)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-jitsi.svg)](https://github.com/robertdebock/ansible-role-jitsi/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-jitsi/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.jitsi
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-jitsi/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.ca_certificates
    - role: robertdebock.roles.hostname
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-jitsi/blob/master/defaults/main.yml):

```yaml
---
# defaults file for jitsi

# You can choose to install different release: `stable`, `testing` or `nightly`.
jitsi_release: stable

# Settings used for the installation of jitsi-meet
jitsi_settings:
  - name: jitsi-meet
    question: jitsi-meet/cert-choice
    value: "Generate a new self-signed certificate (You will later get a chance to obtain a Let's encrypt certificate)"
    type: string
  - name: jitsi-meet
    question: jitsi-meet/jvb-serve
    value: yes|bool
    type: boolean
  - name: jitsi-meet-prosody
    question: jitsi-meet-prosody/jvb-hostname
    value: "{{ ansible_fqdn }}"
    type: string
  - name: jitsi-videobridge
    question: jitsi-videobridge/jvb-hostname
    value: "{{ ansible_fqdn }}"
    type: string
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-jitsi/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.ca_certificates](https://galaxy.ansible.com/robertdebock/ca_certificates)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-ca_certificates/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-ca_certificates/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-ca_certificates/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-ca_certificates)|
|[robertdebock.hostname](https://galaxy.ansible.com/robertdebock/hostname)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-hostname/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-hostname/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-hostname/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-hostname)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-jitsi/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/repository/docker/robertdebock/debian/general)|bullseye|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-jitsi/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-jitsi/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
