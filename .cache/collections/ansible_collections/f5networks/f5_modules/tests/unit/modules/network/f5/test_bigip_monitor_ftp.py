# -*- coding: utf-8 -*-
#
# Copyright: (c) 2019, F5 Networks Inc.
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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_monitor_ftp import (
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
            app_service='my.app.foo',
            parent='parent',
            description='my descr',
            debug=True,
            mode='port',
            filename='/ftp/var/health.txt',
            target_username='admin',
            target_password='sekrit',
            ip='10.10.10.10',
            port=80,
            interval=20,
            timeout=30,
            time_until_up=60,
            up_interval=15,
            manual_resume=True,
            partition='Common'
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.parent == '/Common/parent'
        assert p.app_service == 'my.app.foo'
        assert p.description == 'my descr'
        assert p.debug == 'enabled'
        assert p.ip == '10.10.10.10'
        assert p.target_username == 'admin'
        assert p.target_password == 'sekrit'
        assert p.port == 80
        assert p.destination == '10.10.10.10:80'
        assert p.interval == 20
        assert p.timeout == 30
        assert p.time_until_up == 60
        assert p.up_interval == 15
        assert p.manual_resume == 'enabled'

    def test_api_parameters(self):
        args = load_fixture('load_ltm_monitor_ftp.json')
        p = ApiParameters(params=args)
        assert p.name == 'foo_ftp'
        assert p.destination == '*:*'
        assert p.ip == '*'
        assert p.port == '*'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_monitor_ftp.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_monitor_ftp.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_ftp_monitor(self, *args):
        # Configure the arguments that would be sent to the Ansible module
        set_module_args(dict(
            name='foo_ftp',
            parent='ftp_parent',
            description='description one',
            debug='yes',
            mode='port',
            filename='/ftp/var/health.txt',
            target_username='admin',
            target_password='sekrit',
            ip='10.10.10.10',
            port=80,
            manual_resume='no',
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
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['description'] == 'description one'
        assert results['debug'] == 'yes'
        assert results['parent'] == '/Common/ftp_parent'
        assert results['mode'] == 'port'
        assert results['manual_resume'] == 'no'

    def test_update_ftp_monitor(self, *args):
        set_module_args(dict(
            name='foo_ftp',
            debug='no',
            mode='passive',
            ip='15.15.15.1',
            port=8080,
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = ApiParameters(params=load_fixture('load_ltm_profile_ftp.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()
        assert results['changed'] is True
        assert results['debug'] == 'no'
        assert results['mode'] == 'passive'
        assert results['ip'] == '15.15.15.1'
        assert results['port'] == 8080
