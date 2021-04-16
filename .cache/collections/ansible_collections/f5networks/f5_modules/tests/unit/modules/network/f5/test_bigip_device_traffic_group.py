# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 F5 Networks Inc.
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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_traffic_group import (
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
    def test_module_parameters_1(self):
        args = dict(
            name='foo',
            mac_address=''
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.mac_address == 'none'

    def test_module_parameters_2(self):
        args = dict(
            mac_address='00:00:00:00:00:02'
        )

        p = ModuleParameters(params=args)
        assert p.mac_address == '00:00:00:00:00:02'

    def test_module_parameters_3(self):
        args = dict(
            name='foo',
            ha_order=['bigip1'],
            ha_group='',
            auto_failback='yes',
            auto_failback_time=40
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.ha_order == ['/Common/bigip1']
        assert p.ha_group == 'none'
        assert p.auto_failback == 'true'
        assert p.auto_failback_time == 40

    def test_api_parameters_1(self):
        args = load_fixture('load_tm_cm_traffic_group_1.json')

        p = ApiParameters(params=args)
        assert p.mac_address == 'none'

    def test_api_parameters_2(self):
        args = load_fixture('load_tm_cm_traffic_group_2.json')

        p = ApiParameters(params=args)
        assert p.mac_address == '00:00:00:00:00:02'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_traffic_group.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_traffic_group.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            name='foo',
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
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True

    def test_modify_ha_order(self, *args):
        set_module_args(dict(
            name='traffic-group-2',
            ha_order=['v12-2.ansible.local', 'v12-1.ansible.local'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
        )

        current = ApiParameters(params=load_fixture('load_tg_ha_order.json'))

        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        mm.update_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['ha_order'] == ['/Common/v12-2.ansible.local', '/Common/v12-1.ansible.local']
