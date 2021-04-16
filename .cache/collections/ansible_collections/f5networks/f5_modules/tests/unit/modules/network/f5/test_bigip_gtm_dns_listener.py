# -*- coding: utf-8 -*-
#
# Copyright: (c) 2020, F5 Networks Inc.
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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_dns_listener import (
    ApiParameters, ModuleParameters, ModuleManager, ArgumentSpec
)
from ansible_collections.f5networks.f5_modules.plugins.module_utils.common import F5ModuleError
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
            address='10.0.1.0',
            mask='255.255.255.0',
            port=56,
            advertise='no',
            description='this is description',
            ip_protocol='tcp'
        )

        p = ModuleParameters(params=args)
        assert p.address == '10.0.1.0'
        assert p.mask == '255.255.255.0'
        assert p.port == 56
        assert p.advertise == 'no'
        assert p.description == 'this is description'
        assert p.ip_protocol == 'tcp'

    def test_api_parameters(self):
        args = dict(
            address='10.0.1.0',
            mask='255.255.255.0',
            port=56,
            advertise='no',
            description='this is description',
            ip_protocol='tcp'
        )

        p = ApiParameters(params=args)
        assert p.address == '10.0.1.0'
        assert p.mask == '255.255.255.0'
        assert p.port == 56


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_dns_listener.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_dns_listener.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            address='10.0.1.0',
            mask='255.255.255.0',
            port=53,
            advertise='no',
            state='present',
            description='this is description',
            ip_protocol='tcp',
            translate_address='yes',
            translate_port='no',
            enabled_vlans=[
                '/Common/vlan1',
                '/Common/vlan2'
            ],
            irules=[
                '/Common/rule1',
                '/Common/rule2'
            ],
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)
        results = mm.exec_module()

        assert results['changed'] is True
        assert results['address'] == '10.0.1.0'
        assert results['port'] == 53
        assert results['mask'] == '255.255.255.0'
        assert results['advertise'] == 'no'
        assert results['ip_protocol'] == 'tcp'
        assert results['description'] == 'this is description'
        assert results['translate_address'] == 'enabled'
        assert results['translate_port'] == 'disabled'
        assert results['vlans_enabled'] is True
        assert results['enabled_vlans'][0] == '/Common/vlan1' and results['vlans'][1] == '/Common/vlan2'
        assert results['irules'][0] == '/Common/rule1' and results['irules'][1] == '/Common/rule2'

    def test_update(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            address='10.0.1.0',
            mask='255.255.255.0',
            port=53,
            advertise='no',
            state='present',
            description='this is description',
            ip_protocol='tcp',
            translate_address='yes',
            translate_port='no',
            enabled_vlans=[
                '/Common/vlan1',
                '/Common/vlan2'
            ],
            irules=[
                '/Common/rule1',
                '/Common/rule2'
            ],
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

        current = ApiParameters(
            dict(
                agent_status_traps='disabled'
            )
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        results = mm.exec_module()

        assert results['changed'] is True
        assert results['address'] == '10.0.1.0'
        assert results['port'] == 53
        assert results['mask'] == '255.255.255.0'
        assert results['advertise'] == 'no'
        assert results['ip_protocol'] == 'tcp'
        assert results['description'] == 'this is description'
        assert results['translate_address'] == 'enabled'
        assert results['translate_port'] == 'disabled'
        assert results['enabled_vlans'][0] == '/Common/vlan1' and results['vlans'][1] == '/Common/vlan2'
        assert results['irules'][0] == '/Common/rule1' and results['irules'][1] == '/Common/rule2'

    def test_enabled_vlans_all(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            address='10.0.1.0',
            mask='255.255.255.0',
            port=53,
            advertise='no',
            state='present',
            description='this is description',
            ip_protocol='tcp',
            translate_address='yes',
            translate_port='no',
            enabled_vlans='all',
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

        current = ApiParameters(
            dict(
                agent_status_traps='disabled'
            )
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        results = mm.exec_module()

        assert results['changed'] is True
        assert results['address'] == '10.0.1.0'
        assert results['port'] == 53
        assert results['mask'] == '255.255.255.0'
        assert results['advertise'] == 'no'
        assert results['ip_protocol'] == 'tcp'
        assert results['description'] == 'this is description'
        assert results['translate_address'] == 'enabled'
        assert results['translate_port'] == 'disabled'
        assert results['vlans_enabled'] is True
        assert 'vlans_disabled' not in results

    def test_disabled_vlans(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            address='10.0.1.0',
            mask='255.255.255.0',
            port=53,
            advertise='no',
            state='present',
            description='this is description',
            ip_protocol='tcp',
            translate_address='yes',
            translate_port='no',
            disabled_vlans='all',
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

        current = ApiParameters(
            dict(
                agent_status_traps='disabled'
            )
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        with pytest.raises(F5ModuleError) as ex:
            mm.exec_module()
        assert 'You cannot disable all VLANs. You must name them individually.' in str(ex.value)

    def test_delete(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            address='192.10.0.2',
            state='absent',
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

        current = ApiParameters(
            dict(
                agent_status_traps='disabled'
            )
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=False)
        results = mm.exec_module()

        assert results['changed'] is False

    def test_enable_listener(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            state='enabled',
            address='192.10.0.2',
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

        current = ApiParameters(
            dict(
                agent_status_traps='disabled'
            )
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        results = mm.exec_module()

        assert results['changed'] is True

    def test_disable_listener(self, *args):
        set_module_args(dict(
            name='test-dns-listener',
            state='disabled',
            address='192.10.0.2',
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

        current = ApiParameters(
            dict(
                agent_status_traps='disabled'
            )
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        results = mm.exec_module()

        assert results['changed'] is True
