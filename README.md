# line-bot-sdk-python

[![Build Status](https://travis-ci.org/line/line-bot-sdk-python.svg?branch=master)](https://travis-ci.org/line/line-bot-sdk-python)
[![PyPI version](https://badge.fury.io/py/line-bot-sdk.svg)](https://badge.fury.io/py/line-bot-sdk)
[![Documentation Status](https://readthedocs.org/projects/line-bot-sdk-python/badge/?version=latest)](http://line-bot-sdk-python.readthedocs.io/en/latest/?badge=latest)

SDK of the LINE Messaging API for Python.

## About LINE Messaging API

Please refer to the official API documents for details.

en: https://devdocs.line.me/en/

ja: https://devdocs.line.me/ja/

## Install

```
$ pip install line-bot-sdk
```

## Synopsis

Usage is:

```python
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
```

## API

### LineBotApi

#### \__init__(self, channel_access_token, endpoint='https://api.line.me', timeout=5, http_client=RequestsHttpClient)

Create a new LineBotApi instance.

```python
line_bot_api = linebot.LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
```

You can override `timeout` value at each methods.

#### reply_message(self, reply_token, messages, timeout=None)

Respond to events from users, groups, and rooms.
You can get a reply_token by a Webhook Event Object.

https://devdocs.line.me/en/#reply-message

```python
line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World!'))
```

#### push_message(self, to, messages, timeout=None)

Send messages to users, groups, and rooms at any time.

https://devdocs.line.me/en/#push-message

```python
line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))
```

#### get_profile(self, user_id, timeout=None)

Get user profile information.

https://devdocs.line.me/en/#bot-api-get-profile

```python
profile = line_bot_api.get_profile(user_id)

print(profile.display_name)
print(profile.user_id)
print(profile.picture_url)
print(profile.status_message)
```

#### get_message_content(self, message_id, timeout=None)

Retrieve image, video, and audio data sent by users.

https://devdocs.line.me/en/#get-content

```python
message_content = line_bot_api.get_content(message_id)

with open(file_path, 'wb') as fd:
    for chunk in message_content.iter_content():
        fd.write(chunk)
```

#### leave_group(self, group_id, timeout=None)

Leave a group.

https://devdocs.line.me/en/#leave

```python
line_bot_api.leave_group(group_id)
```

#### leave_room(self, room_id, timeout=None)

Leave a room.

https://devdocs.line.me/en/#leave

```python
line_bot_api.leave_room(room_id)
```

#### ※ Error handle

If LINE API server responses a error, LineBotApi raise LineBotApiError.

https://devdocs.line.me/en/#error-response

```python
try:
    line_bot_api.push_message('to', TextSendMessage(text='Hello World!'))
except linebot.LineBotApiError as e:
    print(e.status_code)
    print(e.error.message)
    print(e.error.details)
```

### Send message object

https://devdocs.line.me/en/#send-message-object

These following class in `linebot.models` package.

#### TextSendMessage

```python
text_message = TextSendMessage(text='Hello, world')
```

#### ImageSendMessage

```python
image_message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
```

#### VideoSendMessage

```python
video_message = VideoSendMessage(
    original_content_url='https://example.com/original.mp4',
    preview_image_url='https://example.com/preview.jpg'
)
```

#### AudioSendMessage

```python
audio_message = AudioSendMessage(
    original_content_url='https://example.com/original.m4a',
    duration=240000
)
```

#### LocationSendMessage

```python
location_message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
```

#### StickerSendMessage

```python
sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
)
```

#### ImagemapSendMessage

```python
imagemap_message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
        URIImagemapAction(
            link_uri='https://example.com/',
            area=ImagemapArea(
                x=0, y=0, width=520, height=1040
            )
        ),
        MessageImagemapAction(
            text='hello',
            area=ImagemapArea(
                x=520, y=0, width=520, height=1040
            )
        )
    ]
)
```

#### TemplateSendMessage - ButtonsTemplate

```python
buttons_template_message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            ),
            URITemplateAction(
                label='uri',
                uri='http://example.com/'
            )
        ]
    )
)
```

#### TemplateSendMessage - ConfirmTemplate

```python
confirm_template_message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='Are you sure?',
        actions=[
            PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='message',
                text='message text'
            )
        ]
    )
)
```

#### TemplateSendMessage - CarouselTemplate

```python
carousel_template_message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://example.com/item1.jpg'
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='uri1',
                        uri='http://example.com/1'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://example.com/item2.jpg'
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='uri2',
                        uri='http://example.com/2'
                    )
                ]
            )
        ]
    )
)
```

## Webhook

### WebhookParser

※ You can use WebhookParser or WebhookHandler

#### \__init__(self, channel_secret)

```python
parser = linebot.WebhookParser('YOUR_CHANNEL_SECRET')
```

#### parse(self, body, signature)

Parse webhook body and build Event Objects List.
If signature does NOT match, raise InvalidSignatureError.

```python
events = parser.parse(body, signature)

for event in events:
    # Do something
```

### WebhookHandler

※ You can use WebhookParser or WebhookHandler

#### \__init__(self, channel_secret)

```python
handler = linebot.WebhookHandler('YOUR_CHANNEL_SECRET')
```

#### handle(self, body, signature)

Handle webhook.
If signature does NOT match, raise InvalidSignatureError.

```python
handler.handle(body, signature)
```

#### Add handler method

You can add handler method by using `add` decorator.

`add(self, event, message=None)`

```python
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
```

When event is instance of MessageEvent and event.message is instance of TextMessage, this handler method is called.

#### Set default handler method

You can set default handler method by using `default` decorator.

`default(self)`

```python
@handler.default()
def default(event):
    print(event)
```

There is no handler for event, this default handler method is called.

### Webhook event object

https://devdocs.line.me/en/#webhooks

These following class in `linebot.models` package.

#### Event

* MessageEvent
  * type
  * timestamp
  * source: [Source](#source)
  * reply_token
  * message: [Message](#message)
* FollowEvent
  * type
  * timestamp
  * source: [Source](#source)
  * reply_token
* UnfollowEvent
  * type
  * timestamp
  * source: [Source](#source)
* JoinEvent
  * type
  * timestamp
  * source: [Source](#source)
  * reply_token
* LeaveEvent
  * type
  * timestamp
  * source: [Source](#source)
* PostbackEvent
  * type
  * timestamp
  * source: [Source](#source)
  * reply_token
  * postback: Postback
    * data
* BeaconEvent
  * type
  * timestamp
  * source: [Source](#source)
  * reply_token
  * beacon: Beacon
    * type
    * hwid

#### Source

* SourceUser
  * type
  * user_id
* SourceGroup
  * type
  * group_id
* SourceRoom
  * type
  * room_id

#### Message

* TextMessage
  * type
  * id
  * text
* ImageMessage
  * type
  * id
* VideoMessage
  * type
  * id
* AudioMessage
  * type
  * id
* LocationMessage
  * type
  * id
  * title
  * address
  * latitude
  * longitude
* StickerMessage
  * type
  * id
  * package_id
  * sticker_id


## Hints

### Examples

#### [simple-server-echo](https://github.com/line/line-bot-sdk-python/tree/master/examples/simple-server-echo)

Sample echo-bot using [wsgiref.simple_server](https://docs.python.org/3/library/wsgiref.html)

#### [flask-echo](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)

Sample echo-bot using [Flask](http://flask.pocoo.org/)

#### [flask-kitchensink](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-kitchensink)

Sample bot using [Flask](http://flask.pocoo.org/)

## API document

```
$ cd docs
$ make html
$ open build/html/index.html
```

OR [![Documentation Status](https://readthedocs.org/projects/line-bot-sdk-python/badge/?version=latest)](http://line-bot-sdk-python.readthedocs.io/en/latest/?badge=latest)

## Requirements

* python >= 2.7 or >= 3.3

## For SDK developers

First install for development.

```
$ pip install -r requirements-dev.txt
```

### Run tests

We test by using tox.
We test the following versions.

* 2.7
* 3.3
* 3.4
* 3.5

If you want to run all tests and run `flake8` against all versions:

```
tox
```

If you want to run all tests against 2.7 version:

```
$ tox -e py27
```

If you want to run a test against 2.7 version and against specific file:

```
$ tox -e py27 -- tests/test_webhook.py
```

And more... TBD
