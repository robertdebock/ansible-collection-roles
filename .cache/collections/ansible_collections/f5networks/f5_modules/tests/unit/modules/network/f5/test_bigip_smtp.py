# -*- coding: utf-8 -*-
#
# Copyright: (c) 2017, F5 Networks Inc.
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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_smtp import (
    ApiParameters, ModuleParameters, ModuleManager, ArgumentSpec
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
            name='foo',
            smtp_server='1.1.1.1',
            smtp_server_port='25',
            smtp_server_username='admin',
            smtp_server_password='password',
            local_host_name='smtp.mydomain.com',
            encryption='tls',
            update_password='always',
            from_address='no-reply@mydomain.com',
            authentication=True,
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.smtp_server == '1.1.1.1'
        assert p.smtp_server_port == 25
        assert p.smtp_server_username == 'admin'
        assert p.smtp_server_password == 'password'
        assert p.local_host_name == 'smtp.mydomain.com'
        assert p.encryption == 'tls'
        assert p.update_password == 'always'
        assert p.from_address == 'no-reply@mydomain.com'
        assert p.authentication_disabled is None
        assert p.authentication_enabled is True

    def test_api_parameters(self):
        p = ApiParameters(params=load_fixture('load_sys_smtp_server.json'))
        assert p.name == 'foo'
        assert p.smtp_server == 'mail.foo.bar'
        assert p.smtp_server_port == 465
        assert p.smtp_server_username == 'admin'
        assert p.smtp_server_password == '$M$Ch$this-is-encrypted=='
        assert p.local_host_name == 'mail-host.foo.bar'
        assert p.encryption == 'ssl'
        assert p.from_address == 'no-reply@foo.bar'
        assert p.authentication_disabled is None
        assert p.authentication_enabled is True


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_smtp.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_smtp.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_monitor(self, *args):
        set_module_args(dict(
            name='foo',
            smtp_server='1.1.1.1',
            smtp_server_port='25',
            smtp_server_username='admin',
            smtp_server_password='password',
            local_host_name='smtp.mydomain.com',
            encryption='tls',
            update_password='always',
            from_address='no-reply@mydomain.com',
            authentication=True,
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['encryption'] == 'tls'
        assert results['smtp_server'] == '1.1.1.1'
        assert results['smtp_server_port'] == 25
        assert results['local_host_name'] == 'smtp.mydomain.com'
        assert results['authentication'] is True
        assert results['from_address'] == 'no-reply@mydomain.com'
        assert 'smtp_server_username' not in results
        assert 'smtp_server_password' not in results
