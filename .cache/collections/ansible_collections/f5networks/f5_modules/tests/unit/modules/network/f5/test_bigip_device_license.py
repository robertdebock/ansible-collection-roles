# -*- coding: utf-8 -*-
#
# Copyright: (c) 2017, F5 Networks Inc.
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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_license import (
    ModuleParameters, ModuleManager, ArgumentSpec
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
            license_key='xxxx-yyyy-zzzz',
            license_server='foo-license.f5.com',
            state='latest',
            accept_eula=True
        )

        p = ModuleParameters(params=args)
        assert p.license_key == 'xxxx-yyyy-zzzz'
        assert p.license_server == 'foo-license.f5.com'
        assert p.state == 'latest'
        assert p.accept_eula is True


class TestModuleManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_device_license.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = True

    def tearDown(self):
        self.patcher1.stop()
        self.p2.stop()

    def test_create(self, *args):
        set_module_args(
            dict(
                license_key='xxxx-yyyy-zzzz',
                license_server='foo-license.f5.com',
                accept_eula=True,
                state='latest',
                provider=dict(
                    server='localhost',
                    password='password',
                    user='admin'
                )
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[False, True])
        mm.read_dossier_from_device = Mock(return_value=True)
        mm.generate_license_from_remote = Mock(return_value=True)
        mm.upload_license_to_device = Mock(return_value=True)
        mm.upload_eula_to_device = Mock(return_value=True)
        mm.reload_license = Mock(return_value=True)
        mm._is_mcpd_ready_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True

    def test_renewal(self, *args):
        set_module_args(
            dict(
                license_key='xxxx-yyyy-zzzz',
                license_server='foo-license.f5.com',
                accept_eula=True,
                state='latest',
                provider=dict(
                    server='localhost',
                    password='password',
                    user='admin'
                )
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[True, True])
        mm.is_revoked = Mock(return_value=False)
        mm.license_valid = Mock(return_value=False)
        mm.read_dossier_from_device = Mock(return_value=True)
        mm.generate_license_from_remote = Mock(return_value=True)
        mm.upload_license_to_device = Mock(return_value=True)
        mm.upload_eula_to_device = Mock(return_value=True)
        mm.reload_license = Mock(return_value=True)
        mm._is_mcpd_ready_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True

    def test_no_renewal(self, *args):
        set_module_args(
            dict(
                license_key='xxxx-yyyy-zzzz',
                license_server='foo-license.f5.com',
                accept_eula=True,
                state='latest',
                provider=dict(
                    server='localhost',
                    password='password',
                    user='admin'
                )
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[True, True])
        mm.is_revoked = Mock(return_value=False)
        mm.license_valid = Mock(return_value=True)
        mm.read_dossier_from_device = Mock(return_value=True)
        mm.generate_license_from_remote = Mock(return_value=True)
        mm.upload_license_to_device = Mock(return_value=True)
        mm.upload_eula_to_device = Mock(return_value=True)
        mm.reload_license = Mock(return_value=True)
        mm._is_mcpd_ready_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is False

    def test_force_renewal(self, *args):
        set_module_args(
            dict(
                license_key='xxxx-yyyy-zzzz',
                license_server='foo-license.f5.com',
                accept_eula=True,
                state='latest',
                force=True,
                provider=dict(
                    server='localhost',
                    password='password',
                    user='admin'
                )
            )
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_if=self.spec.required_if
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.exists = Mock(side_effect=[True, True])
        mm.is_revoked = Mock(return_value=False)
        mm.license_valid = Mock(return_value=True)
        mm.read_dossier_from_device = Mock(return_value=True)
        mm.generate_license_from_remote = Mock(return_value=True)
        mm.upload_license_to_device = Mock(return_value=True)
        mm.upload_eula_to_device = Mock(return_value=True)
        mm.reload_license = Mock(return_value=True)
        mm._is_mcpd_ready_on_device = Mock(return_value=True)

        results = mm.exec_module()
        assert results['changed'] is True
