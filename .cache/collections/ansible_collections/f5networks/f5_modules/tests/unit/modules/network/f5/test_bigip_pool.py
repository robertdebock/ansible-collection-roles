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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_pool import (
    ApiParameters, ModuleParameters, ModuleManager, ArgumentSpec
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
            monitor_type='m_of_n',
            monitors=['/Common/Fake', '/Common/Fake2'],
            quorum=1,
            slow_ramp_time=200,
            reselect_tries=5,
            service_down_action='drop'
        )

        p = ModuleParameters(params=args)
        assert p.monitor_type == 'm_of_n'
        assert p.quorum == 1
        assert p.monitors == 'min 1 of { /Common/Fake /Common/Fake2 }'
        assert p.slow_ramp_time == 200
        assert p.reselect_tries == 5
        assert p.service_down_action == 'drop'

    def test_api_parameters(self):
        args = dict(
            monitor="/Common/Fake and /Common/Fake2 ",
            slowRampTime=200,
            reselectTries=5,
            serviceDownAction='drop'
        )

        p = ApiParameters(params=args)
        assert p.monitors == '/Common/Fake and /Common/Fake2'
        assert p.slow_ramp_time == 200
        assert p.reselect_tries == 5
        assert p.service_down_action == 'drop'

    def test_unknown_module_lb_method(self):
        args = dict(
            lb_method='obscure_hyphenated_fake_method',
        )
        with pytest.raises(F5ModuleError):
            p = ModuleParameters(params=args)
            assert p.lb_method == 'foo'

    def test_unknown_api_lb_method(self):
        args = dict(
            loadBalancingMode='obscure_hypenated_fake_method'
        )
        with pytest.raises(F5ModuleError):
            p = ApiParameters(params=args)
            assert p.lb_method == 'foo'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_pool.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_pool.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_pool(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            description='fakepool',
            service_down_action='drop',
            lb_method='round-robin',
            partition='Common',
            slow_ramp_time=10,
            reselect_tries=1,
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['description'] == 'fakepool'
        assert results['service_down_action'] == 'drop'
        assert results['lb_method'] == 'round-robin'
        assert results['slow_ramp_time'] == 10
        assert results['reselect_tries'] == 1

    def test_create_pool_monitor_type_missing(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            lb_method='round-robin',
            partition='Common',
            monitors=['/Common/tcp', '/Common/http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Common/http', '/Common/tcp']
        assert results['monitor_type'] == 'and_list'

    def test_create_pool_monitors_missing(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            lb_method='round-robin',
            partition='Common',
            monitor_type='and_list',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        msg = "The 'monitors' parameter cannot be empty when " \
              "'monitor_type' parameter is specified"
        with pytest.raises(F5ModuleError) as err:
            mm.exec_module()

        assert str(err.value) == msg

    def test_create_pool_quorum_missing(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            lb_method='round-robin',
            partition='Common',
            monitor_type='m_of_n',
            monitors=['/Common/tcp', '/Common/http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        msg = "Quorum value must be specified with monitor_type 'm_of_n'."
        with pytest.raises(F5ModuleError) as err:
            mm.exec_module()

        assert str(err.value) == msg

    def test_create_pool_monitor_and_list(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            partition='Common',
            monitor_type='and_list',
            monitors=['/Common/tcp', '/Common/http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Common/http', '/Common/tcp']
        assert results['monitor_type'] == 'and_list'

    def test_create_pool_monitor_m_of_n(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            partition='Common',
            monitor_type='m_of_n',
            quorum=1,
            monitors=['/Common/tcp', '/Common/http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Common/http', '/Common/tcp']
        assert results['monitor_type'] == 'm_of_n'

    def test_update_monitors(self, *args):
        set_module_args(dict(
            name='test_pool',
            partition='Common',
            monitor_type='and_list',
            monitors=['/Common/http', '/Common/tcp'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)

        current = ApiParameters(params=load_fixture('load_ltm_pool.json'))

        mm.update_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['monitor_type'] == 'and_list'

    def test_create_pool_monitor_and_list_no_partition(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            monitor_type='and_list',
            monitors=['tcp', 'http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Common/http', '/Common/tcp']
        assert results['monitor_type'] == 'and_list'

    def test_create_pool_monitor_m_of_n_no_partition(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            monitor_type='m_of_n',
            quorum=1,
            monitors=['tcp', 'http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Common/http', '/Common/tcp']
        assert results['monitor_type'] == 'm_of_n'

    def test_create_pool_monitor_and_list_custom_partition(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            partition='Testing',
            monitor_type='and_list',
            monitors=['tcp', 'http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Testing/http', '/Testing/tcp']
        assert results['monitor_type'] == 'and_list'

    def test_create_pool_monitor_m_of_n_custom_partition(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            partition='Testing',
            monitor_type='m_of_n',
            quorum=1,
            monitors=['tcp', 'http'],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert results['monitors'] == ['/Testing/http', '/Testing/tcp']
        assert results['monitor_type'] == 'm_of_n'

    def test_create_pool_with_metadata(self, *args):
        set_module_args(dict(
            pool='fake_pool',
            metadata=dict(ansible='2.4'),
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['name'] == 'fake_pool'
        assert 'metadata' in results
        assert 'ansible' in results['metadata']
        assert results['metadata']['ansible'] == '2.4'

    def test_create_aggregate_pools(self, *args):
        set_module_args(dict(
            aggregate=[
                dict(
                    pool='fake_pool',
                    description='fakepool',
                    service_down_action='drop',
                    lb_method='round-robin',
                    partition='Common',
                    slow_ramp_time=10,
                    reselect_tries=1,
                ),
                dict(
                    pool='fake_pool2',
                    description='fakepool2',
                    service_down_action='drop',
                    lb_method='predictive-node',
                    partition='Common',
                    slow_ramp_time=110,
                    reselect_tries=2,
                )
            ],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            mutually_exclusive=self.spec.mutually_exclusive,
            required_one_of=self.spec.required_one_of
        )

        mm = ModuleManager(module=module)
        mm.create_on_device = Mock(return_value=True)
        mm.exists = Mock(return_value=False)

        results = mm.exec_module()

        assert results['changed'] is True
