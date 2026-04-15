# Migration Guide: `linebot` to `linebot.v3`

Starting with version 3.x, the LINE Bot SDK for Python provides a new set of modules under `linebot.v3`. These modules are auto-generated from the [LINE OpenAPI spec](https://github.com/line/line-openapi), making it easy to keep up with future API changes.

The v3 modules are **not backward-compatible** with the previous `linebot` modules, but both coexist in the same package. This means you can migrate your code incrementally — one file or one endpoint at a time.

> **Note:** Only `linebot.v3` will be maintained going forward. The previous `linebot` modules (v2) will not receive updates.

## Table of Contents

- [Migration procedure](#migration-procedure)
  1. [Upgrade to 3.x](#1-upgrade-to-3x)
  2. [Replace client construction](#2-replace-client-construction)
  3. [Update imports and models](#3-update-imports-and-models)
  4. [Update method calls](#4-update-method-calls)
  5. [Update webhook handler](#5-update-webhook-handler)
  6. [Update error handling](#6-update-error-handling)
  7. [Remove deprecated imports](#7-remove-deprecated-imports)
- [Full echo-bot before/after example](#full-echo-bot-beforeafter-example)
- [Client construction mapping](#client-construction-mapping)
- [Import and type mapping](#import-and-type-mapping)
- [Method mapping](#method-mapping)
- [Error handling](#error-handling)
- [Response headers / x-line-request-id](#response-headers--x-line-request-id)
- [Suppressing deprecation warnings](#suppressing-deprecation-warnings)

---

## Migration procedure

### 1. Upgrade to 3.x

```bash
pip install line-bot-sdk>=3.0
```

Both the deprecated `linebot` modules and the new `linebot.v3` modules are included — no need to install a separate package.

### 2. Replace client construction

**Before (deprecated):**

```python
from linebot import LineBotApi

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
```

**After (v3 — unified client):**

```python
from linebot.v3 import LineBotClient

line_bot_api = LineBotClient(channel_access_token='YOUR_CHANNEL_ACCESS_TOKEN')
```

`LineBotClient` is a convenience wrapper that bundles multiple API clients (messaging, audience, insight, liff, module, moduleattach, shop). If you only need the Messaging API, you can also use the individual client directly:

```python
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi

configuration = Configuration(access_token='YOUR_CHANNEL_ACCESS_TOKEN')
with ApiClient(configuration) as api_client:
    messaging_api = MessagingApi(api_client)
    # use messaging_api...
```

### 3. Update imports and models

Model names have changed. In general:

- **Send messages:** `TextSendMessage` → `TextMessage` (under `linebot.v3.messaging`)
- **Webhook messages:** `TextMessage` → `TextMessageContent` (under `linebot.v3.webhooks`)
- **Sources:** `SourceUser` → `UserSource` (under `linebot.v3.webhooks`)

See [Import and type mapping](#import-and-type-mapping) for the complete table.

### 4. Update method calls

The deprecated API used positional arguments. V3 uses request objects:

**Before (deprecated):**

```python
line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text='Hello!')
)
```

**After (v3):**

```python
from linebot.v3.messaging import ReplyMessageRequest, TextMessage

line_bot_api.reply_message(
    ReplyMessageRequest(
        reply_token=event.reply_token,
        messages=[TextMessage(text='Hello!')]
    )
)
```

See [Method mapping](#method-mapping) for the complete table.

### 5. Update webhook handler

The `WebhookHandler` works the same way, but the decorator message type has changed:

**Before (deprecated):**

```python
from linebot import WebhookHandler
from linebot.models import MessageEvent, TextMessage

handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    ...
```

**After (v3):**

```python
from linebot.v3 import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent

handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    ...
```

### 6. Update error handling

**Before (deprecated):**

```python
from linebot.exceptions import LineBotApiError

try:
    line_bot_api.push_message(to, messages)
except LineBotApiError as e:
    print(e.status_code)
    print(e.error.message)
    print(e.error.details)
```

**After (v3):**

```python
from linebot.v3.messaging.exceptions import ApiException

try:
    line_bot_api.push_message(push_message_request)
except ApiException as e:
    print(e.status)
    print(e.reason)
    print(e.body)
```

### 7. Remove deprecated imports

Once you have migrated all your code and confirmed everything works, remove any remaining imports from the deprecated modules (`linebot.api`, `linebot.models`, `linebot.exceptions`). This eliminates deprecation warnings and ensures your code only depends on maintained modules.

---

## Full echo-bot before/after example

### Before (deprecated)

```python
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run()
```

### After (v3 with handler)

```python
from flask import Flask, request, abort
from linebot.v3 import WebhookHandler, LineBotClient
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import ReplyMessageRequest, TextMessage

app = Flask(__name__)

line_bot_api = LineBotClient(channel_access_token='YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    line_bot_api.reply_message(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[TextMessage(text=event.message.text)]
        )
    )

if __name__ == "__main__":
    app.run()
```

### After (v3 with parser)

```python
from flask import Flask, request, abort
from linebot.v3 import WebhookParser, LineBotClient
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import ReplyMessageRequest, TextMessage

app = Flask(__name__)

line_bot_api = LineBotClient(channel_access_token='YOUR_CHANNEL_ACCESS_TOKEN')
parser = WebhookParser('YOUR_CHANNEL_SECRET')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessageContent):
            continue
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )
    return 'OK'

if __name__ == "__main__":
    app.run()
```

### After (v3 async with FastAPI)

```python
from fastapi import Request, FastAPI, HTTPException
from linebot.v3 import WebhookParser, AsyncLineBotClient
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import ReplyMessageRequest, TextMessage

app = FastAPI()

line_bot_api = AsyncLineBotClient(channel_access_token='YOUR_CHANNEL_ACCESS_TOKEN')
parser = WebhookParser('YOUR_CHANNEL_SECRET')

@app.post("/callback")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']
    body = (await request.body()).decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessageContent):
            continue
        await line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=event.message.text)]
            )
        )
    return 'OK'
```

---

## Client construction mapping

| Deprecated | V3 |
|---|---|
| `LineBotApi(token)` | `LineBotClient(channel_access_token=token)` |
| `AsyncLineBotApi(token, async_http_client)` | `AsyncLineBotClient(channel_access_token=token)` |

`LineBotClient` wraps the following API modules: `messaging`, `audience`, `insight`, `liff`, `module`, `moduleattach`, `shop`.

For OAuth / channel access token management, use the separate `linebot.v3.oauth` module.

---

## Import and type mapping

### Send message types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) |
|---|---|
| `TextSendMessage` | `TextMessage` |
| `ImageSendMessage` | `ImageMessage` |
| `VideoSendMessage` | `VideoMessage` |
| `AudioSendMessage` | `AudioMessage` |
| `LocationSendMessage` | `LocationMessage` |
| `StickerSendMessage` | `StickerMessage` |
| `TemplateSendMessage` | `TemplateMessage` |
| `FlexSendMessage` | `FlexMessage` |
| `ImagemapSendMessage` | `ImagemapMessage` |

### Webhook event types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.webhooks`) |
|---|---|
| `MessageEvent` | `MessageEvent` |
| `FollowEvent` | `FollowEvent` |
| `UnfollowEvent` | `UnfollowEvent` |
| `JoinEvent` | `JoinEvent` |
| `LeaveEvent` | `LeaveEvent` |
| `PostbackEvent` | `PostbackEvent` |
| `AccountLinkEvent` | `AccountLinkEvent` |
| `MemberJoinedEvent` | `MemberJoinedEvent` |
| `MemberLeftEvent` | `MemberLeftEvent` |
| `BeaconEvent` | `BeaconEvent` |
| `VideoPlayCompleteEvent` | `VideoPlayCompleteEvent` |
| `UnsendEvent` | `UnsendEvent` |

### Webhook message content types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.webhooks`) |
|---|---|
| `TextMessage` | `TextMessageContent` |
| `ImageMessage` | `ImageMessageContent` |
| `VideoMessage` | `VideoMessageContent` |
| `AudioMessage` | `AudioMessageContent` |
| `LocationMessage` | `LocationMessageContent` |
| `StickerMessage` | `StickerMessageContent` |
| `FileMessage` | `FileMessageContent` |

### Webhook other content types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.webhooks`) |
|---|---|
| `Postback` | `PostbackContent` |
| `Beacon` | `BeaconContent` |

### Source types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.webhooks`) |
|---|---|
| `SourceUser` | `UserSource` |
| `SourceGroup` | `GroupSource` |
| `SourceRoom` | `RoomSource` |

### Template types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) |
|---|---|
| `ButtonsTemplate` | `ButtonsTemplate` |
| `ConfirmTemplate` | `ConfirmTemplate` |
| `CarouselTemplate` | `CarouselTemplate` |
| `CarouselColumn` | `CarouselColumn` |
| `ImageCarouselTemplate` | `ImageCarouselTemplate` |
| `ImageCarouselColumn` | `ImageCarouselColumn` |

### Action types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `PostbackAction` | `PostbackAction` | |
| `MessageAction` | `MessageAction` | |
| `URIAction` | `URIAction` | |
| `DatetimePickerAction` | `DatetimePickerAction` | |
| `CameraAction` | `CameraAction` | |
| `CameraRollAction` | `CameraRollAction` | |
| `LocationAction` | `LocationAction` | |
| `RichMenuSwitchAction` | `RichMenuSwitchAction` | |
| `AltUri` | `AltUri` | |
| `PostbackTemplateAction` | `PostbackAction` | Alias removed |
| `MessageTemplateAction` | `MessageAction` | Alias removed |
| `URITemplateAction` | `URIAction` | Alias removed |
| `DatetimePickerTemplateAction` | `DatetimePickerAction` | Alias removed |

### Flex message types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `BubbleContainer` | `FlexBubble` | Renamed |
| `CarouselContainer` | `FlexCarousel` | Renamed |
| `BubbleStyle` | `FlexBubbleStyles` | Renamed (added `s`) |
| `BlockStyle` | `FlexBlockStyle` | Renamed |
| `BoxComponent` | `FlexBox` | Renamed |
| `ButtonComponent` | `FlexButton` | Renamed |
| `FillerComponent` | `FlexFiller` | Renamed |
| `IconComponent` | `FlexIcon` | Renamed |
| `ImageComponent` | `FlexImage` | Renamed |
| `SeparatorComponent` | `FlexSeparator` | Renamed |
| `TextComponent` | `FlexText` | Renamed |
| `SpanComponent` | `FlexSpan` | Renamed |
| `VideoComponent` | `FlexVideo` | Renamed |
| `LinearGradientBackground` | `FlexBoxLinearGradient` | Renamed |

### Imagemap types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `URIImagemapAction` | `URIImagemapAction` | |
| `MessageImagemapAction` | `MessageImagemapAction` | |
| `ImagemapArea` | `ImagemapArea` | |
| `BaseSize` | `ImagemapBaseSize` | Renamed |
| `Video` | `ImagemapVideo` | Renamed |
| `ExternalLink` | `ImagemapExternalLink` | Renamed |

### Quick reply types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `QuickReply` | `QuickReply` | |
| `QuickReplyButton` | `QuickReplyItem` | Renamed |

### Rich menu types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `RichMenu` | `RichMenuRequest` | Renamed |
| `RichMenuSize` | `RichMenuSize` | |
| `RichMenuArea` | `RichMenuArea` | |
| `RichMenuBounds` | `RichMenuBounds` | |
| `RichMenuResponse` | `RichMenuResponse` | |
| `RichMenuAlias` | `RichMenuAliasResponse` | Renamed |

### Response types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `Profile` | `UserProfileResponse` | Renamed |
| `BotInfo` | `BotInfoResponse` | Renamed |
| `Group` (from `get_group_summary`) | `GroupSummaryResponse` | Renamed |
| `MemberIds` | `MembersIdsResponse` | Renamed |
| `Content` / `MessageContent` | `bytearray` (via `MessagingApiBlob`) | Different return type |
| `MessageQuotaResponse` | `MessageQuotaResponse` | |
| `MessageQuotaConsumptionResponse` | `QuotaConsumptionResponse` | Renamed |
| `IssueLinkTokenResponse` | `IssueLinkTokenResponse` | |
| `GetWebhookResponse` | `GetWebhookEndpointResponse` | Renamed |
| `TestWebhookResponse` | `TestWebhookEndpointResponse` | Renamed |
| `MessageProgressNarrowcastResponse` | `NarrowcastProgressResponse` | Renamed |
| `MessageDeliveryBroadcastResponse` | `NumberOfMessagesResponse` | Renamed |
| `MessageDeliveryReplyResponse` | `NumberOfMessagesResponse` | Renamed |
| `MessageDeliveryPushResponse` | `NumberOfMessagesResponse` | Renamed |
| `MessageDeliveryMulticastResponse` | `NumberOfMessagesResponse` | Renamed |

### Insight response types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.insight`) | Notes |
|---|---|---|
| `InsightMessageDeliveryResponse` | `GetNumberOfMessageDeliveriesResponse` | Renamed |
| `InsightFollowersResponse` | `GetNumberOfFollowersResponse` | Renamed |
| `InsightDemographicResponse` | `GetFriendsDemographicsResponse` | Renamed |
| `InsightMessageEventResponse` | `GetMessageEventResponse` | Renamed |

### Filter / narrowcast types

| Deprecated (`linebot.models`) | V3 (`linebot.v3.messaging`) | Notes |
|---|---|---|
| `GenderFilter` | `GenderDemographicFilter` | Renamed |
| `AppTypeFilter` | `AppTypeDemographicFilter` | Renamed |
| `AreaFilter` | `AreaDemographicFilter` | Renamed |
| `AgeFilter` | `AgeDemographicFilter` | Renamed |
| `SubscriptionPeriodFilter` | `SubscriptionPeriodDemographicFilter` | Renamed |
| `AudienceRecipient` | `AudienceRecipient` | |
| `RedeliveryRecipient` | `RedeliveryRecipient` | |

### Other types

| Deprecated (`linebot.models`) | V3 | Notes |
|---|---|---|
| `Sender` | `linebot.v3.messaging.Sender` | |
| `Emojis` | `linebot.v3.messaging.Emoji` | Renamed |
| `Error` | `linebot.v3.messaging.ErrorResponse` | Renamed |
| `ErrorDetail` | `linebot.v3.messaging.ErrorDetail` | |

### Exception classes

| Deprecated (`linebot.exceptions`) | V3 |
|---|---|
| `InvalidSignatureError` | `linebot.v3.exceptions.InvalidSignatureError` |
| `LineBotApiError` | `linebot.v3.messaging.exceptions.ApiException` |

---

## Method mapping

All V3 methods also have a `_with_http_info` variant (e.g. `reply_message_with_http_info(...)`) that returns the response headers along with the response body. See [Response headers](#response-headers--x-line-request-id).

### Messaging

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `reply_message(reply_token, messages, ...)` | `reply_message(ReplyMessageRequest(...))` | Positional args → request object |
| `push_message(to, messages, ...)` | `push_message(PushMessageRequest(...))` | |
| `multicast(to, messages, ...)` | `multicast(MulticastRequest(...))` | |
| `broadcast(messages, ...)` | `broadcast(BroadcastRequest(...))` | |
| `narrowcast(messages, ...)` | `narrowcast(NarrowcastRequest(...))` | |

### Message validation

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `validate_reply_message_objects(messages)` | `validate_reply(ValidateMessageRequest(...))` | Renamed |
| `validate_push_message_objects(messages)` | `validate_push(ValidateMessageRequest(...))` | Renamed |
| `validate_multicast_message_objects(messages)` | `validate_multicast(ValidateMessageRequest(...))` | Renamed |
| `validate_broadcast_message_objects(messages)` | `validate_broadcast(ValidateMessageRequest(...))` | Renamed |
| `validate_narrowcast_message_objects(messages)` | `validate_narrowcast(ValidateMessageRequest(...))` | Renamed |

### Profile and group management

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `get_profile(user_id)` | `get_profile(user_id)` | Unchanged |
| `get_group_summary(group_id)` | `get_group_summary(group_id)` | Unchanged |
| `get_group_member_profile(group_id, user_id)` | `get_group_member_profile(group_id, user_id)` | Unchanged |
| `get_room_member_profile(room_id, user_id)` | `get_room_member_profile(room_id, user_id)` | Unchanged |
| `get_group_members_count(group_id)` | `get_group_member_count(group_id)` | Renamed (removed `s`) |
| `get_room_members_count(room_id)` | `get_room_member_count(room_id)` | Renamed (removed `s`) |
| `get_group_member_ids(group_id, start)` | `get_group_members_ids(group_id, start)` | Renamed (added `s`) |
| `get_room_member_ids(room_id, start)` | `get_room_members_ids(room_id, start)` | Renamed (added `s`) |
| `get_followers_ids(limit, start)` | `get_followers(start, limit)` | Renamed, parameter order changed |
| `get_bot_info()` | `get_bot_info()` | Unchanged |
| `leave_group(group_id)` | `leave_group(group_id)` | Unchanged |
| `leave_room(room_id)` | `leave_room(room_id)` | Unchanged |

### Message content

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `get_message_content(message_id)` | `get_message_content(message_id)` | Returns `bytearray` instead of `Content` |

### Rich menu management

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `get_rich_menu(rich_menu_id)` | `get_rich_menu(rich_menu_id)` | Unchanged |
| `create_rich_menu(rich_menu)` | `create_rich_menu(RichMenuRequest(...))` | Uses request object |
| `delete_rich_menu(rich_menu_id)` | `delete_rich_menu(rich_menu_id)` | Unchanged |
| `get_rich_menu_alias(rich_menu_alias_id)` | `get_rich_menu_alias(rich_menu_alias_id)` | Unchanged |
| `get_rich_menu_alias_list()` | `get_rich_menu_alias_list()` | Unchanged |
| `create_rich_menu_alias(rich_menu_alias)` | `create_rich_menu_alias(CreateRichMenuAliasRequest(...))` | Uses request object |
| `update_rich_menu_alias(id, alias)` | `update_rich_menu_alias(id, UpdateRichMenuAliasRequest(...))` | Uses request object |
| `delete_rich_menu_alias(id)` | `delete_rich_menu_alias(id)` | Unchanged |
| `validate_rich_menu_object(rich_menu)` | `validate_rich_menu_object(RichMenuRequest(...))` | Uses request object |
| `get_rich_menu_id_of_user(user_id)` | `get_rich_menu_id_of_user(user_id)` | Unchanged |
| `link_rich_menu_to_user(user_id, rich_menu_id)` | `link_rich_menu_id_to_user(user_id, rich_menu_id)` | Renamed |
| `unlink_rich_menu_from_user(user_id)` | `unlink_rich_menu_id_from_user(user_id)` | Renamed |
| `link_rich_menu_to_users(user_ids, rich_menu_id)` | `link_rich_menu_id_to_users(RichMenuBulkLinkRequest(...))` | Renamed, uses request object |
| `unlink_rich_menu_from_users(user_ids)` | `unlink_rich_menu_id_from_users(RichMenuBulkUnlinkRequest(...))` | Renamed, uses request object |
| `get_rich_menu_image(rich_menu_id)` | `get_rich_menu_image(rich_menu_id)` | Unchanged |
| `set_rich_menu_image(id, content_type, content)` | `set_rich_menu_image(id, body)` | `content_type` removed |
| `get_rich_menu_list()` | `get_rich_menu_list()` | Unchanged |
| `set_default_rich_menu(rich_menu_id)` | `set_default_rich_menu(rich_menu_id)` | Unchanged |
| `get_default_rich_menu()` | `get_default_rich_menu_id()` | Renamed |
| `cancel_default_rich_menu()` | `cancel_default_rich_menu()` | Unchanged |

### Webhook endpoint management

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `set_webhook_endpoint(url)` | `set_webhook_endpoint(SetWebhookEndpointRequest(...))` | Uses request object |
| `get_webhook_endpoint()` | `get_webhook_endpoint()` | Unchanged |
| `test_webhook_endpoint(url)` | `test_webhook_endpoint(TestWebhookEndpointRequest(...))` | Uses request object |

### Link token

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `issue_link_token(user_id)` | `issue_link_token(user_id)` | Unchanged |

### Message delivery statistics

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `get_message_delivery_reply(date)` | `get_number_of_sent_reply_messages(date)` | Renamed |
| `get_message_delivery_push(date)` | `get_number_of_sent_push_messages(date)` | Renamed |
| `get_message_delivery_multicast(date)` | `get_number_of_sent_multicast_messages(date)` | Renamed |
| `get_message_delivery_broadcast(date)` | `get_number_of_sent_broadcast_messages(date)` | Renamed |
| `get_progress_status_narrowcast(request_id)` | `get_narrowcast_progress(request_id)` | Renamed |
| `get_message_quota()` | `get_message_quota()` | Unchanged |
| `get_message_quota_consumption()` | `get_message_quota_consumption()` | Unchanged |
| `get_number_of_units_used_this_month()` | `get_aggregation_unit_usage()` | Renamed |
| `get_name_list_of_units_used_this_month(limit, start)` | `get_aggregation_unit_name_list(limit, start)` | Renamed |

### Insight API

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `get_insight_message_delivery(date)` | `get_number_of_message_deliveries(date)` | Renamed |
| `get_insight_followers(date)` | `get_number_of_followers(date)` | Renamed |
| `get_insight_demographic()` | `get_friends_demographics()` | Renamed |
| `get_insight_message_event(request_id)` | `get_message_event(request_id)` | Renamed |
| `get_statistics_per_unit(unit, from_date, to_date)` | `get_statistics_per_unit(unit, from, to)` | Unchanged |

### Audience management

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| `create_audience_group(name, audiences, is_ifa)` | `create_audience_group(CreateAudienceGroupRequest(...))` | Uses request object |
| `get_audience_group(audience_group_id)` | `get_audience_data(audience_group_id)` | Renamed |
| `get_audience_group_list(page, ...)` | `get_audience_groups(page, ...)` | Renamed |
| `delete_audience_group(audience_group_id)` | `delete_audience_group(audience_group_id)` | Unchanged |
| `rename_audience_group(id, description)` | `update_audience_group_description(id, UpdateAudienceGroupDescriptionRequest(...))` | Renamed, uses request object |
| `add_audiences_to_audience_group(id, audiences, ...)` | `add_audience_to_audience_group(AddAudienceToAudienceGroupRequest(...))` | Renamed, uses request object |
| `create_click_audience_group(desc, request_id, url)` | `create_click_based_audience_group(CreateClickBasedAudienceGroupRequest(...))` | Renamed, uses request object |
| `create_imp_audience_group(desc, request_id)` | `create_imp_based_audience_group(CreateImpBasedAudienceGroupRequest(...))` | Renamed, uses request object |
| `get_audience_group_authority_level()` | _(removed)_ | No V3 equivalent |
| `change_audience_group_authority_level(level)` | _(removed)_ | No V3 equivalent |

### LIFF

| Deprecated (`LineBotApi`) | V3 (`LineBotClient`) | Notes |
|---|---|---|
| _(not in deprecated API)_ | `add_liff_app(AddLiffAppRequest(...))` | New in v3 |
| _(not in deprecated API)_ | `update_liff_app(liff_id, UpdateLiffAppRequest(...))` | New in v3 |
| _(not in deprecated API)_ | `delete_liff_app(liff_id)` | New in v3 |
| _(not in deprecated API)_ | `get_all_liff_apps()` | New in v3 |

### OAuth / Channel access token

OAuth methods that were on `LineBotApi` have been moved to a separate module in v3:

| Deprecated (`LineBotApi`) | V3 (`linebot.v3.oauth.ChannelAccessToken`) | Notes |
|---|---|---|
| `issue_channel_token(client_id, client_secret)` | `issue_channel_token(grant_type, client_id, client_secret)` | `grant_type` now explicit |
| `revoke_channel_token(access_token)` | `revoke_channel_token(access_token)` | Unchanged |
| `issue_channel_access_token_v2_1(client_assertion)` | `issue_channel_token_by_jwt(grant_type, client_assertion_type, client_assertion)` | Renamed, args now explicit |
| `revoke_channel_access_token_v2_1(client_id, client_secret, access_token)` | `revoke_channel_token_by_jwt(client_id, client_secret, access_token)` | Renamed |
| `verify_channel_access_token_v2_1(access_token)` | `verify_channel_token_by_jwt(access_token)` | Renamed |
| `get_channel_token_key_ids_v2_1(client_assertion)` | `gets_all_valid_channel_access_token_key_ids(client_assertion_type, client_assertion)` | Renamed |
| `get_channel_access_tokens_v2_1(client_assertion)` | _(removed)_ | No V3 equivalent |

---

## Error handling

### Before (deprecated)

```python
from linebot.exceptions import LineBotApiError

try:
    line_bot_api.push_message('USER_ID', TextSendMessage(text='Hello!'))
except LineBotApiError as e:
    print(e.status_code)      # HTTP status code (e.g. 400)
    print(e.request_id)       # X-Line-Request-Id
    print(e.error.message)    # Error message from API
    print(e.error.details)    # List of error details
```

### After (v3)

```python
from linebot.v3.messaging import PushMessageRequest, TextMessage
from linebot.v3.messaging.exceptions import ApiException

try:
    line_bot_api.push_message(
        PushMessageRequest(
            to='USER_ID',
            messages=[TextMessage(text='Hello!')]
        )
    )
except ApiException as e:
    print(e.status)    # HTTP status code (e.g. 400)
    print(e.reason)    # Reason phrase
    print(e.headers)   # Response headers (includes x-line-request-id)
    print(e.body)      # Response body as string
```

---

## Response headers / x-line-request-id

In the deprecated API, `x-line-request-id` was only accessible through `LineBotApiError`. In v3, use the `_with_http_info` methods to access response headers for successful requests:

```python
from linebot.v3.messaging import ReplyMessageRequest, TextMessage

response = line_bot_api.reply_message_with_http_info(
    ReplyMessageRequest(
        reply_token=event.reply_token,
        messages=[TextMessage(text='Hello!')]
    )
)

print(response.status_code)                     # HTTP status code
print(response.headers.get('x-line-request-id')) # Request ID
```

---

## Suppressing deprecation warnings

During migration, you may see deprecation warnings when using the old `linebot` modules. To suppress them:

```python
import warnings
from linebot import LineBotSdkDeprecatedIn30

warnings.filterwarnings("ignore", category=LineBotSdkDeprecatedIn30)
```

> **Tip:** Only suppress these warnings temporarily. Once your migration is complete, remove both the warning filter and the deprecated imports.
