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
from linebot.exceptions import (
    LineBotApiError
)
from linebot.models import (
    TextSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.request_id = 'f70dd685-499a-4231-a441-f24b8d4fba21'
        self.headers = {'X-Line-Request-Id': self.request_id, 'HOGE': 'FUGA'}

    @responses.activate
    def test_error_handle(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={
                "message": "Invalid reply token"
            },
            headers=self.headers,
            status=401
        )

        try:
            self.tested.push_message('to', TextSendMessage(text='hoge'))
        except LineBotApiError as e:
            self.assertEqual(e.status_code, 401)
            self.assertEqual(e.error.message, 'Invalid reply token')
            self.assertEqual(e.request_id, self.request_id)
            self.assertEqual(e.headers['HOGE'], 'FUGA')

    @responses.activate
    def test_error_with_detail_handle(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={
                "message": "The request body has 2 error(s)",
                "details": [
                    {
                        "message": "May not be empty",
                        "property": "messages[0].text"
                    },
                    {
                        "message": "Must be one of the following values: [text"
                                   ", image, video, audio, location, sticker, "
                                   "richmessage, template, imagemap]",
                        "property": "messages[1].type"
                    }
                ]
            },
            headers=self.headers,
            status=400
        )

        try:
            self.tested.push_message(
                'to',
                TextSendMessage(text='hoge')
            )
        except LineBotApiError as e:
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.error.message, 'The request body has 2 error(s)')
            self.assertEqual(e.error.details[0].message, 'May not be empty')
            self.assertEqual(e.error.details[0].property, 'messages[0].text')
            self.assertEqual(
                e.error.details[1].message, "Must be one of the following "
                                            "values: [text"
                                            ", image, video, audio, "
                                            "location, sticker, "
                                            "richmessage, template, imagemap]"
            )
            self.assertEqual(e.error.details[1].property, 'messages[1].type')
            self.assertEqual(e.request_id, self.request_id)
            self.assertEqual(e.headers['HOGE'], 'FUGA')

    @responses.activate
    def test_error_handle_get_message_content(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_DATA_ENDPOINT + '/v2/bot/message/1/content',
            json={
                "message": "Invalid reply token"
            },
            headers=self.headers,
            status=404
        )

        try:
            self.tested.get_message_content(1)
        except LineBotApiError as e:
            self.assertEqual(e.status_code, 404)
            self.assertEqual(e.error.message, 'Invalid reply token')
            self.assertEqual(e.request_id, self.request_id)
            self.assertEqual(e.headers['HOGE'], 'FUGA')


if __name__ == '__main__':
    unittest.main()
