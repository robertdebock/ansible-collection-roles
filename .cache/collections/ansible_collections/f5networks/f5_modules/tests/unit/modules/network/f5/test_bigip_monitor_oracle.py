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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_monitor_oracle import (
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
            parent='/Common/oracle',
            interval=5,
            timeout=120,
            time_until_up=20,
            target_username='foobar',
            send='SELECT * from v$instance1',
            database='instance1',
            recv='OPEN',
            recv_column='1',
            recv_row='1',
            count=10,
            manual_resume=True,
            debug=True
        )
        p = ModuleParameters(params=args)
        assert p.parent == '/Common/oracle'
        assert p.interval == 5
        assert p.timeout == 120
        assert p.time_until_up == 20
        assert p.target_username == 'foobar'
        assert p.send == 'SELECT * from v$instance1'
        assert p.recv == 'OPEN'
        assert p.count == 10
        assert p.recv_column == '1'
        assert p.recv_row == '1'
        assert p.manual_resume == 'enabled'
        assert p.debug == 'yes'

    def test_api_parameters(self):
        args = load_fixture('load_oracle_monitor.json')
        p = ApiParameters(params=args)
        assert p.parent == '/Common/oracle'
        assert p.ip == '*'
        assert p.port == '*'
        assert p.time_until_up == 0
        assert p.up_interval == 0
        assert p.manual_resume == 'disabled'
        assert p.target_username == 'user'
        assert p.timeout == 91
        assert p.count == 1
        assert p.send == 'foo'
        assert p.recv == 'bar'
        assert p.recv_column == '3'
        assert p.recv_row == '2'
        assert p.debug == 'no'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_monitor_oracle.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_monitor_oracle.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_monitor(self, *args):
        set_module_args(dict(
            name='oracledb',
            parent='/Common/oracle',
            interval=10,
            timeout=30,
            time_until_up=5,
            target_username='foobar',
            send='SELECT * from v$instance1',
            database='instance1',
            recv='OPEN',
            recv_column='1',
            recv_row='1',
            count=10,
            manual_resume=True,
            debug=True,
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
        mm = ModuleManager(module=module)
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['parent'] == '/Common/oracle'
        assert results['interval'] == 10
        assert results['timeout'] == 30
        assert results['time_until_up'] == 5
        assert results['target_username'] == 'foobar'
        assert results['send'] == 'SELECT * from v$instance1'
        assert results['recv'] == 'OPEN'
        assert results['count'] == 10
        assert results['recv_column'] == '1'
        assert results['recv_row'] == '1'
        assert results['manual_resume'] == 'yes'
        assert results['debug'] == 'yes'
