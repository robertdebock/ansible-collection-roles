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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth import (
    TacacsApiParameters, TacacsModuleParameters, TacacsManager, ModuleManager, ArgumentSpec
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
            type="tacacs",
            authentication="use-all-servers",
            accounting="send-to-all-servers",
            protocol_name="ip",
            secret="$XXXXXXXXXXXXXXXXXXXX==",
            servers=['10.10.10.10', '10.10.10.11'],
            service_name="ppp",
            use_for_auth=True,
            update_secret="on_create",
        )
        p = TacacsModuleParameters(params=args)
        assert p.type == 'tacacs'
        assert p.authentication == 'use-all-servers'
        assert p.accounting == 'send-to-all-servers'

    def test_api_parameters(self):
        args = load_fixture('load_tm_auth_tacacs_1.json')
        p = TacacsApiParameters(params=args)
        assert p.authentication == 'use-first-server'
        assert p.accounting == 'send-to-first-server'
        assert p.protocol_name == 'ftp'
        assert p.secret == 'secret'
        assert p.servers == ['11.11.11.11']
        assert p.service_name == 'ppp'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_auth.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            type="tacacs",
            authentication="use-all-servers",
            accounting="send-to-all-servers",
            protocol_name="ip",
            secret="secret",
            servers=['10.10.10.10', '10.10.10.11'],
            service_name="ppp",
            use_for_auth=True,
            update_secret="on_create",
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
        m1 = TacacsManager(module=module)
        m1.exists = Mock(return_value=False)
        m1.create_on_device = Mock(return_value=True)
        m1.update_auth_source_on_device = Mock(return_value=True)

        mm = ModuleManager(module=module)
        mm.get_manager = Mock(return_value=m1)

        results = mm.exec_module()
        assert results['changed'] is True
