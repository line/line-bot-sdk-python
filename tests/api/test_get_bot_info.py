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
    def test_get_bot_info(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/info',
            json={
                "userId": "Ub9952f8...",
                "basicId": "@216ru...",
                "premiumId": "@example",
                "displayName": "Example name",
                "pictureUrl": "https://obs.line-apps.com/...",
                "chatMode": "chat",
                "markAsReadMode": "manual",
            },
            status=200
        )

        bot = self.tested.get_bot_info()

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/info')
        self.assertEqual(bot.user_id, 'Ub9952f8...')
        self.assertEqual(bot.basic_id, '@216ru...')
        self.assertEqual(bot.premium_id, '@example')
        self.assertEqual(bot.display_name, 'Example name')
        self.assertEqual(bot.picture_url, 'https://obs.line-apps.com/...')
        self.assertEqual(bot.chat_mode, 'chat')
        self.assertEqual(bot.mark_as_read_mode, 'manual')


if __name__ == '__main__':
    unittest.main()
