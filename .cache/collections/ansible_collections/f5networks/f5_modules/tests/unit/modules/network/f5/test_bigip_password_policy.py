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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_password_policy import (
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
            expiration_warning=7,
            max_duration=99999,
            max_login_failures=0,
            min_duration=0,
            min_length=6,
            password_memory=0,
            policy_enforcement=False,
            required_lowercase=0,
            required_numeric=0,
            required_special=0,
            required_uppercase=0,
        )

        p = ModuleParameters(params=args)
        assert p.expiration_warning == 7
        assert p.max_duration == 99999
        assert p.max_login_failures == 0
        assert p.min_duration == 0
        assert p.password_memory == 0
        assert p.policy_enforcement == 'no'
        assert p.required_lowercase == 0
        assert p.required_numeric == 0
        assert p.required_special == 0
        assert p.required_uppercase == 0

    def test_api_parameters(self):
        args = load_fixture('load_tm_auth_password_policy_1.json')

        p = ApiParameters(params=args)
        assert p.expiration_warning == 7
        assert p.max_duration == 99999
        assert p.max_login_failures == 0
        assert p.min_duration == 0
        assert p.password_memory == 0
        assert p.policy_enforcement == 'no'
        assert p.required_lowercase == 0
        assert p.required_numeric == 0
        assert p.required_special == 0
        assert p.required_uppercase == 0


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_password_policy.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_password_policy.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_partition(self, *args):
        set_module_args(dict(
            expiration_warning=7,
            max_duration=9999,
            max_login_failures=0,
            min_duration=0,
            min_length=6,
            password_memory=0,
            policy_enforcement='no',
            required_lowercase=0,
            required_numeric=0,
            required_special=0,
            required_uppercase=0,
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = ApiParameters(params=load_fixture('load_tm_auth_password_policy_1.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(side_effect=[False, True])
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
