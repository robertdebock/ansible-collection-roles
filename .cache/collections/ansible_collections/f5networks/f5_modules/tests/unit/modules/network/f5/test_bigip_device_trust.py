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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_trust import (
    Parameters, ModuleManager, ArgumentSpec
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
            peer_server='10.10.10.10',
            peer_hostname='foo.bar.baz',
            peer_user='admin',
            peer_password='secret'
        )

        p = Parameters(params=args)
        assert p.peer_server == '10.10.10.10'
        assert p.peer_hostname == 'foo.bar.baz'
        assert p.peer_user == 'admin'
        assert p.peer_password == 'secret'

    def test_module_parameters_with_peer_type(self):
        args = dict(
            peer_server='10.10.10.10',
            peer_hostname='foo.bar.baz',
            peer_user='admin',
            peer_password='secret',
            type='peer'
        )

        p = Parameters(params=args)
        assert p.peer_server == '10.10.10.10'
        assert p.peer_hostname == 'foo.bar.baz'
        assert p.peer_user == 'admin'
        assert p.peer_password == 'secret'
        assert p.type is True

    def test_module_parameters_with_subordinate_type(self):
        args = dict(
            peer_server='10.10.10.10',
            peer_hostname='foo.bar.baz',
            peer_user='admin',
            peer_password='secret',
            type='subordinate'
        )

        p = Parameters(params=args)
        assert p.peer_server == '10.10.10.10'
        assert p.peer_hostname == 'foo.bar.baz'
        assert p.peer_user == 'admin'
        assert p.peer_password == 'secret'
        assert p.type is False

    def test_hyphenated_peer_hostname(self):
        args = dict(
            peer_hostname='hn---hyphen____underscore.hmatsuda.local',
        )

        p = Parameters(params=args)
        assert p.peer_hostname == 'hn---hyphen____underscore.hmatsuda.local'

    def test_numbered_peer_hostname(self):
        args = dict(
            peer_hostname='BIG-IP_12x_ans2.example.local',
        )

        p = Parameters(params=args)
        assert p.peer_hostname == 'BIG-IP_12x_ans2.example.local'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_trust.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_trust.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_device_trust(self, *args):
        set_module_args(dict(
            peer_server='10.10.10.10',
            peer_hostname='foo.bar.baz',
            peer_user='admin',
            peer_password='secret',
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
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True

    def test_create_device_trust_idempotent(self, *args):
        set_module_args(dict(
            peer_server='10.10.10.10',
            peer_hostname='foo.bar.baz',
            peer_user='admin',
            peer_password='secret',
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
        mm.exists = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is False
