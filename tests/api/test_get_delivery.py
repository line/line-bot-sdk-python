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
        self.date = '20190101'

    @responses.activate
    def test_get_delivery_broadcast(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/delivery/broadcast?date={}'.format(self.date),
            json={
                'status': 'ready',
                'success': 10000
            },
            status=200
        )

        res = self.tested.get_message_delivery_broadcast(self.date)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('ready', res.status)
        self.assertEqual(10000, res.success)

    @responses.activate
    def test_get_delivery_push(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/delivery/push?date={}'.format(self.date),
            json={
                'status': 'ready',
                'success': 10000
            },
            status=200
        )

        res = self.tested.get_message_delivery_push(self.date)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('ready', res.status)
        self.assertEqual(10000, res.success)

    @responses.activate
    def test_get_delivery_reply(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/delivery/reply?date={}'.format(self.date),
            json={
                'status': 'ready',
                'success': 10000
            },
            status=200
        )

        res = self.tested.get_message_delivery_reply(self.date)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('ready', res.status)
        self.assertEqual(10000, res.success)

    @responses.activate
    def test_get_delivery_multicast(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT +
            '/v2/bot/message/delivery/multicast?date={}'.format(self.date),
            json={
                'status': 'ready',
                'success': 10000
            },
            status=200
        )

        res = self.tested.get_message_delivery_multicast(self.date)
        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual('ready', res.status)
        self.assertEqual(10000, res.success)


if __name__ == '__main__':
    unittest.main()
