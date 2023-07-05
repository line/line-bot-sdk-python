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
    def test_test_webhook_endpoint_with_endpoint(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/channel/webhook/test',
            json={
                "success": True,
                "timestamp": "2020-09-30T05:38:20.031Z",
                "statusCode": 200,
                "reason": "OK",
                "detail": "200"
            },
            status=200
        )

        result = self.tested.test_webhook_endpoint('endpoint')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/channel/webhook/test')
        self.assertEqual(result.success, True)
        self.assertEqual(result.timestamp, '2020-09-30T05:38:20.031Z')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.reason, 'OK')
        self.assertEqual(result.detail, '200')


if __name__ == '__main__':
    unittest.main()
