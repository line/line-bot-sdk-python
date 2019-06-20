# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from __future__ import unicode_literals, absolute_import

import unittest

import responses

from linebot import (
    LineBotApi
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

    @responses.activate
    def test_get_message_quota(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/quota',
            json={
                'type': 'limited',
                'value': 1000
            },
            status=200
        )
        res = self.tested.get_message_quota()
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('limited', res.type)
        self.assertEqual(1000, res.value)

    @responses.activate
    def test_get_message_quota_2(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/quota',
            json={'type': 'none'},
            status=200
        )
        res = self.tested.get_message_quota()
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('none', res.type)

    @responses.activate
    def test_get_message_quota_consumption(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/quota/consumption',
            json={'totalUsage': 500},
            status=200
        )
        res = self.tested.get_message_quota_consumption()
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(500, res.total_usage)


if __name__ == '__main__':
    unittest.main()
