# [Ansible role haproxy](#haproxy)

Install and configure haproxy on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-haproxy/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-haproxy/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-haproxy/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-haproxy)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/haproxy)](https://galaxy.ansible.com/robertdebock/haproxy)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-haproxy.svg)](https://github.com/robertdebock/ansible-role-haproxy/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-haproxy/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.haproxy
      haproxy_frontends:
        - name: http
          address: "*"
          port: 80
          default_backend: backend
        - name: https
          address: "*"
          port: 443
          default_backend: backend
          ssl: true
          crts:
            - /tmp/haproxy.keycrt
        - name: smtp
          address: "*"
          port: 25
          default_backend: smtp
          mode: tcp
        - name: prometheus
          address: "*"
          port: 8405
          mode: http
          http_request: use-service prometheus-exporter
          no_log: true
      haproxy_backend_default_balance: roundrobin
      haproxy_backends:
        - name: backend
          httpcheck: true
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
          balance: leastconn
          mode: tcp
          # You can also refer to a list of servers.
          servers:
            - name: first
              address: "127.0.0.1"
              port: 25
            - name: second
              address: "127.0.0.2"
              port: 25
          port: 25
        - name: vault
          mode: tcp
          httpcheck: GET /v1/sys/health HTTP/1.1
          servers: "{{ groups['all'] }}"
          http_send_name_header: Host
          port: 8200
          options:
            - check
            - check-ssl
            - ssl verify none

      haproxy_listen_default_balance: roundrobin
      haproxy_listens:
        - name: listen
          address: "*"
          httpcheck: true
          listen_port: 8081
          balance: roundrobin
          # You can refer to hosts in an Ansible group.
          # The `ansible_default_ipv4` will be used as an address to connect to.
          servers: "{{ groups['all'] }}"
          port: 8080
          options:
            - maxconn 100000
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-haproxy/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
    - role: robertdebock.roles.epel
    - role: robertdebock.roles.buildtools
    - role: robertdebock.roles.python_pip
    - role: robertdebock.roles.openssl
      openssl_key_directory: /tmp
      openssl_items:
        - name: haproxy
          common_name: "{{ ansible_fqdn }}"
    # This role is applied to serve as a mock "backend" server. See `molecule/default/verify.yml`.
    - role: robertdebock.roles.httpd
      httpd_port: 8080

  vars:
    _httpd_data_directory:
      default: /var/www/html
      Alpine: /var/www/localhost/htdocs
      Suse: /srv/www/htdocs

    httpd_data_directory: "{{ _httpd_data_directory[ansible_os_family] | default(_httpd_data_directory['default'] ) }}"
  post_tasks:
    - name: Place health check
      ansible.builtin.copy:
        content: 'ok'
        dest: "{{ httpd_data_directory }}/health.html"

    - name: Place sample page
      ansible.builtin.copy:
        content: 'Hello world!'
        dest: "{{ httpd_data_directory }}/index.html"
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-haproxy/blob/master/defaults/main.yml):

```yaml
---
# defaults file for haproxy

# Complete HAProxy configuration as a string (alternative to individual parameters)
# If set, this will be used instead of individual parameters
# haproxy_config: |
#   global
#       log         127.0.0.1 local2
#       chroot      /var/lib/haproxy
#       pidfile     /var/run/haproxy.pid
#       maxconn     4000
#       user        haproxy
#       group       haproxy
#       daemon
#       stats       socket /var/lib/haproxy/stats

#   defaults
#       mode                    http
#       log                     global
#       option                  httplog
#       option                  dontlognull
#       option                  http-server-close
#       option                  forwardfor except 127.0.0.0/8
#       option                  redispatch
#       retries                 3
#       timeout http-request    10s
#       timeout queue           10s
#       timeout connect         10s
#       timeout client          1m
#       timeout server          1m
#       timeout http-keep-alive 10s
#       timeout check           10s
#       maxconn                 3000

#   listen stats
#       bind                0.0.0.0:1936
#       mode                http
#       stats               enable
#       stats               uri /stats

#   frontend http
#       bind *:80
#       default_backend backend
#       mode http
#       option httplog

#   backend backend
#       balance roundrobin
#       mode http
#       server server1 127.0.0.1:8080 check
#       server server2 127.0.0.2:8080 check

# Default is to use individual parameters.
haproxy_config: ""

# Configure stats in HAProxy?
haproxy_stats: true
haproxy_stats_port: 1936
haproxy_stats_bind_addr: "0.0.0.0"

# Default setttings for HAProxy.
haproxy_mode: http
haproxy_options:
  - httplog
  - dontlognull
  - http-server-close
  - forwardfor except 127.0.0.0/8
  - redispatch
haproxy_retries: 3
haproxy_timeout_http_request: 10s
haproxy_timeout_connect: 10s
haproxy_timeout_client: 1m
haproxy_timeout_server: 1m
haproxy_timeout_http_keep_alive: 10s
haproxy_timeout_check: 10s
haproxy_maxconn: 3000

# A list of frontends. See `molecule/default/converge.yml` for an example.
haproxy_frontends: []
haproxy_backend_default_balance: roundrobin
haproxy_backends: []

# For the listening lists:
haproxy_listen_default_balance: roundrobin
haproxy_listens: []
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-haproxy/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.buildtools](https://galaxy.ansible.com/robertdebock/buildtools)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-buildtools/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-buildtools/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-buildtools/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-buildtools)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|
|[robertdebock.epel](https://galaxy.ansible.com/robertdebock/epel)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-epel/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-epel/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-epel/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-epel)|
|[robertdebock.httpd](https://galaxy.ansible.com/robertdebock/httpd)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-httpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-httpd/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-httpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-httpd)|
|[robertdebock.openssl](https://galaxy.ansible.com/robertdebock/openssl)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-openssl/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-openssl/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-openssl/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-openssl)|
|[robertdebock.python_pip](https://galaxy.ansible.com/robertdebock/python_pip)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-python_pip/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-python_pip/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-python_pip/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-python_pip)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-haproxy/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-haproxy/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-haproxy/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
