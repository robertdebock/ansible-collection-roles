# [Ansible role tfe](#tfe)

Install and configure tfe on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-tfe/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-tfe/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-tfe/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-tfe)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/tfe)](https://galaxy.ansible.com/robertdebock/tfe)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-tfe.svg)](https://github.com/robertdebock/ansible-role-tfe/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-tfe/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.tfe
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-tfe/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.docker_ce
    - role: robertdebock.roles.docker_compose

  post_tasks:
    # The role docker_ce skips starting on Docker hosts.
    - name: Start docker daemon
      ansible.builtin.service:
        name: docker
        state: started
        enabled: true
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-tfe/blob/master/defaults/main.yml):

```yaml
---
# defaults file for tfe

# Select the image to use for Terraform Enterprise. This includes the version.
# The latest tfe version can be found here:
# https://developer.hashicorp.com/terraform/enterprise/releases/2023/v202303-1
tfe_image: "images.releases.hashicorp.com/hashicorp/terraform-enterprise:v202309-1"

# Paste the license of Terraform Enterprise here. It's a long string.
# If the license is not set or empty, many tasks will be skipped, resulting in
# a non-working Terraform Enterprise instance. Not setting a license can help
# with testing.
tfe_license: ""

# Configure a hostname, used to redirect HTTP(S) requests.
tfe_hostname: "tfe.example.com"

# An encryption password for the TFE application.
tfe_encryption_password: "S0meP@ssword"

# A list of CIDR notated subnets that are allowed to create an "Initial Admin
# Token".
tfe_iact_subnets: []
#   - "10.0.0.0/8"
#   - "192.168.0.0/24"

# The following variables are used to configure the TLS certificate and key for
# the web interface of Terraform Enterprise. The certificate and key should be
# placed in the `files` directory of your playbook.
#
# You can create a self-signed certificate with the following command:
#
# openssl req -x509 -nodes -newkey rsa:4096 -keyout key.pem -out cert.pem \
# -sha256 -days 365
# cp cert.pem bundle.pem
tfe_tls_certificate: "cert.pem"
tfe_tls_key: "key.pem"
tfe_tls_bundle: "bundle.pem"

# You can set the operational mode to either: "disk", "external" or "active-active".
tfe_operational_mode: "active-active"

# Maximum number of Terraform runs that can execute concurrently on each Terraform Enterprise node.
tfe_capacity_concurrency: 10

# Enable log forwarding by setting a path.
# The file (basename) will originate from this Ansible role, unless you have
# a custom file in your `files/` directory of your playbook directory.
# tfe_log_forwarding_config_path: /etc/terraform-enterprise/fluent-bit/fluent-bit.conf

# Details on the database host. This host should already exist, this role
# does not create a database.
# These variables are required when `tfe_operational_mode` is set to `active-active` or `external`.
tfe_database_host: "tfe.RaNdOm.eu-west-1.rds.amazonaws.com"
tfe_database_user: "tfe"
tfe_database_password: "my_pass_c0mpl.x"
tfe_database_name: "tfe"
tfe_database_parameters: "sslmode=disable"

# Detail on the object storage. This role does not create the bucket.
# These variables are required when `tfe_operational_mode` is set to `active-active` or `external`.
tfe_object_storage_s3_endpoint: ""
tfe_object_storage_s3_use_instance_profile: false
tfe_object_storage_s3_bucket: "SomeBucketName"
tfe_object_storage_s3_access_key_id: ""
tfe_object_storage_s3_secret_access_key: ""
tfe_object_storage_s3_region: "eu-west-1"

# Details on the Redis host. This host should already exist, this role
# does not create a Redis instance.
# These variables are required when `tfe_operational_mode` is set to `active-active`.
tfe_redis_host: "tfe.RaNdOm.0001.euw1.cache.amazonaws.com"
tfe_redis_user: "tfe"
tfe_redis_password: "my_pass_c0mpl.x"
tfe_redis_use_tls: false
tfe_redis_use_auth: false

# The internal Vault requires an internal address of the node.
tfe_vault_cluster_address: "https://{{ ansible_default_ipv4.address }}:8201"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-tfe/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.docker_ce](https://galaxy.ansible.com/robertdebock/docker_ce)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-docker_ce/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-docker_ce/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-docker_ce/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-docker_ce)|
|[robertdebock.docker_compose](https://galaxy.ansible.com/robertdebock/docker_compose)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-docker_compose/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-docker_compose/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-docker_compose/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-docker_compose)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-tfe/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|bullseye|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|38, 39|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-tfe/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-tfe/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
