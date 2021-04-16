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
from ansible.module_utils.six import iteritems

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_info import (
    Parameters, VirtualAddressesFactManager, ArgumentSpec, ModuleManager
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


class FakeVirtualAddress:
    def __init__(self, *args, **kwargs):
        attrs = kwargs.pop('params', {})
        for key, value in iteritems(attrs):
            setattr(self, key, value)


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        args = dict(
            gather_subset=['virtual-servers'],
        )
        p = Parameters(params=args)
        assert p.gather_subset == ['virtual-servers']


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()

        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_info.modules_provisioned')
        self.m1 = self.p1.start()
        self.m1.return_value = ['ltm', 'gtm', 'asm']
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_info.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_info.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()

    def test_get_trunk_facts(self, *args):
        set_module_args(dict(
            gather_subset=['virtual-addresses'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        fixture1 = load_fixture('load_ltm_virtual_address_collection_1.json')
        collection = fixture1['items']

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        tm = VirtualAddressesFactManager(module=module)
        tm.read_collection_from_device = Mock(return_value=collection)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.get_manager = Mock(return_value=tm)

        results = mm.exec_module()

        assert results['queried'] is True
        assert 'virtual_addresses' in results
        assert len(results['virtual_addresses']) > 0
