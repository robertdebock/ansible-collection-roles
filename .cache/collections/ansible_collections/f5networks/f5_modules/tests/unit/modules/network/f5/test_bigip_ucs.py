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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ucs import (
    ModuleParameters, ModuleManager, ArgumentSpec, V1Manager, V2Manager
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
            ucs="/root/bigip.localhost.localdomain.ucs",
            force=True,
            include_chassis_level_config=True,
            no_license=True,
            no_platform_check=True,
            passphrase="foobar",
            reset_trust=True,
            state='installed'
        )

        p = ModuleParameters(params=args)
        assert p.ucs == '/root/bigip.localhost.localdomain.ucs'
        assert p.force is True
        assert p.include_chassis_level_config is True
        assert p.no_license is True
        assert p.no_platform_check is True
        assert p.passphrase == "foobar"
        assert p.reset_trust is True
        assert p.install_command == \
            "tmsh load sys ucs /var/local/ucs/bigip.localhost.localdomain.ucs " \
            "include-chassis-level-config no-license no-platform-check " \
            "passphrase foobar reset-trust"

    def test_module_parameters_false_ucs_booleans(self):
        args = dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            include_chassis_level_config=False,
            no_license=False,
            no_platform_check=False,
            reset_trust=False
        )

        p = ModuleParameters(params=args)
        assert p.ucs == '/root/bigip.localhost.localdomain.ucs'
        assert p.include_chassis_level_config is False
        assert p.no_license is False
        assert p.no_platform_check is False
        assert p.reset_trust is False
        assert p.install_command == "tmsh load sys ucs /var/local/ucs/bigip.localhost.localdomain.ucs"


class TestV1Manager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ucs.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ucs.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '12.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()
        self.patcher1.stop()

    def test_ucs_default_present(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=True)

        vm = V1Manager(module=module)
        vm.create_on_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[False, True])

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_explicit_present(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=True)

        vm = V1Manager(module=module)
        vm.create_on_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[False, True])

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_installed(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            state='installed',
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=True)

        vm = V1Manager(module=module)
        vm.create_on_device = Mock(return_value=True)
        vm.exists = Mock(return_value=True)
        vm.install_on_device = Mock(return_value=True)

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_absent_exists(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            state='absent',
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=True)

        vm = V1Manager(module=module)
        vm.remove_from_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[True, False])

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_absent_fails(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            state='absent',
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=True)

        vm = V1Manager(module=module)
        vm.remove_from_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[True, True])

        with pytest.raises(F5ModuleError) as ex:
            vm.exec_module()
        assert 'Failed to delete' in str(ex.value)


class TestV2Manager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ucs.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_ucs.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()
        self.patcher1.stop()

    def test_ucs_default_present(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=False)

        vm = V2Manager(module=module)
        vm.create_on_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[False, True])

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_explicit_present(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=False)

        vm = V2Manager(module=module)
        vm.create_on_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[False, True])

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_installed(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            state='installed',
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=False)

        vm = V2Manager(module=module)
        vm.create_on_device = Mock(return_value=True)
        vm.exists = Mock(return_value=True)
        vm.install_on_device = Mock(return_value=True)

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_absent_exists(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            state='absent',
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=False)

        vm = V1Manager(module=module)
        vm.remove_from_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[True, False])

        results = vm.exec_module()

        assert results['changed'] is True

    def test_ucs_absent_fails(self, *args):
        set_module_args(dict(
            ucs="/root/bigip.localhost.localdomain.ucs",
            state='absent',
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

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.is_version_v1 = Mock(return_value=False)

        vm = V1Manager(module=module)
        vm.remove_from_device = Mock(return_value=True)
        vm.exists = Mock(side_effect=[True, True])

        with pytest.raises(F5ModuleError) as ex:
            vm.exec_module()
        assert 'Failed to delete' in str(ex.value)
