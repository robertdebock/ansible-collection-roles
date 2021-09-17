# [minikube](#minikube)

Install and configure minikube on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-minikube/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-minikube/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-minikube/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-minikube)|[![quality](https://img.shields.io/ansible/quality/42933)](https://galaxy.ansible.com/robertdebock/minikube)|[![downloads](https://img.shields.io/ansible/role/d/42933)](https://galaxy.ansible.com/robertdebock/minikube)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-minikube.svg)](https://github.com/robertdebock/ansible-role-minikube/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.minikube
      minikube_user: minikube
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
    - role: robertdebock.core_dependencies
    - role: robertdebock.epel
    - role: robertdebock.python_pip
    - role: robertdebock.docker
    - role: robertdebock.kubectl
    - role: robertdebock.sysctl
      sysctl_items:
        - name: net.bridge.bridge-nf-call-iptables
          value: 1
        - name: fs.protected_regular
          value: 0
    - role: robertdebock.users
      users_user_list:
        - name: minikube
          groups: docker
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for minikube

minikube_version: 1.20.0-0

# `minikube start` should start as a non-root-user. This should be an exising
# user on the Linux system. (Hint: robertdebock.users)
minikube_user: minikube

minikube_command: /usr/bin/minikube start --driver=none
# minikube_command: /usr/bin/minikube start --vm-driver=none --apiserver-ips 127.0.0.1 --apiserver-name localhost --extra-config=kubelet.cgroup-driver=systemd
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-minikube/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.docker](https://galaxy.ansible.com/robertdebock/docker)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-docker/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-docker/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-docker/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-docker)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.kubectl](https://galaxy.ansible.com/robertdebock/kubectl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-kubectl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-kubectl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-kubectl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-kubectl)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-service)|
|[robertdebock.sysctl](https://galaxy.ansible.com/robertdebock/sysctl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-sysctl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-sysctl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-sysctl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-sysctl)|
|[robertdebock.users](https://galaxy.ansible.com/robertdebock/users)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-users/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-users/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-users/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-users)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-minikube/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|all|
|fedora|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some roles can't run on a specific distribution or version. Here are some exceptions.

| variation                 | reason                 |
|---------------------------|------------------------|
| CentOS 6 | Depending role (python_pip) does not work on CentOS 6. |

## [Included version(s)](#included-versions)

This role [refers to a version](https://github.com/robertdebock/ansible-role-minikube/blob/master/defaults/main.yml) released by Google. Check the released version(s) here:
- [A Debian package of Minikube](https://storage.googleapis.com/minikube/releases).
- [A Red Hat package of Minikube](https://storage.googleapis.com/minikube/releases).

This version reference means a role may get outdated. Monthly tests occur to see if [bit-rot](https://en.wikipedia.org/wiki/Software_rot) occured. If you however find a problem, please create an issue, I'll get on it as soon as possible.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-minikube/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
