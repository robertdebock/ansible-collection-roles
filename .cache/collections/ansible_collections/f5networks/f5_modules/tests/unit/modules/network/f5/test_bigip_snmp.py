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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_snmp import (
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
            agent_status_traps='enabled',
            agent_authentication_traps='enabled',
            contact='Alice@foo.org',
            device_warning_traps='enabled',
            location='Lunar orbit',
        )
        p = ModuleParameters(params=args)
        assert p.agent_status_traps == 'enabled'
        assert p.agent_authentication_traps == 'enabled'
        assert p.device_warning_traps == 'enabled'
        assert p.location == 'Lunar orbit'
        assert p.contact == 'Alice@foo.org'

    def test_module_parameters_disabled(self):
        args = dict(
            agent_status_traps='disabled',
            agent_authentication_traps='disabled',
            device_warning_traps='disabled',
        )
        p = ModuleParameters(params=args)
        assert p.agent_status_traps == 'disabled'
        assert p.agent_authentication_traps == 'disabled'
        assert p.device_warning_traps == 'disabled'

    def test_api_parameters(self):
        args = dict(
            agentTrap='enabled',
            authTrap='enabled',
            bigipTraps='enabled',
            sysLocation='Lunar orbit',
            sysContact='Alice@foo.org',
        )
        p = ApiParameters(params=args)
        assert p.agent_status_traps == 'enabled'
        assert p.agent_authentication_traps == 'enabled'
        assert p.device_warning_traps == 'enabled'
        assert p.location == 'Lunar orbit'
        assert p.contact == 'Alice@foo.org'

    def test_api_parameters_disabled(self):
        args = dict(
            agentTrap='disabled',
            authTrap='disabled',
            bigipTraps='disabled',
        )
        p = ApiParameters(params=args)
        assert p.agent_status_traps == 'disabled'
        assert p.agent_authentication_traps == 'disabled'
        assert p.device_warning_traps == 'disabled'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_snmp.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_snmp.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_update_agent_status_traps(self, *args):
        set_module_args(dict(
            agent_status_traps='enabled',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = ApiParameters(
            params=dict(
                agent_status_traps='disabled'
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['agent_status_traps'] == 'enabled'

    def test_update_allowed_addresses(self, *args):
        set_module_args(dict(
            allowed_addresses=[
                '127.0.0.0/8',
                '10.10.10.10',
                'foo',
                'baz.foo.com'
            ],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = ApiParameters(
            params=dict(
                allowed_addresses=['127.0.0.0/8']
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert len(results['allowed_addresses']) == 4
        assert results['allowed_addresses'] == [
            '10.10.10.10', '127.0.0.0/8', 'baz.foo.com', 'foo'
        ]

    def test_update_allowed_addresses_default(self, *args):
        set_module_args(dict(
            allowed_addresses=[
                'default'
            ],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = ApiParameters(
            params=dict(
                allowed_addresses=['10.0.0.0']
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert len(results['allowed_addresses']) == 1
        assert results['allowed_addresses'] == ['127.0.0.0/8']

    def test_update_allowed_addresses_empty(self, *args):
        set_module_args(dict(
            allowed_addresses=[''],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = ApiParameters(
            params=dict(
                allowed_addresses=['10.0.0.0']
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert len(results['allowed_addresses']) == 1
        assert results['allowed_addresses'] == ['127.0.0.0/8']
