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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_profile_sip import (
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
            parent='bar',
            security=False,
            description='my description',
            community='foo_community',
            dialog_aware=True,
            enable_sip_firewall=False,
            insert_via_header=True,
            user_via_header='SIP/2.0/UDP 10.10.10.10:5060',
            secure_via_header=True,
            terminate_on_bye=False,
            max_size=2048,
            log_profile='alg_profile',
            log_publisher='baz_publish',
            insert_record_route_header=True,
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.parent == '/Common/bar'
        assert p.security == 'disabled'
        assert p.description == 'my description'
        assert p.community == 'foo_community'
        assert p.dialog_aware == 'enabled'
        assert p.enable_sip_firewall == 'no'
        assert p.insert_via_header == 'enabled'
        assert p.user_via_header == 'SIP/2.0/UDP 10.10.10.10:5060'
        assert p.terminate_on_bye == 'disabled'
        assert p.max_size == 2048
        assert p.log_profile == '/Common/alg_profile'
        assert p.log_publisher == '/Common/baz_publish'
        assert p.insert_record_route_header == 'enabled'

    def test_api_parameters(self):
        args = load_fixture('load_profile_sip.json')
        p = ApiParameters(params=args)
        assert p.name == 'foobar'
        assert p.max_size == 65535
        assert p.parent == '/Common/sip'
        assert p.dialog_aware == 'enabled'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_profile_sip.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_profile_sip.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_sip_profile(self, *args):
        # Configure the arguments that would be sent to the Ansible module
        set_module_args(dict(
            name='foo',
            parent='bar',
            max_size=8192,
            log_profile='alg_profile',
            log_publisher='baz_publish',
            dialog_aware='yes',
            enable_sip_firewall='no',
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
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['parent'] == '/Common/bar'
        assert results['max_size'] == 8192
        assert results['log_profile'] == '/Common/alg_profile'
        assert results['log_publisher'] == '/Common/baz_publish'
        assert results['dialog_aware'] == 'yes'
        assert results['enable_sip_firewall'] == 'no'

    def test_update_sip_profile(self, *args):
        set_module_args(dict(
            name='foobar',
            description='my description',
            insert_via_header=True,
            user_via_header='SIP/2.0/UDP 10.10.10.10:5060',
            secure_via_header=True,
            terminate_on_bye=False,
            max_size=2048,
            log_profile='alg_profile',
            log_publisher='baz_publish',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = ApiParameters(params=load_fixture('load_profile_sip.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()
        assert results['changed'] is True
        assert results['description'] == 'my description'
        assert results['insert_via_header'] == 'yes'
        assert results['user_via_header'] == 'SIP/2.0/UDP 10.10.10.10:5060'
        assert results['secure_via_header'] == 'yes'
        assert results['terminate_on_bye'] == 'no'
        assert results['max_size'] == 2048
        assert results['log_profile'] == '/Common/alg_profile'
        assert results['log_publisher'] == '/Common/baz_publish'
