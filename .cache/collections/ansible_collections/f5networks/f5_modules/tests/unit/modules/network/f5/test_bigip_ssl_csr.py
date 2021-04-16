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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ssl_csr import (
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
            name='ssl_csr_1',
            common_name='ssl_csr_1',
            key_name='ssl_key_1',
            dest='/tmp/ssl_csr_1'
        )

        p = ModuleParameters(params=args)
        assert p.name == 'ssl_csr_1'
        assert p.common_name == 'ssl_csr_1'
        assert p.key_name == 'ssl_key_1'
        assert p.dest == '/tmp/ssl_csr_1'

    def test_api_parameters(self):
        args = load_fixture('load_sys_crypto_csr.json')
        p = ApiParameters(params=args)
        assert p.name == 'ssl_csr_1'
        assert p.common_name == 'ssl_csr_1'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ssl_csr.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ssl_csr.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create(self, *args):
        set_module_args(dict(
            name='ssl_csr_1',
            common_name='ssl_csr_1',
            key_name='ssl_key_1',
            dest='/tmp/ssl_csr_1',
            force=True,
            state='present',
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
        mm.version_is_less_than_14 = Mock(return_value=False)
        mm.exists = Mock(return_value=False)
        mm.file_exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)
        mm._move_csr_to_download = Mock(return_value=True)
        mm._delete_csr = Mock(return_value=True)
        mm._download_file = Mock(return_value=True)
        mm.remove_from_device = Mock(return_value=True)

        with patch('os.path.exists') as mo:
            mo.return_value = True
            results = mm.exec_module()

        assert results['changed'] is True
