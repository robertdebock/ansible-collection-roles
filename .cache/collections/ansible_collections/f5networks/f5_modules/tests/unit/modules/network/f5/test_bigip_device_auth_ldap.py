# -*- coding: utf-8 -*-
#
# Copyright: (c) 2018, F5 Networks Inc.
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import json
import pytest
import sys

if sys.version_info < (2, 7):
    pytestmark = pytest.mark.skip("F5 Ansible modules require Python >= 2.7")

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth_ldap import (
    ApiParameters, ModuleManager, ArgumentSpec
)
from ansible_collections.f5networks.f5_modules.tests.unit.compat import unittest
from ansible_collections.f5networks.f5_modules.tests.unit.compat.mock import Mock, patch
from ansible_collections.f5networks.f5_modules.tests.unit.modules.utils import set_module_args


fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
fixture_data = {}


def load_fixture(name):
    path = os.path.join(fixture_path, name)

    if path in fixture_data:
        return fixture_data[path]

    with open(path) as f:
        data = f.read()

    try:
        data = json.loads(data)
    except Exception:
        pass

    fixture_data[path] = data
    return data


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        args = dict(
            servers=['10.10.10.10', '10.10.10.11'],
            port=389,
            remote_directory_tree='foo',
            scope='base',
            bind_dn='bar',
            bind_password='secret',
            user_template='alice',
            check_member_attr=False,
            ssl='no',
            ca_cert='default.crt',
            client_key='default.key',
            client_cert='default1.crt',
            validate_certs=True,
            login_ldap_attr='bob',
            fallback_to_local=True,
            update_password='on_create',
        )
        p = ApiParameters(params=args)
        assert p.port == 389
        assert p.servers == ['10.10.10.10', '10.10.10.11']
        assert p.remote_directory_tree == 'foo'
        assert p.scope == 'base'
        assert p.bind_dn == 'bar'
        assert p.bind_password == 'secret'
        assert p.user_template == 'alice'
        assert p.check_member_attr == 'no'
        assert p.ssl == 'no'
        assert p.ca_cert == '/Common/default.crt'
        assert p.client_key == '/Common/default.key'
        assert p.client_cert == '/Common/default1.crt'
        assert p.validate_certs == 'yes'
        assert p.login_ldap_attr == 'bob'
        assert p.fallback_to_local == 'yes'
        assert p.update_password == 'on_create'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth_ldap.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth_ldap.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            servers=['10.10.10.10', '10.10.10.11'],
            update_password='on_create',
            state='present',
            provider=dict(
                password='admin',
                server='localhost',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)
        mm.update_auth_source_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True
