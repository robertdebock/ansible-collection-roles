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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_command import (
    Parameters, ModuleManager, V1Manager, V2Manager, ArgumentSpec
)
from ansible_collections.f5networks.f5_modules.tests.unit.compat import unittest
from ansible_collections.f5networks.f5_modules.tests.unit.compat.mock import Mock, patch
from ansible_collections.f5networks.f5_modules.tests.unit.modules.utils import set_module_args

fixture_path = os.path.join(os.path.dirname(__file__), 'fixtures')
fixture_data = {}


def load_fixture(name):
    path = os.path.join(fixture_path, name)
    with open(path) as f:
        data = f.read()
    try:
        data = json.loads(data)
    except Exception:
        pass
    return data


class TestParameters(unittest.TestCase):

    def test_module_parameters(self):
        args = dict(
            commands=[
                "tmsh show sys version"
            ],
        )
        p = Parameters(params=args)
        assert len(p.commands) == 1


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.patcher1 = patch('time.sleep')
        self.patcher1.start()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_command.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_command.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.patcher1.stop()
        self.p2.stop()
        self.p3.stop()

    def test_run_single_command(self, *args):
        set_module_args(dict(
            commands=[
                "tmsh show sys version"
            ],
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

        m1 = V2Manager(module=module)
        m1.execute_on_device = Mock(return_value=['resp1', 'resp2'])

        mm = ModuleManager(module=module)
        mm._run_commands = Mock(return_value=[])
        mm.get_manager = Mock(return_value=m1)

        results = mm.exec_module()

        assert results['changed'] is False
        assert mm._run_commands.call_count == 0

    def test_run_single_modification_command(self, *args):
        set_module_args(dict(
            commands=[
                "tmsh create ltm virtual foo"
            ],
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

        m1 = V2Manager(module=module)
        m1.execute_on_device = Mock(return_value=['resp1', 'resp2'])

        mm = ModuleManager(module=module)
        mm._run_commands = Mock(return_value=[])
        mm.get_manager = Mock(return_value=m1)

        results = mm.exec_module()

        assert results['changed'] is True
        assert mm._run_commands.call_count == 0

    def test_cli_command(self, *args):
        set_module_args(dict(
            commands=[
                "show sys version"
            ],
            provider=dict(
                server='localhost',
                password='password',
                user='admin',
                transport='cli'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode
        )

        m1 = V1Manager(module=module)
        m1.execute_on_device = Mock(return_value=['resp1', 'resp2', 'resp3'])

        mm = ModuleManager(module=module)
        mm._run_commands = Mock(return_value=[])
        mm.get_manager = Mock(return_value=m1)

        results = mm.exec_module()

        assert results['changed'] is False

        # call count is two on CLI transport because we must first
        # determine if the remote CLI is in tmsh mode or advanced shell
        # (bash) mode.
        #
        # 1 call for the shell check
        # 1 call for the command in the "commands" list above
        #
        # Can we change this in the future by making the terminal plugin
        # find this out ahead of time?
        assert m1.execute_on_device.call_count == 3

    def test_command_with_commas(self, *args):
        set_module_args(dict(
            commands="""
              tmsh create /auth ldap system-auth {bind-dn uid=binduser,
              cn=users,dc=domain,dc=com bind-pw $ENCRYPTEDPW check-roles-group
              enabled search-base-dn cn=users,dc=domain,dc=com servers add {
              ldap.server.com } }
            """,
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
        m1 = V2Manager(module=module)
        m1.execute_on_device = Mock(return_value=['resp1', 'resp2'])

        mm = ModuleManager(module=module)
        mm.get_manager = Mock(return_value=m1)

        results = mm.exec_module()

        assert results['changed'] is True

    def test_normalizing_command_show(self, *args):
        args = dict(
            commands=[
                "show sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'show sys version'

    def test_normalizing_command_delete(self, *args):
        args = dict(
            commands=[
                "delete sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'delete sys version'

    def test_normalizing_command_modify(self, *args):
        args = dict(
            commands=[
                "modify sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'modify sys version'

    def test_normalizing_command_list(self, *args):
        args = dict(
            commands=[
                "list sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'list sys version'

    def test_normalizing_command_tmsh_show(self, *args):
        args = dict(
            commands=[
                "tmsh show sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'show sys version'

    def test_normalizing_command_tmsh_delete(self, *args):
        args = dict(
            commands=[
                "tmsh delete sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'delete sys version'

    def test_normalizing_command_tmsh_modify(self, *args):
        args = dict(
            commands=[
                "tmsh modify sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'modify sys version'

    def test_normalizing_command_tmsh_list(self, *args):
        args = dict(
            commands=[
                "tmsh list sys version"
            ],
        )

        result = V2Manager.normalize_commands(args['commands'])

        assert result[0] == 'list sys version'
