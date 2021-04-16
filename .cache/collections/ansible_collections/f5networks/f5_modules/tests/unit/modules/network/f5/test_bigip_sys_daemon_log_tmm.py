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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_sys_daemon_log_tmm import (
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
            arp_log_level='warning',
            http_compression_log_level='error',
            http_log_level='error',
            ip_log_level='warning',
            irule_log_level='informational',
            layer4_log_level='notice',
            net_log_level='warning',
            os_log_level='notice',
            pva_log_level='debug',
            ssl_log_level='warning',
        )
        p = ModuleParameters(params=args)
        assert p.arp_log_level == 'warning'
        assert p.http_compression_log_level == 'error'
        assert p.http_log_level == 'error'
        assert p.ip_log_level == 'warning'
        assert p.irule_log_level == 'informational'
        assert p.layer4_log_level == 'notice'
        assert p.net_log_level == 'warning'
        assert p.os_log_level == 'notice'
        assert p.pva_log_level == 'debug'
        assert p.ssl_log_level == 'warning'

    def test_api_parameters(self):
        args = load_fixture('load_tmm_log.json')
        p = ApiParameters(params=args)
        assert p.arp_log_level == 'warning'
        assert p.http_compression_log_level == 'error'
        assert p.http_log_level == 'error'
        assert p.ip_log_level == 'warning'
        assert p.irule_log_level == 'informational'
        assert p.layer4_log_level == 'notice'
        assert p.net_log_level == 'warning'
        assert p.os_log_level == 'notice'
        assert p.pva_log_level == 'informational'
        assert p.ssl_log_level == 'warning'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_sys_daemon_log_tmm.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_sys_daemon_log_tmm.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_update(self, *args):
        set_module_args(dict(
            arp_log_level='debug',
            layer4_log_level='debug',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = ApiParameters(params=load_fixture('load_tmm_log.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(return_value=False)
        mm.read_current_from_device = Mock(return_value=current)
        mm.update_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True
