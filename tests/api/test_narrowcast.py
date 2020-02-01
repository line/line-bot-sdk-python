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

from linebot import LineBotApi


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast'
        self.messages = [{
            'type': 'text',
            'text': 'Hello, world'
        }]
        self.recipient = None
        self.filter = None
        self.limit = None

    @responses.activate
    def test_narrowcast_text_message_without_condition(self):
        expected = {
            'messages': self.messages,
            'recipient': self.recipient,
            'filter': self.filter,
            'limit': self.limit,
        }
        responses.add(
            responses.POST,
            self.endpoint,
            json=expected,
            status=202
        )

        self.tested.narrowcast(messages=self.messages)

        request = responses.calls[0].request

        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.url, self.endpoint)
        self.assertEqual(request.body, json.dumps(expected))

    @responses.activate
    def test_narrowcast_text_message(self):
        self.recipient = {
            'type': "audience",
            'audienceGroupId': 5614991017776
        }
        self.filter = {
            'demographic': {
                'type': "area",
                'oneOf': [
                    "android"
                ]
            }
        }
        self.limit = {'max': 100}
        expected = {
            'messages': self.messages,
            'recipient': self.recipient,
            'filter': self.filter,
            'limit': self.limit,
        }

        responses.add(
            responses.POST,
            self.endpoint,
            json=expected,
            status=202
        )

        self.tested.narrowcast(
            messages=self.messages,
            recipient=self.recipient,
            filter=self.filter,
            limit=self.limit)

        request = responses.calls[0].request

        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.url, self.endpoint)
        self.assertEqual(request.body, json.dumps(expected))


if __name__ == '__main__':
    unittest.main()
