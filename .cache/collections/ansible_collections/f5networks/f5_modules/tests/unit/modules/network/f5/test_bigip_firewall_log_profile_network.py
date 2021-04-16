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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_log_profile_network import (
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
            profile_name='foo',
            rate_limit=150000,
            log_publisher='/Common/foobar',
            log_tcp_errors=dict(
                enabled='yes',
                rate_limit=10000,
            ),
            log_tcp_events=dict(
                enabled='yes',
                rate_limit=30000,
            ),
            log_ip_errors=dict(
                enabled='yes',
                rate_limit=60000,
            ),
            log_matches_accept_rule=dict(
                enabled='yes',
                rate_limit=80000,
            ),
            log_matches_drop_rule=dict(
                enabled='no',
                rate_limit='indefinite',
            ),
            log_matches_reject_rule=dict(
                enabled='no',
                rate_limit='indefinite',
            ),
            log_format_delimiter='.',
            log_storage_format='field-list',
            log_message_fields=['vlan', 'translated_vlan', 'src_ip']
        )

        p = ModuleParameters(params=args)
        assert p.profile_name == 'foo'
        assert p.rate_limit == 150000
        assert p.log_publisher == '/Common/foobar'
        assert p.log_tcp_events == 'enabled'
        assert p.rate_tcp_events == 30000
        assert p.log_ip_errors == 'enabled'
        assert p.rate_ip_errors == 60000
        assert p.log_tcp_errors == 'enabled'
        assert p.rate_tcp_errors == 10000
        assert p.log_acl_match_accept == 'enabled'
        assert p.rate_acl_match_accept == 80000
        assert p.log_acl_match_drop == 'disabled'
        assert p.rate_acl_match_drop == 4294967295
        assert p.log_acl_match_reject == 'disabled'
        assert p.rate_acl_match_reject == 4294967295
        assert p.log_format_delimiter == '.'
        assert p.log_storage_format == 'field-list'

    def test_api_parameters(self):
        args = load_fixture('load_afm_global_network_log_network.json')

        p = ApiParameters(params=args)
        assert p.rate_limit == 4294967295
        assert p.log_tcp_events == 'disabled'
        assert p.rate_tcp_events == 4294967295
        assert p.log_ip_errors == 'disabled'
        assert p.rate_ip_errors == 4294967295
        assert p.log_tcp_errors == 'disabled'
        assert p.rate_tcp_errors == 4294967295
        assert p.log_acl_match_accept == 'disabled'
        assert p.rate_acl_match_accept == 4294967295
        assert p.log_acl_match_drop == 'disabled'
        assert p.rate_acl_match_drop == 4294967295
        assert p.log_acl_match_reject == 'disabled'
        assert p.rate_acl_match_reject == 4294967295
        assert p.log_format_delimiter == ','
        assert p.log_storage_format == 'none'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_log_profile_network.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_firewall_log_profile_network.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            profile_name='foo',
            rate_limit=150000,
            log_publisher='/Common/foobar',
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
        mm.exists = Mock(side_effect=[False, True])
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['rate_limit'] == 150000
        assert results['log_publisher'] == '/Common/foobar'
