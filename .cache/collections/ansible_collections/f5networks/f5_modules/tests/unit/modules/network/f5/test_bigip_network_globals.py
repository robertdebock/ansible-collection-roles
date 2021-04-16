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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_network_globals import (
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
            stp=dict(
                config_name='foobar',
                config_revision=1,
                description='description',
                fwd_delay=16,
                hello_time=2,
                max_age=6,
                max_hops=2,
                mode='mstp',
                transmit_hold=1
            ),
            multicast=dict(
                max_pending_packets=2000,
                max_pending_routes=200,
                rate_limit=True,
                route_lookup_timeout=80000,
            ),
            dag=dict(
                round_robin_mode='local',
                dag_ipv6_prefix_len=64,
                icmp_hash='ipicmp',
            ),
            lldp=dict(
                enabled=True,
                max_neighbors_per_port=200,
                reinit_delay=1000,
                tx_delay=1500,
                tx_hold=200,
                tx_interval=100
            )
        )
        p = ModuleParameters(params=args)
        assert p.stp_config_name == 'foobar'
        assert p.stp_config_revision == 1
        assert p.stp_description == 'description'
        assert p.stp_fwd_delay == 16
        assert p.stp_hello_time == 2
        assert p.stp_max_age == 6
        assert p.stp_max_hops == 2
        assert p.stp_mode == 'mstp'
        assert p.stp_transmit_hold == 1
        assert p.mcast_max_pending_packets == 2000
        assert p.mcast_max_pending_routes == 200
        assert p.mcast_rate_limit == 'enabled'
        assert p.mcast_route_lookup_timeout == 80000
        assert p.dag_round_robin_mode == 'local'
        assert p.dag_ipv6_prefix_len == 64
        assert p.dag_icmp_hash == 'ipicmp'
        assert p.lldp_enabled is True
        assert p.lldp_disabled is None
        assert p.lldp_max_neighbors_per_port == 200
        assert p.lldp_reinit_delay == 1000
        assert p.lldp_tx_delay == 1500
        assert p.lldp_tx_hold == 200
        assert p.lldp_tx_interval == 100

    def test_api_parameters(self):
        args = dict(
            stp=load_fixture('load_stp_globals.json'),
            multicast=load_fixture('load_mcast_globals.json'),
            dag=load_fixture('load_dag_globals.json'),
            lldp=load_fixture('load_lldp_globals.json')
        )

        p = ApiParameters(params=args)

        assert p.stp_config_name is None
        assert p.stp_config_revision == 0
        assert p.stp_description is None
        assert p.stp_fwd_delay == 15
        assert p.stp_hello_time == 2
        assert p.stp_max_age == 20
        assert p.stp_max_hops == 20
        assert p.stp_mode == 'passthru'
        assert p.stp_transmit_hold == 6
        assert p.mcast_max_pending_packets == 16
        assert p.mcast_max_pending_routes == 256
        assert p.mcast_rate_limit == 'enabled'
        assert p.mcast_route_lookup_timeout == 2
        assert p.dag_round_robin_mode == 'global'
        assert p.dag_ipv6_prefix_len == 128
        assert p.dag_icmp_hash == 'icmp'
        assert p.lldp_enabled is None
        assert p.lldp_disabled is True
        assert p.lldp_max_neighbors_per_port == 10
        assert p.lldp_reinit_delay == 2
        assert p.lldp_tx_delay == 0
        assert p.lldp_tx_hold == 5
        assert p.lldp_tx_interval == 0


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_network_globals.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_network_globals.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_update_all_settings(self, *args):
        set_module_args(dict(
            stp=dict(
                config_name='foobar',
                config_revision=1,
                max_hops=2,
                mode='mstp',
                transmit_hold=1
            ),
            multicast=dict(
                max_pending_routes=200,
                rate_limit='no',
            ),
            dag=dict(
                round_robin_mode='local',
                dag_ipv6_prefix_len=64,
                icmp_hash='ipicmp',
            ),
            lldp=dict(
                enabled='yes',
                tx_delay=1500,
                tx_hold=200,
                tx_interval=100
            ),
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = dict(
            stp=load_fixture('load_stp_globals.json'),
            multicast=load_fixture('load_mcast_globals.json'),
            dag=load_fixture('load_dag_globals.json'),
            lldp=load_fixture('load_lldp_globals.json')
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_one_of=self.spec.required_one_of
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=ApiParameters(params=current))

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['stp']['config_name'] == 'foobar'
        assert results['stp']['config_revision'] == 1
        assert results['stp']['max_hops'] == 2
        assert results['stp']['mode'] == 'mstp'
        assert results['stp']['transmit_hold'] == 1
        assert results['dag']['dag_ipv6_prefix_len'] == 64
        assert results['dag']['icmp_hash'] == 'ipicmp'
        assert results['multicast']['rate_limit'] == 'no'
        assert results['multicast']['max_pending_routes'] == 200
        assert results['lldp']['enabled'] == 'yes'
        assert results['lldp']['tx_delay'] == 1500
        assert results['lldp']['tx_hold'] == 200
        assert results['lldp']['tx_interval'] == 100

    def test_update_one_group(self, *args):
        set_module_args(dict(
            stp=dict(
                hello_time=1,
                mode='rstp',
            ),
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        # Configure the parameters that would be returned by querying the
        # remote device
        current = dict(
            stp=load_fixture('load_stp_globals.json'),
            multicast=None,
            dag=None,
            lldp=None,
        )

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_one_of=self.spec.required_one_of
        )
        mm = ModuleManager(module=module)

        # Override methods to force specific logic in the module to happen
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=ApiParameters(params=current))

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['stp']['hello_time'] == 1
        assert results['stp']['mode'] == 'rstp'
