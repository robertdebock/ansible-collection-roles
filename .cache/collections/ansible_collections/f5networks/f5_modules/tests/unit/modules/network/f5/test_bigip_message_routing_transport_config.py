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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_message_routing_transport_config import (
    ApiParameters, ModuleParameters, ModuleManager, GenericModuleManager, ArgumentSpec
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
            partition='foobar',
            description='my description',
            profiles=['genericmsg', 'foo_udp'],
            src_addr_translation=dict(
                type='snat',
                pool='some_pool1'
            ),
            src_port=1023,
            rules=['rule1', 'rule2'],
        )
        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.partition == 'foobar'
        assert p.description == 'my description'
        assert p.profiles == ['/foobar/genericmsg', '/foobar/foo_udp']
        assert p.snat_type == 'snat'
        assert p.snat_pool == '/foobar/some_pool1'
        assert p.src_port == 1023
        assert p.rules == ['/foobar/rule1', '/foobar/rule2']

    def test_api_parameters(self):
        args = load_fixture('load_generic_transport_config.json')

        p = ApiParameters(params=args)
        assert p.name == 'gen1'
        assert p.partition == 'Common'
        assert p.profiles == ['/Common/diametersession', '/Common/tcp']
        assert p.snat_type == 'snat'
        assert p.src_port == 0
        assert p.snat_pool == '/Common/test_snat'
        assert p.rules == ['/Common/test']


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_message_routing_transport_config.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_message_routing_transport_config.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_generic_transport(self, *args):
        set_module_args(dict(
            name='foo',
            partition='foobar',
            description='my description',
            profiles=['genericmsg', 'foo_udp'],
            src_addr_translation=dict(
                type='snat',
                pool='some_pool1'
            ),
            src_port=1023,
            rules=['rule1', 'rule2'],
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
        gm = GenericModuleManager(module=module)
        gm.exists = Mock(return_value=False)
        gm.create_on_device = Mock(return_value=True)

        mm = ModuleManager(module=module)
        mm.version_less_than_14 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=gm)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['description'] == 'my description'
        assert results['src_addr_translation'] == dict(type='snat', pool='/foobar/some_pool1')
        assert results['src_port'] == 1023
        assert results['rules'] == ['/foobar/rule1', '/foobar/rule2']
        assert results['profiles'] == ['/foobar/genericmsg', '/foobar/foo_udp']

    def test_update_generic_transport(self, *args):
        set_module_args(dict(
            name='gen1',
            src_port=1024,
            rules=['/Common/barfoo'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = ApiParameters(params=load_fixture('load_generic_transport_config.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
        )

        # Override methods in the specific type of manager
        gm = GenericModuleManager(module=module)
        gm.exists = Mock(return_value=True)
        gm.update_on_device = Mock(return_value=True)
        gm.read_current_from_device = Mock(return_value=current)

        mm = ModuleManager(module=module)
        mm.version_less_than_14 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=gm)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['src_port'] == 1024
        assert results['rules'] == ['/Common/barfoo']
