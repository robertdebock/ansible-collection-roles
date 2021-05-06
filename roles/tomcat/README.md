# [tomcat](#tomcat)

Install and configure tomcat on your system.

|GitHub|GitLab|Quality|Downloads|Version|
|------|------|-------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-tomcat/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-tomcat/actions)|[![gitlab](https://gitlab.com/robertdebock/ansible-role-tomcat/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-tomcat)|[![quality](https://img.shields.io/ansible/quality/22945)](https://galaxy.ansible.com/robertdebock/tomcat)|[![downloads](https://img.shields.io/ansible/role/d/22945)](https://galaxy.ansible.com/robertdebock/tomcat)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-tomcat.svg)](https://github.com/robertdebock/ansible-role-tomcat/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from `molecule/resources/converge.yml` and is tested on each push, pull request and release.
```yaml
---
- name: converge
  hosts: all
  become: yes
  gather_facts: yes

  vars:
    tomcat_address: 127.0.0.1
    tomcat_instances:
      - name: "tomcat"
      - name: "tomcat-version-7"
        version: 7
        shutdown_port: 8007
        non_ssl_connector_port: 8082
        ssl_connector_port: 8445
        ajp_port: 8011
      - name: "tomcat-version-8"
        version: 8
        shutdown_port: 8008
        non_ssl_connector_port: 8083
        ssl_connector_port: 8446
        ajp_port: 8012
      - name: "tomcat-version-9"
        version: 9
        shutdown_port: 8019
        non_ssl_connector_port: 8084
        ssl_connector_port: 8447
        ajp_port: 8013
      - name: "tomcat-specific"
        user: "specificuser"
        group: "specificgroup"
        shutdown_port: 8020
        shutdown_pass: shutme
        non_ssl_connector_port: 8085
        ssl_connector_port: 8448
        ajp_port: 8014
        xms: 256M
        xmx: 512M
      - name: "tomcat-with-wars"
        shutdown_port: 8021
        non_ssl_connector_port: 8086
        ssl_connector_port: 8449
        ajp_port: 8015
        wars:
          - url: https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war
          - url: "https://github.com/aeimer/java-example-helloworld-war/raw/master/dist/helloworld.war"
      - name: "tomcat-java_opts"
        shutdown_port: 8022
        non_ssl_connector_port: 8087
        ssl_connector_port: 8449
        ajp_port: 8016
        java_opts:
          - name: UMASK
            value: "0007"
      - name: "tomcat-with_lib"
        shutdown_port: 8023
        non_ssl_connector_port: 8088
        ssl_connector_port: 8450
        ajp_port: 8017
        libs:
          - url: "https://search.maven.org/remotecontent?filepath=io/prometheus/simpleclient/0.6.0/simpleclient-0.6.0.jar"
      - name: "tomcat-access-logs"
        shutdown_port: 8024
        non_ssl_connector_port: 8089
        ssl_connector_port: 8451
        ajp_port: 8018
        access_log_enabled: yes
        access_log_directory: "my-logs"
        access_log_prefix: my-access-logs
        access_log_suffix: ".log"
        access_log_pattern: "%h %l %u %t &quot;%r&quot; %s %b"
      - name: "tomcat-config-files"
        shutdown_port: 8025
        non_ssl_connector_port: 8090
        ssl_connector_port: 8452
        ajp_port: 8019
        config_files:
          - src: "{{ role_path }}/files/dummy.properties"
            dest: "./"
            mode: "0644"

  roles:
    - role: robertdebock.tomcat
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
    - role: robertdebock.core_dependencies
    - role: robertdebock.java
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

These variables are set in `defaults/main.yml`:
```yaml
---
# defaults file for tomcat

# Some "sane" defaults.
tomcat_name: tomcat
tomcat_directory: /opt
tomcat_version: 8
tomcat_user: tomcat
tomcat_group: tomcat
tomcat_xms: 512M
tomcat_xmx: 1024M
tomcat_non_ssl_connector_port: 8080
tomcat_ssl_connector_port: 8443
tomcat_shutdown_port: 8005
tomcat_shutdown_pass: SHUTDOWN
tomcat_ajp_port: 8009
tomcat_jre_home: /usr
tomcat_service_state: started
tomcat_service_enabled: yes
# You can bind Tomcat to a specified address globally using this variable, or
# in the `tomcat_instances`. The `tomcat_instances.address` is more specific
# so it takes priority over `tomcat_address`.
tomcat_address: 0.0.0.0

# Configure tomcat access logs
tomcat_access_log_enabled: yes
tomcat_access_log_directory: logs
tomcat_access_log_prefix: localhost_access_log
tomcat_access_log_suffix: ".txt"
tomcat_access_log_pattern: "%h %l %u %t &quot;%r&quot; %s %b"

# This role allows multiple installations of Apache Tomcat, each in their own
# location, potentially of different version.
# This is done by defining a "tomcat_instances" where "name:" is a unique
# identifier of an instance.
# The default tomcat_instances is one instance using the defaults described
# in defaults/main.yml.
tomcat_instances:
  - name: "{{ tomcat_name }}"
    version: "{{ tomcat_version }}"
    user: "{{ tomcat_user }}"
    group: "{{ tomcat_group }}"
    xms: "{{ tomcat_xms }}"
    xmx: "{{ tomcat_xmx }}"
    non_ssl_connector_port: "{{ tomcat_non_ssl_connector_port }}"
    ssl_connector_port: "{{ tomcat_ssl_connector_port }}"
    shutdown_port: "{{ tomcat_shutdown_port }}"
    ajp_port: "{{ tomcat_ajp_port }}"
    ajp_secret: ""
    # You can pick an address per instance:
    # address: 127.0.0.1
    packet_size: "8192"
    java_opts:
      - name: JRE_HOME
        value: "{{ tomcat_jre_home }}"
    access_log_enabled: "{{ tomcat_access_log_enabled }}"
    access_log_directory: "{{ tomcat_access_log_directory }}"
    access_log_prefix: "{{ tomcat_access_log_prefix }}"
    access_log_suffix: "{{ tomcat_access_log_suffix }}"
    access_log_pattern: "{{ tomcat_access_log_pattern }}"
    service_state: "{{ tomcat_service_state }}"
    service_enabled: "{{ tomcat_service_enabled }}"

# The explicit version to use when referring to the short name.
tomcat_version7: 7.0.107
tomcat_version8: 8.5.60
tomcat_version9: 9.0.40

# The location where to download Apache Tomcat from.
tomcat_mirror: "https://archive.apache.org"

# If you want to download Tomcat from another location, adjust these parameters
# to your liking. For "normal" use, this does not require modification.
_tomcat_unarchive_urls:
  7:
    url: "{{ tomcat_mirror }}/dist/tomcat/tomcat-7/v{{ tomcat_version7 }}/bin/apache-tomcat-{{ tomcat_version7 }}.tar.gz"
  8:
    url: "{{ tomcat_mirror }}/dist/tomcat/tomcat-8/v{{ tomcat_version8 }}/bin/apache-tomcat-{{ tomcat_version8 }}.tar.gz"
  9:
    url: "{{ tomcat_mirror }}/dist/tomcat/tomcat-9/v{{ tomcat_version9 }}/bin/apache-tomcat-{{ tomcat_version9 }}.tar.gz"

tomcat_unarchive_url: "{{ _tomcat_unarchive_urls[tomcat_version].url }}"
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-tomcat/blob/master/requirements.txt).

## [Status of requirements](#status-of-requirements)

The following roles are used to prepare a system. You may choose to prepare your system in another way, I have tested these roles as well.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-core_dependencies)|
|[robertdebock.java](https://galaxy.ansible.com/robertdebock/java)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-java/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-java/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-java/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-java)|
|[robertdebock.service](https://galaxy.ansible.com/robertdebock/service)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-service/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-service/actions)|[![Build Status GitLab ](https://gitlab.com/robertdebock/ansible-role-service/badges/master/pipeline.svg)](https://gitlab.com/robertdebock/ansible-role-service)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-tomcat/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|el|7, 8|
|debian|buster, bullseye|
|fedora|33, 34|
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
| amazonlinux:1 | Not idempotent. |
| alpine | Restart fails. |

## [Included version(s)](#included-versions)

This role [refers to a version](https://github.com/robertdebock/ansible-role-tomcat/blob/master/defaults/main.yml) released by Apache Tomcat. Check the released version(s) here:
- [Tomcat version 7](https://tomcat.apache.org/download-70.cgi).
- [Tomcat version 8](https://tomcat.apache.org/download-80.cgi).
- [Tomcat version 9](https://tomcat.apache.org/download-90.cgi).

This version reference means a role may get outdated. Monthly tests occur to see if [bit-rot](https://en.wikipedia.org/wiki/Software_rot) occured. If you however find a problem, please create an issue, I'll get on it as soon as possible.
If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-tomcat/issues)

## [License](#license)

Apache-2.0

## [Contributors](#contributors)

I'd like to thank everybody that made contributions to this repository. It motivates me, improves the code and is just fun to collaborate.

- [gaima8](https://github.com/gaima8)
- [brunoleon](https://github.com/brunoleon)
- [javid90khan](https://github.com/javid90khan)
- [patsevanton](https://github.com/patsevanton)
- [till](https://github.com/till)

## [Author Information](#author-information)

[Robert de Bock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
