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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vlan import (
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


class BigIpObj(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        args = dict(
            name='somevlan',
            tag=213,
            description='fakevlan',
            untagged_interfaces=['1.1'],
            hw_syn_cookie=True,
        )
        p = ModuleParameters(params=args)

        assert p.name == 'somevlan'
        assert p.tag == 213
        assert p.description == 'fakevlan'
        assert p.untagged_interfaces == ['1.1']
        assert p.hw_syn_cookie == 'enabled'

    def test_api_parameters(self):
        args = dict(
            name='somevlan',
            description='fakevlan',
            tag=213
        )

        p = ApiParameters(params=args)

        assert p.name == 'somevlan'
        assert p.tag == 213
        assert p.description == 'fakevlan'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vlan.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_vlan.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_vlan(self, *args):
        set_module_args(dict(
            name='somevlan',
            description='fakevlan',
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['description'] == 'fakevlan'

    def test_create_vlan_tagged_interface(self, *args):
        set_module_args(dict(
            name='somevlan',
            tagged_interface=['2.1'],
            tag=213,
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['tagged_interfaces'] == ['2.1']
        assert results['tag'] == 213

    def test_create_vlan_untagged_interface(self, *args):
        set_module_args(dict(
            name='somevlan',
            untagged_interface=['2.1'],
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['untagged_interfaces'] == ['2.1']

    def test_create_vlan_tagged_interfaces(self, *args):
        set_module_args(dict(
            name='somevlan',
            tagged_interface=['2.1', '1.1'],
            tag=213,
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['tagged_interfaces'] == ['1.1', '2.1']
        assert results['tag'] == 213

    def test_create_vlan_untagged_interfaces(self, *args):
        set_module_args(dict(
            name='somevlan',
            untagged_interface=['2.1', '1.1'],
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['untagged_interfaces'] == ['1.1', '2.1']

    def test_update_vlan_untag_interface(self, *args):
        set_module_args(dict(
            name='somevlan',
            untagged_interface=['2.1'],
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)

        current = ApiParameters(params=load_fixture('load_vlan.json'))
        interfaces = load_fixture('load_vlan_interfaces.json')
        current.update({'interfaces': interfaces})

        mm.update_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['untagged_interfaces'] == ['2.1']

    def test_update_vlan_tag_interface(self, *args):
        set_module_args(dict(
            name='somevlan',
            tagged_interface=['2.1'],
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)

        current = ApiParameters(params=load_fixture('load_vlan.json'))

        mm.update_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['tagged_interfaces'] == ['2.1']

    def test_update_vlan_description(self, *args):
        set_module_args(dict(
            name='somevlan',
            description='changed_that',
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive
        )

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)

        current = ApiParameters(params=load_fixture('update_vlan_description.json'))

        mm.update_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['description'] == 'changed_that'
