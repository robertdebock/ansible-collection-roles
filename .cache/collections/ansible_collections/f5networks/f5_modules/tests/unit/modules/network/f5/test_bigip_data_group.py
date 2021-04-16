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

from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_data_group import (
    ModuleParameters, ModuleManager, ExternalManager, InternalManager,
    ArgumentSpec, RecordsEncoder, RecordsDecoder
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


class TestAuxClasses(unittest.TestCase):
    def setUp(self):
        self.ip_encode = RecordsEncoder(record_type='ip', separator=':=')
        self.int_encode = RecordsEncoder(record_type='int', separator=':=')
        self.str_encode = RecordsEncoder(record_type='str', separator=':=')
        self.ip_decode = RecordsDecoder(record_type='ip', separator=':=')
        self.int_decode = RecordsDecoder(record_type='int', separator=':=')
        self.str_decode = RecordsDecoder(record_type='str', separator=':=')

    def test_encode_ipv6_ipv4_cidr_dict(self, *args):
        dg1 = dict(key='10.0.0.0/8', value='Network1')
        dg2 = dict(key='2402:6940::/32', value='Network2')
        dg3 = dict(key='192.168.1.1/32', value='Host1')
        dg4 = dict(key='2402:9400:1000::/128', value='Host2')

        net1 = self.ip_encode.encode(dg1)
        net2 = self.ip_encode.encode(dg2)
        host1 = self.ip_encode.encode(dg3)
        host2 = self.ip_encode.encode(dg4)

        assert net1 == 'network 10.0.0.0 prefixlen 8 := Network1'
        assert net2 == 'network 2402:6940:: prefixlen 32 := Network2'
        assert host1 == 'host 192.168.1.1 := Host1'
        assert host2 == 'host 2402:9400:1000:: := Host2'

    def test_encode_ipv6_ipv4_cidr_rd_dict(self, *args):
        dg1 = dict(key='10.0.0.0%11/8', value='Network1')
        dg2 = dict(key='2402:6940::%11/32', value='Network2')
        dg3 = dict(key='192.168.1.1%11/32', value='Host1')
        dg4 = dict(key='2402:9400:1000::%11/128', value='Host2')

        net1 = self.ip_encode.encode(dg1)
        net2 = self.ip_encode.encode(dg2)
        host1 = self.ip_encode.encode(dg3)
        host2 = self.ip_encode.encode(dg4)

        assert net1 == 'network 10.0.0.0%11 prefixlen 8 := Network1'
        assert net2 == 'network 2402:6940::%11 prefixlen 32 := Network2'
        assert host1 == 'host 192.168.1.1%11 := Host1'
        assert host2 == 'host 2402:9400:1000::%11 := Host2'

    def test_encode_ipv6_ipv4_cidr_str(self, *args):
        dg1 = '10.0.0.0/8'
        dg2 = '2402:6940::/32 := Network2'
        dg3 = '192.168.1.1/32 := Host1'
        dg4 = '2402:9400:1000::/128'

        net1 = self.ip_encode.encode(dg1)
        net2 = self.ip_encode.encode(dg2)
        host1 = self.ip_encode.encode(dg3)
        host2 = self.ip_encode.encode(dg4)

        assert net1 == 'network 10.0.0.0 prefixlen 8 := 10.0.0.0'
        assert net2 == 'network 2402:6940:: prefixlen 32 := Network2'
        assert host1 == 'host 192.168.1.1 := Host1'
        assert host2 == 'host 2402:9400:1000:: := 2402:9400:1000::'

    def test_encode_ipv6_ipv4_cidr_rd_str(self, *args):
        dg1 = '10.0.0.0%12/8'
        dg2 = 'network 2402:6940::%12 prefixlen 32 := Network2'
        dg3 = 'host 192.168.1.1%12 := Host1'
        dg4 = '2402:9400:1000::%12/128'

        net1 = self.ip_encode.encode(dg1)
        net2 = self.ip_encode.encode(dg2)
        host1 = self.ip_encode.encode(dg3)
        host2 = self.ip_encode.encode(dg4)

        assert net1 == 'network 10.0.0.0%12 prefixlen 8 := 10.0.0.0%12'
        assert net2 == 'network 2402:6940::%12 prefixlen 32 := Network2'
        assert host1 == 'host 192.168.1.1%12 := Host1'
        assert host2 == 'host 2402:9400:1000::%12 := 2402:9400:1000::%12'

    def test_encode_host_net_ptrn_str(self, *args):
        dg1 = 'network 10.0.0.0 prefixlen 8 := Network1'
        dg2 = 'network 2402:6940:: prefixlen 32 := Network2'
        dg3 = 'host 192.168.1.1 := Host1'
        dg4 = 'host 2402:9400:1000:: := Host2'

        net1 = self.ip_encode.encode(dg1)
        net2 = self.ip_encode.encode(dg2)
        host1 = self.ip_encode.encode(dg3)
        host2 = self.ip_encode.encode(dg4)

        assert net1 == 'network 10.0.0.0 prefixlen 8 := Network1'
        assert net2 == 'network 2402:6940:: prefixlen 32 := Network2'
        assert host1 == 'host 192.168.1.1 := Host1'
        assert host2 == 'host 2402:9400:1000:: := Host2'

    def test_encode_int_and_str(self, *args):
        dg1 = dict(key=1, value='one')
        dg2 = '10'
        dg3 = dict(key='one', value='is_not_the_answer')
        dg4 = 'fifty'

        int1 = self.int_encode.encode(dg1)
        int2 = self.int_encode.encode(dg2)
        str1 = self.str_encode.encode(dg3)
        str2 = self.str_encode.encode(dg4)

        assert int1 == '1 := one'
        assert int2 == '10 := ""'
        assert str1 == 'one := is_not_the_answer'
        assert str2 == 'fifty := ""'

    def test_decode_ipv6_ipv4_cidr_rd(self, *args):
        dg1 = 'network 192.168.0.0%11 prefixlen 16 := "Network3"'
        dg2 = 'network 2402:9400:1000:0::%11 prefixlen 64 := "Network4"'
        dg3 = 'host 172.16.1.1%11 := "Host3"'
        dg4 = 'host 2001:0db8:85a3:0000:0000:8a2e:0370:7334%11 := "Host4"'

        net1 = self.ip_decode.decode(dg1)
        net2 = self.ip_decode.decode(dg2)
        host1 = self.ip_decode.decode(dg3)
        host2 = self.ip_decode.decode(dg4)

        assert net1 == dict(name='192.168.0.0%11/16', data='Network3')
        assert net2 == dict(name='2402:9400:1000:0::%11/64', data='Network4')
        assert host1 == dict(name='172.16.1.1%11/32', data='Host3')
        assert host2 == dict(name='2001:0db8:85a3:0000:0000:8a2e:0370:7334%11/128', data='Host4')

    def test_decode_int_str(self, *args):
        dg1 = '10'
        dg2 = 'one := "is_not_the_answer"'

        int1 = self.int_decode.decode(dg1)
        str1 = self.str_decode.decode(dg2)

        assert int1 == dict(name='10', data="")
        assert str1 == dict(name='one', data='is_not_the_answer')


class TestParameters(unittest.TestCase):
    def test_module_parameters(self):
        args = dict(
            name='foo',
            type='address',
            delete_data_group_file=False,
            internal=False,
            records=[
                dict(
                    key='10.10.10.10/32',
                    value='bar'
                )
            ],
            separator=':=',
            state='present',
            partition='Common'
        )

        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.type == 'ip'
        assert p.delete_data_group_file is False
        assert len(p.records) == 1
        assert 'data' in p.records[0]
        assert 'name' in p.records[0]
        assert p.records[0]['data'] == 'bar'
        assert p.records[0]['name'] == '10.10.10.10/32'
        assert p.separator == ':='
        assert p.state == 'present'
        assert p.partition == 'Common'


class TestManager(unittest.TestCase):

    def setUp(self):
        self.spec = ArgumentSpec()
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_data_group.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_data_group.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p2.stop()
        self.p3.stop()

    def test_create_external_datagroup_type_string(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=False,
            records_src="{0}/data-group-string.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = ExternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True

    def test_create_external_incorrect_address_data(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=False,
            type='address',
            records_src="{0}/data-group-string.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = ExternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        with pytest.raises(F5ModuleError) as ex:
            mm0.exec_module()

        assert "When specifying an 'address' type, the value to the left of the separator must be an IP." == str(ex.value)

    def test_create_external_incorrect_integer_data(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=False,
            type='integer',
            records_src="{0}/data-group-string.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = ExternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        with pytest.raises(F5ModuleError) as ex:
            mm0.exec_module()

        assert "When specifying an 'integer' type, the value to the left of the separator must be a number." == str(ex.value)

    def test_remove_data_group_keep_file(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=False,
            state='absent',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = ExternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[True, False])
        mm1.remove_from_device = Mock(return_value=True)
        mm1.external_file_exists = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True

    def test_remove_data_group_remove_file(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=True,
            internal=False,
            state='absent',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = ExternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[True, False])
        mm1.remove_from_device = Mock(return_value=True)
        mm1.external_file_exists = Mock(return_value=True)
        mm1.remove_data_group_file_from_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True

    def test_create_internal_datagroup_type_string(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=True,
            records_src="{0}/data-group-string.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = InternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True

    def test_create_internal_incorrect_integer_data(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=True,
            type='integer',
            records_src="{0}/data-group-string.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = InternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        with pytest.raises(F5ModuleError) as ex:
            mm0.exec_module()

        assert "When specifying an 'integer' type, the value to the left of the separator must be a number." == str(ex.value)

    def test_create_internal_datagroup_type_integer(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=True,
            type='integer',
            records_src="{0}/data-group-integer.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = InternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True

    def test_create_internal_datagroup_type_address(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=True,
            type='address',
            records_src="{0}/data-group-address.txt".format(fixture_path),
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = InternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True

    def test_create_internal_datagroup_type_address_list(self, *args):
        set_module_args(dict(
            name='foo',
            delete_data_group_file=False,
            internal=True,
            type='address',
            records=[
                dict(
                    key='10.0.0.0/8',
                    value='Network1'
                ),
                dict(
                    key='172.16.0.0/12',
                    value='Network2'
                ),
                dict(
                    key='192.168.20.1/16',
                    value='Network3'
                ),
                dict(
                    key='192.168.20.1',
                    value='Host1'
                ),
                dict(
                    key='172.16.1.1',
                    value='Host2'
                )
            ],
            separator=':=',
            state='present',
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
            mutually_exclusive=self.spec.mutually_exclusive,
        )

        # Override methods in the specific type of manager
        mm1 = InternalManager(module=module, params=module.params)
        mm1.exists = Mock(side_effect=[False, True])
        mm1.create_on_device = Mock(return_value=True)

        # Override methods to force specific logic in the module to happen
        mm0 = ModuleManager(module=module)
        mm0.get_manager = Mock(return_value=mm1)

        results = mm0.exec_module()

        assert results['changed'] is True
