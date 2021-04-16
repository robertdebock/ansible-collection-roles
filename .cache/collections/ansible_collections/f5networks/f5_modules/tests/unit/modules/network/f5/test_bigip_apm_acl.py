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
from ansible_collections.f5networks.f5_modules.plugins.modules.bigip_apm_acl import (
    ApiParameters, ModuleParameters, ModuleManager, ArgumentSpec
)
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
    def test_module_parameters(self):
        args = dict(
            name='foo',
            acl_order=0,
            type='static',
            path_match_case=True,
            description='foobar',
            entries=[
                dict(action='allow',
                     dst_port='80',
                     dst_addr='192.168.1.1',
                     src_port='443',
                     src_addr='10.10.10.0',
                     src_mask='255.255.255.128',
                     protocol='tcp',
                     host_name='foobar.com',
                     paths='/shopfront',
                     scheme='https'
                     )
            ]
        )
        p = ModuleParameters(params=args)
        assert p.name == 'foo'
        assert p.acl_order == 0
        assert p.type == 'static'
        assert p.path_match_case == 'true'
        assert p.description == 'foobar'
        assert p.entries[0] == dict(action='allow',
                                    dstEndPort=80,
                                    dstStartPort=80,
                                    dstSubnet='192.168.1.1/32',
                                    srcEndPort=443,
                                    srcStartPort=443,
                                    srcSubnet='10.10.10.0/25',
                                    protocol=6,
                                    host='foobar.com',
                                    paths='/shopfront',
                                    scheme='https'
                                    )

    def test_api_parameters(self):
        args = load_fixture('load_apm_acl.json')

        p = ApiParameters(params=args)
        assert p.name == 'lastone'
        assert p.acl_order == 2
        assert p.type == 'static'
        assert p.path_match_case == 'false'
        assert p.description == 'foobar'
        assert p.entries[0] == dict(action='discard',
                                    dstEndPort=0,
                                    dstStartPort=0,
                                    dstSubnet='0.0.0.0/0',
                                    srcEndPort=0,
                                    srcStartPort=0,
                                    srcSubnet='0.0.0.0/0',
                                    protocol=1,
                                    scheme='any',
                                    log='none'
                                    )


class TestManager(unittest.TestCase):
    def setUp(self):
        self.spec = ArgumentSpec()
        self.p1 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_apm_acl.module_provisioned')
        self.m1 = self.p1.start()
        self.m1.return_value = True
        self.p2 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_apm_acl.tmos_version')
        self.p3 = patch('ansible_collections.f5networks.f5_modules.plugins.modules.bigip_apm_acl.send_teem')
        self.m2 = self.p2.start()
        self.m2.return_value = '14.1.0'
        self.m3 = self.p3.start()
        self.m3.return_value = True

    def tearDown(self):
        self.p1.stop()
        self.p2.stop()
        self.p3.stop()

    def test_create_L4_L7_ACL(self, *args):
        set_module_args(dict(
            name='foo',
            acl_order=0,
            type='static',
            path_match_case=True,
            description='my description',
            entries=[
                dict(action='allow',
                     dst_port='80',
                     dst_addr='192.168.1.1',
                     src_port='443',
                     src_addr='10.10.10.0',
                     src_mask='255.255.255.128',
                     protocol='tcp',
                     host_name='foobar.com',
                     paths='/shopfront',
                     scheme='https'
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
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=False)
        mm.create_on_device = Mock(return_value=True)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['acl_order'] == 0
        assert results['description'] == 'my description'
        assert results['type'] == 'static'
        assert results['path_match_case'] == 'yes'
        assert results['entries'] == [
            dict(action='allow',
                 dst_port='80',
                 dst_addr='192.168.1.1',
                 src_port='443',
                 src_addr='10.10.10.0',
                 src_mask='255.255.255.128',
                 protocol='tcp',
                 host_name='foobar.com',
                 paths='/shopfront',
                 scheme='https'
                 )]

    def test_update_L4_L7_ACL(self, *args):
        set_module_args(dict(
            name='lastone',
            acl_order=0,
            path_match_case='yes',
            entries=[
                dict(action='allow',
                     dst_port='80',
                     dst_addr='192.168.1.1',
                     src_port='443',
                     src_addr='10.10.10.0',
                     src_mask='255.255.255.128',
                     protocol='tcp',
                     host_name='foobar.com',
                     paths='/shopfront',
                     scheme='https'
                     )
            ],
            provider=dict(
                server='localhost',
                password='password',
                user='admin'
            )
        ))

        current = ApiParameters(params=load_fixture('load_apm_acl.json'))

        module = AnsibleModule(
            argument_spec=self.spec.argument_spec,
            supports_check_mode=self.spec.supports_check_mode,
        )

        # Override methods in the specific type of manager
        mm = ModuleManager(module=module)
        mm.exists = Mock(return_value=True)
        mm.update_on_device = Mock(return_value=True)
        mm.read_current_from_device = Mock(return_value=current)

        results = mm.exec_module()

        assert results['changed'] is True
        assert results['acl_order'] == 0
        assert results['path_match_case'] == 'yes'
        assert results['entries'] == [
            dict(action='allow',
                 dst_port='80',
                 dst_addr='192.168.1.1',
                 src_port='443',
                 src_addr='10.10.10.0',
                 src_mask='255.255.255.128',
                 protocol='tcp',
                 host_name='foobar.com',
                 paths='/shopfront',
                 scheme='https'
                 )]
