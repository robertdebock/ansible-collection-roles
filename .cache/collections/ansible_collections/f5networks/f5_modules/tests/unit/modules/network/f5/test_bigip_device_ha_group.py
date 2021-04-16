# -*- coding: utf-8 -*-
#
# Copyright: (c) 2018, F5 Networks Inc.
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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_ha_group import (
    ModuleParameters, ModuleManager, ArgumentSpec
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
    def test_module_parameters_v13(self):
        args = dict(
            name='foobar',
            description='baz',
            active_bonus=20,
            enable='yes',
            state='present',
            pools=[
                dict(
                    pool_name='fakepool',
                    attribute='percent-up-members',
                    weight=30,
                    minimum_threshold=2,
                    partition='Common'
                )
            ],
            trunks=[
                dict(
                    trunk_name='faketrunk',
                    attribute='percent-up-members',
                    weight=30,
                    minimum_threshold=2
                )
            ]
        )

        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_ha_group.tmos_version')
        self.m1 = self.p1.start()
        self.m1.return_value = '13.1.0'

        p = ModuleParameters(params=args)

        assert p.name == 'foobar'
        assert p.state == 'present'
        assert p.active_bonus == 20
        assert p.enabled is True
        assert p.pools == [{'name': '/Common/fakepool', 'attribute': 'percent-up-members',
                            'weight': 30, 'minimumThreshold': 2}]
        assert p.trunks == [{'name': 'faketrunk', 'attribute': 'percent-up-members',
                             'weight': 30, 'minimumThreshold': 2}]

        self.p1.stop()

    def test_module_parameters_v12(self):
        args = dict(
            name='foobar',
            description='baz',
            active_bonus=20,
            enable='yes',
            state='present',
            pools=[
                dict(
                    pool_name='fakepool',
                    attribute='percent-up-members',
                    weight=30,
                    minimum_threshold=2,
                    partition='Common'
                )
            ],
            trunks=[
                dict(
                    trunk_name='faketrunk',
                    attribute='percent-up-members',
                    weight=20,
                    minimum_threshold=1
                )
            ]
        )

        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_ha_group.tmos_version')
        self.m1 = self.p1.start()
        self.m1.return_value = '12.1.0'

        p = ModuleParameters(params=args)

        assert p.name == 'foobar'
        assert p.state == 'present'
        assert p.active_bonus == 20
        assert p.enabled is True
        assert p.pools == [{'name': '/Common/fakepool', 'attribute': 'percent-up-members',
                            'weight': 30, 'threshold': 2}]
        assert p.trunks == [{'name': 'faketrunk', 'attribute': 'percent-up-members',
                             'weight': 20, 'threshold': 1}]

        self.p1.stop()


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()

        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_ha_group.tmos_version')
        self.m1 = self.p1.start()
        self.m1.return_value = '13.1.0'
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_ha_group.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = True

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()

    def test_create_ha_group(self, *args):
        set_module_args(dict(
            name='fake_group',
            state='present',
            description='baz',
            active_bonus=20,
            enable='yes',
            pools=[
                dict(
                    pool_name='fakepool',
                    attribute='percent-up-members',
                    weight=30,
                    minimum_threshold=2,
                    partition='Common'
                )
            ],
            trunks=[
                dict(
                    trunk_name='faketrunk',
                    attribute='percent-up-members',
                    weight=20,
                    minimum_threshold=1
                )
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
        assert results['name'] == 'fake_group'
        assert results['description'] == 'baz'
        assert results['active_bonus'] == 20
        assert results['enable'] == 'yes'
        assert results['pools'] == [{'pool_name': '/Common/fakepool', 'attribute': 'percent-up-members',
                                     'weight': 30, 'minimum_threshold': 2}]
        assert results['trunks'] == [{'trunk_name': 'faketrunk', 'attribute': 'percent-up-members',
                                      'weight': 20, 'minimum_threshold': 1}]
