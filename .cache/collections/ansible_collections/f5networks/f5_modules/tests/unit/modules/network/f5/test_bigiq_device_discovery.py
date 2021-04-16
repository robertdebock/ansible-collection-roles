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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigiq_device_discovery import (
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
            device_address='192.168.1.1',
            device_username='admin',
            device_password='admin',
            device_port=10443,
            ha_name='bazfoo',
            use_bigiq_sync='yes',
            modules=['asm', 'ltm', 'security_shared']
        )

        p = ModuleParameters(params=args)
        assert p.device_address == '192.168.1.1'
        assert p.device_username == 'admin'
        assert p.device_password == 'admin'
        assert p.device_port == 10443
        assert p.ha_name == 'bazfoo'
        assert p.use_bigiq_sync is True
        assert p.modules == ['asm', 'adc_core', 'security_shared']

    def test_api_parameters(self):
        args = load_fixture('load_machine_resolver.json')

        p = ApiParameters(params=args)
        assert sorted(p.modules) == sorted(['asm', 'adc_core', 'security_shared'])


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigiq_device_discovery.bigiq_version')
        self.m1 = self.p1.start()
        self.m1.return_value = '6.1.0'
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigiq_device_discovery.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = True

    def tearDown(self):
        self.patcher1.stop()
        self.p1.stop()
        self.p2.stop()

    def test_create(self, *args):
        set_module_args(dict(
            device_address='192.168.1.1',
            device_username='admin',
            device_password='admin',
            modules=['asm', 'ltm', 'security_shared'],
            provider=dict(
                password='password',
                server='localhost',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[False, True])
        mm.set_trust_with_device = Mock(return_value=True)
        mm.discover_on_device = Mock(return_value=True)
        mm.import_modules_on_device = Mock(return_value=True)
        mm.check_bigiq_version = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
