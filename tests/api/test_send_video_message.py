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
    VideoSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.video_message = VideoSendMessage(
            original_content_url='https://example.com/original.mp4',
            preview_image_url='https://example.com/preview.jpg',
            tracking_id='TrackId'
        )

        self.message = [{
            "type": "video",
            "originalContentUrl": "https://example.com/original.mp4",
            "previewImageUrl": "https://example.com/preview.jpg",
            "trackingId": "TrackId"
        }]

    @responses.activate
    def test_push_video_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.video_message)

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
                "messages": self.message
            }
        )

    @responses.activate
    def test_reply_video_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.video_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                "messages": self.message,
                'notificationDisabled': False,
            }
        )

    @responses.activate
    def test_multicast_video_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to1', 'to2'], self.video_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ['to1', 'to2'],
                "messages": self.message,
                "notificationDisabled": False,
            }
        )


if __name__ == '__main__':
    unittest.main()
