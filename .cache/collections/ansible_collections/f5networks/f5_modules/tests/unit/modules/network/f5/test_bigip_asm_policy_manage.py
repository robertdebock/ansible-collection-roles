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
from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_asm_policy_manage import (
    V1ModuleParameters, V1Manager, ModuleManager, ArgumentSpec
)
from ansible_collections.f5networks.f5_modules.plugins.module_utils.common import F5ModuleError
from ansible_collections.f5networks.f5_modules.tests.unit.modules.utils import set_module_args
from ansible_collections.f5networks.f5_modules.tests.unit.compat import unittest
from ansible_collections.f5networks.f5_modules.tests.unit.compat.mock import (
    Mock, patch
)


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
    def test_module_parameters_template(self):
        args = dict(
            name='fake_policy',
            state='present',
            template='LotusDomino 6.5 (http)'
        )

        p = V1ModuleParameters(params=args)
        assert p.name == 'fake_policy'
        assert p.state == 'present'
        assert p.template == 'POLICY_TEMPLATE_LOTUSDOMINO_6_5_HTTP'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.policy = os.path.join(fixture_path, 'fake_policy.xml')
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_asm_policy_manage.module_provisioned')
        self.m1 = self.p1.start()
        self.m1.return_value = True
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_asm_policy_manage.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_asm_policy_manage.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.patcher1.stop()
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()

    def test_activate_create_from_template(self, *args):
        set_module_args(dict(
            name='fake_policy',
            template='OWA Exchange 2007 (https)',
            state='present',
            active='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=False)
        v1.import_to_device = Mock(return_value=True)
        v1.wait_for_task = Mock(side_effect=[True, True])
        v1.read_current_from_device = Mock(return_value=current)
        v1.apply_on_device = Mock(return_value=True)
        v1.create_from_template_on_device = Mock(return_value=True)
        v1._file_is_missing = Mock(return_value=False)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_policy'
        assert results['template'] == 'OWA Exchange 2007 (https)'
        assert results['active'] == 'yes'

    def test_activate_create_by_name(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            active='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=False)
        v1.import_to_device = Mock(return_value=True)
        v1.wait_for_task = Mock(side_effect=[True, True])
        v1.create_on_device = Mock(return_value=True)
        v1.create_blank = Mock(return_value=True)
        v1.read_current_from_device = Mock(return_value=current)
        v1.apply_on_device = Mock(return_value=True)
        v1._file_is_missing = Mock(return_value=False)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_policy'
        assert results['active'] == 'yes'

    def test_activate_policy_exists_inactive(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            active='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=True)
        v1.update_on_device = Mock(return_value=True)
        v1.wait_for_task = Mock(side_effect=[True, True])
        v1.read_current_from_device = Mock(return_value=current)
        v1.apply_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['active'] == 'yes'

    def test_activate_policy_exists_active(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            active='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_active.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=True)
        v1.read_current_from_device = Mock(return_value=current)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is False

    def test_deactivate_policy_exists_active(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            active='no',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_active.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=True)
        v1.read_current_from_device = Mock(return_value=current)
        v1.update_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True

    def test_deactivate_policy_exists_inactive(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            active='no',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=True)
        v1.read_current_from_device = Mock(return_value=current)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is False

    def test_create_from_template(self, *args):
        set_module_args(dict(
            name='fake_policy',
            template='LotusDomino 6.5 (http)',
            state='present',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=False)
        v1.create_from_template_on_device = Mock(return_value=True)
        v1.wait_for_task = Mock(side_effect=[True, True])
        v1.read_current_from_device = Mock(return_value=current)
        v1._file_is_missing = Mock(return_value=False)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_policy'
        assert results['template'] == 'LotusDomino 6.5 (http)'

    def test_create_by_name(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=False)
        v1.import_to_device = Mock(return_value=True)
        v1.wait_for_task = Mock(side_effect=[True, True])
        v1.create_on_device = Mock(return_value=True)
        v1.create_blank = Mock(return_value=True)
        v1.read_current_from_device = Mock(return_value=current)
        v1.apply_on_device = Mock(return_value=True)
        v1._file_is_missing = Mock(return_value=False)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_policy'

    def test_delete_policy(self, *args):
        set_module_args(dict(
            name='fake_policy',
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
        v1 = V1Manager(module=module)
        v1.exists = Mock(side_effect=[True, False])
        v1.remove_from_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        results = mm.exec_module()

        assert results['changed'] is True

    def test_activate_policy_raises(self, *args):
        set_module_args(dict(
            name='fake_policy',
            state='present',
            active='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = V1ModuleParameters(params=load_fixture('load_asm_policy_inactive.json'))
        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        msg = 'Apply policy task failed.'
        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=True)
        v1.wait_for_task = Mock(return_value=False)
        v1.update_on_device = Mock(return_value=True)
        v1.read_current_from_device = Mock(return_value=current)
        v1.apply_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        with pytest.raises(F5ModuleError) as err:
            mm.exec_module()
        assert str(err.value) == msg

    def test_create_policy_raises(self, *args):
        set_module_args(dict(
            name='fake_policy',
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

        msg = 'Failed to create ASM policy: fake_policy'
        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(return_value=False)
        v1.create_on_device = Mock(return_value=False)
        v1._file_is_missing = Mock(return_value=False)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        with pytest.raises(F5ModuleError) as err:
            mm.exec_module()
        assert str(err.value) == msg

    def test_delete_policy_raises(self, *args):
        set_module_args(dict(
            name='fake_policy',
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
        msg = 'Failed to delete ASM policy: fake_policy'
        # Override methods to force specific logic in the module to happen
        v1 = V1Manager(module=module)
        v1.exists = Mock(side_effect=[True, True])
        v1.remove_from_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm = ModuleManager(module=module)
        mm.version_is_less_than_13 = Mock(return_value=False)
        mm.get_manager = Mock(return_value=v1)

        with pytest.raises(F5ModuleError) as err:
            mm.exec_module()
        assert str(err.value) == msg
