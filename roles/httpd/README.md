# [httpd](#httpd)

Install and configure httpd on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-httpd)|[![quality](https://img.shields.io/ansible/quality/21855)](https://galaxy.ansible.com/robertdebock/httpd)|[![downloads](https://img.shields.io/ansible/role/d/21855)](https://galaxy.ansible.com/robertdebock/httpd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-httpd.svg)](https://github.com/robertdebock/ansible-role-httpd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  vars_files:
    - ../../vars/main.yml
    - ../../defaults/main.yml

  roles:
    - role: robertdebock.httpd
      # https_ssl_enable: yes
      httpd_port: 8080
      httpd_ssl_port: 8443
      httpd_locations:
        - name: my_location
          location: /my_location
          backend_url: "http://localhost:8080/myapplication"
      # httpd_vhosts:
      #   - name: my_vhost_docroot
      #     servername: www1.example.com
      #     documentroot: "{{ httpd_data_directory }}/www1.example.com"
      #   - name: my_vhost_backend_http
      #     servername: www2.example.com
      #     backend_url: "http://www.example.com/"
      #     serveralias:
      #       - example.com
      #       - www.example.com
      #   - name: my_vhost_remote
      #     servername: www3.example.com
      #     remote: "http://localhost:3128/"
      #   - name: my_vhost_backend_https
      #     servername: www4.example.com
      #     backend_url: "https://www.example.com/"
      #   - name: my_vhost_piratebay
      #     servername: piratebay.nl
      #     backend_url: "https://thepirate-bay.org/"
      #     proxy_preserve_host: Off
      #     proxy_requests: Off
      #     setenv:
      #       - name: force-proxy-request-1.0
      #         value: 1
      #       - name: proxy-nokeepalive
      #         value: 1
      #       - name: proxy-initial-not-pooled
      #       - name: proxy-sendchunks
      #         value: 1
      httpd_directories:
        - name: my_directory
          path: "{{ httpd_data_directory }}/my_directory"
          # options:
          #   - Indexes
          #   - FollowSymLinks
          allow_override: All
```

The machine needs to be prepared in CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  gather_facts: no
  become: yes

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.epel
    - role: robertdebock.buildtools
    - role: robertdebock.python_pip
    - role: robertdebock.openssl
      openssl_items:
        - name: apache-httpd
          common_name: "{{ ansible_fqdn }}"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for httpd

# The servername to use.
httpd_servername: "{{ ansible_fqdn }}"

# The non-SSL port to use.
httpd_port: 80

# Enable (self-signed certificates) SSL?
https_ssl_enable: no

# To configure https, set the hostname to listen to.
httpd_ssl_servername: "{{ ansible_fqdn }}"

# For SSL a TCP port is required.
httpd_ssl_port: 443

# SSL Certificate:
httpd_openssl_crt: "{{ httpd_openssl_crt_directory }}/apache-httpd.crt"

# SSL Key
httpd_openssl_key: "{{ httpd_openssl_key_directory }}/apache-httpd.key"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-httpd/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-openssl)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|
|[robertdebock.selinux](https://galaxy.ansible.com/robertdebock/selinux)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-selinux/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-selinux/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-selinux/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-selinux)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-httpd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|buster, bullseye|
|fedora|all|
|opensuse|all|
|ubuntu|focal, bionic|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.

## [Exceptions](#exceptions)

Some variarations of the build matrix do not work. These are the variations and reasons why the build won't work:

| variation                 | reason                 |
|---------------------------|------------------------|
| Alpine | ImportError: Error loading shared library /tmp/pip-build-env-23ZqyN/lib/python2.7/site-packages/_cffi_backend.so: Operation not permitted |
| amazonlinux | Dependency (python_pip) not available. |


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-httpd/issues)

## [License](#license)

Apache-2.0


## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
