# line-bot-sdk-python

SDK of the LINE Messaging API for Python.

## About LINE Messaging API

Please refer to the official API documents for details.

en: https://devdocs.line.me/en/

ja: https://devdocs.line.me/ja/

## Install

```
pip install line_bot
```

## Synopsis

Usage is:

```python
from flask import Flask, request, abort

import line_bot

app = Flask(__name__)

line_bot_api = line_bot.LineBotApi('CHANNEL_ACCESS_TOKEN')
signature_validator = line_bot.SignatureValidator('CHANNEL_SECRET')
handler = line_bot.WebhookHandler()


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    # check signature
    if not signature_validator.validate(body, signature):
        abort(400)

    # handle webhook body
    handler.handle(body=body)
    return 'OK'


@handler.add(line_bot.MessageEvent, message=line_bot.TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        line_bot.TextSendMessage(text=event.message.text)
    )

```

## API

### line_bot.LineBotApi

#### \__init__(self, channel_access_token, endpoint='https://api.line.me', timeout=5, http_client=RequestsHttpClient)

Create a new LineBotApi instance.

```python
line_bot_api = line_bot.LineBotApi('CHANNEL_ACCESS_TOKEN')
```

You can override `timeout` value at each methods.

#### reply_message(self, reply_token, messages, timeout=None)

Respond to events from users, groups, and rooms.  
You can get a reply_token by a Webhook Event Object. And see also parse method's document.

https://devdocs.line.me/en/#reply-message

```python
line_bot_api.reply_message(
    reply_token, line_bot.TextSendMessage(text='Hello World!'))
```

#### push_message(self, to, messages, timeout=None)

Send messages to users, groups, and rooms at any time.

https://devdocs.line.me/en/#push-message

```python
line_bot_api.push_message(
    to, line_bot.TextSendMessage(text='Hello World!'))

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

#### get_content_stream(self, message_id, chunk_size=1024, timeout=None)

Retrieve image, video, and audio data sent by users.

https://devdocs.line.me/en/#get-content

```python
stream = line_bot_api.get_content_stream(message_id)

with open(file_path, 'wb') as fd:
    for chunk in stream:
        fd.write(chunk)
```

#### leave_group(self, group_id, timeout=None)

Leave a group.

https://devdocs.line.me/en/#leave

```python
line_bot_api.leave_group(group_id)
```

#### leave_room(self, group_id, timeout=None)

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
    line_bot_api.push_message(
        'to',
        TextSendMessage(text='hoge')
    )
except LineBotApiError as e:
    print(e.error.message)
    print(e.error.details)
```

## Webhook

### line_bot.SignatureValidator

#### \__init__(self, channel_secret)

Create a new SignatureValidator instance.

```python
signature_validator = line_bot.SignatureValidator('CHANNEL_SECRET')
```

#### validate(self, body, signature):

validate signature(X-Line-Signature header value) to confirm that the request was sent from the LINE platform.

https://devdocs.line.me/ja/#webhook-authentication

```python
result = signature_validator.validate(body, signature)
```

### line_bot.WebhookParser

#### \__init__(self)

```python
parser = WebhookParser()
```

#### parse(self, body)

(Optional)  
Parse webhook body and build Event Objects List.

```python
events = parser.parse(body)
```

### line_bot.WebhookHandler

