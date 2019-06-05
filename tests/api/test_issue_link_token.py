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
    def test_issue_line_token(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/linkToken',
            json={
                "linkToken": "xxxx",
            },
            status=200
        )

        issue_link_token_response = self.tested.issue_link_token('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/user/user_id/linkToken')
        self.assertEqual(issue_link_token_response.link_token, 'xxxx')


if __name__ == '__main__':
    unittest.main()
