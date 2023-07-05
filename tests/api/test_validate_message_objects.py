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


class TestSendTestMessage(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        # test data
        self.text_message = TextSendMessage(text='Hello, world')
        self.message = [{"type": "text", "text": "Hello, world"}]

    @responses.activate
    def test_validate_push_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/push',
            json={}, status=200, headers={'X-Line-Request-Id': 'request_id_test'}
        )

        response = self.tested.validate_push_message_objects(self.text_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/push')
        self.assertEqual(
            json.loads(request.body),
            {
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def test_validate_reply_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/reply',
            json={}, status=200, headers={'X-Line-Request-Id': 'request_id_test'}
        )

        response = self.tested.validate_reply_message_objects(self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/reply')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def test_validate_multicast_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/multicast',
            json={}, status=200, headers={'X-Line-Request-Id': 'request_id_test'}
        )

        response = self.tested.validate_multicast_message_objects(self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/multicast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def validate_test_broadcast_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/broadcast',
            json={}, status=200, headers={'X-Line-Request-Id': 'request_id_test'}
        )

        response = self.tested.validate_broadcast_message_objects(self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/broadcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)

    @responses.activate
    def validate_test_narrowcast_text_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/narrowcast',
            json={}, status=200, headers={'X-Line-Request-Id': 'request_id_test'}
        )

        response = self.tested.validate_narrowcast_message_objects(self.text_message)

        request = responses.calls[0].request
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/validate/narrowcast')
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            json.loads(request.body),
            {
                "messages": self.message
            }
        )
        self.assertEqual('request_id_test', response.request_id)


if __name__ == '__main__':
    unittest.main()
