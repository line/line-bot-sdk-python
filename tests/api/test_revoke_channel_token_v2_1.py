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
        self.endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/oauth2/v2.1/revoke'
        self.client_id = 'client_id'
        self.client_secret = 'client_secret'
        self.access_token = 'W1TeHCgfH2Liwa.....'

    @responses.activate
    def test_issue_line_token_v2_1(self):
        responses.add(
            responses.POST,
            self.endpoint,
            status=200
        )

        self.tested.revoke_channel_token_v2_1(self.client_id, self.client_secret, self.access_token)

        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual(self.endpoint, request.url)

        encoded_body = parse.parse_qs(request.body)
        self.assertEqual(self.client_id, encoded_body['client_id'][0])
        self.assertEqual(self.client_secret, encoded_body['client_secret'][0])
        self.assertEqual(self.access_token, encoded_body['access_token'][0])


if __name__ == '__main__':
    unittest.main()
