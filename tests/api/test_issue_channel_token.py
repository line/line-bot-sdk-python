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

import sys
import unittest

import responses

from linebot import (
    LineBotApi
)

PY3 = sys.version_info[0] == 3
if PY3:
    from urllib import parse
else:
    import urlparse as parse


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/v2/oauth/accessToken'
        self.access_token = "W1TeHCgfH2Liwa....."
        self.expires_in = 2592000
        self.token_type = "Bearer"
        self.client_id = 'client_id'
        self.client_secret = 'client_secret'

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

        issue_access_token_response = self.tested.issue_channel_token(
            self.client_id,
            self.client_secret
        )

        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual(self.endpoint, request.url)
        self.assertEqual('application/x-www-form-urlencoded', request.headers['content-type'])
        self.assertEqual(self.access_token, issue_access_token_response.access_token)
        self.assertEqual(self.expires_in, issue_access_token_response.expires_in)
        self.assertEqual(self.token_type, issue_access_token_response.token_type)

        encoded_body = parse.parse_qs(request.body)
        self.assertEqual('client_credentials', encoded_body['grant_type'][0])
        self.assertEqual(self.client_id, encoded_body['client_id'][0])
        self.assertEqual(self.client_secret, encoded_body['client_secret'][0])


if __name__ == '__main__':
    unittest.main()
