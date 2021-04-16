========================================
Community MySQL Collection Release Notes
========================================

.. contents:: Topics


v2.0.0
======

Release Summary
---------------

This is release 2.0.0 of the ``community.mysql`` collection, released on 2021-04-15.

Major Changes
-------------

- mysql_replication - the return value ``Is_Slave`` and ``Is_Master`` will be replaced with ``Is_Replica`` and ``Is_Primary`` in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/145).
- mysql_replication - the word ``master`` in messages returned by the module will be replaced with ``primary`` in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/145).
- mysql_replication - the word ``slave`` in messages returned by the module replaced with ``replica`` (https://github.com/ansible-collections/community.mysql/issues/98).
- mysql_user - the ``REQUIRESSL`` is an alias for the ``ssl`` key in the ``tls_requires`` option in ``community.mysql`` 2.0.0 and support will be dropped altogether in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/issues/121).

Minor Changes
-------------

- mysql module utils - change deprecated connection parameters ``passwd`` and ``db`` to ``password`` and ``database`` (https://github.com/ansible-collections/community.mysql/pull/116).
- mysql_collection - introduce codebabse split to handle divergences between MySQL and MariaDB (https://github.com/ansible-collections/community.mysql/pull/103).
- mysql_info - add `version.full` and `version.suffix` return values (https://github.com/ansible-collections/community.mysql/issues/114).
- mysql_user - deprecate the ``REQUIRESSL`` privilege (https://github.com/ansible-collections/community.mysql/issues/101).

Bugfixes
--------

- mysql_user - add support for ``REPLICA MONITOR`` privilege (https://github.com/ansible-collections/community.mysql/issues/105).

v1.3.0
======

Release Summary
---------------

This is the minor release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection
that have been added after the release of ``community.mysql`` 1.2.0.

Major Changes
-------------

- mysql_replication - the mode options values ``getslave``, ``startslave``, ``stopslave``, ``resetslave``, ``resetslaveall` and the master_use_gtid option ``slave_pos`` are deprecated (see the alternative values) and will be removed in ``community.mysql`` 3.0.0 (https://github.com/ansible-collections/community.mysql/pull/97).
- mysql_replication - the word ``SLAVE`` in messages returned by the module will be changed to ``REPLICA`` in ``community.mysql`` 2.0.0 (https://github.com/ansible-collections/community.mysql/issues/98).

Minor Changes
-------------

- mysql_replication - deprecate offending terminology, add alternative choices to the ``mode`` option (https://github.com/ansible-collections/community.mysql/issues/78).

Bugfixes
--------

- mysql_user - fix handling of INSERT, UPDATE, REFERENCES on columns (https://github.com/ansible-collections/community.mysql/issues/106).
- mysql_user - the module is not idempotent when SELECT on columns granted (https://github.com/ansible-collections/community.mysql/issues/99).

v1.2.0
======

Release Summary
---------------

This is the minor release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection
that have been added after the release of ``community.mysql`` 1.1.2.

Minor Changes
-------------

- mysql_user - refactor to reduce cursor.execute() calls in preparation for adding query logging (https://github.com/ansible-collections/community.mysql/pull/76).

Bugfixes
--------

- mysql_user - add ``SHOW_ROUTINE`` privilege support (https://github.com/ansible-collections/community.mysql/issues/86).
- mysql_user - fixed creating user with encrypted password in MySQL 8.0 (https://github.com/ansible-collections/community.mysql/pull/79).

v1.1.2
======

Release Summary
---------------

This is the patch release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection that
have been added after the release of ``community.mysql`` 1.1.1.

Minor Changes
-------------

- mysql_query - simple refactoring of query type check (https://github.com/ansible-collections/community.mysql/pull/58).
- mysql_user - simple refactoring of priv type check (https://github.com/ansible-collections/community.mysql/pull/58).

Bugfixes
--------

- mysql_db - fix false warning related to ``unsafe_login_password`` option (https://github.com/ansible-collections/community.mysql/issues/33).
- mysql_replication - fix crashes of mariadb >= 10.5.1 and mysql >= 8.0.22 caused by using deprecated terminology (https://github.com/ansible-collections/community.mysql/issues/70).
- mysql_user - fixed change detection when using append_privs (https://github.com/ansible-collections/community.mysql/pull/72).

v1.1.1
======

Release Summary
---------------

This is the patch release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection that
have been added after the release of ``community.mysql`` 1.1.0.


Bugfixes
--------

- mysql_query - fix failing when single-row query contains commas (https://github.com/ansible-collections/community.mysql/issues/51).

v1.1.0
======

Release Summary
---------------

This is the minor release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection that have been added after the release of ``community.mysql`` 1.0.2.


Minor Changes
-------------

- mysql modules - add the ``check_hostname`` option (https://github.com/ansible-collections/community.mysql/issues/28).
- mysql modules - patch the ``Connection`` class to add a destructor that ensures connections to the server are explicitly closed (https://github.com/ansible-collections/community.mysql/pull/44).

Bugfixes
--------

- mysql modules - fix crash when ``!includedir`` option is in config file (https://github.com/ansible-collections/community.mysql/issues/46).

v1.0.2
======

Release Summary
---------------

This is the patch release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection that have been added after the release of ``community.mysql`` 1.0.1.


Bugfixes
--------

- mysql_user - fix module's crash when modifying a user with ``host_all`` (https://github.com/ansible-collections/community.mysql/issues/39).

v1.0.1
======

Release Summary
---------------

This is the patch release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection that have been added after the release of ``community.mysql`` 1.0.0.


Bugfixes
--------

- mysql_db - fix false warning related to ``unsafe_login_password`` option (https://github.com/ansible-collections/community.mysql/issues/33).
- mysql_user - added tests to verify that TLS requirements are removed with an empty ``tls_requires`` option (https://github.com/ansible-collections/community.mysql/issues/20).
- mysql_user - correct procedure to check existing TLS requirements (https://github.com/ansible-collections/community.mysql/pull/26).
- mysql_user - minor syntax fixes (https://github.com/ansible-collections/community.mysql/pull/26).

v1.0.0
======

Release Summary
---------------

This is the first proper release of the ``community.mysql`` collection.
This changelog contains all changes to the modules in this collection that were added after the release of Ansible 2.9.0.


Minor Changes
-------------

- mysql_db - add ``master_data`` parameter (https://github.com/ansible/ansible/pull/66048).
- mysql_db - add ``skip_lock_tables`` option (https://github.com/ansible/ansible/pull/66688).
- mysql_db - add the ``check_implicit_admin`` parameter (https://github.com/ansible/ansible/issues/24418).
- mysql_db - add the ``dump_extra_args`` parameter (https://github.com/ansible/ansible/pull/67747).
- mysql_db - add the ``executed_commands`` returned value (https://github.com/ansible/ansible/pull/65498).
- mysql_db - add the ``force`` parameter (https://github.com/ansible/ansible/pull/65547).
- mysql_db - add the ``restrict_config_file`` parameter (https://github.com/ansible/ansible/issues/34488).
- mysql_db - add the ``unsafe_login_password`` parameter (https://github.com/ansible/ansible/issues/63955).
- mysql_db - add the ``use_shell`` parameter (https://github.com/ansible/ansible/issues/20196).
- mysql_info - add ``exclude_fields`` parameter (https://github.com/ansible/ansible/issues/63319).
- mysql_info - add ``global_status`` filter parameter option and return (https://github.com/ansible/ansible/pull/63189).
- mysql_info - add ``return_empty_dbs`` parameter to list empty databases (https://github.com/ansible/ansible/issues/65727).
- mysql_replication - add ``channel`` parameter (https://github.com/ansible/ansible/issues/29311).
- mysql_replication - add ``connection_name`` parameter (https://github.com/ansible/ansible/issues/46243).
- mysql_replication - add ``fail_on_error`` parameter (https://github.com/ansible/ansible/pull/66252).
- mysql_replication - add ``master_delay`` parameter (https://github.com/ansible/ansible/issues/51326).
- mysql_replication - add ``master_use_gtid`` parameter (https://github.com/ansible/ansible/pull/62648).
- mysql_replication - add ``queries`` return value (https://github.com/ansible/ansible/pull/63036).
- mysql_replication - add support of ``resetmaster`` choice to ``mode`` parameter (https://github.com/ansible/ansible/issues/42870).
- mysql_user - ``priv`` parameter can be string or dictionary (https://github.com/ansible/ansible/issues/57533).
- mysql_user - add TLS REQUIRES parameters (https://github.com/ansible-collections/community.mysql/pull/9).
- mysql_user - add ``plugin_auth_string`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add ``plugin_hash_string`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add ``plugin`` parameter (https://github.com/ansible/ansible/pull/44267).
- mysql_user - add the resource_limits parameter (https://github.com/ansible-collections/community.general/issues/133).
- mysql_variables - add ``mode`` parameter (https://github.com/ansible/ansible/issues/60119).

Bugfixes
--------

- mysql - dont mask ``mysql_connect`` function errors from modules (https://github.com/ansible/ansible/issues/64560).
- mysql_db - fix Broken pipe error appearance when state is import and the target file is compressed (https://github.com/ansible/ansible/issues/20196).
- mysql_db - fix bug in the ``db_import`` function introduced by https://github.com/ansible/ansible/pull/56721 (https://github.com/ansible/ansible/issues/65351).
- mysql_info - add parameter for __collect to get only what are wanted (https://github.com/ansible-collections/community.general/pull/136).
- mysql_replication - allow to pass empty values to parameters (https://github.com/ansible/ansible/issues/23976).
- mysql_user - Fix idempotence when long grant lists are used (https://github.com/ansible/ansible/issues/68044)
- mysql_user - Remove false positive ``no_log`` warning for ``update_password`` option
- mysql_user - add ``INVOKE LAMBDA`` privilege support (https://github.com/ansible-collections/community.general/issues/283).
- mysql_user - add missed privileges to support (https://github.com/ansible-collections/community.general/issues/617).
- mysql_user - fix ``host_all`` arguments conversion string formatting error (https://github.com/ansible/ansible/issues/29644).
- mysql_user - fix overriding password to the same (https://github.com/ansible-collections/community.general/issues/543).
- mysql_user - fix support privileges with underscore (https://github.com/ansible/ansible/issues/66974).
- mysql_user - fix the error No database selected (https://github.com/ansible/ansible/issues/68070).
- mysql_user - make sure current_pass_hash is a string before using it in comparison (https://github.com/ansible/ansible/issues/60567).
- mysql_variable - fix the module doesn't support variables name with dot (https://github.com/ansible/ansible/issues/54239).
