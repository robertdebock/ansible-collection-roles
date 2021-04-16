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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_cgnat_lsn_pool import (
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
            name='foo',
            description='foobar',
            client_conn_limit=300,
            harpin_mode='yes',
            icmp_echo='no',
            inbound_connections='explicit',
            mode='pba',
            persistence_mode='address-port',
            persistence_timeout=180,
            route_advertisement='yes',
            pba_block_idle_timeout=50,
            pba_block_lifetime=1800,
            pba_block_size=10,
            pba_client_block_limit=1,
            pba_zombie_timeout=10,
            port_range_low=1080,
            port_range_high=1090,
            egress_intf_enabled='yes',
            egress_interfaces=['tunnel1', 'tunnel2'],
            members=['10.10.10.0/25', '10.10.10.128/25'],
            backup_members=['12.12.12.0/25', '12.12.12.128/25'],
            log_profile='foo_profile',
            log_publisher='baz_publisher',
            partition='Common'
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.description == 'foobar'
        assert p.client_conn_limit == 300
        assert p.harpin_mode == 'enabled'
        assert p.icmp_echo == 'disabled'
        assert p.inbound_connections == 'explicit'
        assert p.mode == 'pba'
        assert p.persistence_mode == 'address-port'
        assert p.persistence_timeout == 180
        assert p.route_advertisement == 'enabled'
        assert p.pba_block_idle_timeout == 50
        assert p.pba_block_lifetime == 1800
        assert p.pba_block_size == 10
        assert p.pba_client_block_limit == 1
        assert p.pba_zombie_timeout == 10
        assert p.port_range_low == 1080
        assert p.port_range_high == 1090
        assert p.egress_intf_enabled == 'yes'
        assert '/Common/tunnel1' and '/Common/tunnel2' in p.egress_interfaces
        assert '12.12.10.0/25' and '12.12.12.128/25' in p.backup_members
        assert '10.10.10.0/25' and '10.10.10.128/25' in p.members
        assert p.log_profile == '/Common/foo_profile'
        assert p.log_publisher == '/Common/baz_publisher'

    def test_api_parameters(self):
        args = load_fixture('load_cgnat_lsn_pool.json')

        p = ApiParameters(params=args)
        assert p.name == 'test_pool'
        assert p.client_conn_limit == 0
        assert p.harpin_mode == 'disabled'
        assert p.icmp_echo == 'disabled'
        assert p.inbound_connections == 'disabled'
        assert p.mode == 'deterministic'
        assert p.persistence_mode == 'address'
        assert p.persistence_timeout == 300
        assert p.route_advertisement == 'disabled'
        assert p.pba_block_idle_timeout == 3600
        assert p.pba_block_lifetime == 0
        assert p.pba_block_size == 64
        assert p.pba_client_block_limit == 1
        assert p.pba_zombie_timeout == 0
        assert p.port_range_low == 1025
        assert p.port_range_high == 6954
        assert p.egress_intf_enabled == 'no'
        assert '/Common/http-tunnel' in p.egress_interfaces
        assert '11.11.11.1/32' in p.backup_members
        assert '101.10.10.0/24' in p.members
        assert p.log_profile == '/Common/lsn_log_profile'
        assert p.log_publisher == '/Common/default-ipsec-log-publisher'


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_cgnat_lsn_pool.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_cgnat_lsn_pool.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_LSN_pool(self, *args):
        set_module_args(dict(
            name='foo',
            description='foobar',
            client_conn_limit=300,
            harpin_mode='yes',
            icmp_echo='no',
            inbound_connections='explicit',
            mode='pba',
            persistence_mode='address-port',
            persistence_timeout=180,
            route_advertisement='yes',
            pba_block_idle_timeout=50,
            pba_block_lifetime=1800,
            pba_block_size=10,
            pba_client_block_limit=1,
            pba_zombie_timeout=10,
            port_range_low=1080,
            port_range_high=1090,
            egress_intf_enabled='yes',
            egress_interfaces=['tunnel1', 'tunnel2'],
            members=['10.10.10.0/25', '10.10.10.128/25'],
            backup_members=['12.12.12.0/25', '12.12.12.128/25'],
            log_profile='foo_profile',
            log_publisher='baz_publisher',
            partition='Common',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_together=self.spec.required_together,
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['description'] == 'foobar'
        assert results['client_conn_limit'] == 300
        assert results['harpin_mode'] == 'yes'
        assert results['icmp_echo'] == 'no'
        assert results['inbound_connections'] == 'explicit'
        assert results['mode'] == 'pba'
        assert results['persistence_mode'] == 'address-port'
        assert results['persistence_timeout'] == 180
        assert results['route_advertisement'] == 'yes'
        assert results['pba_block_idle_timeout'] == 50
        assert results['pba_block_lifetime'] == 1800
        assert results['pba_block_size'] == 10
        assert results['pba_client_block_limit'] == 1
        assert results['pba_zombie_timeout'] == 10
        assert results['port_range_low'] == 1080
        assert results['port_range_high'] == 1090
        assert results['egress_intf_enabled'] == 'yes'
        assert '/Common/tunnel1' and '/Common/tunnel2' in results['egress_interfaces']
        assert '12.12.10.0/25' and '12.12.12.128/25' in results['backup_members']
        assert '10.10.10.0/25' and '10.10.10.128/25' in results['members']
        assert results['log_profile'] == '/Common/foo_profile'
        assert results['log_publisher'] == '/Common/baz_publisher'

    def test_update_LSN_pool(self, *args):
        set_module_args(dict(
            name='test_pool',
            description='foobar',
            mode='napt',
            members=['15.15.15.0/25'],
            backup_members='',
            harpin_mode='yes',
            route_advertisement='yes',
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))
        current = ApiParameters(params=load_fixture('load_cgnat_lsn_pool.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
            required_together=self.spec.required_together,
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['description'] == 'foobar'
        assert results['mode'] == 'napt'
        assert results['members'] == ['15.15.15.0/25']
        assert results['backup_members'] == []
        assert results['harpin_mode'] == 'yes'
        assert results['route_advertisement'] == 'yes'
