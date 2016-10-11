# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import unittest

import responses

from line_bot import (
    LineBotApi
)
from line_bot.exceptions import (
    LineBotApiError
)
from line_bot.models import (
    TextSendMessage
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

    @responses.activate
    def test_error_handle(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={
                "message": "Invalid reply token"
            },
            status=401
        )

        try:
            self.tested.push_message(
                'to',
                TextSendMessage(text='hoge')
            )
        except LineBotApiError as e:
            self.assertEqual(e.status_code, 401)
            self.assertEqual(e.error.message, 'Invalid reply token')

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
            status=400
        )

        try:
            self.tested.push_message(
                'to',
                TextSendMessage(text='hoge')
            )
        except LineBotApiError as e:
            self.assertEqual(e.status_code, 400)
            self.assertEqual(
                e.error.message, 'The request body has 2 error(s)'
            )
            self.assertEqual(
                e.error.details[0].message, 'May not be empty'
            )
            self.assertEqual(
                e.error.details[0].property, 'messages[0].text'
            )
            self.assertEqual(
                e.error.details[1].message, "Must be one of the following "
                                            "values: [text"
                                            ", image, video, audio, "
                                            "location, sticker, "
                                            "richmessage, template, imagemap]"
            )
            self.assertEqual(
                e.error.details[1].property, 'messages[1].type'
            )

    @responses.activate
    def test_error_handle_get_content(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/1/content',
            json={
                "message": "Invalid reply token"
            },
            status=404
        )

        try:
            self.tested.get_content_stream(1)
        except LineBotApiError as e:
            self.assertEqual(e.status_code, 404)
            self.assertEqual(e.error.message, 'Invalid reply token')
