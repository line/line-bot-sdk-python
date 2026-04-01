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

import unittest
from urllib.parse import parse_qs

from pytest_httpserver import HTTPServer
from linebot.v3.oauth import (
    Configuration,
    ApiClient,
    ChannelAccessToken,
)


class TestIssueStatelessChannelToken(unittest.TestCase):

    def test_issue_stateless_channel_token_by_jwt_assertion(self):
        client_assertion = 'eyJhbGciOiJSUzI.q....'
        client_assertion_type = 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer'

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/oauth2/v3/token",
                method="POST",
            ).respond_with_json(
                {
                    'access_token': 'test_access_token',
                    'expires_in': 900,
                    'token_type': 'Bearer',
                },
                status=200,
            )

            configuration = Configuration(host=httpserver.url_for("/"))
            with ApiClient(configuration) as api_client:
                api = ChannelAccessToken(api_client)
                api.line_base_path = httpserver.url_for("/")

                response = api.issue_stateless_channel_token_by_jwt_assertion(
                    client_assertion,
                )

            self.assertEqual(response.access_token, 'test_access_token')
            self.assertEqual(response.expires_in, 900)
            self.assertEqual(response.token_type, 'Bearer')
            self.assertEqual(len(httpserver.log), 1)

            request, _ = httpserver.log[0]
            encoded_body = parse_qs(request.data.decode('utf-8'))
            self.assertEqual(encoded_body['grant_type'], ['client_credentials'])
            self.assertEqual(encoded_body['client_assertion_type'], [client_assertion_type])
            self.assertEqual(encoded_body['client_assertion'], [client_assertion])
            self.assertNotIn('client_id', encoded_body)
            self.assertNotIn('client_secret', encoded_body)

    def test_issue_stateless_channel_token_by_client_secret(self):
        client_id = 'test_client_id'
        client_secret = 'test_client_secret'

        with HTTPServer() as httpserver:
            httpserver.expect_request(
                uri="/oauth2/v3/token",
                method="POST",
            ).respond_with_json(
                {
                    'access_token': 'test_access_token',
                    'expires_in': 900,
                    'token_type': 'Bearer',
                },
                status=200,
            )

            configuration = Configuration(host=httpserver.url_for("/"))
            with ApiClient(configuration) as api_client:
                api = ChannelAccessToken(api_client)
                api.line_base_path = httpserver.url_for("/")

                response = api.issue_stateless_channel_token_by_client_secret(
                    client_id,
                    client_secret,
                )

            self.assertEqual(response.access_token, 'test_access_token')
            self.assertEqual(response.expires_in, 900)
            self.assertEqual(response.token_type, 'Bearer')
            self.assertEqual(len(httpserver.log), 1)

            request, _ = httpserver.log[0]
            encoded_body = parse_qs(request.data.decode('utf-8'))
            self.assertEqual(encoded_body['grant_type'], ['client_credentials'])
            self.assertEqual(encoded_body['client_id'], [client_id])
            self.assertEqual(encoded_body['client_secret'], [client_secret])
            self.assertNotIn('client_assertion_type', encoded_body)
            self.assertNotIn('client_assertion', encoded_body)


if __name__ == '__main__':
    unittest.main()
