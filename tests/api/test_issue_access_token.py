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
        self.endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/oauth/accessToken'
        self.access_token = "W1TeHCgfH2Liwa....."
        self.expires_in = 2592000
        self.token_type = "Bearer"

    @responses.activate
    def test_issue_line_token(self):
        responses.add(
            responses.POST,
            self.endpoint,
            json={
                "access_token": self.access_token,
                "expires_in": self.expires_in,
                "token_type": self.token_type
            },
            status=200
        )

        issue_access_token_response = self.tested.issue_access_token(
            'client_credentials',
            'client_id',
            'client_secret'
        )

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.url, self.endpoint)
        self.assertEqual(request.headers['content-type'], 'application/x-www-form-urlencoded')
        self.assertEqual(issue_access_token_response.access_token, self.access_token)
        self.assertEqual(issue_access_token_response.expires_in, self.expires_in)
        self.assertEqual(issue_access_token_response.token_type, self.token_type)


if __name__ == '__main__':
    unittest.main()
