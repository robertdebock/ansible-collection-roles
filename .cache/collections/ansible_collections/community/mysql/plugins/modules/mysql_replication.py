#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2013, Balazs Pocze <banyek@gawker.com>
# Copyright: (c) 2019, Andrew Klychkov (@Andersson007) <aaklychkov@mail.ru>
# Certain parts are taken from Mark Theunissen's mysqldb module
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
---
module: mysql_replication
short_description: Manage MySQL replication
description:
- Manages MySQL server replication, replica, master status, get and change master host.
author:
- Balazs Pocze (@banyek)
- Andrew Klychkov (@Andersson007)
options:
  mode:
    description:
    - Module operating mode. Could be
      C(changemaster) (CHANGE MASTER TO),
      C(getmaster) (SHOW MASTER STATUS),
      C(getreplica | getslave) (SHOW REPLICA | SLAVE STATUS),
      C(startreplica | startslave) (START REPLICA | SLAVE),
      C(stopreplica | stopslave) (STOP REPLICA | SLAVE),
      C(resetmaster) (RESET MASTER) - supported since community.mysql 0.1.0,
      C(resetreplica, resetslave) (RESET REPLICA | SLAVE),
      C(resetreplicaall, resetslave) (RESET REPLICA | SLAVE ALL).
    type: str
    choices:
    - changemaster
    - getmaster
    - getreplica
    - getslave
    - startreplica
    - startslave
    - stopreplica
    - stopslave
    - resetmaster
    - resetreplica
    - resetslave
    - resetreplicaall
    - resetslaveall
    default: getreplica
  master_host:
    description:
    - Same as mysql variable.
    type: str
  master_user:
    description:
    - Same as mysql variable.
    type: str
  master_password:
    description:
    - Same as mysql variable.
    type: str
  master_port:
    description:
    - Same as mysql variable.
    type: int
  master_connect_retry:
    description:
    - Same as mysql variable.
    type: int
  master_log_file:
    description:
    - Same as mysql variable.
    type: str
  master_log_pos:
    description:
    - Same as mysql variable.
    type: int
  relay_log_file:
    description:
    - Same as mysql variable.
    type: str
  relay_log_pos:
    description:
    - Same as mysql variable.
    type: int
  master_ssl:
    description:
    - Same as the C(MASTER_SSL) mysql variable.
    - When setting it to C(yes), the connection attempt only succeeds
      if an encrypted connection can be established.
    - For details, refer to
      L(MySQL encrypted replication documentation,https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).
    type: bool
    default: false
  master_ssl_ca:
    description:
    - Same as the C(MASTER_SSL_CA) mysql variable.
    - For details, refer to
      L(MySQL encrypted replication documentation,https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).
    type: str
  master_ssl_capath:
    description:
    - Same as the C(MASTER_SSL_CAPATH) mysql variable.
    - For details, refer to
      L(MySQL encrypted replication documentation,https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).
    type: str
  master_ssl_cert:
    description:
    - Same as the C(MASTER_SSL_CERT) mysql variable.
    - For details, refer to
      L(MySQL encrypted replication documentation,https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).
    type: str
  master_ssl_key:
    description:
    - Same as the C(MASTER_SSL_KEY) mysql variable.
    - For details, refer to
      L(MySQL encrypted replication documentation,https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).
    type: str
  master_ssl_cipher:
    description:
    - Same as the C(MASTER_SSL_CIPHER) mysql variable.
    - Specifies a colon-separated list of one or more ciphers permitted by the replica for the replication connection.
    - For details, refer to
      L(MySQL encrypted replication documentation,https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html).
    type: str
  master_auto_position:
    description:
    - Whether the host uses GTID based replication or not.
    type: bool
    default: false
  master_use_gtid:
    description:
    - Configures the replica to use the MariaDB Global Transaction ID.
    - C(disabled) equals MASTER_USE_GTID=no command.
    - To find information about available values see
      U(https://mariadb.com/kb/en/library/change-master-to/#master_use_gtid).
    - Available since MariaDB 10.0.2.
    - C(replica_pos) has been introduced in MariaDB 10.5.1 and
      it is an alias for C(slave_pos).
    choices: [current_pos, replica_pos, slave_pos, disabled]
    type: str
    version_added: '0.1.0'
  master_delay:
    description:
    - Time lag behind the master's state (in seconds).
    - Available from MySQL 5.6.
    - For more information see U(https://dev.mysql.com/doc/refman/8.0/en/replication-delayed.html).
    type: int
    version_added: '0.1.0'
  connection_name:
    description:
    - Name of the master connection.
    - Supported from MariaDB 10.0.1.
    - Mutually exclusive with I(channel).
    - For more information see U(https://mariadb.com/kb/en/library/multi-source-replication/).
    type: str
    version_added: '0.1.0'
  channel:
    description:
    - Name of replication channel.
    - Multi-source replication is supported from MySQL 5.7.
    - Mutually exclusive with I(connection_name).
    - For more information see U(https://dev.mysql.com/doc/refman/8.0/en/replication-multi-source.html).
    type: str
    version_added: '0.1.0'
  fail_on_error:
    description:
    - Fails on error when calling mysql.
    type: bool
    default: False
    version_added: '0.1.0'

notes:
- If an empty value for the parameter of string type is needed, use an empty string.

extends_documentation_fragment:
- community.mysql.mysql


seealso:
- module: community.mysql.mysql_info
- name: MySQL replication reference
  description: Complete reference of the MySQL replication documentation.
  link: https://dev.mysql.com/doc/refman/8.0/en/replication.html
- name: MySQL encrypted replication reference.
  description: Setting up MySQL replication to use encrypted connection.
  link: https://dev.mysql.com/doc/refman/8.0/en/replication-solutions-encrypted-connections.html
- name: MariaDB replication reference
  description: Complete reference of the MariaDB replication documentation.
  link: https://mariadb.com/kb/en/library/setting-up-replication/
'''

EXAMPLES = r'''
- name: Stop mysql replica thread
  community.mysql.mysql_replication:
    mode: stopreplica

- name: Get master binlog file name and binlog position
  community.mysql.mysql_replication:
    mode: getmaster

- name: Change master to master server 192.0.2.1 and use binary log 'mysql-bin.000009' with position 4578
  community.mysql.mysql_replication:
    mode: changemaster
    master_host: 192.0.2.1
    master_log_file: mysql-bin.000009
    master_log_pos: 4578

- name: Check replica status using port 3308
  community.mysql.mysql_replication:
    mode: getreplica
    login_host: ansible.example.com
    login_port: 3308

- name: On MariaDB change master to use GTID current_pos
  community.mysql.mysql_replication:
    mode: changemaster
    master_use_gtid: current_pos

- name: Change master to use replication delay 3600 seconds
  community.mysql.mysql_replication:
    mode: changemaster
    master_host: 192.0.2.1
    master_delay: 3600

- name: Start MariaDB replica with connection name master-1
  community.mysql.mysql_replication:
    mode: startreplica
    connection_name: master-1

- name: Stop replication in channel master-1
  community.mysql.mysql_replication:
    mode: stopreplica
    channel: master-1

- name: >
    Run RESET MASTER command which will delete all existing binary log files
    and reset the binary log index file on the master
  community.mysql.mysql_replication:
    mode: resetmaster

- name: Run start replica and fail the task on errors
  community.mysql.mysql_replication:
    mode: startreplica
    connection_name: master-1
    fail_on_error: yes

- name: Change master and fail on error (like when replica thread is running)
  community.mysql.mysql_replication:
    mode: changemaster
    fail_on_error: yes

'''

RETURN = r'''
queries:
  description: List of executed queries which modified DB's state.
  returned: always
  type: list
  sample: ["CHANGE MASTER TO MASTER_HOST='master2.example.com',MASTER_PORT=3306"]
  version_added: '0.1.0'
'''

import os
import warnings

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.mysql.plugins.module_utils.mysql import (
    mysql_connect,
    mysql_driver,
    mysql_driver_fail_msg,
    mysql_common_argument_spec,
)
from ansible.module_utils._text import to_native
from distutils.version import LooseVersion

executed_queries = []


def get_master_status(cursor):
    cursor.execute("SHOW MASTER STATUS")
    masterstatus = cursor.fetchone()
    return masterstatus


def get_replica_status(cursor, connection_name='', channel='', term='REPLICA'):
    if connection_name:
        query = "SHOW %s '%s' STATUS" % (term, connection_name)
    else:
        query = "SHOW %s STATUS" % term

    if channel:
        query += " FOR CHANNEL '%s'" % channel

    cursor.execute(query)
    replica_status = cursor.fetchone()
    return replica_status


def stop_replica(module, cursor, connection_name='', channel='', fail_on_error=False, term='REPLICA'):
    if connection_name:
        query = "STOP %s '%s'" % (term, connection_name)
    else:
        query = 'STOP %s' % term

    if channel:
        query += " FOR CHANNEL '%s'" % channel

    try:
        executed_queries.append(query)
        cursor.execute(query)
        stopped = True
    except mysql_driver.Warning as e:
        stopped = False
    except Exception as e:
        if fail_on_error:
            module.fail_json(msg="STOP REPLICA failed: %s" % to_native(e))
        stopped = False
    return stopped


def reset_replica(module, cursor, connection_name='', channel='', fail_on_error=False, term='REPLICA'):
    if connection_name:
        query = "RESET %s '%s'" % (term, connection_name)
    else:
        query = 'RESET %s' % term

    if channel:
        query += " FOR CHANNEL '%s'" % channel

    try:
        executed_queries.append(query)
        cursor.execute(query)
        reset = True
    except mysql_driver.Warning as e:
        reset = False
    except Exception as e:
        if fail_on_error:
            module.fail_json(msg="RESET REPLICA failed: %s" % to_native(e))
        reset = False
    return reset


def reset_replica_all(module, cursor, connection_name='', channel='', fail_on_error=False, term='REPLICA'):
    if connection_name:
        query = "RESET %s '%s' ALL" % (term, connection_name)
    else:
        query = 'RESET %s ALL' % term

    if channel:
        query += " FOR CHANNEL '%s'" % channel

    try:
        executed_queries.append(query)
        cursor.execute(query)
        reset = True
    except mysql_driver.Warning as e:
        reset = False
    except Exception as e:
        if fail_on_error:
            module.fail_json(msg="RESET REPLICA ALL failed: %s" % to_native(e))
        reset = False
    return reset


def reset_master(module, cursor, fail_on_error=False):
    query = 'RESET MASTER'
    try:
        executed_queries.append(query)
        cursor.execute(query)
        reset = True
    except mysql_driver.Warning as e:
        reset = False
    except Exception as e:
        if fail_on_error:
            module.fail_json(msg="RESET MASTER failed: %s" % to_native(e))
        reset = False
    return reset


def start_replica(module, cursor, connection_name='', channel='', fail_on_error=False, term='REPLICA'):
    if connection_name:
        query = "START %s '%s'" % (term, connection_name)
    else:
        query = 'START %s' % term

    if channel:
        query += " FOR CHANNEL '%s'" % channel

    try:
        executed_queries.append(query)
        cursor.execute(query)
        started = True
    except mysql_driver.Warning as e:
        started = False
    except Exception as e:
        if fail_on_error:
            module.fail_json(msg="START REPLICA failed: %s" % to_native(e))
        started = False
    return started


def changemaster(cursor, chm, connection_name='', channel=''):
    if connection_name:
        query = "CHANGE MASTER '%s' TO %s" % (connection_name, ','.join(chm))
    else:
        query = 'CHANGE MASTER TO %s' % ','.join(chm)

    if channel:
        query += " FOR CHANNEL '%s'" % channel

    executed_queries.append(query)
    cursor.execute(query)


def main():
    argument_spec = mysql_common_argument_spec()
    argument_spec.update(
        mode=dict(type='str', default='getreplica', choices=[
            'getmaster', 'getreplica', 'getslave', 'changemaster',
            'stopreplica', 'stopslave', 'startreplica', 'startslave',
            'resetmaster', 'resetreplica', 'resetslave',
            'resetreplicaall', 'resetslaveall']),
        master_auto_position=dict(type='bool', default=False),
        master_host=dict(type='str'),
        master_user=dict(type='str'),
        master_password=dict(type='str', no_log=True),
        master_port=dict(type='int'),
        master_connect_retry=dict(type='int'),
        master_log_file=dict(type='str'),
        master_log_pos=dict(type='int'),
        relay_log_file=dict(type='str'),
        relay_log_pos=dict(type='int'),
        master_ssl=dict(type='bool', default=False),
        master_ssl_ca=dict(type='str'),
        master_ssl_capath=dict(type='str'),
        master_ssl_cert=dict(type='str'),
        master_ssl_key=dict(type='str', no_log=False),
        master_ssl_cipher=dict(type='str'),
        master_use_gtid=dict(type='str', choices=[
            'current_pos', 'replica_pos', 'slave_pos', 'disabled']),
        master_delay=dict(type='int'),
        connection_name=dict(type='str'),
        channel=dict(type='str'),
        fail_on_error=dict(type='bool', default=False),
    )
    module = AnsibleModule(
        argument_spec=argument_spec,
        mutually_exclusive=[
            ['connection_name', 'channel']
        ],
    )
    mode = module.params["mode"]
    master_host = module.params["master_host"]
    master_user = module.params["master_user"]
    master_password = module.params["master_password"]
    master_port = module.params["master_port"]
    master_connect_retry = module.params["master_connect_retry"]
    master_log_file = module.params["master_log_file"]
    master_log_pos = module.params["master_log_pos"]
    relay_log_file = module.params["relay_log_file"]
    relay_log_pos = module.params["relay_log_pos"]
    master_ssl = module.params["master_ssl"]
    master_ssl_ca = module.params["master_ssl_ca"]
    master_ssl_capath = module.params["master_ssl_capath"]
    master_ssl_cert = module.params["master_ssl_cert"]
    master_ssl_key = module.params["master_ssl_key"]
    master_ssl_cipher = module.params["master_ssl_cipher"]
    master_auto_position = module.params["master_auto_position"]
    ssl_cert = module.params["client_cert"]
    ssl_key = module.params["client_key"]
    ssl_ca = module.params["ca_cert"]
    check_hostname = module.params["check_hostname"]
    connect_timeout = module.params['connect_timeout']
    config_file = module.params['config_file']
    master_delay = module.params['master_delay']
    if module.params.get("master_use_gtid") == 'disabled':
        master_use_gtid = 'no'
    else:
        master_use_gtid = module.params["master_use_gtid"]
    connection_name = module.params["connection_name"]
    channel = module.params['channel']
    fail_on_error = module.params['fail_on_error']

    if mysql_driver is None:
        module.fail_json(msg=mysql_driver_fail_msg)
    else:
        warnings.filterwarnings('error', category=mysql_driver.Warning)

    login_password = module.params["login_password"]
    login_user = module.params["login_user"]

    try:
        cursor, db_conn = mysql_connect(module, login_user, login_password, config_file,
                                        ssl_cert, ssl_key, ssl_ca, None, cursor_class='DictCursor',
                                        connect_timeout=connect_timeout, check_hostname=check_hostname)
    except Exception as e:
        if os.path.exists(config_file):
            module.fail_json(msg="unable to connect to database, check login_user and "
                                 "login_password are correct or %s has the credentials. "
                                 "Exception message: %s" % (config_file, to_native(e)))
        else:
            module.fail_json(msg="unable to find %s. Exception message: %s" % (config_file, to_native(e)))

    cursor.execute("SELECT VERSION()")
    if 'mariadb' in cursor.fetchone()["VERSION()"].lower():
        from ansible_collections.community.mysql.plugins.module_utils.implementations.mariadb import replication as impl
    else:
        from ansible_collections.community.mysql.plugins.module_utils.implementations.mysql import replication as impl

    # Since MySQL 8.0.22 and MariaDB 10.5.1,
    # "REPLICA" must be used instead of "SLAVE"
    if impl.uses_replica_terminology(cursor):
        replica_term = 'REPLICA'
        if master_use_gtid == 'slave_pos':
            module.deprecate('master_use_gtid "slave_pos" value is deprecated, use "replica_pos" instead.',
                             version='3.0.0', collection_name='community.mysql')
            master_use_gtid = 'replica_pos'
    else:
        replica_term = 'SLAVE'
        if master_use_gtid == 'replica_pos':
            master_use_gtid = 'slave_pos'

    if mode in "getmaster":
        status = get_master_status(cursor)
        if not isinstance(status, dict):
            status = dict(Is_Master=False, msg="Server is not configured as mysql master")
        else:
            status['Is_Master'] = True
        module.exit_json(queries=executed_queries, **status)

    elif mode in ("getreplica", "getslave"):
        if mode == "getslave":
            module.deprecate('"getslave" option is deprecated, use "getreplica" instead.',
                             version='3.0.0', collection_name='community.mysql')

        status = get_replica_status(cursor, connection_name, channel, replica_term)
        if not isinstance(status, dict):
            # TODO: announce it and replace with Replica
            # in the next major release. Maybe a warning?
            status = dict(Is_Slave=False, msg="Server is not configured as mysql replica")
        else:
            # TODO: announce it and replace with Replica
            # in the next major release. Maybe a warning?
            status['Is_Slave'] = True
        module.exit_json(queries=executed_queries, **status)

    elif mode in "changemaster":
        chm = []
        result = {}
        if master_host is not None:
            chm.append("MASTER_HOST='%s'" % master_host)
        if master_user is not None:
            chm.append("MASTER_USER='%s'" % master_user)
        if master_password is not None:
            chm.append("MASTER_PASSWORD='%s'" % master_password)
        if master_port is not None:
            chm.append("MASTER_PORT=%s" % master_port)
        if master_connect_retry is not None:
            chm.append("MASTER_CONNECT_RETRY=%s" % master_connect_retry)
        if master_log_file is not None:
            chm.append("MASTER_LOG_FILE='%s'" % master_log_file)
        if master_log_pos is not None:
            chm.append("MASTER_LOG_POS=%s" % master_log_pos)
        if master_delay is not None:
            chm.append("MASTER_DELAY=%s" % master_delay)
        if relay_log_file is not None:
            chm.append("RELAY_LOG_FILE='%s'" % relay_log_file)
        if relay_log_pos is not None:
            chm.append("RELAY_LOG_POS=%s" % relay_log_pos)
        if master_ssl:
            chm.append("MASTER_SSL=1")
        if master_ssl_ca is not None:
            chm.append("MASTER_SSL_CA='%s'" % master_ssl_ca)
        if master_ssl_capath is not None:
            chm.append("MASTER_SSL_CAPATH='%s'" % master_ssl_capath)
        if master_ssl_cert is not None:
            chm.append("MASTER_SSL_CERT='%s'" % master_ssl_cert)
        if master_ssl_key is not None:
            chm.append("MASTER_SSL_KEY='%s'" % master_ssl_key)
        if master_ssl_cipher is not None:
            chm.append("MASTER_SSL_CIPHER='%s'" % master_ssl_cipher)
        if master_auto_position:
            chm.append("MASTER_AUTO_POSITION=1")
        if master_use_gtid is not None:
            chm.append("MASTER_USE_GTID=%s" % master_use_gtid)
        try:
            changemaster(cursor, chm, connection_name, channel)
        except mysql_driver.Warning as e:
            result['warning'] = to_native(e)
        except Exception as e:
            module.fail_json(msg='%s. Query == CHANGE MASTER TO %s' % (to_native(e), chm))
        result['changed'] = True
        module.exit_json(queries=executed_queries, **result)
    elif mode in ("startreplica", "startslave"):
        if mode == "startslave":
            module.deprecate('"startslave" option is deprecated, use "startreplica" instead.',
                             version='3.0.0', collection_name='community.mysql')

        started = start_replica(module, cursor, connection_name, channel, fail_on_error, replica_term)
        if started is True:
            module.exit_json(msg="Replica started ", changed=True, queries=executed_queries)
        else:
            module.exit_json(msg="Replica already started (Or cannot be started)", changed=False, queries=executed_queries)
    elif mode in ("stopreplica", "stopslave"):
        if mode == "stopslave":
            module.deprecate('"stopslave" option is deprecated, use "stopreplica" instead.',
                             version='3.0.0', collection_name='community.mysql')

        stopped = stop_replica(module, cursor, connection_name, channel, fail_on_error, replica_term)
        if stopped is True:
            module.exit_json(msg="Replica stopped", changed=True, queries=executed_queries)
        else:
            module.exit_json(msg="Replica already stopped", changed=False, queries=executed_queries)
    elif mode in "resetmaster":
        reset = reset_master(module, cursor, fail_on_error)
        if reset is True:
            module.exit_json(msg="Master reset", changed=True, queries=executed_queries)
        else:
            module.exit_json(msg="Master already reset", changed=False, queries=executed_queries)
    elif mode in ("resetreplica", "resetslave"):
        if mode == "resetslave":
            module.deprecate('"resetslave" option is deprecated, use "resetreplica" instead.',
                             version='3.0.0', collection_name='community.mysql')

        reset = reset_replica(module, cursor, connection_name, channel, fail_on_error, replica_term)
        if reset is True:
            module.exit_json(msg="Replica reset", changed=True, queries=executed_queries)
        else:
            module.exit_json(msg="Replica already reset", changed=False, queries=executed_queries)
    elif mode in ("resetreplicaall", "resetslaveall"):
        if mode == "resetslaveall":
            module.deprecate('"resetslaveall" option is deprecated, use "resetreplicaall" instead.',
                             version='3.0.0', collection_name='community.mysql')

        reset = reset_replica_all(module, cursor, connection_name, channel, fail_on_error, replica_term)
        if reset is True:
            module.exit_json(msg="Replica reset", changed=True, queries=executed_queries)
        else:
            module.exit_json(msg="Replica already reset", changed=False, queries=executed_queries)

    warnings.simplefilter("ignore")


if __name__ == '__main__':
    main()
