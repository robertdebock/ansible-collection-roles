# [Ansible role vsftpd](#vsftpd)

Install and configure vsftpd on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-vsftpd/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-vsftpd/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-vsftpd/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-vsftpd)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/vsftpd)](https://galaxy.ansible.com/robertdebock/vsftpd)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-vsftpd.svg)](https://github.com/robertdebock/ansible-role-vsftpd/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-vsftpd/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.vsftpd
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-vsftpd/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-vsftpd/blob/master/defaults/main.yml):

```yaml
---
# defaults file for vsftpd

# Allow anonymous FTP? (Beware - allowed by default if you disable this).
vsftpd_anonymous_enable: true

# Enable this to allow local users to log in.
vsftpd_local_enable: true

# Enable this to enable any form of FTP write command.
vsftpd_write_enable: true

# Default umask for local users is 077. You may wish to change this to 022,
# if your users expect that (022 is used by most other ftpd's)
vsftpd_local_umask: "022"

# Enable this to allow the anonymous FTP user to upload files. This only
# has an effect if the above global write enable is activated. Also, you will
# obviously need to create a directory writable by the FTP user.
# When SELinux is enforcing check for SE bool allow_ftpd_anon_write, allow_ftpd_full_access
vsftpd_anon_upload_enable: false

# Enable this if you want the anonymous FTP user to be able to create
# new directories.
vsftpd_anon_mkdir_write_enable: false

# Activate directory messages - messages given to remote users when they
# go into a certain directory.
vsftpd_dirmessage_enable: true

# Activate logging of uploads/downloads.
vsftpd_xferlog_enable: true

# Make sure PORT transfer connections originate from port 20 (ftp-data).
vsftpd_connect_from_port_20: true

# If you want, you can arrange for uploaded anonymous files to be owned by
# a different user. Note! Using "root" for uploaded files is not
# recommended!
vsftpd_chown_uploads: false
vsftpd_chown_username: whoever

# You may override where the log file goes if you like. The default is shown
# below.
vsftpd_xferlog_file: /var/log/xferlog

# If you want, you can have your log file in standard ftpd xferlog format.
# Note that the default log file location is /var/log/xferlog in this case.
vsftpd_xferlog_std_format: true

# You may change the default value for timing out an idle session.
vsftpd_idle_session_timeout: 600

# You may change the default value for timing out a data connection.
vsftpd_data_connection_timeout: 120

# It is recommended that you define on your system a unique user which the
# ftp server can use as a totally isolated and unprivileged user.
vsftpd_nopriv_user: ftpsecure

# Enable this and the server will recognise asynchronous ABOR requests. Not
# recommended for security (the code is non-trivial). Not enabling it,
# however, may confuse older FTP clients.
vsftpd_async_abor_enable: true

# By default the server will pretend to allow ASCII mode but in fact ignore
# the request. Turn on the below options to have the server actually do ASCII
# mangling on files when in ASCII mode. The vsftpd.conf(5) man page explains
# the behaviour when these options are disabled.
# Beware that on some FTP servers, ASCII support allows a denial of service
# attack (DoS) via the command "SIZE /big/file" in ASCII mode. vsftpd
# predicted this attack and has always been safe, reporting the size of the
# raw file.
# ASCII mangling is a horrible feature of the protocol.
vsftpd_ascii_upload_enable: false
vsftpd_ascii_download_enable: false

# You may fully customise the login banner string:
vsftpd_ftpd_banner: "Welcome to blah FTP service."

# You may specify a file of disallowed anonymous e-mail addresses. Apparently
# useful for combatting certain DoS attacks.
vsftpd_deny_email_enable: true
# (default follows)
vsftpd_banned_email_file: /etc/vsftpd/banned_emails

# You may specify an explicit list of local users to chroot() to their home
# directory. If chroot_local_user is YES, then this list becomes a list of
# users to NOT chroot().
# (Warning! chroot'ing can be very dangerous. If using chroot, make sure that
# the user does not have write access to the top level directory within the
# chroot)
vsftpd_chroot_local_user: false
vsftpd_chroot_list_enable: false
# (default follows)
vsftpd_chroot_list_file: /etc/vsftpd/chroot_list

# You may activate the "-R" option to the builtin ls. This is disabled by
# default to avoid remote users being able to cause excessive I/O on large
# sites. However, some broken FTP clients such as "ncftp" and "mirror" assume
# the presence of the "-R" option, so there is a strong case for enabling it.
vsftpd_ls_recurse_enable: false

# When "listen" directive is enabled, vsftpd runs in standalone mode and
# listens on IPv4 sockets. This directive cannot be used in conjunction
# with the listen_ipv6 directive.
vsftpd_listen: false

# This directive enables listening on IPv6 sockets. By default, listening
# on the IPv6 "any" address (::) will accept connections from both IPv6
# and IPv4 clients. It is not necessary to listen on *both* IPv4 and IPv6
# sockets. If you want that (perhaps because you want to listen on specific
# addresses) then you must run two copies of vsftpd with two configuration
# files.
# Make sure, that one of the listen options is commented !!
vsftpd_listen_ipv6: true

vsftpd_pam_service_name: vsftpd
vsftpd_userlist_enable: true

# If enabled, vsftpd will display directory listings with the time
# in  your  local  time  zone.  The default is to display GMT. The
# times returned by the MDTM FTP command are also affected by this
# option.
vsftpd_use_localtime: true

# This option should be the name of a directory which is empty.  Also, the
# directory should not be writable by the ftp user. This directory is used
# as a secure chroot() jail at times vsftpd does not require filesystem
# access.
vsftpd_secure_chroot_dir: /var/run/vsftpd/empty

# This option specifies the location of the RSA certificate to use for SSL
# encrypted connections.
# vsftpd_rsa_cert_file: /etc/ssl/certs/ssl-cert-snakeoil.pem
# vsftpd_rsa_private_key_file: /etc/ssl/private/ssl-cert-snakeoil.key
vsftpd_ssl_enable: false
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-vsftpd/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-vsftpd/png/requirements.png "Dependencies")

## [Compatibility](#compatibility)

This role has been tested on these [container images](https://hub.docker.com/u/robertdebock):

|container|tags|
|---------|----|
|[Alpine](https://hub.docker.com/r/robertdebock/alpine)|all|
|[Amazon](https://hub.docker.com/r/robertdebock/amazonlinux)|Candidate|
|[Debian](https://hub.docker.com/r/robertdebock/debian)|all|
|[EL](https://hub.docker.com/r/robertdebock/enterpriselinux)|9|
|[Fedora](https://hub.docker.com/r/robertdebock/fedora)|all|
|[Ubuntu](https://hub.docker.com/r/robertdebock/ubuntu)|all|

The minimum version of Ansible required is 2.12, tests have been done to:

- The previous version.
- The current version.
- The development version.

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-vsftpd/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-vsftpd/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
