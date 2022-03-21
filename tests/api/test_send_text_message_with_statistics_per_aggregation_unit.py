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

import json
import unittest

import responses

from linebot import (
    LineBotApi
)
from linebot.models import (
    TextSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        # test data
        self.text_message = TextSendMessage(text='Hello, world')
        self.message = [{"type": "text", "text": "Hello, world"}]

    @responses.activate
    def test_push_text_message_with_statistics_per_aggregation_unit(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to',
                                 TextSendMessage(text='Hello, world'),
                                 custom_aggregation_units="promotion_a")

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "to",
                'notificationDisabled': False,
                "messages": [
                    {
                        "type": "text",
                        "text": "Hello, world"
                    }
                ],
                "customAggregationUnits": ["promotion_a"]
            }
        )

    @responses.activate
    def test_push_text_message_with_statistics_per_aggregation_unit_array(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to',
                                 TextSendMessage(text='Hello, world'),
                                 custom_aggregation_units=["promotion_a"])

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": "to",
                'notificationDisabled': False,
                "messages": [
                    {
                        "type": "text",
                        "text": "Hello, world"
                    }
                ],
                "customAggregationUnits": ["promotion_a"]
            }
        )

    @responses.activate
    def test_multicast_text_message_with_statistics_per_aggregation_unit(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to'],
                              TextSendMessage(text='Hello, world'),
                              custom_aggregation_units="promotion_a")

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ["to"],
                'notificationDisabled': False,
                "messages": [
                    {
                        "type": "text",
                        "text": "Hello, world"
                    }
                ],
                "customAggregationUnits": ["promotion_a"]
            }
        )

    @responses.activate
    def test_multicast_text_message_with_statistics_per_aggregation_unit_array(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to'],
                              TextSendMessage(text='Hello, world'),
                              custom_aggregation_units=["promotion_a"])

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ["to"],
                'notificationDisabled': False,
                "messages": [
                    {
                        "type": "text",
                        "text": "Hello, world"
                    }
                ],
                "customAggregationUnits": ["promotion_a"]
            }
        )


if __name__ == '__main__':
    unittest.main()
