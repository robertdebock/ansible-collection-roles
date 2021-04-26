# [gitlab_runner](#gitlab_runner)

Install and configure gitlab-runner on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-gitlab_runner/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-gitlab_runner/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-gitlab_runner/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-gitlab_runner)|[![quality](https://img.shields.io/ansible/quality/40614)](https://galaxy.ansible.com/robertdebock/gitlab_runner)|[![downloads](https://img.shields.io/ansible/role/d/40614)](https://galaxy.ansible.com/robertdebock/gitlab_runner)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-gitlab_runner.svg)](https://github.com/robertdebock/ansible-role-gitlab_runner/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.gitlab_runner
      gitlab_runner_token: fake-token
      gitlab_runner_register_runner: no
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
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for gitlab_runner

# These are the setting you need to register a runner.
# gitlab_runner_token: 123ABC

# Should this role register the gitlab runner?
gitlab_runner_register_runner: yes

# The name as shown in the GitLab webinterface.
gitlab_runner_name: "{{ ansible_fqdn }}"

# The URL to register the runner to.
gitlab_runner_url: "https://gitlab.com/"

# The tags, comma separated.
gitlab_runner_tags: "docker,my_runner"

# The type of executor. Choose from: "ssh", "shell", "parallels", "virtualbox",
# "docker", "docker_machine", "kubernetes" or "custom"
gitlab_runner_executor: docker

# The docker image to run.
gitlab_runner_docker_image: "alpine:latest"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-gitlab_runner/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-gitlab_runner/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|7, 8|
|debian|buster|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| Alpine | Not supported, see https://docs.gitlab.com/ee/install/requirements.html |
| Archlinux | Not supported, see https://docs.gitlab.com/ee/install/requirements.html |
| EL 8 | Not supported, see https://docs.gitlab.com/ee/install/requirements.html |
| Fedora | Not supported, see https://docs.gitlab.com/ee/install/requirements.html |
| Ubuntu rolling | Not supported, see https://docs.gitlab.com/ee/install/requirements.html |
| debian:buster | Not supported, see https://docs.gitlab.com/runner/install/linux-repository.html |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-gitlab_runner/issues)

## [License](#license)

Apache-2.0

## [Contributors](#contributors)

I'd like to thank everybody that made contributions to this repository. It motivates me, improves the code and is just fun to collaborate.

- [dbenaben](https://github.com/dbenaben)

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
