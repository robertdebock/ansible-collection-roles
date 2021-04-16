from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from distutils.version import LooseVersion
from ansible_collections.community.mysql.plugins.module_utils.mysql import get_server_version


def use_old_user_mgmt(cursor):
    version = get_server_version(cursor)

    return LooseVersion(version) < LooseVersion("5.7")


def supports_identified_by_password(cursor):
    version = get_server_version(cursor)
    return LooseVersion(version) < LooseVersion("8")
