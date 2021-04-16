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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_remote_syslog import (
    ModuleParameters, ModuleManager, ArgumentSpec
)
from ansible_collections.f5networks.f5_modules.plugins.module_utils.common import F5ModuleError
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
            remote_host='10.10.10.10',
            remote_port=514,
            local_ip='1.1.1.1'
        )

        p = ModuleParameters(params=args)
        assert p.remote_host == '10.10.10.10'
        assert p.remote_port == 514
        assert p.local_ip == '1.1.1.1'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_remote_syslog.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_remote_syslog.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_remote_syslog(self, *args):
        set_module_args(dict(
            remote_host='1.1.1.1',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        fixture = load_fixture('load_tm_sys_syslog_1.json')
        current = fixture['remoteServers']

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

    def test_create_remote_syslog_idempotent(self, *args):
        set_module_args(dict(
            name='remotesyslog1',
            remote_host='10.10.10.10',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        fixture = load_fixture('load_tm_sys_syslog_1.json')
        current = fixture['remoteServers']

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is False

    def test_update_remote_port(self, *args):
        set_module_args(dict(
            remote_host='10.10.10.10',
            remote_port=800,
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        fixture = load_fixture('load_tm_sys_syslog_1.json')
        current = fixture['remoteServers']

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        mm.update_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['remote_port'] == 800

    def test_update_local_ip(self, *args):
        set_module_args(dict(
            remote_host='10.10.10.10',
            local_ip='2.2.2.2',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        fixture = load_fixture('load_tm_sys_syslog_1.json')
        current = fixture['remoteServers']

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        mm.update_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['local_ip'] == '2.2.2.2'

    def test_update_no_name_dupe_host(self, *args):
        set_module_args(dict(
            remote_host='10.10.10.10',
            local_ip='2.2.2.2',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        fixture = load_fixture('load_tm_sys_syslog_2.json')
        current = fixture['remoteServers']

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)
        mm.update_on_device = Mock(return_value=True)

        with pytest.raises(F5ModuleError) as ex:
            mm.exec_module()

        assert "Multiple occurrences of hostname" in str(ex.value)
