# [gitlab_runner](#gitlab_runner)

Install and configure gitlab-runner on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-gitlab_runner/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-gitlab_runner/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-gitlab_runner/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-gitlab_runner)|[![quality](https://img.shields.io/ansible/quality/40614)](https://galaxy.ansible.com/robertdebock/gitlab_runner)|[![downloads](https://img.shields.io/ansible/role/d/40614)](https://galaxy.ansible.com/robertdebock/gitlab_runner)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-gitlab_runner.svg)](https://github.com/robertdebock/ansible-role-gitlab_runner/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-gitlab_runner/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.roles.gitlab_runner
      gitlab_runner_tags:
        - docker
        - my_runner
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-gitlab_runner/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-gitlab_runner/blob/master/defaults/main.yml):

```yaml
---
# defaults file for gitlab_runner

# These are the setting you need to register a runner.
# gitlab_runner_registration_token: "123ABC"

# The name as shown in the GitLab webinterface.
gitlab_runner_name: "{{ ansible_fqdn }}"

# The URL to register the runner to.
gitlab_runner_url: "https://gitlab.com/"

# The list of tags.
gitlab_runner_tags: []

# The type of executor. Choose from: "ssh", "shell", "parallels", "virtualbox",
# "docker", "docker_machine", "kubernetes" or "custom"
gitlab_runner_executor: docker

# The docker image to run.
gitlab_runner_docker_image: "alpine:latest"

# The version of the GitLab runner to install.
gitlab_runner_version: "16.1.0"

# Set the amount of concurrent jobs.
gitlab_runner_concurrency: "{{ ansible_processor_vcpus }}"

# Activate or deactivate privileged runner
gitlab_runner_privileged: true
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-gitlab_runner/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-gitlab_runner/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/repository/docker/robertdebock/enterpriselinux/general)|all|
|[Ubuntu](https://hub.docker.com/repository/docker/robertdebock/ubuntu/general)|bionic, focal|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-gitlab_runner/issues)

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-gitlab_runner/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
