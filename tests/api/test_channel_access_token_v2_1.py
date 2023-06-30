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
        self.access_token = 'W1TeHCgfH2Liwa.....'
        self.expires_in = 2592000
        self.token_type = 'Bearer'
        self.client_assertion = 'eyJhbGciOiJSUzI.q....'
        self.client_id = 'client_id'
        self.client_secret = 'client_secret'
        self.client_assertion_type = 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'
        self.key_id = 'sDTOzw5wIfxxxxPEzcmeQA'
        self.scope = 'profile chat_message.write'

    @responses.activate
    def test_issue_channel_access_token_v2_1(self):
        endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/oauth2/v2.1/token'
        responses.add(
            responses.POST,
            endpoint,
            json={
                'access_token': self.access_token,
                'expires_in': self.expires_in,
                'token_type': self.token_type,
                'key_id': self.key_id
            },
            status=200
        )

        issue_access_token_response = self.tested.issue_channel_access_token_v2_1(
            self.client_assertion
        )

        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual(endpoint, request.url)
        self.assertEqual('application/x-www-form-urlencoded', request.headers['content-type'])
        self.assertEqual(self.access_token, issue_access_token_response.access_token)
        self.assertEqual(self.expires_in, issue_access_token_response.expires_in)
        self.assertEqual(self.token_type, issue_access_token_response.token_type)

        encoded_body = parse.parse_qs(request.body)
        self.assertEqual('client_credentials', encoded_body['grant_type'][0])
        self.assertEqual(self.client_assertion_type, encoded_body['client_assertion_type'][0])
        self.assertEqual(self.client_assertion, encoded_body['client_assertion'][0])

    @responses.activate
    def test_get_channel_access_token_v2_1(self):

        endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/oauth2/v2.1/tokens'
        responses.add(
            responses.GET,
            endpoint,
            json={
                'access_tokens': [
                    'fgIkeLcl3.....',
                    'eyJhbGciO.....',
                    'oeLklsSi7.....'
                ]
            },
            status=200
        )
        channel_access_tokens_response = self.tested.get_channel_access_tokens_v2_1(
            self.client_assertion
        )

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            parse.unquote(request.url),
            parse.unquote('{}?client_assertion={}&client_assertion_type={}'.format(
                endpoint, self.client_assertion, self.client_assertion_type
            ))
        )
        self.assertEqual(channel_access_tokens_response.access_tokens, [
            'fgIkeLcl3.....',
            'eyJhbGciO.....',
            'oeLklsSi7.....'
        ])

    @responses.activate
    def test_revoke_channel_access_token_v2_1(self):
        endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/oauth2/v2.1/revoke'

        responses.add(
            responses.POST,
            endpoint,
            status=200
        )

        self.tested.revoke_channel_access_token_v2_1(
            self.client_id, self.client_secret, self.access_token
        )

        request = responses.calls[0].request
        self.assertEqual('POST', request.method)
        self.assertEqual(endpoint, request.url)

        encoded_body = parse.parse_qs(request.body)
        self.assertEqual(self.client_id, encoded_body['client_id'][0])
        self.assertEqual(self.client_secret, encoded_body['client_secret'][0])
        self.assertEqual(self.access_token, encoded_body['access_token'][0])

    @responses.activate
    def test_verify_channel_access_token_v2_1(self):
        endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/oauth2/v2.1/verify'

        responses.add(
            responses.GET,
            endpoint,
            status=200,
            json={
                'client_id': self.client_id,
                'expires_in': self.expires_in,
                'scope': self.scope,
            },
        )

        self.tested.verify_channel_access_token_v2_1(self.access_token)

        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(
            parse.unquote(request.url),
            parse.unquote('{}?access_token={}'.format(
                endpoint, self.access_token
            ))
        )

    @responses.activate
    def test_get_channel_token_key_ids_v2_1(self):
        endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/oauth2/v2.1/tokens/kid'

        responses.add(
            responses.GET,
            endpoint,
            status=200,
            json={
                'kids': [self.key_id],
            },
        )

        self.tested.get_channel_token_key_ids_v2_1(self.client_assertion, self.client_assertion_type)

        request = responses.calls[0].request
        self.assertEqual('GET', request.method)
        self.assertEqual(
            parse.unquote(request.url),
            parse.unquote('{}?client_assertion={}&client_assertion_type={}'.format(
                endpoint, self.client_assertion, self.client_assertion_type
            ))
        )


if __name__ == '__main__':
    unittest.main()
