LINE Messaging API SDK for Python
=================================

|Build Status| |Documentation Status|

SDK of the LINE Messaging API for Python.

Introduction
------------
The LINE Messaging API SDK for Python makes it easy to develop bots using LINE Messaging API, and you can create a sample bot within minutes.


Documentation
-------------

See the official API documentation for more information

English: https://developers.line.biz/en/docs/messaging-api/overview/

Japanese: https://developers.line.biz/ja/docs/messaging-api/overview/

Requirements
------------

-  Python >= 3.7

Installation
------------

::

    $ pip install line-bot-sdk

Synopsis
--------

Usage:

.. code:: python

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
            print("Invalid signature. Please check your channel access token/channel secret.")
            abort(400)

        return 'OK'


    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))


    if __name__ == "__main__":
        app.run()

API
---

LineBotApi
~~~~~~~~~~

\_\_init\_\_(self, channel\_access\_token, endpoint='https://api.line.me', timeout=5, http\_client=RequestsHttpClient)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new LineBotApi instance.

.. code:: python

    line_bot_api = linebot.LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')

You can override the ``timeout`` value for each method.

reply\_message(self, reply\_token, messages, notification_disabled=False, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Respond to events from users, groups, and rooms. You can get a
reply\_token from a webhook event object.

https://developers.line.biz/en/reference/messaging-api/#send-reply-message

.. code:: python

    line_bot_api.reply_message(reply_token, TextSendMessage(text='Hello World!'))

push\_message(self, to, messages, notification_disabled=False, custom_aggregation_units=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send messages to users, groups, and rooms at any time.

https://developers.line.biz/en/reference/messaging-api/#send-push-message

.. code:: python

    line_bot_api.push_message(to, TextSendMessage(text='Hello World!'))

multicast(self, to, messages, notification_disabled=False, custom_aggregation_units=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send push messages to multiple users at any time. Messages cannot be sent to groups or rooms.

https://developers.line.biz/en/reference/messaging-api/#send-multicast-message

.. code:: python

    line_bot_api.multicast(['to1', 'to2'], TextSendMessage(text='Hello World!'))

broadcast(self, messages, notification_disabled=False, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send push messages to multiple users at any time.

https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message

.. code:: python

    line_bot_api.broadcast(TextSendMessage(text='Hello World!'))

narrowcast(self, messages, recipient=None, filter=None, limit=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a push message to multiple users specified by attributes (such as age, gender, OS, and region)
or retargeting (audiences).

https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message

.. code:: python

    line_bot_api.narrowcast(
        messages=TextSendMessage(text='Hello World!'),
        recipient=AudienceRecipient(group_id=5614991017776),
        filter=Filter(demographic=AgeFilter(gte="age_35", lt="age_40")),
        limit=Limit(max=10)
    )

get_progress_status_narrowcast(self, request_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get progress status of narrowcast messages sent.

https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status

.. code:: python

    narrowcast_progress = line_bot_api.get_progress_status_narrowcast(request_id)
    assert narrowcast_progress.phase == 'succeeded'
    print(narrowcast.success_count)
    print(narrowcast.failure_count)
    print(narrowcast.target_count)


get\_profile(self, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get user profile information.

https://developers.line.biz/en/reference/messaging-api/#get-profile

.. code:: python

    profile = line_bot_api.get_profile(user_id)

    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)
    print(profile.status_message)

get\_group\_summary(self, group\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Gets the group ID, group name, and group icon URL of a group
where the LINE Official Account is a member.

https://developers.line.biz/en/reference/messaging-api/#get-group-summary

.. code:: python

    summary = line_bot_api.get_group_summary(group_id)
    print(summary.group_id)
    print(summary.group_name)
    print(summary.picture_url)

get\_group\_member\_profile(self, group\_id, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the user profile of a member of a group that the bot is in. This can be
the user ID of a user who has not added the bot as a friend or has blocked
the bot.

https://developers.line.biz/en/reference/messaging-api/#get-group-member-profile

.. code:: python

    profile = line_bot_api.get_group_member_profile(group_id, user_id)

    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)

get\_room\_member\_profile(self, room\_id, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the user profile of a member of a room that the bot is in. This can be the
user ID of a user who has not added the bot as a friend or has blocked the bot.

https://developers.line.biz/en/reference/messaging-api/#get-room-member-profile

.. code:: python

    profile = line_bot_api.get_room_member_profile(room_id, user_id)

    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)

get\_group\_member\_ids(self, group\_id, start=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the user IDs of the members of a group that the bot is in.
This includes the user IDs of users who have not added the bot as a friend or has blocked the bot.

https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids

.. code:: python

    member_ids_res = line_bot_api.get_group_member_ids(group_id)

    print(member_ids_res.member_ids)
    print(member_ids_res.next)

get\_room\_member\_ids(self, room\_id, start=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the user IDs of the members of a room that the bot is in.
This includes the user IDs of users who have not added the bot as a friend or has blocked the bot.

https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids

.. code:: python

    member_ids_res = line_bot_api.get_room_member_ids(room_id)

    print(member_ids_res.member_ids)
    print(member_ids_res.next)

get\_group\_members\_count(self, group\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the count of members in a group.

https://developers.line.biz/en/reference/messaging-api/#get-members-group-count

.. code:: python

    group_count = line_bot_api.get_group_members_count(group_id)
    print(group_count)

get\_room\_members\_count(self, room\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the count of members in a room.

https://developers.line.biz/en/reference/messaging-api/#get-members-room-count

.. code:: python

    room_count = line_bot_api.get_room_members_count(room_id)
    print(room_count)

get\_message\_content(self, message\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieve image, video, and audio data sent by users.

https://developers.line.biz/en/reference/messaging-api/#get-content

.. code:: python

    message_content = line_bot_api.get_message_content(message_id)

    with open(file_path, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)

leave\_group(self, group\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leave a group.

https://developers.line.biz/en/reference/messaging-api/#leave-group

.. code:: python

    line_bot_api.leave_group(group_id)

leave\_room(self, room\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Leave a room.

https://developers.line.biz/en/reference/messaging-api/#leave-room

.. code:: python

    line_bot_api.leave_room(room_id)

get\_rich\_menu(self, rich\_menu\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a rich menu via a rich menu ID.

https://developers.line.biz/en/reference/messaging-api/#get-rich-menu

.. code:: python

    rich_menu = line_bot_api.get_rich_menu(rich_menu_id)
    print(rich_menu.rich_menu_id)

validate\_rich\_menu\_object(self, rich\_menu, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Validate a rich menu object.
You can verify that a rich menu object is valid as a request body for creating rich menu.

https://developers.line.biz/ja/reference/messaging-api/#validate-rich-menu-object

.. code:: python

    rich_menu_to_validate = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="Nice richmenu",
        chat_bar_text="Tap here",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me'))]
    )
    line_bot_api.validate_rich_menu_object(rich_menu=rich_menu_to_validate)

create\_rich\_menu(self, rich\_menu, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Creates a rich menu.
You must upload a rich menu image and link the rich menu to a user for the rich menu to be displayed. You can create up to 1000 rich menus for one LINE Official Account with the Messaging API.

https://developers.line.biz/en/reference/messaging-api/#create-rich-menu

.. code:: python

    rich_menu_to_create = RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=False,
        name="Nice richmenu",
        chat_bar_text="Tap here",
        areas=[RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me'))]
    )
    rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
    print(rich_menu_id)

delete\_rich\_menu(self, rich\_menu\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletes a rich menu.

https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu

.. code:: python

    line_bot_api.delete_rich_menu(rich_menu_id)

get\_rich\_menu\_id\_of\_user(self, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the ID of the rich menu linked to a user.

https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-id-of-user

.. code:: python

    rich_menu_id = line_bot_api.get_rich_menu_id_of_user(user_id)
    print(rich_menu_id)

link\_rich\_menu\_to\_user(self, user\_id, rich\_menu\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Links a rich menu to a user. Only one rich menu can be linked to a user at one time.

https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user

.. code:: python

    line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)

link\_rich\_menu\_to\_users(self, user\_ids, rich\_menu\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Links a rich menu to multiple users.

https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-users

.. code:: python

    line_bot_api.link_rich_menu_to_users(<user_ids>, <rich_menu_id>)

unlink\_rich\_menu\_from\_user(self, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlinks a rich menu from a user.

https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user

.. code:: python

    line_bot_api.unlink_rich_menu_from_user(user_id)

unlink\_rich\_menu\_from\_users(self, user\_ids, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Unlinks rich menus from multiple users.

https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-users

.. code:: python

    line_bot_api.unlink_rich_menu_from_users(<user_ids>)

get\_rich\_menu\_image(self, rich\_menu\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Downloads an image associated with a rich menu.

https://developers.line.biz/en/reference/messaging-api/#download-rich-menu-image

.. code:: python

    content = line_bot_api.get_rich_menu_image(rich_menu_id)
    with open(file_path, 'wb') as fd:
        for chunk in content.iter_content():
            fd.write(chunk)

set\_rich\_menu\_image(self, rich\_menu\_id, content\_type, content, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uploads and attaches an image to a rich menu.

https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image

.. code:: python

    with open(file_path, 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, content_type, f)

get\_rich\_menu\_list(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets a list of all uploaded rich menus.

https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-list

.. code:: python

    rich_menu_list = line_bot_api.get_rich_menu_list()
    for rich_menu in rich_menu_list:
        print(rich_menu.rich_menu_id)

set\_default\_rich\_menu(self, rich\_menu\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sets the default rich menu.

https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu

.. code:: python

    line_bot_api.set_default_rich_menu(<rich_menu_id>)

get\_default\_rich\_menu(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gets the ID of the default rich menu set with the Messaging API.

https://developers.line.biz/en/reference/messaging-api/#get-default-rich-menu-id

.. code:: python

    line_bot_api.get_default_rich_menu()

cancel\_default\_rich\_menu(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cancels the default rich menu set with the Messaging API.

https://developers.line.biz/en/reference/messaging-api/#cancel-default-rich-menu

.. code:: python

    line_bot_api.cancel_default_rich_menu()

issue\_link\_token(self, user\_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Issues a link token used for the account link feature.

https://developers.line.biz/en/reference/messaging-api/#issue-link-token

.. code:: python

    link_token_response = line_bot_api.issue_link_token(<user_id>)
    print(link_token_response)

issue\_channel\_token(self, client_id, client_secret, grant_type='client_credentials', timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Issues a short-lived channel access token.

https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token

.. code:: python

    channel_token_response = line_bot_api.issue_channel_token(<client_id>, <client_secret>)
    print(access_token_response)

revoke\_channel\_token(self, access_token, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Revokes a channel access token.

https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token

.. code:: python

    line_bot_api.revoke_channel_token(<access_token>)

get\_insight\_message\_delivery(self, date, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the number of messages sent on a specified day.

https://developers.line.biz/en/reference/messaging-api/#get-number-of-delivery-messages

.. code:: python

    insight = line_bot_api.get_insight_message_delivery('20191231')
    print(insight.api_broadcast)

get\_insight\_followers(self, date, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get the number of users who have added the bot on or before a specified date.

https://developers.line.biz/en/reference/messaging-api/#get-number-of-followers

.. code:: python

    insight = line_bot_api.get_insight_followers('20191231')
    print(insight.followers)

get\_insight\_demographic(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieve the demographic attributes for a bot's friends.

https://developers.line.biz/en/reference/messaging-api/#get-demographic

.. code:: python

    insight = line_bot_api.get_insight_demographic()
    print(insight.genders)

get\_insight\_message\_event(self, request_id, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return statistics about how users interact with broadcast messages.

https://developers.line.biz/en/reference/messaging-api/#get-message-event

.. code:: python

    broadcast_response = line_bot_api.broadcast(TextSendMessage(text='Hello World!'))
    insight = line_bot_api.get_insight_message_event(broadcast_response.request_id)
    print(insight.overview)

get\_statistics\_per\_unit(self, custom_aggregation_unit, from_date, to_date, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return statistics about how users interact with push and multicast messages.

https://developers.line.biz/en/reference/partner-docs/#get-statistics-per-unit

.. code:: python

    unit_name = 'promotion_a'
    line_bot_api.push_message('to', TextSendMessage(text='Hello World!'), custom_aggregation_units=unit_name)
    insight = line_bot_api.get_statistics_per_unit(unit_name, '20210301', '20210331')
    print(insight.overview)

get\_number\_of\_units\_used\_this\_month(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the number of aggregation units used this month.

https://developers.line.biz/en/reference/partner-docs/#get-number-of-units-used-this-month

.. code:: python

    usage = line_bot_api.get_number_of_units_used_this_month()
    print(usage.num_of_custom_aggregation_units)

get\_name\_list\_of\_units\_used\_this\_month(self, limit=100, start=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return the name list of units used this month for statistics aggregation.

https://developers.line.biz/en/reference/partner-docs/#get-name-list-of-units-used-this-month

.. code:: python

    name_list = line_bot_api.get_name_list_of_units_used_this_month()
    print(name_list.custom_aggregation_units)
    print(name_list.next)

get\_bot\_info(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get bot's basic information.

https://developers.line.biz/en/reference/messaging-api/#get-bot-info

.. code:: python

    bot_info = line_bot_api.get_bot_info()

    print(bot_info.display_name)
    print(bot_info.user_id)
    print(bot_info.basic_id)
    print(bot_info.premium_id)
    print(bot_info.picture_url)
    print(bot_info.chat_mode)
    print(bot_info.mark_as_read_mode)

set\_webhook\_endpoint(self, webhook_endpoint, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the webhook endpoint URL.

https://developers.line.biz/en/reference/messaging-api/#set-webhook-endpoint-url

.. code:: python

    line_bot_api.set_webhook_endpoint(<webhook_endpoint_URL>)

get\_webhook\_endpoint(self, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get information on a webhook endpoint.

https://developers.line.biz/en/reference/messaging-api/#get-webhook-endpoint-information

.. code:: python

    webhook = line_bot_api.get_webhook_endpoint()
    print(webhook.endpoint)
    print(webhook.active)

test\_webhook\_endpoint(self, webhook_endpoint=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check if the configured webhook endpoint can receive a test webhook event.

https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint

.. code:: python

    test_result = line_bot_api.test_webhook_endpoint()
    print(test_result.success)
    print(test_result.timestamp)
    print(test_result.status_code)
    print(test_result.reason)
    print(test_result.detail)

get\_followers\_ids(self, limit=300, start=None, timeout=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Get a list of users who added your LINE Official Account as a friend.

https://developers.line.biz/en/reference/messaging-api/#get-follower-ids

.. code:: python

    test_result = line_bot_api.get_followers_ids()
    print(test_result.user_ids)
    print(test_result.next)

※ Error handling
^^^^^^^^^^^^^^^^^

If the LINE API server returns an error, LineBotApi raises LineBotApiError.

https://developers.line.biz/en/reference/messaging-api/#error-responses

.. code:: python

    try:
        line_bot_api.push_message('to', TextSendMessage(text='Hello World!'))
    except linebot.exceptions.LineBotApiError as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error.message)
        print(e.error.details)

Message objects
~~~~~~~~~~~~~~~

https://developers.line.biz/en/reference/messaging-api/#message-objects

The following classes are found in the ``linebot.models`` package.

TextSendMessage
^^^^^^^^^^^^^^^

.. code:: python

    text_message = TextSendMessage(text='Hello, world')

TextSendMessage-Emoji
^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    emoji = [
        {
            "index": 0,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "001"
        },  
        {
            "index": 13,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "002"
        }
    ]
    text_message = TextSendMessage(text='$ LINE emoji $', emojis=emoji)

ImageSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    image_message = ImageSendMessage(
        original_content_url='https://example.com/original.jpg',
        preview_image_url='https://example.com/preview.jpg'
    )

VideoSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    video_message = VideoSendMessage(
        original_content_url='https://example.com/original.mp4',
        preview_image_url='https://example.com/preview.jpg'
    )

AudioSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    audio_message = AudioSendMessage(
        original_content_url='https://example.com/original.m4a',
        duration=240000
    )

LocationSendMessage
^^^^^^^^^^^^^^^^^^^

.. code:: python

    location_message = LocationSendMessage(
        title='my location',
        address='Tokyo',
        latitude=35.65910807942215,
        longitude=139.70372892916203
    )

StickerSendMessage
^^^^^^^^^^^^^^^^^^

.. code:: python

    sticker_message = StickerSendMessage(
        package_id='1',
        sticker_id='1'
    )

ImagemapSendMessage
^^^^^^^^^^^^^^^^^^^

.. code:: python

    imagemap_message = ImagemapSendMessage(
        base_url='https://example.com/base',
        alt_text='this is an imagemap',
        base_size=BaseSize(height=1040, width=1040),
        video=Video(
            original_content_url='https://example.com/video.mp4',
            preview_image_url='https://example.com/video_preview.jpg',
            area=ImagemapArea(
                x=0, y=0, width=1040, height=585
            ),
            external_link=ExternalLink(
                link_uri='https://example.com/see_more.html',
                label='See More',
            ),
        ),
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

TemplateSendMessage - ButtonsTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://example.com/image.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackAction(
                    label='postback',
                    display_text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageAction(
                    label='message',
                    text='message text'
                ),
                URIAction(
                    label='uri',
                    uri='http://example.com/'
                )
            ]
        )
    )

TemplateSendMessage - ConfirmTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    confirm_template_message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='Are you sure?',
            actions=[
                PostbackAction(
                    label='postback',
                    display_text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageAction(
                    label='message',
                    text='message text'
                )
            ]
        )
    )

TemplateSendMessage - CarouselTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackAction(
                            label='postback1',
                            display_text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
                        URIAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ], 
                    default_action=[
                        URIAction(
                            label="uri1".,
                            uri='http://example.com/1'
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackAction(
                            label='postback2',
                            display_text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageAction(
                            label='message2',
                            text='message text2'
                        ),
                        URIAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ], 
                    default_action=[
                        URIAction(
                            label="uri1".,
                            uri='http://example.com/1'
                    ]
                )
            ]
        )
    )

TemplateSendMessage - ImageCarouselTemplate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    image_carousel_template_message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://example.com/item1.jpg',
                    action=PostbackAction(
                        label='postback1',
                        display_text='postback text1',
                        data='action=buy&itemid=1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://example.com/item2.jpg',
                    action=PostbackAction(
                        label='postback2',
                        display_text='postback text2',
                        data='action=buy&itemid=2'
                    )
                )
            ]
        )
    )

FlexSendMessage
^^^^^^^^^^^^^^^^

.. code:: python

    flex_message = FlexSendMessage(
        alt_text='hello',
        contents=BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://example.com/cafe.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            )
        )
    )

※ You can pass a **dict** to FlexSendMessage#contents as follows:

.. code:: python

    flex_message = FlexSendMessage(
        alt_text='hello',
        contents={
            'type': 'bubble',
            'direction': 'ltr',
            'hero': {
                'type': 'image',
                'url': 'https://example.com/cafe.jpg',
                'size': 'full',
                'aspectRatio': '20:13',
                'aspectMode': 'cover',
                'action': { 'type': 'uri', 'uri': 'http://example.com', 'label': 'label' }
            }
        }
    )

Thus, You can send a JSON designed with `Flex Message Simulator <https://developers.line.biz/console/fx/>`__.

With QuickReply
^^^^^^^^^^^^^^^

.. code:: python

    text_message = TextSendMessage(text='Hello, world',
                                   quick_reply=QuickReply(items=[
                                       QuickReplyButton(action=MessageAction(label="label", text="text"))
                                   ]))

With Sender
^^^^^^^^^^^

.. code:: python

    text_message = TextSendMessage(text='Hello, world',
                                   sender=Sender(name='name', icon_url='https://example.com/icon.jpg'))

Webhook
-------

WebhookParser
~~~~~~~~~~~~~

※ You can use WebhookParser

\_\_init\_\_(self, channel\_secret)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    parser = linebot.WebhookParser('YOUR_CHANNEL_SECRET')

parse(self, body, signature, as_payload=False)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Parses the webhook body, and returns a list of Event objects or a WebhookPayload object (depending on as_payload).
If the signature does NOT match, ``InvalidSignatureError`` is raised.

.. code:: python

    events = parser.parse(body, signature)

    for event in events:
        do_something(event)

.. code:: python

    payload = parser.parse(body, signature, as_payload=True)

    for event in payload.events:
        do_something(payload.event, payload.destination)

WebhookHandler
~~~~~~~~~~~~~~

※ You can use WebhookHandler

\_\_init\_\_(self, channel\_secret)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    handler = linebot.WebhookHandler('YOUR_CHANNEL_SECRET')

handle(self, body, signature)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Handles webhooks with **handlers** added
by the decorators `add <#add-self-event-message-none>`__ and `default <#default-self>`__.
If the signature does NOT match, ``InvalidSignatureError`` is raised.

.. code:: python

    handler.handle(body, signature)

add(self, event, message=None)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a **handler** method by using this decorator.

.. code:: python

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

When the event is an instance of MessageEvent and event.message is an instance of TextMessage,
this handler method is called.

.. code:: python

    @handler.add(MessageEvent)
    def handle_message(event, destination):
        # do something

If the arity of the handler method is more than one,
a destination property in a webhook request is passed to it as the second argument.

.. code:: python

    @handler.add(FollowEvent)
    def handle_follow():
        # do something

If the arity of the handler method is zero, the handler method is called with no arguments.

default(self)
^^^^^^^^^^^^^

Set the default **handler** method by using this decorator.

.. code:: python

    @handler.default()
    def default(event):
        print(event)

If there is no handler for an event, this default handler method is called.

WebhookPayload
~~~~~~~~~~~~~~~

https://developers.line.biz/en/reference/messaging-api/#request-body

- WebhookPayload
    - destination
    - events: list[`Event <#event>`__]

Webhook event object
~~~~~~~~~~~~~~~~~~~~

https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects

The following classes are found in the ``linebot.models`` package.

`Event <https://line-bot-sdk-python.readthedocs.io/en/stable/linebot.models.html#module-linebot.models.events>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- MessageEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - message: `Message <#message>`__
- FollowEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
- UnfollowEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
- JoinEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
- LeaveEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
- PostbackEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - postback: Postback
        - data
        - params: dict
- BeaconEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - beacon: Beacon
        - type
        - hwid
        - device_message
- MemberJoinedEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - joined: Joined
- MemberLeftEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - left: Left
- AccountLinkEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - link: Link
- ThingsEvent
    - type
    - mode
    - timestamp
    - source: `Source <#source>`__
    - reply\_token
    - things: DeviceLink | DeviceUnlink | ScenarioResult

Source
^^^^^^

- SourceUser
    - type
    - user\_id
- SourceGroup
    - type
    - group\_id
    - user\_id
- SourceRoom
    - type
    - room\_id
    - user\_id

Message
^^^^^^^

- TextMessage
    - type
    - id
    - text
- TextMessage-Emoji
    - type
    - id
    - text
    - emojis_index
    - emojis_productId
    - emojis_emojiId
- ImageMessage
    - type
    - id
    - content_provider
- VideoMessage
    - type
    - id
    - duration
    - content_provider
- AudioMessage
    - type
    - id
    - duration
    - content_provider
- LocationMessage
    - type
    - id
    - title
    - address
    - latitude
    - longitude
- StickerMessage
    - type
    - id
    - package\_id
    - sticker\_id
    - sticker\_resource\_type
    - keywords
    - text
- FileMessage
    - type
    - id
    - file\_size
    - file\_name

Hints
-----

Experimental Asyncio support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The LINE Messaging API SDK for Python includes experimental asyncio support.
(API may change without notice in a future version)

.. code:: python

    import os
    import sys
    from argparse import ArgumentParser

    import asyncio
    import aiohttp
    from aiohttp import web

    import logging

    from aiohttp.web_runner import TCPSite

    from linebot import (
        AsyncLineBotApi, WebhookParser
    )
    from linebot.aiohttp_async_http_client import AiohttpAsyncHttpClient
    from linebot.exceptions import (
        InvalidSignatureError
    )
    from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage,
    )

    # get channel_secret and channel_access_token from your environment variable
    channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
    channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
    if channel_secret is None:
        print('Specify LINE_CHANNEL_SECRET as environment variable.')
        sys.exit(1)
    if channel_access_token is None:
        print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
        sys.exit(1)


    class Handler:
        def __init__(self, line_bot_api, parser):
            self.line_bot_api = line_bot_api
            self.parser = parser

        async def echo(self, request):
            signature = request.headers['X-Line-Signature']
            body = await request.text()

            try:
                events = self.parser.parse(body, signature)
            except InvalidSignatureError:
                return web.Response(status=400, text='Invalid signature')

            for event in events:
                if not isinstance(event, MessageEvent):
                    continue
                if not isinstance(event.message, TextMessage):
                    continue

                await self.line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=event.message.text)
                )

            return web.Response(text="OK\n")


    async def main(port=8000):
        session = aiohttp.ClientSession()
        async_http_client = AiohttpAsyncHttpClient(session)
        line_bot_api = AsyncLineBotApi(channel_access_token, async_http_client)
        parser = WebhookParser(channel_secret)

        handler = Handler(line_bot_api, parser)

        app = web.Application()
        app.add_routes([web.post('/callback', handler.echo)])

        runner = web.AppRunner(app)
        await runner.setup()
        site = TCPSite(runner=runner, port=port)
        await site.start()
        while True:
            await asyncio.sleep(3600)  # sleep forever


    if __name__ == "__main__":
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

        arg_parser = ArgumentParser(
            usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
        )
        arg_parser.add_argument('-p', '--port', type=int, default=8000, help='port')
        options = arg_parser.parse_args()

        asyncio.run(main(options.port))



Examples
~~~~~~~~

`simple-server-echo <https://github.com/line/line-bot-sdk-python/tree/master/examples/simple-server-echo>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sample echo-bot using
`wsgiref.simple\_server <https://docs.python.org/3/library/wsgiref.html>`__

`flask-echo <https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sample echo-bot using `Flask <http://flask.pocoo.org/>`__

`flask-kitchensink <https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-kitchensink>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sample bot using `Flask <http://flask.pocoo.org/>`__

API documentation
-----------------

::

    $ cd docs
    $ make html
    $ open build/html/index.html

OR |Documentation Status|

Help and media
--------------
FAQ: https://developers.line.biz/en/faq/

Community Q&A: https://www.line-community.me/questions

News: https://developers.line.biz/en/news/

Twitter: @LINE_DEV

Versioning
----------
This project respects semantic versioning

See http://semver.org/

Contributing
------------
Please check `CONTRIBUTING <CONTRIBUTING.md>`__ before making a contribution.

For SDK developers
------------------

First install for development.

::

    $ pip install -r requirements-dev.txt

Run tests
~~~~~~~~~

Test by using tox. We test against the following versions.

-  3.7
-  3.8
-  3.9
-  3.10

To run all tests and to run ``flake8`` against all versions, use:

::

    tox

To run all tests against version 3.7, use:

::

    $ tox -e py3.7

To run a test against version 3.7 and against a specific file, use:

::

    $ tox -e py3.7 -- tests/test_webhook.py


.. |Build Status| image:: https://travis-ci.org/line/line-bot-sdk-python.svg?branch=master
   :target: https://travis-ci.org/line/line-bot-sdk-python
.. |PyPI version| image:: https://badge.fury.io/py/line-bot-sdk.svg
   :target: https://badge.fury.io/py/line-bot-sdk
.. |Documentation Status| image:: https://readthedocs.org/projects/line-bot-sdk-python/badge/?version=stable
   :target: http://line-bot-sdk-python.readthedocs.io/en/stable

License
--------

::

    Copyright (C) 2016 LINE Corp.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
