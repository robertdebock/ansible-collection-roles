# [haproxy](#haproxy)

Install and configure haproxy on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-haproxy/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-haproxy/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-haproxy/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-haproxy)|[![quality](https://img.shields.io/ansible/quality/28674)](https://galaxy.ansible.com/robertdebock/haproxy)|[![downloads](https://img.shields.io/ansible/role/d/28674)](https://galaxy.ansible.com/robertdebock/haproxy)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-haproxy.svg)](https://github.com/robertdebock/ansible-role-haproxy/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/default/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: Converge
  hosts: all
  become: yes
  gather_facts: yes

  roles:
    - role: robertdebock.haproxy
      haproxy_frontends:
        - name: http
          address: "*"
          port: 80
          default_backend: backend
        - name: https
          address: "*"
          port: 443
          default_backend: backend
          ssl: yes
          crts:
            - /tmp/haproxy.keycrt
        - name: smtp
          address: "*"
          port: 25
          default_backend: smtp
          mode: tcp
      haproxy_backend_default_balance: roundrobin
      haproxy_backends:
        - name: backend
          httpcheck: yes
          # You can tell how the health check must be done.
          # This requires haproxy version 2
          # http_check:
          #   send:
          #     method: GET
          #     uri: /health.html
          #   expect: status 200
          balance: roundrobin
          # You can refer to hosts in an Ansible group.
          # The `ansible_default_ipv4` will be used as an address to connect to.
          servers: "{{ groups['all'] }}"
          port: 8080
          options:
            - check
        - name: smtp
          httpcheck: yes
          balance: roundrobin
          # You can also refer to a list of servers.
          servers:
            - name: first
              address: "127.0.0.1"
              port: 25
            - name: second
              address: "127.0.0.2"
              port: 25
          port: 25
          options:
            - check
```

The machine needs to be prepared. In CI this is done using `molecule/default/prepare.yml`:
```yaml
---
- name: Prepare
  hosts: all
  become: yes
  gather_facts: no

  roles:
    - role: robertdebock.bootstrap
    - role: robertdebock.core_dependencies
    - role: robertdebock.epel
    - role: robertdebock.buildtools
    - role: robertdebock.python_pip
    - role: robertdebock.openssl
      openssl_key_directory: /tmp
      openssl_items:
        - name: haproxy
          common_name: "{{ ansible_fqdn }}"
    # This role is applied to serve as a mock "backend" server. See `molecule/default/verify.yml`.
    - role: robertdebock.httpd
      httpd_port: 8080

  vars:
    _httpd_data_directory:
      default: /var/www/html
      Alpine: /var/www/localhost/htdocs
      Suse: /srv/www/htdocs

    httpd_data_directory: "{{ _httpd_data_directory[ansible_os_family] | default(_httpd_data_directory['default'] ) }}"
  post_tasks:
    - name: place health check
      ansible.builtin.copy:
        content: 'ok'
        dest: "{{ httpd_data_directory }}/health.html"

    - name: place sample page
      ansible.builtin.copy:
        content: 'Hello world!'
        dest: "{{ httpd_data_directory }}/index.html"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for haproxy

# Configure stats in HAProxy?
haproxy_stats: yes
haproxy_stats_port: 1936
haproxy_stats_bind_addr: 0.0.0.0

# Default setttings for HAProxy.
haproxy_retries: 3
haproxy_timeout_http_request: 10s
haproxy_timeout_connect: 10s
haproxy_timeout_client: 1m
haproxy_timeout_server: 1m
haproxy_timeout_http_keep_alive: 10s
haproxy_timeout_check: 10s
haproxy_maxconn: 3000
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-haproxy/blob/master/requirements.txt).

## [Status of used roles](#status-of-requirements)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-buildtools)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-httpd)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-openssl)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-python_pip)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-haproxy/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|8|
|debian|all|
|fedora|all|
|opensuse|all|
|ubuntu|all|

The minimum version of Ansible required is 2.10, tests have been done to:

- The previous version.
- The current version.
- The development version.


If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-haproxy/issues)

## [License](#license)

Apache-2.0

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
