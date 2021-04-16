#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2012, Mark Theunissen <mark.theunissen@gmail.com>
# Sponsored by Four Kitchens http://fourkitchens.com.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: mysql_user
short_description: Adds or removes a user from a MySQL database
description:
   - Adds or removes a user from a MySQL database.
options:
  name:
    description:
      - Name of the user (role) to add or remove.
    type: str
    required: true
  password:
    description:
      - Set the user's password.
    type: str
  encrypted:
    description:
      - Indicate that the 'password' field is a `mysql_native_password` hash.
    type: bool
    default: no
  host:
    description:
      - The 'host' part of the MySQL username.
    type: str
    default: localhost
  host_all:
    description:
      - Override the host option, making ansible apply changes
        to all hostnames for a given user.
      - This option cannot be used when creating users.
    type: bool
    default: no
  priv:
    description:
      - "MySQL privileges string in the format: C(db.table:priv1,priv2)."
      - "Multiple privileges can be specified by separating each one using
        a forward slash: C(db.table:priv/db.table:priv)."
      - The format is based on MySQL C(GRANT) statement.
      - Database and table names can be quoted, MySQL-style.
      - If column privileges are used, the C(priv1,priv2) part must be
        exactly as returned by a C(SHOW GRANT) statement. If not followed,
        the module will always report changes. It includes grouping columns
        by permission (C(SELECT(col1,col2)) instead of C(SELECT(col1),SELECT(col2))).
      - Can be passed as a dictionary (see the examples).
    type: raw
  append_privs:
    description:
      - Append the privileges defined by priv to the existing ones for this
        user instead of overwriting existing ones.
    type: bool
    default: no
  tls_requires:
    description:
      - Set requirement for secure transport as a dictionary of requirements (see the examples).
      - Valid requirements are SSL, X509, SUBJECT, ISSUER, CIPHER.
      - SUBJECT, ISSUER and CIPHER are complementary, and mutually exclusive with SSL and X509.
      - U(https://mariadb.com/kb/en/securing-connections-for-client-and-server/#requiring-tls).
    type: dict
    version_added: 1.0.0
  sql_log_bin:
    description:
      - Whether binary logging should be enabled or disabled for the connection.
    type: bool
    default: yes
  state:
    description:
      - Whether the user should exist.
      - When C(absent), removes the user.
    type: str
    choices: [ absent, present ]
    default: present
  check_implicit_admin:
    description:
      - Check if mysql allows login as root/nopassword before trying supplied credentials.
      - If success, passed I(login_user)/I(login_password) will be ignored.
    type: bool
    default: no
  update_password:
    description:
      - C(always) will update passwords if they differ.
      - C(on_create) will only set the password for newly created users.
    type: str
    choices: [ always, on_create ]
    default: always
  plugin:
    description:
      - User's plugin to authenticate (``CREATE USER user IDENTIFIED WITH plugin``).
    type: str
    version_added: '0.1.0'
  plugin_hash_string:
    description:
      - User's plugin hash string (``CREATE USER user IDENTIFIED WITH plugin AS plugin_hash_string``).
    type: str
    version_added: '0.1.0'
  plugin_auth_string:
    description:
      - User's plugin auth_string (``CREATE USER user IDENTIFIED WITH plugin BY plugin_auth_string``).
    type: str
    version_added: '0.1.0'
  resource_limits:
    description:
      - Limit the user for certain server resources. Provided since MySQL 5.6 / MariaDB 10.2.
      - "Available options are C(MAX_QUERIES_PER_HOUR: num), C(MAX_UPDATES_PER_HOUR: num),
        C(MAX_CONNECTIONS_PER_HOUR: num), C(MAX_USER_CONNECTIONS: num)."
      - Used when I(state=present), ignored otherwise.
    type: dict
    version_added: '0.1.0'

notes:
   - "MySQL server installs with default I(login_user) of C(root) and no password.
     To secure this user as part of an idempotent playbook, you must create at least two tasks:
     1) change the root user's password, without providing any I(login_user)/I(login_password) details,
     2) drop a C(~/.my.cnf) file containing the new root credentials.
     Subsequent runs of the playbook will then succeed by reading the new credentials from the file."
   - Currently, there is only support for the C(mysql_native_password) encrypted password hash module.
   - Supports (check_mode).

seealso:
- module: community.mysql.mysql_info
- name: MySQL access control and account management reference
  description: Complete reference of the MySQL access control and account management documentation.
  link: https://dev.mysql.com/doc/refman/8.0/en/access-control.html
- name: MySQL provided privileges reference
  description: Complete reference of the MySQL provided privileges documentation.
  link: https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html

author:
- Jonathan Mainguy (@Jmainguy)
- Benjamin Malynovytch (@bmalynovytch)
- Lukasz Tomaszkiewicz (@tomaszkiewicz)
extends_documentation_fragment:
- community.mysql.mysql

'''

EXAMPLES = r'''
- name: Removes anonymous user account for localhost
  community.mysql.mysql_user:
    name: ''
    host: localhost
    state: absent

- name: Removes all anonymous user accounts
  community.mysql.mysql_user:
    name: ''
    host_all: yes
    state: absent

- name: Create database user with name 'bob' and password '12345' with all database privileges
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: '*.*:ALL'
    state: present

- name: Create database user using hashed password with all database privileges
  community.mysql.mysql_user:
    name: bob
    password: '*EE0D72C1085C46C5278932678FBE2C6A782821B4'
    encrypted: yes
    priv: '*.*:ALL'
    state: present

- name: Create database user with password and all database privileges and 'WITH GRANT OPTION'
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: '*.*:ALL,GRANT'
    state: present

- name: Create user with password, all database privileges and 'WITH GRANT OPTION' in db1 and db2
  community.mysql.mysql_user:
    state: present
    name: bob
    password: 12345dd
    priv:
      'db1.*': 'ALL,GRANT'
      'db2.*': 'ALL,GRANT'

# Note that REQUIRESSL is a special privilege that should only apply to *.* by itself.
# Setting this privilege in this manner is deprecated.
# Use 'tls_requires' instead.
- name: Modify user to require SSL connections
  community.mysql.mysql_user:
    name: bob
    append_privs: yes
    priv: '*.*:REQUIRESSL'
    state: present

- name: Modify user to require TLS connection with a valid client certificate
  community.mysql.mysql_user:
    name: bob
    tls_requires:
      x509:
    state: present

- name: Modify user to require TLS connection with a specific client certificate and cipher
  community.mysql.mysql_user:
    name: bob
    tls_requires:
      subject: '/CN=alice/O=MyDom, Inc./C=US/ST=Oregon/L=Portland'
      cipher: 'ECDHE-ECDSA-AES256-SHA384'

- name: Modify user to no longer require SSL
  community.mysql.mysql_user:
    name: bob
    tls_requires:

- name: Ensure no user named 'sally'@'localhost' exists, also passing in the auth credentials
  community.mysql.mysql_user:
    login_user: root
    login_password: 123456
    name: sally
    state: absent

# check_implicit_admin example
- name: >
    Ensure no user named 'sally'@'localhost' exists, also passing in the auth credentials.
    If mysql allows root/nopassword login, try it without the credentials first.
    If it's not allowed, pass the credentials
  community.mysql.mysql_user:
    check_implicit_admin: yes
    login_user: root
    login_password: 123456
    name: sally
    state: absent

- name: Ensure no user named 'sally' exists at all
  community.mysql.mysql_user:
    name: sally
    host_all: yes
    state: absent

- name: Specify grants composed of more than one word
  community.mysql.mysql_user:
    name: replication
    password: 12345
    priv: "*.*:REPLICATION CLIENT"
    state: present

- name: Revoke all privileges for user 'bob' and password '12345'
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: "*.*:USAGE"
    state: present

# Example privileges string format
# mydb.*:INSERT,UPDATE/anotherdb.*:SELECT/yetanotherdb.*:ALL

- name: Example using login_unix_socket to connect to server
  community.mysql.mysql_user:
    name: root
    password: abc123
    login_unix_socket: /var/run/mysqld/mysqld.sock

- name: Example of skipping binary logging while adding user 'bob'
  community.mysql.mysql_user:
    name: bob
    password: 12345
    priv: "*.*:USAGE"
    state: present
    sql_log_bin: no

- name: Create user 'bob' authenticated with plugin 'AWSAuthenticationPlugin'
  community.mysql.mysql_user:
    name: bob
    plugin: AWSAuthenticationPlugin
    plugin_hash_string: RDS
    priv: '*.*:ALL'
    state: present

- name: Limit bob's resources to 10 queries per hour and 5 connections per hour
  community.mysql.mysql_user:
    name: bob
    resource_limits:
      MAX_QUERIES_PER_HOUR: 10
      MAX_CONNECTIONS_PER_HOUR: 5

# Example .my.cnf file for setting the root password
# [client]
# user=root
# password=n<_665{vS43y
'''

RETURN = '''#'''

import re
import string

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.mysql.plugins.module_utils.database import SQLParseError
from ansible_collections.community.mysql.plugins.module_utils.mysql import (
    mysql_connect, mysql_driver, mysql_driver_fail_msg, mysql_common_argument_spec
)
from ansible.module_utils.six import iteritems
from ansible.module_utils._text import to_native


VALID_PRIVS = frozenset(('CREATE', 'DROP', 'GRANT', 'GRANT OPTION',
                         'LOCK TABLES', 'REFERENCES', 'EVENT', 'ALTER',
                         'DELETE', 'INDEX', 'INSERT', 'SELECT', 'UPDATE',
                         'CREATE TEMPORARY TABLES', 'TRIGGER', 'CREATE VIEW',
                         'SHOW VIEW', 'ALTER ROUTINE', 'CREATE ROUTINE',
                         'EXECUTE', 'FILE', 'CREATE TABLESPACE', 'CREATE USER',
                         'PROCESS', 'PROXY', 'RELOAD', 'REPLICATION CLIENT',
                         'REPLICATION SLAVE', 'SHOW DATABASES', 'SHUTDOWN',
                         'SUPER', 'ALL', 'ALL PRIVILEGES', 'USAGE',
                         'REQUIRESSL',  # Deprecated, to be removed in version 3.0.0
                         'CREATE ROLE', 'DROP ROLE', 'APPLICATION_PASSWORD_ADMIN',
                         'AUDIT_ADMIN', 'BACKUP_ADMIN', 'BINLOG_ADMIN',
                         'BINLOG_ENCRYPTION_ADMIN', 'CLONE_ADMIN', 'CONNECTION_ADMIN',
                         'ENCRYPTION_KEY_ADMIN', 'FIREWALL_ADMIN', 'FIREWALL_USER',
                         'GROUP_REPLICATION_ADMIN', 'INNODB_REDO_LOG_ARCHIVE',
                         'NDB_STORED_USER', 'PERSIST_RO_VARIABLES_ADMIN',
                         'REPLICATION_APPLIER', 'REPLICATION_SLAVE_ADMIN',
                         'RESOURCE_GROUP_ADMIN', 'RESOURCE_GROUP_USER',
                         'ROLE_ADMIN', 'SESSION_VARIABLES_ADMIN', 'SET_USER_ID',
                         'SYSTEM_USER', 'SYSTEM_VARIABLES_ADMIN', 'SYSTEM_USER',
                         'TABLE_ENCRYPTION_ADMIN', 'VERSION_TOKEN_ADMIN',
                         'XA_RECOVER_ADMIN', 'LOAD FROM S3', 'SELECT INTO S3',
                         'INVOKE LAMBDA',
                         'ALTER ROUTINE',
                         'BINLOG ADMIN',
                         'BINLOG MONITOR',
                         'BINLOG REPLAY',
                         'CONNECTION ADMIN',
                         'READ_ONLY ADMIN',
                         'REPLICATION MASTER ADMIN',
                         'REPLICATION SLAVE ADMIN',
                         'SET USER',
                         'SHOW_ROUTINE',
                         'SLAVE MONITOR',
                         'REPLICA MONITOR',))


class InvalidPrivsError(Exception):
    pass

# ===========================================
# MySQL module specific support methods.
#


def get_mode(cursor):
    cursor.execute('SELECT @@GLOBAL.sql_mode')
    result = cursor.fetchone()
    mode_str = result[0]
    if 'ANSI' in mode_str:
        mode = 'ANSI'
    else:
        mode = 'NOTANSI'
    return mode


def user_exists(cursor, user, host, host_all):
    if host_all:
        cursor.execute("SELECT count(*) FROM mysql.user WHERE user = %s", (user,))
    else:
        cursor.execute("SELECT count(*) FROM mysql.user WHERE user = %s AND host = %s", (user, host))

    count = cursor.fetchone()
    return count[0] > 0


def sanitize_requires(tls_requires):
    sanitized_requires = {}
    if tls_requires:
        for key in tls_requires.keys():
            sanitized_requires[key.upper()] = tls_requires[key]
        if any([key in ["CIPHER", "ISSUER", "SUBJECT"] for key in sanitized_requires.keys()]):
            sanitized_requires.pop("SSL", None)
            sanitized_requires.pop("X509", None)
            return sanitized_requires

        if "X509" in sanitized_requires.keys():
            sanitized_requires = "X509"
        else:
            sanitized_requires = "SSL"

        return sanitized_requires
    return None


def mogrify_requires(query, params, tls_requires):
    if tls_requires:
        if isinstance(tls_requires, dict):
            k, v = zip(*tls_requires.items())
            requires_query = " AND ".join(("%s %%s" % key for key in k))
            params += v
        else:
            requires_query = tls_requires
        query = " REQUIRE ".join((query, requires_query))
    return query, params


def do_not_mogrify_requires(query, params, tls_requires):
    return query, params


def get_tls_requires(cursor, user, host):
    if user:
        if not impl.use_old_user_mgmt(cursor):
            query = "SHOW CREATE USER '%s'@'%s'" % (user, host)
        else:
            query = "SHOW GRANTS for '%s'@'%s'" % (user, host)

        cursor.execute(query)
        require_list = [tuple[0] for tuple in filter(lambda x: "REQUIRE" in x[0], cursor.fetchall())]
        require_line = require_list[0] if require_list else ""
        pattern = r"(?<=\bREQUIRE\b)(.*?)(?=(?:\bPASSWORD\b|$))"
        requires_match = re.search(pattern, require_line)
        requires = requires_match.group().strip() if requires_match else ""
        if any((requires.startswith(req) for req in ('SSL', 'X509', 'NONE'))):
            requires = requires.split()[0]
            if requires == 'NONE':
                requires = None
        else:
            import shlex

            items = iter(shlex.split(requires))
            requires = dict(zip(items, items))
        return requires or None


def get_grants(cursor, user, host):
    cursor.execute("SHOW GRANTS FOR %s@%s", (user, host))
    grants_line = list(filter(lambda x: "ON *.*" in x[0], cursor.fetchall()))[0]
    pattern = r"(?<=\bGRANT\b)(.*?)(?=(?:\bON\b))"
    grants = re.search(pattern, grants_line[0]).group().strip()
    return grants.split(", ")


def user_add(cursor, user, host, host_all, password, encrypted,
             plugin, plugin_hash_string, plugin_auth_string, new_priv,
             tls_requires, check_mode):
    # we cannot create users without a proper hostname
    if host_all:
        return False

    if check_mode:
        return True

    # Determine what user management method server uses
    old_user_mgmt = impl.use_old_user_mgmt(cursor)

    mogrify = do_not_mogrify_requires if old_user_mgmt else mogrify_requires

    if password and encrypted:
        if impl.supports_identified_by_password(cursor):
            query_with_args = "CREATE USER %s@%s IDENTIFIED BY PASSWORD %s", (user, host, password)
        else:
            query_with_args = "CREATE USER %s@%s IDENTIFIED WITH mysql_native_password AS %s", (user, host, password)
    elif password and not encrypted:
        if old_user_mgmt:
            query_with_args = "CREATE USER %s@%s IDENTIFIED BY %s", (user, host, password)
        else:
            cursor.execute("SELECT CONCAT('*', UCASE(SHA1(UNHEX(SHA1(%s)))))", (password,))
            encrypted_password = cursor.fetchone()[0]
            query_with_args = "CREATE USER %s@%s IDENTIFIED WITH mysql_native_password AS %s", (user, host, encrypted_password)
    elif plugin and plugin_hash_string:
        query_with_args = "CREATE USER %s@%s IDENTIFIED WITH %s AS %s", (user, host, plugin, plugin_hash_string)
    elif plugin and plugin_auth_string:
        query_with_args = "CREATE USER %s@%s IDENTIFIED WITH %s BY %s", (user, host, plugin, plugin_auth_string)
    elif plugin:
        query_with_args = "CREATE USER %s@%s IDENTIFIED WITH %s", (user, host, plugin)
    else:
        query_with_args = "CREATE USER %s@%s", (user, host)

    query_with_args_and_tls_requires = query_with_args + (tls_requires,)
    cursor.execute(*mogrify(*query_with_args_and_tls_requires))

    if new_priv is not None:
        for db_table, priv in iteritems(new_priv):
            privileges_grant(cursor, user, host, db_table, priv, tls_requires)
    if tls_requires is not None:
        privileges_grant(cursor, user, host, "*.*", get_grants(cursor, user, host), tls_requires)
    return True


def is_hash(password):
    ishash = False
    if len(password) == 41 and password[0] == '*':
        if frozenset(password[1:]).issubset(string.hexdigits):
            ishash = True
    return ishash


def user_mod(cursor, user, host, host_all, password, encrypted,
             plugin, plugin_hash_string, plugin_auth_string, new_priv,
             append_privs, tls_requires, module):
    changed = False
    msg = "User unchanged"
    grant_option = False

    # Determine what user management method server uses
    old_user_mgmt = impl.use_old_user_mgmt(cursor)

    if host_all:
        hostnames = user_get_hostnames(cursor, user)
    else:
        hostnames = [host]

    for host in hostnames:
        # Handle clear text and hashed passwords.
        if bool(password):

            # Get a list of valid columns in mysql.user table to check if Password and/or authentication_string exist
            cursor.execute("""
                SELECT COLUMN_NAME FROM information_schema.COLUMNS
                WHERE TABLE_SCHEMA = 'mysql' AND TABLE_NAME = 'user' AND COLUMN_NAME IN ('Password', 'authentication_string')
                ORDER BY COLUMN_NAME DESC LIMIT 1
            """)
            colA = cursor.fetchone()

            cursor.execute("""
                SELECT COLUMN_NAME FROM information_schema.COLUMNS
                WHERE TABLE_SCHEMA = 'mysql' AND TABLE_NAME = 'user' AND COLUMN_NAME IN ('Password', 'authentication_string')
                ORDER BY COLUMN_NAME ASC  LIMIT 1
            """)
            colB = cursor.fetchone()

            # Select hash from either Password or authentication_string, depending which one exists and/or is filled
            cursor.execute("""
                SELECT COALESCE(
                        CASE WHEN %s = '' THEN NULL ELSE %s END,
                        CASE WHEN %s = '' THEN NULL ELSE %s END
                    )
                FROM mysql.user WHERE user = %%s AND host = %%s
                """ % (colA[0], colA[0], colB[0], colB[0]), (user, host))
            current_pass_hash = cursor.fetchone()[0]
            if isinstance(current_pass_hash, bytes):
                current_pass_hash = current_pass_hash.decode('ascii')

            if encrypted:
                encrypted_password = password
                if not is_hash(encrypted_password):
                    module.fail_json(msg="encrypted was specified however it does not appear to be a valid hash expecting: *SHA1(SHA1(your_password))")
            else:
                if old_user_mgmt:
                    cursor.execute("SELECT PASSWORD(%s)", (password,))
                else:
                    cursor.execute("SELECT CONCAT('*', UCASE(SHA1(UNHEX(SHA1(%s)))))", (password,))
                encrypted_password = cursor.fetchone()[0]

            if current_pass_hash != encrypted_password:
                msg = "Password updated"
                if module.check_mode:
                    return (True, msg)
                if old_user_mgmt:
                    cursor.execute("SET PASSWORD FOR %s@%s = %s", (user, host, encrypted_password))
                    msg = "Password updated (old style)"
                else:
                    try:
                        cursor.execute("ALTER USER %s@%s IDENTIFIED WITH mysql_native_password AS %s", (user, host, encrypted_password))
                        msg = "Password updated (new style)"
                    except (mysql_driver.Error) as e:
                        # https://stackoverflow.com/questions/51600000/authentication-string-of-root-user-on-mysql
                        # Replacing empty root password with new authentication mechanisms fails with error 1396
                        if e.args[0] == 1396:
                            cursor.execute(
                                "UPDATE mysql.user SET plugin = %s, authentication_string = %s, Password = '' WHERE User = %s AND Host = %s",
                                ('mysql_native_password', encrypted_password, user, host)
                            )
                            cursor.execute("FLUSH PRIVILEGES")
                            msg = "Password forced update"
                        else:
                            raise e
                changed = True

        # Handle plugin authentication
        if plugin:
            cursor.execute("SELECT plugin, authentication_string FROM mysql.user "
                           "WHERE user = %s AND host = %s", (user, host))
            current_plugin = cursor.fetchone()

            update = False

            if current_plugin[0] != plugin:
                update = True

            if plugin_hash_string and current_plugin[1] != plugin_hash_string:
                update = True

            if plugin_auth_string and current_plugin[1] != plugin_auth_string:
                # this case can cause more updates than expected,
                # as plugin can hash auth_string in any way it wants
                # and there's no way to figure it out for
                # a check, so I prefer to update more often than never
                update = True

            if update:
                if plugin_hash_string:
                    query_with_args = "ALTER USER %s@%s IDENTIFIED WITH %s AS %s", (user, host, plugin, plugin_hash_string)
                elif plugin_auth_string:
                    query_with_args = "ALTER USER %s@%s IDENTIFIED WITH %s BY %s", (user, host, plugin, plugin_auth_string)
                else:
                    query_with_args = "ALTER USER %s@%s IDENTIFIED WITH %s", (user, host, plugin)

                cursor.execute(*query_with_args)
                changed = True

        # Handle privileges
        if new_priv is not None:
            curr_priv = privileges_get(cursor, user, host)

            # If the user has privileges on a db.table that doesn't appear at all in
            # the new specification, then revoke all privileges on it.
            for db_table, priv in iteritems(curr_priv):
                # If the user has the GRANT OPTION on a db.table, revoke it first.
                if "GRANT" in priv:
                    grant_option = True
                if db_table not in new_priv:
                    if user != "root" and "PROXY" not in priv and not append_privs:
                        msg = "Privileges updated"
                        if module.check_mode:
                            return (True, msg)
                        privileges_revoke(cursor, user, host, db_table, priv, grant_option)
                        changed = True

            # If the user doesn't currently have any privileges on a db.table, then
            # we can perform a straight grant operation.
            for db_table, priv in iteritems(new_priv):
                if db_table not in curr_priv:
                    msg = "New privileges granted"
                    if module.check_mode:
                        return (True, msg)
                    privileges_grant(cursor, user, host, db_table, priv, tls_requires)
                    changed = True

            # If the db.table specification exists in both the user's current privileges
            # and in the new privileges, then we need to see if there's a difference.
            db_table_intersect = set(new_priv.keys()) & set(curr_priv.keys())
            for db_table in db_table_intersect:

                # If appending privileges, only the set difference between new privileges and current privileges matter.
                # The symmetric difference isn't relevant for append because existing privileges will not be revoked.
                if append_privs:
                    priv_diff = set(new_priv[db_table]) - set(curr_priv[db_table])
                else:
                    priv_diff = set(new_priv[db_table]) ^ set(curr_priv[db_table])

                if len(priv_diff) > 0:
                    msg = "Privileges updated"
                    if module.check_mode:
                        return (True, msg)
                    if not append_privs:
                        privileges_revoke(cursor, user, host, db_table, curr_priv[db_table], grant_option)
                    privileges_grant(cursor, user, host, db_table, new_priv[db_table], tls_requires)
                    changed = True

        # Handle TLS requirements
        current_requires = get_tls_requires(cursor, user, host)
        if current_requires != tls_requires:
            msg = "TLS requires updated"
            if module.check_mode:
                return (True, msg)
            if not old_user_mgmt:
                pre_query = "ALTER USER"
            else:
                pre_query = "GRANT %s ON *.* TO" % ",".join(get_grants(cursor, user, host))

            if tls_requires is not None:
                query = " ".join((pre_query, "%s@%s"))
                query_with_args = mogrify_requires(query, (user, host), tls_requires)
            else:
                query = " ".join((pre_query, "%s@%s REQUIRE NONE"))
                query_with_args = query, (user, host)

            cursor.execute(*query_with_args)
            changed = True

    return (changed, msg)


def user_delete(cursor, user, host, host_all, check_mode):
    if check_mode:
        return True

    if host_all:
        hostnames = user_get_hostnames(cursor, user)
    else:
        hostnames = [host]

    for hostname in hostnames:
        cursor.execute("DROP USER %s@%s", (user, hostname))

    return True


def user_get_hostnames(cursor, user):
    cursor.execute("SELECT Host FROM mysql.user WHERE user = %s", (user,))
    hostnames_raw = cursor.fetchall()
    hostnames = []

    for hostname_raw in hostnames_raw:
        hostnames.append(hostname_raw[0])

    return hostnames


def privileges_get(cursor, user, host):
    """ MySQL doesn't have a better method of getting privileges aside from the
    SHOW GRANTS query syntax, which requires us to then parse the returned string.
    Here's an example of the string that is returned from MySQL:

     GRANT USAGE ON *.* TO 'user'@'localhost' IDENTIFIED BY 'pass';

    This function makes the query and returns a dictionary containing the results.
    The dictionary format is the same as that returned by privileges_unpack() below.
    """
    output = {}
    cursor.execute("SHOW GRANTS FOR %s@%s", (user, host))
    grants = cursor.fetchall()

    def pick(x):
        if x == 'ALL PRIVILEGES':
            return 'ALL'
        else:
            return x

    for grant in grants:
        res = re.match("""GRANT (.+) ON (.+) TO (['`"]).*\\3@(['`"]).*\\4( IDENTIFIED BY PASSWORD (['`"]).+\\6)? ?(.*)""", grant[0])
        if res is None:
            raise InvalidPrivsError('unable to parse the MySQL grant string: %s' % grant[0])
        privileges = res.group(1).split(",")
        privileges = [pick(x.strip()) for x in privileges]

        # Handle cases when there's privs like GRANT SELECT (colA, ...) in privs.
        # To this point, the privileges list can look like
        # ['SELECT (`A`', '`B`)', 'INSERT'] that is incorrect (SELECT statement is splitted).
        # Columns should also be sorted to compare it with desired privileges later.
        # Determine if there's a case similar to the above:
        privileges = normalize_col_grants(privileges)

        if "WITH GRANT OPTION" in res.group(7):
            privileges.append('GRANT')
        db = res.group(2)
        output.setdefault(db, []).extend(privileges)
    return output


def normalize_col_grants(privileges):
    """Fix and sort grants on columns in privileges list

    Make ['SELECT (A, B)', 'INSERT (A, B)', 'DETELE']
    from ['SELECT (A', 'B)', 'INSERT (B', 'A)', 'DELETE'].
    See unit tests in tests/unit/plugins/modules/test_mysql_user.py
    """
    for grant in ('SELECT', 'UPDATE', 'INSERT', 'REFERENCES'):
        start, end = has_grant_on_col(privileges, grant)
        # If not, either start and end will be None
        if start is not None:
            privileges = handle_grant_on_col(privileges, start, end)

    return privileges


def has_grant_on_col(privileges, grant):
    """Check if there is a statement like SELECT (colA, colB)
    in the privilege list.

    Return (start index, end index).
    """
    # Determine elements of privileges where
    # columns are listed
    start = None
    end = None
    for n, priv in enumerate(privileges):
        if '%s (' % grant in priv:
            # We found the start element
            start = n

        if start is not None and ')' in priv:
            # We found the end element
            end = n
            break

    if start is not None and end is not None:
        # if the privileges list consist of, for example,
        # ['SELECT (A', 'B), 'INSERT'], return indexes of related elements
        return start, end
    else:
        # If start and end position is the same element,
        # it means there's expression like 'SELECT (A)',
        # so no need to handle it
        return None, None


def handle_grant_on_col(privileges, start, end):
    """Handle cases when the privs like SELECT (colA, ...) is in the privileges list."""
    # When the privileges list look like ['SELECT (colA,', 'colB)']
    # (Notice that the statement is splitted)
    if start != end:
        output = list(privileges[:start])

        select_on_col = ', '.join(privileges[start:end + 1])

        select_on_col = sort_column_order(select_on_col)

        output.append(select_on_col)

        output.extend(privileges[end + 1:])

    # When it look like it should be, e.g. ['SELECT (colA, colB)'],
    # we need to be sure, the columns is sorted
    else:
        output = list(privileges)
        output[start] = sort_column_order(output[start])

    return output


def sort_column_order(statement):
    """Sort column order in grants like SELECT (colA, colB, ...).

    MySQL changes columns order like below:
    ---------------------------------------
    mysql> GRANT SELECT (testColA, testColB), INSERT ON `testDb`.`testTable` TO 'testUser'@'localhost';
    Query OK, 0 rows affected (0.04 sec)

    mysql> flush privileges;
    Query OK, 0 rows affected (0.00 sec)

    mysql> SHOW GRANTS FOR testUser@localhost;
    +---------------------------------------------------------------------------------------------+
    | Grants for testUser@localhost                                                               |
    +---------------------------------------------------------------------------------------------+
    | GRANT USAGE ON *.* TO 'testUser'@'localhost'                                                |
    | GRANT SELECT (testColB, testColA), INSERT ON `testDb`.`testTable` TO 'testUser'@'localhost' |
    +---------------------------------------------------------------------------------------------+

    We should sort columns in our statement, otherwise the module always will return
    that the state has changed.
    """
    # 1. Extract stuff inside ()
    # 2. Split
    # 3. Sort
    # 4. Put between () and return

    # "SELECT/UPDATE/.. (colA, colB) => "colA, colB"
    tmp = statement.split('(')
    priv_name = tmp[0]
    columns = tmp[1].rstrip(')')

    # "colA, colB" => ["colA", "colB"]
    columns = columns.split(',')

    for i, col in enumerate(columns):
        col = col.strip()
        columns[i] = col.strip('`')

    columns.sort()
    return '%s(%s)' % (priv_name, ', '.join(columns))


def privileges_unpack(priv, mode):
    """ Take a privileges string, typically passed as a parameter, and unserialize
    it into a dictionary, the same format as privileges_get() above. We have this
    custom format to avoid using YAML/JSON strings inside YAML playbooks. Example
    of a privileges string:

     mydb.*:INSERT,UPDATE/anotherdb.*:SELECT/yetanother.*:ALL

    The privilege USAGE stands for no privileges, so we add that in on *.* if it's
    not specified in the string, as MySQL will always provide this by default.
    """
    if mode == 'ANSI':
        quote = '"'
    else:
        quote = '`'
    output = {}
    privs = []
    for item in priv.strip().split('/'):
        pieces = item.strip().rsplit(':', 1)
        dbpriv = pieces[0].rsplit(".", 1)

        # Check for FUNCTION or PROCEDURE object types
        parts = dbpriv[0].split(" ", 1)
        object_type = ''
        if len(parts) > 1 and (parts[0] == 'FUNCTION' or parts[0] == 'PROCEDURE'):
            object_type = parts[0] + ' '
            dbpriv[0] = parts[1]

        # Do not escape if privilege is for database or table, i.e.
        # neither quote *. nor .*
        for i, side in enumerate(dbpriv):
            if side.strip('`') != '*':
                dbpriv[i] = '%s%s%s' % (quote, side.strip('`'), quote)
        pieces[0] = object_type + '.'.join(dbpriv)

        if '(' in pieces[1]:
            output[pieces[0]] = re.split(r',\s*(?=[^)]*(?:\(|$))', pieces[1].upper())
            for i in output[pieces[0]]:
                privs.append(re.sub(r'\s*\(.*\)', '', i))
        else:
            output[pieces[0]] = pieces[1].upper().split(',')
            privs = output[pieces[0]]

        # Handle cases when there's privs like GRANT SELECT (colA, ...) in privs.
        output[pieces[0]] = normalize_col_grants(output[pieces[0]])

        new_privs = frozenset(privs)
        if not new_privs.issubset(VALID_PRIVS):
            raise InvalidPrivsError('Invalid privileges specified: %s' % new_privs.difference(VALID_PRIVS))

    if '*.*' not in output:
        output['*.*'] = ['USAGE']

    return output


def privileges_revoke(cursor, user, host, db_table, priv, grant_option):
    # Escape '%' since mysql db.execute() uses a format string
    db_table = db_table.replace('%', '%%')
    if grant_option:
        query = ["REVOKE GRANT OPTION ON %s" % db_table]
        query.append("FROM %s@%s")
        query = ' '.join(query)
        cursor.execute(query, (user, host))
    priv_string = ",".join([p for p in priv if p not in ('GRANT', )])
    query = ["REVOKE %s ON %s" % (priv_string, db_table)]
    query.append("FROM %s@%s")
    query = ' '.join(query)
    cursor.execute(query, (user, host))


def privileges_grant(cursor, user, host, db_table, priv, tls_requires):
    # Escape '%' since mysql db.execute uses a format string and the
    # specification of db and table often use a % (SQL wildcard)
    db_table = db_table.replace('%', '%%')
    priv_string = ",".join([p for p in priv if p not in ('GRANT', )])
    query = ["GRANT %s ON %s" % (priv_string, db_table)]
    query.append("TO %s@%s")
    params = (user, host)
    if tls_requires and impl.use_old_user_mgmt(cursor):
        query, params = mogrify_requires(" ".join(query), params, tls_requires)
        query = [query]
    if 'GRANT' in priv:
        query.append("WITH GRANT OPTION")
    query = ' '.join(query)
    cursor.execute(query, params)


def convert_priv_dict_to_str(priv):
    """Converts privs dictionary to string of certain format.

    Args:
        priv (dict): Dict of privileges that needs to be converted to string.

    Returns:
        priv (str): String representation of input argument.
    """
    priv_list = ['%s:%s' % (key, val) for key, val in iteritems(priv)]

    return '/'.join(priv_list)


def handle_requiressl_in_priv_string(module, priv, tls_requires):
    module.deprecate('The "REQUIRESSL" privilege is deprecated, use the "tls_requires" option instead.',
                     version='3.0.0', collection_name='community.mysql')
    priv_groups = re.search(r"(.*?)(\*\.\*:)([^/]*)(.*)", priv)
    if priv_groups.group(3) == "REQUIRESSL":
        priv = priv_groups.group(1) + priv_groups.group(4) or None
    else:
        inner_priv_groups = re.search(r"(.*?),?REQUIRESSL,?(.*)", priv_groups.group(3))
        priv = '{0}{1}{2}{3}'.format(
            priv_groups.group(1),
            priv_groups.group(2),
            ','.join(filter(None, (inner_priv_groups.group(1), inner_priv_groups.group(2)))),
            priv_groups.group(4)
        )
    if not tls_requires:
        tls_requires = "SSL"
    else:
        module.warn('Ignoring "REQUIRESSL" privilege as "tls_requires" is defined and it takes precedence.')
    return priv, tls_requires


# Alter user is supported since MySQL 5.6 and MariaDB 10.2.0
def server_supports_alter_user(cursor):
    """Check if the server supports ALTER USER statement or doesn't.

    Args:
        cursor (cursor): DB driver cursor object.

    Returns: True if supports, False otherwise.
    """
    cursor.execute("SELECT VERSION()")
    version_str = cursor.fetchone()[0]
    version = version_str.split('.')

    if 'mariadb' in version_str.lower():
        # MariaDB 10.2 and later
        if int(version[0]) * 1000 + int(version[1]) >= 10002:
            return True
        else:
            return False
    else:
        # MySQL 5.6 and later
        if int(version[0]) * 1000 + int(version[1]) >= 5006:
            return True
        else:
            return False


def get_resource_limits(cursor, user, host):
    """Get user resource limits.

    Args:
        cursor (cursor): DB driver cursor object.
        user (str): User name.
        host (str): User host name.

    Returns: Dictionary containing current resource limits.
    """

    query = ('SELECT max_questions AS MAX_QUERIES_PER_HOUR, '
             'max_updates AS MAX_UPDATES_PER_HOUR, '
             'max_connections AS MAX_CONNECTIONS_PER_HOUR, '
             'max_user_connections AS MAX_USER_CONNECTIONS '
             'FROM mysql.user WHERE User = %s AND Host = %s')
    cursor.execute(query, (user, host))
    res = cursor.fetchone()

    if not res:
        return None

    current_limits = {
        'MAX_QUERIES_PER_HOUR': res[0],
        'MAX_UPDATES_PER_HOUR': res[1],
        'MAX_CONNECTIONS_PER_HOUR': res[2],
        'MAX_USER_CONNECTIONS': res[3],
    }
    return current_limits


def match_resource_limits(module, current, desired):
    """Check and match limits.

    Args:
        module (AnsibleModule): Ansible module object.
        current (dict): Dictionary with current limits.
        desired (dict): Dictionary with desired limits.

    Returns: Dictionary containing parameters that need to change.
    """

    if not current:
        # It means the user does not exists, so we need
        # to set all limits after its creation
        return desired

    needs_to_change = {}

    for key, val in iteritems(desired):
        if key not in current:
            # Supported keys are listed in the documentation
            # and must be determined in the get_resource_limits function
            # (follow 'AS' keyword)
            module.fail_json(msg="resource_limits: key '%s' is unsupported." % key)

        try:
            val = int(val)
        except Exception:
            module.fail_json(msg="Can't convert value '%s' to integer." % val)

        if val != current.get(key):
            needs_to_change[key] = val

    return needs_to_change


def limit_resources(module, cursor, user, host, resource_limits, check_mode):
    """Limit user resources.

    Args:
        module (AnsibleModule): Ansible module object.
        cursor (cursor): DB driver cursor object.
        user (str): User name.
        host (str): User host name.
        resource_limit (dict): Dictionary with desired limits.
        check_mode (bool): Run the function in check mode or not.

    Returns: True, if changed, False otherwise.
    """
    if not server_supports_alter_user(cursor):
        module.fail_json(msg="The server version does not match the requirements "
                             "for resource_limits parameter. See module's documentation.")

    current_limits = get_resource_limits(cursor, user, host)

    needs_to_change = match_resource_limits(module, current_limits, resource_limits)

    if not needs_to_change:
        return False

    if needs_to_change and check_mode:
        return True

    # If not check_mode
    tmp = []
    for key, val in iteritems(needs_to_change):
        tmp.append('%s %s' % (key, val))

    query = "ALTER USER %s@%s"
    query += ' WITH %s' % ' '.join(tmp)
    cursor.execute(query, (user, host))
    return True


# ===========================================
# Module execution.
#


def main():
    argument_spec = mysql_common_argument_spec()
    argument_spec.update(
        user=dict(type='str', required=True, aliases=['name']),
        password=dict(type='str', no_log=True),
        encrypted=dict(type='bool', default=False),
        host=dict(type='str', default='localhost'),
        host_all=dict(type="bool", default=False),
        state=dict(type='str', default='present', choices=['absent', 'present']),
        priv=dict(type='raw'),
        tls_requires=dict(type='dict'),
        append_privs=dict(type='bool', default=False),
        check_implicit_admin=dict(type='bool', default=False),
        update_password=dict(type='str', default='always', choices=['always', 'on_create'], no_log=False),
        sql_log_bin=dict(type='bool', default=True),
        plugin=dict(default=None, type='str'),
        plugin_hash_string=dict(default=None, type='str'),
        plugin_auth_string=dict(default=None, type='str'),
        resource_limits=dict(type='dict'),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    login_user = module.params["login_user"]
    login_password = module.params["login_password"]
    user = module.params["user"]
    password = module.params["password"]
    encrypted = module.boolean(module.params["encrypted"])
    host = module.params["host"].lower()
    host_all = module.params["host_all"]
    state = module.params["state"]
    priv = module.params["priv"]
    tls_requires = sanitize_requires(module.params["tls_requires"])
    check_implicit_admin = module.params["check_implicit_admin"]
    connect_timeout = module.params["connect_timeout"]
    config_file = module.params["config_file"]
    append_privs = module.boolean(module.params["append_privs"])
    update_password = module.params['update_password']
    ssl_cert = module.params["client_cert"]
    ssl_key = module.params["client_key"]
    ssl_ca = module.params["ca_cert"]
    check_hostname = module.params["check_hostname"]
    db = ''
    sql_log_bin = module.params["sql_log_bin"]
    plugin = module.params["plugin"]
    plugin_hash_string = module.params["plugin_hash_string"]
    plugin_auth_string = module.params["plugin_auth_string"]
    resource_limits = module.params["resource_limits"]
    if priv and not isinstance(priv, (str, dict)):
        module.fail_json(msg="priv parameter must be str or dict but %s was passed" % type(priv))

    if priv and isinstance(priv, dict):
        priv = convert_priv_dict_to_str(priv)

    if priv and "REQUIRESSL" in priv:
        priv, tls_requires = handle_requiressl_in_priv_string(module, priv, tls_requires)

    if mysql_driver is None:
        module.fail_json(msg=mysql_driver_fail_msg)

    cursor = None
    try:
        if check_implicit_admin:
            try:
                cursor, db_conn = mysql_connect(module, "root", "", config_file, ssl_cert, ssl_key, ssl_ca, db,
                                                connect_timeout=connect_timeout, check_hostname=check_hostname)
            except Exception:
                pass

        if not cursor:
            cursor, db_conn = mysql_connect(module, login_user, login_password, config_file, ssl_cert, ssl_key, ssl_ca, db,
                                            connect_timeout=connect_timeout, check_hostname=check_hostname)
    except Exception as e:
        module.fail_json(msg="unable to connect to database, check login_user and login_password are correct or %s has the credentials. "
                             "Exception message: %s" % (config_file, to_native(e)))

    if not sql_log_bin:
        cursor.execute("SET SQL_LOG_BIN=0;")

    global impl
    cursor.execute("SELECT VERSION()")
    if 'mariadb' in cursor.fetchone()[0].lower():
        from ansible_collections.community.mysql.plugins.module_utils.implementations.mariadb import user as mysqluser
        impl = mysqluser
    else:
        from ansible_collections.community.mysql.plugins.module_utils.implementations.mysql import user as mariauser
        impl = mariauser

    if priv is not None:
        try:
            mode = get_mode(cursor)
        except Exception as e:
            module.fail_json(msg=to_native(e))
        try:
            priv = privileges_unpack(priv, mode)
        except Exception as e:
            module.fail_json(msg="invalid privileges string: %s" % to_native(e))

    if state == "present":
        if user_exists(cursor, user, host, host_all):
            try:
                if update_password == "always":
                    changed, msg = user_mod(cursor, user, host, host_all, password, encrypted,
                                            plugin, plugin_hash_string, plugin_auth_string,
                                            priv, append_privs, tls_requires, module)
                else:
                    changed, msg = user_mod(cursor, user, host, host_all, None, encrypted,
                                            plugin, plugin_hash_string, plugin_auth_string,
                                            priv, append_privs, tls_requires, module)

            except (SQLParseError, InvalidPrivsError, mysql_driver.Error) as e:
                module.fail_json(msg=to_native(e))
        else:
            if host_all:
                module.fail_json(msg="host_all parameter cannot be used when adding a user")
            try:
                changed = user_add(cursor, user, host, host_all, password, encrypted,
                                   plugin, plugin_hash_string, plugin_auth_string,
                                   priv, tls_requires, module.check_mode)
                if changed:
                    msg = "User added"

            except (SQLParseError, InvalidPrivsError, mysql_driver.Error) as e:
                module.fail_json(msg=to_native(e))

        if resource_limits:
            changed = limit_resources(module, cursor, user, host, resource_limits, module.check_mode) or changed

    elif state == "absent":
        if user_exists(cursor, user, host, host_all):
            changed = user_delete(cursor, user, host, host_all, module.check_mode)
            msg = "User deleted"
        else:
            changed = False
            msg = "User doesn't exist"
    module.exit_json(changed=changed, user=user, msg=msg)


if __name__ == '__main__':
    main()
