##############################################################################
# Copyright (c) 2017 Huawei Technologies Co.,Ltd and others.
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import unittest
import mock

from yardstick.benchmark.scenarios.lib.delete_keypair import DeleteKeypair


class DeleteKeypairTestCase(unittest.TestCase):

    @mock.patch('yardstick.common.openstack_utils.get_nova_client')
    @mock.patch('yardstick.common.openstack_utils.delete_keypair')
    def test_detach_volume(self, mock_get_nova_client, mock_delete_keypair):
        options = {
            'key_name': 'yardstick_key'
        }
        args = {"options": options}
        obj = DeleteKeypair(args, {})
        obj.run({})
        mock_get_nova_client.assert_called_once()
        mock_delete_keypair.assert_called_once()
