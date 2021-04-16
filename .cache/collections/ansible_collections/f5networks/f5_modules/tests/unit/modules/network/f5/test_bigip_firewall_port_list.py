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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_port_list import (
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
            description='this is a description',
            ports=[1, 2, 3, 4],
            port_ranges=['10-20', '30-40', '50-60'],
            port_lists=['/Common/foo', 'foo']
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.description == 'this is a description'
        assert len(p.ports) == 4
        assert len(p.port_ranges) == 3
        assert len(p.port_lists) == 2

    def test_api_parameters(self):
        args = load_fixture('load_security_port_list_1.json')

        p = ApiParameters(params=args)
        assert len(p.ports) == 4
        assert len(p.port_ranges) == 3
        assert len(p.port_lists) == 1
        assert sorted(p.ports) == [1, 2, 3, 4]
        assert sorted(p.port_ranges) == ['10-20', '30-40', '50-60']
        assert p.port_lists[0] == '/Common/_sys_self_allow_tcp_defaults'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_port_list.module_provisioned')
        self.m1 = self.p1.start()
        self.m1.return_value = True
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_port_list.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_port_list.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()

    def tearDown(self):
        self.p1.stop()

    def test_create(self, *args):
        set_module_args(dict(
            name='foo',
            description='this is a description',
            ports=[1, 2, 3, 4],
            port_ranges=['10-20', '30-40', '50-60'],
            port_lists=['/Common/foo', 'foo'],
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
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)
        mm.module_provisioned = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert 'ports' in results
        assert 'port_lists' in results
        assert 'port_ranges' in results
        assert len(results['ports']) == 4
        assert len(results['port_ranges']) == 3
        assert len(results['port_lists']) == 2
        assert results['description'] == 'this is a description'
