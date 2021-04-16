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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_pool import (
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
            preferred_lb_method='topology',
            alternate_lb_method='ratio',
            fallback_lb_method='fewest-hops',
            fallback_ip='10.10.10.10',
            type='a'
        )
        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.preferred_lb_method == 'topology'
        assert p.alternate_lb_method == 'ratio'
        assert p.fallback_lb_method == 'fewest-hops'
        assert p.fallback_ip == '10.10.10.10'
        assert p.type == 'a'

    def test_module_parameters_members(self):
        args = dict(
            partition='Common',
            members=[
                dict(
                    server='foo',
                    virtual_server='bar'
                )
            ]
        )
        p = ModuleParameters(params=args)
        assert len(p.members) == 1
        assert p.members[0] == '/Common/foo:bar'

    def test_api_parameters(self):
        args = dict(
            name='foo',
            loadBalancingMode='topology',
            alternateMode='ratio',
            fallbackMode='fewest-hops',
            fallbackIp='10.10.10.10'
        )
        p = ApiParameters(params=args)
        assert p.name == 'foo'
        assert p.preferred_lb_method == 'topology'
        assert p.alternate_lb_method == 'ratio'
        assert p.fallback_lb_method == 'fewest-hops'
        assert p.fallback_ip == '10.10.10.10'

    def test_api_parameters_members(self):
        args = load_fixture('load_gtm_pool_a_with_members_1.json')
        p = ApiParameters(params=args)
        assert len(p.members) == 3
        assert p.members[0] == '/Common/server1:vs1'
        assert p.members[1] == '/Common/server1:vs2'
        assert p.members[2] == '/Common/server1:vs3'


class TestModuledManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_pool.module_provisioned')
        self.m1 = self.p1.start()
        self.m1.return_value = True
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_pool.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_gtm_pool.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()

    def test_create_pool(self, *args):
        set_module_args(dict(
            name='foo',
            preferred_lb_method='round-robin',
            type='a',
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

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.module_provisioned = Mock(return_value=True)
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['preferred_lb_method'] == 'round-robin'

    def test_update_pool(self, *args):
        set_module_args(dict(
            name='foo',
            preferred_lb_method='topology',
            alternate_lb_method='drop-packet',
            fallback_lb_method='cpu',
            type='a',
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

        current = ApiParameters(params=load_fixture('load_gtm_pool_a_default.json'))

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.module_provisioned = Mock(return_value=True)
        mm.exists = Mock(side_effect=[True, True])
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['preferred_lb_method'] == 'topology'
        assert results['alternate_lb_method'] == 'drop-packet'
        assert results['fallback_lb_method'] == 'cpu'

    def test_delete_pool(self, *args):
        set_module_args(dict(
            name='foo',
            type='a',
            state='absent',
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

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.module_provisioned = Mock(return_value=True)
        mm.exists = Mock(side_effect=[True, False])
        mm.version_is_less_than_12 = Mock(return_value=False)
        mm.remove_from_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
