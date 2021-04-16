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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_virtual_server import (
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
            server_name='server1',
            address='1.1.1.1',
            port=22,
            translation_address='2.2.2.2',
            translation_port=443,
            availability_requirements=dict(
                type='at_least',
                at_least=2,
            ),
            monitors=['http', 'tcp', 'gtp'],
            virtual_server_dependencies=[
                dict(
                    server='server2',
                    virtual_server='vs2'
                )
            ],
            link='link1',
            limits=dict(
                bits_enabled=True,
                packets_enabled=True,
                connections_enabled=True,
                bits_limit=100,
                packets_limit=200,
                connections_limit=300
            ),
            state='present'
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.server_name == 'server1'
        assert p.address == '1.1.1.1'
        assert p.port == 22
        assert p.translation_address == '2.2.2.2'
        assert p.translation_port == 443
        assert p.availability_requirement_type == 'at_least'
        assert p.at_least == 2
        assert p.monitors == 'min 2 of { /Common/http /Common/tcp /Common/gtp }'
        assert len(p.virtual_server_dependencies) == 1
        assert p.link == '/Common/link1'
        assert p.bits_enabled == 'enabled'
        assert p.bits_limit == 100
        assert p.packets_enabled == 'enabled'
        assert p.packets_limit == 200
        assert p.connections_enabled == 'enabled'
        assert p.connections_limit == 300

    def test_api_parameters(self):
        args = load_fixture('load_gtm_server_virtual_2.json')

        p = ApiParameters(params=args)
        assert p.name == 'vs2'
        assert p.address == '6.6.6.6'
        assert p.port == 8080
        assert p.translation_address == 'none'
        assert p.translation_port == 0
        assert p.availability_requirement_type == 'all'
        assert p.monitors == '/Common/gtp'
        assert p.bits_enabled == 'enabled'
        assert p.bits_limit == 100
        assert p.packets_enabled == 'enabled'
        assert p.packets_limit == 200
        assert p.connections_enabled == 'enabled'
        assert p.connections_limit == 300


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_virtual_server.module_provisioned')
        self.m1 = self.p1.start()
        self.m1.return_value = True
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_virtual_server.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_virtual_server.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()

    def test_create_datacenter(self, *args):
        set_module_args(dict(
            server_name='foo',
            name='vs1',
            address='1.1.1.1',
            state='present',
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

        results = mm.exec_module()
        assert results['changed'] is True
