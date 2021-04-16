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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vcmp_guest import (
    ModuleParameters, ApiParameters, ModuleManager, ArgumentSpec
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
            initial_image='BIGIP-12.1.0.1.0.1447-HF1.iso',
            mgmt_network='bridged',
            mgmt_address='1.2.3.4/24',
            vlans=[
                'vlan1',
                'vlan2'
            ]
        )

        p = ModuleParameters(params=args)
        assert p.initial_image == 'BIGIP-12.1.0.1.0.1447-HF1.iso'
        assert p.mgmt_network == 'bridged'

    def test_module_parameters_mgmt_bridged_without_subnet(self):
        args = dict(
            mgmt_network='bridged',
            mgmt_address='1.2.3.4'
        )

        p = ModuleParameters(params=args)
        assert p.mgmt_network == 'bridged'
        assert p.mgmt_address == '1.2.3.4/32'

    def test_module_parameters_mgmt_address_cidr(self):
        args = dict(
            mgmt_network='bridged',
            mgmt_address='1.2.3.4/24'
        )

        p = ModuleParameters(params=args)
        assert p.mgmt_network == 'bridged'
        assert p.mgmt_address == '1.2.3.4/24'

    def test_module_parameters_mgmt_address_subnet(self):
        args = dict(
            mgmt_network='bridged',
            mgmt_address='1.2.3.4/255.255.255.0'
        )

        p = ModuleParameters(params=args)
        assert p.mgmt_network == 'bridged'
        assert p.mgmt_address == '1.2.3.4/24'

    def test_module_parameters_mgmt_route(self):
        args = dict(
            mgmt_route='1.2.3.4'
        )

        p = ModuleParameters(params=args)
        assert p.mgmt_route == '1.2.3.4'

    def test_module_parameters_vcmp_software_image_facts(self):
        # vCMP images may include a forward slash in their names. This is probably
        # related to the slots on the system, but it is not a valid value to specify
        # that slot when providing an initial image
        args = dict(
            initial_image='BIGIP-12.1.0.1.0.1447-HF1.iso/1',
        )

        p = ModuleParameters(params=args)
        assert p.initial_image == 'BIGIP-12.1.0.1.0.1447-HF1.iso/1'

    def test_api_parameters(self):
        args = dict(
            initialImage="BIGIP-tmos-tier2-13.1.0.0.0.931.iso",
            managementGw="2.2.2.2",
            managementIp="1.1.1.1/24",
            managementNetwork="bridged",
            state="deployed",
            vlans=[
                "/Common/vlan1",
                "/Common/vlan2"
            ]
        )

        p = ApiParameters(params=args)
        assert p.initial_image == 'BIGIP-tmos-tier2-13.1.0.0.0.931.iso'
        assert p.mgmt_route == '2.2.2.2'
        assert p.mgmt_address == '1.1.1.1/24'
        assert '/Common/vlan1' in p.vlans
        assert '/Common/vlan2' in p.vlans

    def test_api_parameters_with_hotfix(self):
        args = dict(
            initialImage="BIGIP-14.1.0.3-0.0.6.iso",
            initialHotfix="Hotfix-BIGIP-14.1.0.3.0.5.6-ENG.iso",
            managementGw="2.2.2.2",
            managementIp="1.1.1.1/24",
            managementNetwork="bridged",
            state="deployed",
            vlans=[
                "/Common/vlan1",
                "/Common/vlan2"
            ]
        )

        p = ApiParameters(params=args)
        assert p.initial_image == 'BIGIP-14.1.0.3-0.0.6.iso'
        assert p.initial_hotfix == 'Hotfix-BIGIP-14.1.0.3.0.5.6-ENG.iso'
        assert p.mgmt_route == '2.2.2.2'
        assert p.mgmt_address == '1.1.1.1/24'
        assert '/Common/vlan1' in p.vlans
        assert '/Common/vlan2' in p.vlans


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()

        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vcmp_guest.ModuleParameters.initial_image_exists')
        self.m1 = self.p1.start()
        self.m1.return_value = True
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vcmp_guest.ModuleParameters.initial_hotfix_exists')
        self.m2 = self.p2.start()
        self.m2.return_value = True
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vcmp_guest.tmos_version')
        self.p4 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vcmp_guest.send_teem')
        self.m3 = self.p3.start()
        self.m3.return_value = '14.1.0'
        self.m4 = self.p4.start()
        self.m4.return_value = True

    def tearDown(self):
        self.patcher1.stop()
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()
        self.p4.stop()

    def test_create_vcmpguest(self, *args):
        set_module_args(dict(
            name="guest1",
            mgmt_network="bridged",
            mgmt_address="10.10.10.10/24",
            initial_image="BIGIP-13.1.0.0.0.931.iso",
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)
        mm.is_deployed = Mock(side_effect=[False, True, True, True, True])
        mm.deploy_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'guest1'

    def test_create_vcmpguest_with_hotfix(self, *args):
        set_module_args(dict(
            name="guest2",
            mgmt_network="bridged",
            mgmt_address="10.10.10.10/24",
            initial_image="BIGIP-14.1.0.3-0.0.6.iso",
            initial_hotfix="Hotfix-BIGIP-14.1.0.3.0.5.6-ENG.iso",
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)
        mm.is_deployed = Mock(side_effect=[False, True, True, True, True])
        mm.deploy_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'guest2'
