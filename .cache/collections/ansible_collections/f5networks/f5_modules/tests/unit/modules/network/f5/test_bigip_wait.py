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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_wait import (
    Parameters, ModuleManager, V2Manager, ArgumentSpec
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
            type='standard',
            delay=3,
            timeout=500,
            sleep=10,
            msg='We timed out during waiting for BIG-IP :-('
        )

        p = Parameters(params=args)
        assert p.delay == 3
        assert p.timeout == 500
        assert p.sleep == 10
        assert p.msg == 'We timed out during waiting for BIG-IP :-('

    def test_module_string_parameters(self):
        args = dict(
            type='standard',
            delay='3',
            timeout='500',
            sleep='10',
            msg='We timed out during waiting for BIG-IP :-('
        )

        p = Parameters(params=args)
        assert p.delay == 3
        assert p.timeout == 500
        assert p.sleep == 10
        assert p.msg == 'We timed out during waiting for BIG-IP :-('


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_wait.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_wait.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()
        self.patcher1.stop()

    def test_wait_already_available(self, *args):
        set_module_args(dict(
            provider=dict(
                server='localhost',
                password='password',
                user='admin',
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods to force specific logic in the module to happen
        m1 = V2Manager(module=module)
        mm = ModuleManager(module=module)
        mm.get_manager = Mock(return_value=m1)

        m1._connect_to_device = Mock(return_value=True)
        m1._device_is_rebooting = Mock(return_value=False)
        m1._is_mprov_running_on_device = Mock(return_value=False)
        m1._get_client_connection = Mock(return_value=True)
        m1._rest_endpoints_ready = Mock(side_effect=[False, False, True])

        results = mm.exec_module()

        assert results['changed'] is False
        assert results['elapsed'] == 0
