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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth_radius import (
    ApiParameters, ModuleManager, ArgumentSpec, ModuleParameters
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
            servers=['foo1', 'foo2'],
            retries=5,
            service_type='login',
            accounting_bug=False,
            fallback_to_local=True,
            use_for_auth=True,
        )
        p = ModuleParameters(params=args)

        assert '/Common/foo1' and '/Common/foo2' in p.servers
        assert p.retries == 5
        assert p.use_for_auth == 'yes'
        assert p.accounting_bug == 'disabled'
        assert p.service_type == "login"
        assert p.fallback_to_local == 'yes'

    def test_api_parameters(self):
        args = load_fixture('load_radius_config.json')

        p = ApiParameters(params=args)
        assert p.retries == 3
        assert p.service_type == 'authenticate-only'
        assert p.accounting_bug == 'disabled'
        assert p.servers == ['/Common/system_auth_name1']


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth_radius.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth_radius.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            servers=['foo1', 'foo2'],
            retries=5,
            service_type='login',
            accounting_bug=False,
            fallback_to_local=True,
            use_for_auth=True,
            state='present',
            provider=dict(
                password='admin',
                server='localhost',
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
        mm.update_auth_source_on_device = Mock(return_value=True)
        mm.update_fallback_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True
        assert '/Common/foo1' and '/Common/foo2' in results['servers']
        assert results['retries'] == 5
        assert results['accounting_bug'] == 'disabled'
        assert results['service_type'] == 'login'
        assert results['fallback_to_local'] == 'yes'
