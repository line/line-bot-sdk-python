import json
import unittest
import responses
from linebot import LineBotApi


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')
        self.endpoint = LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/narrowcast'
        self.messages = [{
            'type': 'text',
            'text': 'Hello, world'
        }]
        self.recipient = None
        self.filter = None
        self.limit = None

    @responses.activate
    def test_narrowcast_text_message_without_condition(self):
        expected = {
            'messages': self.messages,
            'recipient': self.recipient,
            'filter': self.filter,
            'limit': self.limit,
        }
        responses.add(
            responses.POST,
            self.endpoint,
            json=expected,
            status=202
        )

        self.tested.narrowcast(messages=self.messages)

        request = responses.calls[0].request

        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.url, self.endpoint)
        self.assertEqual(request.body, json.dumps(expected))

    @responses.activate
    def test_narrowcast_text_message(self):
        self.recipient = {
            'type': "audience",
            'audienceGroupId': 5614991017776
        }
        self.filter = {
            'demographic': {
                'type': "area",
                'oneOf': [
                    "android"
                ]
            }
        }
        self.limit = {'max': 100}
        expected = {
            'messages': self.messages,
            'recipient': self.recipient,
            'filter': self.filter,
            'limit': self.limit,
        }

        responses.add(
            responses.POST,
            self.endpoint,
            json=expected,
            status=202
        )

        self.tested.narrowcast(
            messages=self.messages,
            recipient=self.recipient,
            filter=self.filter,
            limit=self.limit)

        request = responses.calls[0].request

        self.assertEqual(request.method, 'POST')
        self.assertEqual(request.url, self.endpoint)
        self.assertEqual(request.body, json.dumps(expected))


if __name__ == '__main__':
    unittest.main()
