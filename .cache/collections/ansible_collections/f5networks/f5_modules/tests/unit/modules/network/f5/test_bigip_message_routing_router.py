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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_message_routing_router import (
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
            ignore_client_port='no',
            inherited_traffic_group='yes',
            use_local_connection='no',
            max_pending_bytes=20000,
            max_pending_messages=300,
            max_retries=32,
            mirror='yes',
            mirrored_msg_sweeper_interval=3000,
            routes=['test1', 'test2'],
            traffic_group='footraffic',
        )
        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.partition == 'foobar'
        assert p.description == 'my description'
        assert p.ignore_client_port == 'no'
        assert p.inherited_traffic_group == 'true'
        assert p.use_local_connection == 'no'
        assert p.max_pending_bytes == 20000
        assert p.max_pending_messages == 300
        assert p.max_retries == 32
        assert p.mirror == 'enabled'
        assert p.mirrored_msg_sweeper_interval == 3000
        assert p.routes == ['/foobar/test1', '/foobar/test2']
        assert p.traffic_group == '/Common/footraffic'

    def test_api_parameters(self):
        args = load_fixture('load_generic_router.json')

        p = ApiParameters(params=args)
        assert p.name == 'messagerouter'
        assert p.partition == 'Common'
        assert p.ignore_client_port == 'no'
        assert p.inherited_traffic_group == 'true'
        assert p.use_local_connection == 'yes'
        assert p.max_pending_bytes == 23768
        assert p.max_pending_messages == 64
        assert p.max_retries == 1
        assert p.mirror == 'disabled'
        assert p.mirrored_msg_sweeper_interval == 1000
        assert p.traffic_group == '/Common/traffic-group-1'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_message_routing_router.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_message_routing_router.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_generic_router(self, *args):
        set_module_args(dict(
            name='foo',
            partition='foobar',
            description='my description',
            ignore_client_port='no',
            inherited_traffic_group='yes',
            use_local_connection='no',
            max_pending_bytes=20000,
            max_pending_messages=300,
            max_retries=32,
            mirror='yes',
            mirrored_msg_sweeper_interval=3000,
            routes=['test1', 'test2'],
            traffic_group='footraffic',
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
        assert results['ignore_client_port'] == 'no'
        assert results['inherited_traffic_group'] == 'yes'
        assert results['use_local_connection'] == 'no'
        assert results['max_pending_bytes'] == 20000
        assert results['max_pending_messages'] == 300
        assert results['max_retries'] == 32
        assert results['mirror'] == 'yes'
        assert results['mirrored_msg_sweeper_interval'] == 3000
        assert results['traffic_group'] == '/Common/footraffic'
        assert results['routes'] == ['/foobar/test1', '/foobar/test2']

    def test_update_generic_router(self, *args):
        set_module_args(dict(
            name='messagerouter',
            use_local_connection='no',
            mirror='yes',
            routes=['/Common/example'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = ApiParameters(params=load_fixture('load_generic_router.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
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
        assert results['use_local_connection'] == 'no'
        assert results['mirror'] == 'yes'
        assert results['routes'] == ['/Common/example']
