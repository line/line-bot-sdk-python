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
    TemplateSendMessage, ButtonsTemplate,
    PostbackAction, MessageAction,
    URIAction, AltUri, DatetimePickerAction,
    ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn
)


class TestLineBotApi(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tested = LineBotApi('channel_secret')

        self.button_template_message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://example.com/image.jpg',
                title='Menu', text='Please select',
                actions=[
                    PostbackAction(
                        label='postback', display_text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message', text='message text'
                    ),
                    URIAction(
                        label='uri', uri='http://example.com/',
                        alt_uri=AltUri(desktop="http://example.com/desktop")
                    )
                ]
            )
        )

        self.button_message = [{
            "type": "template",
            "altText": "Buttons template",
            "template": {
                "type": "buttons",
                "thumbnailImageUrl":
                    "https://example.com/image.jpg",
                "title": "Menu",
                "text": "Please select",
                "actions": [
                    {
                        "type": "postback",
                        "label": "postback",
                        "displayText": "postback text",
                        "data": "action=buy&itemid=1"
                    },
                    {
                        "type": "message",
                        "label": "message",
                        "text": "message text"
                    },
                    {
                        "type": "uri",
                        "label": "uri",
                        "uri": "http://example.com/",
                        "altUri": {
                            "desktop": "http://example.com/desktop"
                        }
                    }
                ]
            }
        }]

        self.confirm_template_message = TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
                text='Are you sure?',
                actions=[
                    PostbackAction(
                        label='postback', display_text='postback text',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label='message', text='message text'
                    )
                ]
            )
        )

        self.confirm_message = [{
            "type": "template",
            "altText": "Confirm template",
            "template": {
                "type": "confirm",
                "text": "Are you sure?",
                "actions": [
                    {
                        "type": "postback",
                        "label": "postback",
                        "displayText": "postback text",
                        "data": "action=buy&itemid=1"
                    },
                    {
                        "type": "message",
                        "label": "message",
                        "text": "message text"
                    }
                ]
            }
        }]

        self.carousel_template_message = TemplateSendMessage(
            alt_text='Carousel template',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://example.com'
                                            '/item1.jpg',
                        title='this is menu1', text='description1',
                        actions=[
                            PostbackAction(
                                label='postback1', display_text='postback text1',
                                data='action=buy&itemid=1'
                            ),
                            MessageAction(
                                label='message1', text='message text1'
                            ),
                            URIAction(
                                label='uri1',
                                uri='http://example.com/1'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://example.com'
                                            '/item2.jpg',
                        image_background_color='#000000',
                        title='this is menu2', text='description2',
                        actions=[
                            PostbackAction(
                                label='postback2', display_text='postback text2',
                                data='action=buy&itemid=2'
                            ),
                            MessageAction(
                                label='message2', text='message text2'
                            ),
                            URIAction(
                                label='uri2',
                                uri='http://example.com/2'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://example.com'
                                            '/item3.jpg',
                        title='this is menu3', text='description3',
                        actions=[
                            DatetimePickerAction(
                                label="datetime picker date",
                                data="action=sell&itemid=2&mode=date",
                                mode="date",
                                initial="2013-04-01",
                                min="2011-06-23",
                                max="2017-09-08"
                            ),
                            DatetimePickerAction(
                                label="datetime picker time",
                                data="action=sell&itemid=2&mode=time",
                                mode="time",
                                initial="10:00",
                                min="00:00",
                                max="23:59"
                            ),
                            DatetimePickerAction(
                                label="datetime picker datetime",
                                data="action=sell&itemid=2&mode=datetime",
                                mode="datetime",
                                initial="2013-04-01T10:00",
                                min="2011-06-23T00:00",
                                max="2017-09-08T23:59"
                            )
                        ]
                    )
                ]
            )
        )

        self.carousel_message = [{
            "type": "template",
            "altText": "Carousel template",
            "template": {
                "type": "carousel",
                "columns": [
                    {
                        "thumbnailImageUrl":
                            "https://example.com/item1.jpg",
                        "title": "this is menu1",
                        "text": "description1",
                        "actions": [
                            {
                                "type": "postback",
                                "label": "postback1",
                                "displayText": "postback text1",
                                "data": "action=buy&itemid=1"
                            },
                            {
                                "type": "message",
                                "label": "message1",
                                "text": "message text1"
                            },
                            {
                                "type": "uri",
                                "label": "uri1",
                                "uri": "http://example.com/1"
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl":
                            "https://example.com/item2.jpg",
                        "imageBackgroundColor": "#000000",
                        "title": "this is menu2",
                        "text": "description2",
                        "actions": [
                            {
                                "type": "postback",
                                "label": "postback2",
                                "displayText": "postback text2",
                                "data": "action=buy&itemid=2"
                            },
                            {
                                "type": "message",
                                "label": "message2",
                                "text": "message text2"
                            },
                            {
                                "type": "uri",
                                "label": "uri2",
                                "uri": "http://example.com/2"
                            }
                        ]
                    },
                    {
                        "thumbnailImageUrl":
                            "https://example.com/item3.jpg",
                        "title": "this is menu3",
                        "text": "description3",
                        "actions": [
                            {
                                "type": "datetimepicker",
                                "label": "datetime picker date",
                                "data": "action=sell&itemid=2&mode=date",
                                "mode": "date",
                                "initial": "2013-04-01",
                                "min": "2011-06-23",
                                "max": "2017-09-08"
                            },
                            {
                                "type": "datetimepicker",
                                "label": "datetime picker time",
                                "data": "action=sell&itemid=2&mode=time",
                                "mode": "time",
                                "initial": "10:00",
                                "min": "00:00",
                                "max": "23:59"
                            },
                            {
                                "type": "datetimepicker",
                                "label": "datetime picker datetime",
                                "data": "action=sell&itemid=2&mode=datetime",
                                "mode": "datetime",
                                "initial": "2013-04-01T10:00",
                                "min": "2011-06-23T00:00",
                                "max": "2017-09-08T23:59"
                            }
                        ]
                    }
                ],
            }
        }]

        self.image_carousel_template_message = TemplateSendMessage(
            alt_text='Image carousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://example.com/'
                                  'item1.jpg',
                        action=PostbackAction(
                            label='postback1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com'
                                  '/item2.jpg',
                        action=MessageAction(
                            label='message2',
                            text='message text2'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://example.com/'
                                  'item3.jpg',
                        action=URIAction(
                            label='uri1',
                            uri='https://example.com/1'
                        )
                    )
                ]
            )
        )

        self.image_carousel_message = [{
            "type": "template",
            "altText": "Image carousel template",
            "template": {
                "type": "image_carousel",
                "columns": [
                    {
                        "imageUrl": "https://example.com/item1.jpg",
                        "action": {
                            "type": "postback",
                            "label": "postback1",
                            "data": "action=buy&itemid=1",
                        }
                    },
                    {
                        "imageUrl": "https://example.com/item2.jpg",
                        "action": {
                            "type": "message",
                            "label": "message2",
                            "text": "message text2"
                        }
                    },
                    {
                        "imageUrl": "https://example.com/item3.jpg",
                        "action": {
                            "type": "uri",
                            "label": "uri1",
                            "uri": "https://example.com/1"
                        }
                    }
                ]
            }
        }]

    @responses.activate
    def test_push_buttons_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.button_template_message)

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
                "messages": self.button_message
            }
        )

    @responses.activate
    def test_reply_buttons_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.button_template_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                'notificationDisabled': False,
                "messages": self.button_message
            }
        )

    @responses.activate
    def test_push_confirm_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.confirm_template_message)

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
                "messages": self.confirm_message
            }
        )

    @responses.activate
    def test_reply_confirm_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.confirm_template_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply'
        )
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                'notificationDisabled': False,
                "messages": self.confirm_message
            }
        )

    @responses.activate
    def test_push_carousel_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.carousel_template_message)

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
                "messages": self.carousel_message
            }
        )

    @responses.activate
    def test_reply_carousel_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.carousel_template_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                'notificationDisabled': False,
                "messages": self.carousel_message
            }
        )

    @responses.activate
    def test_multicast_carousel_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to1', 'to2'], self.carousel_template_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ['to1', 'to2'],
                'notificationDisabled': False,
                "messages": self.carousel_message
            }
        )

    @responses.activate
    def test_push_image_carousel_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/push',
            json={}, status=200
        )

        self.tested.push_message('to', self.image_carousel_template_message)

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
                "messages": self.image_carousel_message
            }
        )

    @responses.activate
    def test_reply_image_carousel_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply',
            json={}, status=200
        )

        self.tested.reply_message('replyToken', self.image_carousel_template_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/reply')
        self.assertEqual(
            json.loads(request.body),
            {
                "replyToken": "replyToken",
                'notificationDisabled': False,
                "messages": self.image_carousel_message
            }
        )

    @responses.activate
    def test_multicast_image_carousel_template_message(self):
        responses.add(
            responses.POST,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast',
            json={}, status=200
        )

        self.tested.multicast(['to1', 'to2'], self.image_carousel_template_message)

        request = responses.calls[0].request
        self.assertEqual(request.method, 'POST')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/message/multicast')
        self.assertEqual(
            json.loads(request.body),
            {
                "to": ['to1', 'to2'],
                'notificationDisabled': False,
                "messages": self.image_carousel_message
            }
        )


if __name__ == '__main__':
    unittest.main()
