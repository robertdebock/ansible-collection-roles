# [Ansible role postfix](#postfix)

Install and configure postfix on your system.

|GitHub|GitLab|Downloads|Version|
|------|------|---------|-------|
|[![github](https://github.com/robertdebock/ansible-role-postfix/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-postfix/actions)|[![gitlab](https://gitlab.com/robertdebock-iac/ansible-role-postfix/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-postfix)|[![downloads](https://img.shields.io/ansible/role/d/robertdebock/postfix)](https://galaxy.ansible.com/robertdebock/postfix)|[![Version](https://img.shields.io/github/release/robertdebock/ansible-role-postfix.svg)](https://github.com/robertdebock/ansible-role-postfix/releases/)|

## [Example Playbook](#example-playbook)

This example is taken from [`molecule/default/converge.yml`](https://github.com/robertdebock/ansible-role-postfix/blob/master/molecule/default/converge.yml) and is tested on each push, pull request and release.

```yaml
---
- name: Converge
  hosts: all
  become: true
  gather_facts: true

  roles:
    - role: robertdebock.roles.postfix
      # postfix_relayhost: "[relay.example.com]"
      postfix_myhostname: "smtp.example.com"
      postfix_mydomain: "example.com"
      postfix_myorigin: "example.com"
      postfix_mynetworks:
        - 127.0.0.0/8
        - 192.168.0.0/16
      postfix_aliases:
        - name: root
          destination: test@example.com
      # Ziggo settings: ("email-address" and "email-password" are placeholders)
      postfix_relayhost: "[smtp.ziggo.nl]:587"
      postfix_smtp_sasl_auth_enable: true
      postfix_smtp_sasl_password_map: "/etc/postfix/relay_pass"
      postfix_smtp_sasl_security_options: ""
      postfix_smtp_tls_wrappermode: false
      postfix_smtp_tls_security_level: may
      postfix_smtp_sasl_password_map_content: |
        [smtp.ziggo.nl]:587 email-address:email-password
```

The machine needs to be prepared. In CI this is done using [`molecule/default/prepare.yml`](https://github.com/robertdebock/ansible-role-postfix/blob/master/molecule/default/prepare.yml):

```yaml
---
- name: Prepare
  hosts: all
  become: true
  gather_facts: false

  roles:
    - role: robertdebock.roles.bootstrap
    - role: robertdebock.roles.core_dependencies
```

Also see a [full explanation and example](https://robertdebock.nl/how-to-use-these-roles.html) on how to use these roles.

## [Role Variables](#role-variables)

The default values for the variables are set in [`defaults/main.yml`](https://github.com/robertdebock/ansible-role-postfix/blob/master/defaults/main.yml):

```yaml
---
# defaults file for postfix

# These settings are required in postfix.
postfix_myhostname: "{{ ansible_fqdn }}"
postfix_mydomain: "{{ ansible_domain | default('localdomain', true) }}"
postfix_myorigin: "{{ ansible_domain | default('localdomain', true) }}"

# To "listen" on public interfaces, set inet_interfaces to something like
# "all" or the name of the interface, such as "eth0".
postfix_inet_interfaces: "loopback-only"

# Enable IPv4, and IPv6 if supported - if IPV4 only set to ipv4
postfix_inet_protocols: all

# Set a banner
postfix_banner: "$myhostname ESMTP $mail_name"

# The distination tells Postfix what mails to accept mail for.
postfix_mydestination: $mydomain, $myhostname, localhost.$mydomain, localhost

# To accept email from other machines, set the mynetworks to something like
# "- 192.168.0.0/24".
postfix_mynetworks:
  - 127.0.0.0/8

# These settings change the role of the postfix server to a relay host.
# postfix_relay_domains: "$mydestination"

# If you want to forward emails to another central relay server, set relayhost.
# use brackets to sent to the A-record of the relayhost.
# postfix_relayhost: "[relay.example.com]"

# Set the restrictions for receiving mails.
postfix_smtpd_recipient_restrictions:
  - permit_mynetworks
  - permit_sasl_authenticated
  - reject_unauth_destination
  - reject_invalid_hostname
  - reject_non_fqdn_hostname
  - reject_non_fqdn_sender
  - reject_non_fqdn_recipient
  - reject_unknown_sender_domain
  - reject_unknown_recipient_domain
  - reject_rbl_client sbl.spamhaus.org
  - reject_rbl_client cbl.abuseat.org
  - reject_rbl_client dul.dnsbl.sorbs.net
  - permit

postfix_smtpd_sender_restrictions:
  - reject_unknown_sender_domain

# The default SMTP TLS security level for the Postfix SMTP client
# Valid values are: dane, encrypt, fingerprint, may, none, secure, verify
postfix_smtp_tls_security_level: none

# To enable spamassassin, ensure spamassassin is installed,
# (hint: role: robertdebock.spamassassin) and set these two variables:
# postfix_spamassassin: enabled
# postfix_spamassassin_user: spamd

# To enable clamav, ensure clamav is installed,
# (hint: role: robertdebock.clamav) and set this variable:
# postfix_clamav: enabled

# You can configure aliases here. Typically redirecting `root` is a good plan.
# postfix_aliases:
#   - name: root
#     destination: robert@meinit.nl

# You can configure sender access controls here.
# postfix_sender_access:
#   - domain: gooddomain.com
#     action: OK
#   - domain: baddomain.com
#     action: REJECT

# You can configure recipient access controls here.
# postfix_recipient_access:
#   - domain: gooddomain.com
#     action: OK
#   - domain: baddomain.com
#     action: REJECT

# You can disable SSL/TLS versions here.
# postfix_tls_protocols: '!SSLv2, !SSLv3, !TLSv1, !TLSv1.1'

# You can supply a transport_maps Jinja2 template here
# postfix_transport_maps_template: /path/to/transport.j2

# You can supply a header_checks Jinja2 template here
# postfix_header_checks_template: /path/to/header_checks.j2

# Whether or not to use the local biff service.
# postfix_biff: true

# With locally submitted mail, append the string ".$mydomain" to addresses that have no ".domain" information
# postfix_append_dot_mydomain: false

# The alias databases that are used for local(8) delivery
# postfix_alias_maps: "hash:/etc/aliases"

# A prefix that the virtual(8) delivery agent prepends to all pathname results from $virtual_mailbox_maps table lookups.
# postfix_virtual_mailbox_base: /var/mail

# Optional lookup tables with all valid addresses in the domains that match $virtual_mailbox_domains.
# postfix_virtual_mailbox_maps: mysql:/etc/postfix/mysql-virtual_mailbox_maps.cf

# Postfix is final destination for the specified list of domains; mail is delivered via the $virtual_transport mail delivery transport
# postfix_virtual_mailbox_domains: "$virtual_mailbox_maps"

# Postfix is final destination for the specified list of virtual alias domains, that is, domains for which all addresses are aliased to addresses in other local or remote domains.
# postfix_virtual_alias_domains: "$virtual_alias_maps"

# Optional lookup tables that alias specific mail addresses or domains to other local or remote address.
# postix_virtual_alias_maps: "$virtual_maps"

# Lookup tables with the per-recipient user ID that the virtual(8) delivery agent uses while writing to the recipient's mailbox.
# postfix_virtual_uid_maps: "static:2000"

# Lookup tables with the per-recipient group ID for virtual(8) mailbox delivery.
# postfix_virtual_gid_maps: "static:2000"

# Enable SASL authentication in the Postfix SMTP server.
# postfix_smtpd_sasl_auth_enable: true

# The name of the Postfix SMTP server's local SASL authentication realm.
# postfix_smtpd_sasl_local_domain: $myhostname

# Postfix SMTP server SASL security options; as of Postfix 2.3 the list of available features depends on the SASL server implementation that is selected with smtpd_sasl_type.
# postfix_smtpd_sasl_security_options: noanonymous

# Report the SASL authenticated user name in the smtpd(8) Received message header.
# postfix_smtpd_sasl_authenticated_header: true

# Enable interoperability with remote SMTP clients that implement an obsolete version of the AUTH command (RFC 4954).
# postfix_broken_sasl_auth_clients: false

# A file containing (PEM format) CA certificates of root CAs trusted to sign either remote SMTP client certificates or intermediate CA certificates.
# postfix_smtpd_tls_CAfile: /etc/letsencrypt/live/smtp.syhosting.ch/chain.pem

# File with the Postfix SMTP server RSA certificate in PEM format.
# postfix_smtpd_tls_cert_file: /etc/letsencrypt/live/smtp.syhosting.ch/cert.pem

# Local file with the Postfix SMTP server RSA certificate in PEM format which shall be copied to the target host.
# postfix_smtpd_tls_cert_file_source: ./certs/cert.pem

# File with the Postfix SMTP server RSA private key in PEM format.
# postfix_smtpd_tls_key_file: /etc/letsencrypt/live/smtp.syhosting.ch/privkey.pem

# Local file with the Postfix SMTP server RSA private key in PEM format which shall be copied to the target host.
# postfix_smtpd_tls_key_file_source: ./certs/privkey.pem

# Request that the Postfix SMTP server produces Received: message headers that include information about the protocol and cipher used, as well as the remote SMTP client CommonName and client certificate issuer CommonName.
# postfix_smtpd_tls_received_header: true

# The default SMTP TLS security level for the Postfix SMTP client; when a non-empty value is specified, this overrides the obsolete parameters smtp_use_tls, smtp_enforce_tls, and smtp_tls_enforce_peername.
# postfix_smtpd_tls_security_level: may

# Ask a remote SMTP client for a client certificate.
# postfix_smtpd_tls_ask_ccert: true

# Enable additional Postfix SMTP server logging of TLS activity.
# postfix_smtpd_tls_loglevel: 1

# Name of the file containing the optional Postfix SMTP server TLS session cache.
# postfix_smtpd_tls_session_cache_database: btree:/var/lib/postfix/smtpd_tls_session_cache

# A file containing CA certificates of root CAs trusted to sign either remote SMTP server certificates or intermediate CA certificates.
# postfix_smtp_tls_CAfile: /etc/letsencrypt/live/smtp.syhosting.ch/chain.pem

# File with the Postfix SMTP client RSA certificate in PEM format.
# postfix_smtp_tls_cert_file: /etc/letsencrypt/live/smtp.syhosting.ch/cert.pem

# File with the Postfix SMTP client RSA private key in PEM format.
# postfix_smtp_tls_key_file: /etc/letsencrypt/live/smtp.syhosting.ch/privkey.pem

# Name of the file containing the optional Postfix SMTP client TLS session cache.
# postfix_smtp_tls_session_cache_database: btree:/var/lib/postfix/smtp_tls_session_cache

# The external entropy source for the in-memory tlsmgr(8) pseudo random number generator (PRNG) pool.
# postfix_tls_random_source: dev:/dev/urandom

# TLS protocols accepted by the Postfix SMTP server with mandatory TLS encryption.
# postfix_smtpd_tls_mandatory_protocols: TLSv1

# TLS protocols that the Postfix SMTP client will use with mandatory TLS encryption.
# postfix_smtp_tls_mandatory_protocols: TLSv1

# The default mail delivery transport and next-hop destination for final delivery to domains listed with $virtual_mailbox_domains.
# postfix_virtual_transport: maildrop1

# Optional pathname of a mailbox file relative to a local(8) user's home directory.
# postfix_home_mailbox: Maildir/

# The maximal size in bytes of a message, including envelope information.
# postfix_message_size_limit: 10240000

# Require that a remote SMTP client introduces itself with the HELO or EHLO command before sending the MAIL command or other commands that require EHLO negotiation.
# postfix_smtpd_helo_required: false

# The time unit over which client connection rates and other rates are calculated.
# postfix_anvil_rate_time_unit: 60s

# The maximal number of connection attempts any client is allowed to make to this service per time unit.
# postfix_smtpd_client_connection_rate_limit: 10

# How many simultaneous connections any client is allowed to make to this service.
# postfix_smtpd_client_connection_count_limit: 10

# Consider a bounce message as undeliverable, when delivery fails with a temporary error, and the time in the queue has reached the bounce_queue_lifetime limit.
# postfix_bounce_queue_lifetime: 5d

# The location of Postfix README files that describe how to build, configure or operate a specific Postfix subsystem or feature.
# postfix_readme_directory: /usr/share/doc/postfix

# The location of Postfix HTML files that describe how to build, configure or operate a specific Postfix subsystem or feature.
# postfix_html_directory: /usr/share/doc/postfix/html

# List of custom master.cf entries if more services are needed outside of postfix defaults
# postfix_master_custom: []

# You can change the port where Postfix listens on.
# Postfix used `/etc/services` to map service names to port numbers like `2525`.
# So either specifcy a port number or a service name like `smtp`.
postfix_smtp_listen_port: smtp

postfix_smtp_sasl_auth_enable: false
postfix_smtp_sasl_password_map: ""
postfix_smtp_sasl_security_options: ""
postfix_smtp_tls_wrappermode: false
postfix_smtp_sasl_password_map_content: ""
```

## [Requirements](#requirements)

- pip packages listed in [requirements.txt](https://github.com/robertdebock/ansible-role-postfix/blob/master/requirements.txt).

## [State of used roles](#state-of-used-roles)

The following roles are used to prepare a system. You can prepare your system in another way.

| Requirement | GitHub | GitLab |
|-------------|--------|--------|
|[robertdebock.bootstrap](https://galaxy.ansible.com/robertdebock/bootstrap)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-bootstrap/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-bootstrap/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-bootstrap)|
|[robertdebock.core_dependencies](https://galaxy.ansible.com/robertdebock/core_dependencies)|[![Build Status GitHub](https://github.com/robertdebock/ansible-role-core_dependencies/workflows/Ansible%20Molecule/badge.svg)](https://github.com/robertdebock/ansible-role-core_dependencies/actions)|[![Build Status GitLab](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies/badges/master/pipeline.svg)](https://gitlab.com/robertdebock-iac/ansible-role-core_dependencies)|

## [Context](#context)

This role is a part of many compatible roles. Have a look at [the documentation of these roles](https://robertdebock.nl/) for further information.

Here is an overview of related roles:
![dependencies](https://raw.githubusercontent.com/robertdebock/ansible-role-postfix/png/requirements.png "Dependencies")

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

If you find issues, please register them in [GitHub](https://github.com/robertdebock/ansible-role-postfix/issues).

## [License](#license)

[Apache-2.0](https://github.com/robertdebock/ansible-role-postfix/blob/master/LICENSE).

## [Author Information](#author-information)

[robertdebock](https://robertdebock.nl/)

Please consider [sponsoring me](https://github.com/sponsors/robertdebock).
