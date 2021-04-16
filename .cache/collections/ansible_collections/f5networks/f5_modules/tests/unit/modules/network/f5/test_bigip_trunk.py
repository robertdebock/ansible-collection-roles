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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_trunk import (
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
            interfaces=[
                '1.3', '1.1'
            ],
            link_selection_policy='auto',
            frame_distribution_hash='destination-mac',
            lacp_enabled=True,
            lacp_mode='active',
            lacp_timeout='long'
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.interfaces == ['1.1', '1.3']
        assert p.link_selection_policy == 'auto'
        assert p.frame_distribution_hash == 'dst-mac'
        assert p.lacp_enabled is True
        assert p.lacp_mode == 'active'
        assert p.lacp_timeout == 'long'

    def test_api_parameters(self):
        args = load_fixture('load_tm_net_trunk_1.json')

        p = ApiParameters(params=args)
        assert p.name == 'foo'
        assert p.frame_distribution_hash == 'dst-mac'
        assert p.lacp_enabled is False
        assert p.lacp_mode == 'active'
        assert p.lacp_timeout == 'long'
        assert p.interfaces == ['1.3']
        assert p.link_selection_policy == 'maximum-bandwidth'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_trunk.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_trunk.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            name='foo',
            interfaces=[
                '1.3', '1.1'
            ],
            link_selection_policy='auto',
            frame_distribution_hash='destination-mac',
            lacp_enabled=True,
            lacp_mode='active',
            lacp_timeout='long',
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
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['link_selection_policy'] == 'auto'
        assert results['frame_distribution_hash'] == 'destination-mac'
        assert results['lacp_enabled'] is True
        assert results['lacp_mode'] == 'active'
        assert results['lacp_timeout'] == 'long'
