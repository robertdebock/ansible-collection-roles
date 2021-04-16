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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_virtual_address import (
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
            state='present',
            address='1.1.1.1',
            netmask='2.2.2.2',
            connection_limit='10',
            arp='enabled',
            auto_delete='enabled',
            icmp_echo='enabled',
            availability_calculation='always',
        )
        p = ModuleParameters(params=args)
        assert p.state == 'present'
        assert p.address == '1.1.1.1'
        assert p.netmask == '2.2.2.2'
        assert p.connection_limit == 10
        assert p.arp == 'enabled'
        assert p.auto_delete == 'true'
        assert p.icmp_echo == 'enabled'
        assert p.availability_calculation == 'none'

    def test_api_parameters(self):
        args = load_fixture('load_ltm_virtual_address_default.json')
        p = ApiParameters(params=args)
        assert p.name == '1.1.1.1'
        assert p.address == '1.1.1.1'
        assert p.arp == 'enabled'
        assert p.auto_delete == 'true'
        assert p.connection_limit == 0
        assert p.state == 'enabled'
        assert p.icmp_echo == 'enabled'
        assert p.netmask == '255.255.255.255'
        assert p.route_advertisement_type == 'disabled'
        assert p.availability_calculation == 'any'

    def test_module_parameters_advertise_route_all(self):
        args = dict(
            availability_calculation='when_all_available'
        )
        p = ModuleParameters(params=args)
        assert p.availability_calculation == 'all'

    def test_module_parameters_advertise_route_any(self):
        args = dict(
            availability_calculation='when_any_available'
        )
        p = ModuleParameters(params=args)
        assert p.availability_calculation == 'any'

    def test_module_parameters_icmp_echo_disabled(self):
        args = dict(
            icmp_echo='disabled'
        )
        p = ModuleParameters(params=args)
        assert p.icmp_echo == 'disabled'

    def test_module_parameters_icmp_echo_selective(self):
        args = dict(
            icmp_echo='selective'
        )
        p = ModuleParameters(params=args)
        assert p.icmp_echo == 'selective'

    def test_module_parameters_auto_delete_disabled(self):
        args = dict(
            auto_delete='disabled'
        )
        p = ModuleParameters(params=args)
        assert p.auto_delete == 'false'

    def test_module_parameters_arp_disabled(self):
        args = dict(
            arp='disabled'
        )
        p = ModuleParameters(params=args)
        assert p.arp == 'disabled'

    def test_module_parameters_state_present(self):
        args = dict(
            state='present'
        )
        p = ModuleParameters(params=args)
        assert p.state == 'present'
        assert p.enabled == 'yes'

    def test_module_parameters_state_absent(self):
        args = dict(
            state='absent'
        )
        p = ModuleParameters(params=args)
        assert p.state == 'absent'

    def test_module_parameters_state_enabled(self):
        args = dict(
            state='enabled'
        )
        p = ModuleParameters(params=args)
        assert p.state == 'enabled'
        assert p.enabled == 'yes'

    def test_module_parameters_state_disabled(self):
        args = dict(
            state='disabled'
        )
        p = ModuleParameters(params=args)
        assert p.state == 'disabled'
        assert p.enabled == 'no'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_virtual_address.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_virtual_address.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_virtual_address(self, *args):
        set_module_args(dict(
            state='present',
            address='1.1.1.1',
            netmask='2.2.2.2',
            connection_limit='10',
            arp='yes',
            auto_delete='yes',
            icmp_echo='enabled',
            advertise_route='always',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_one_of=self.spec.required_one_of
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True

    def test_delete_virtual_address(self, *args):
        set_module_args(dict(
            state='absent',
            address='1.1.1.1',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_one_of=self.spec.required_one_of
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[True, False])
        mm.remove_from_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True
