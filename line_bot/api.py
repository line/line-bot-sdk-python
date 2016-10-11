# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from .__about__ import __version__
from .exceptions import LineBotApiError
from .http_client import (
    RequestsHttpClient, HttpClient
)
from .models.error import Error
from .models.profile import Profile


class LineBotApi(object):
    DEFAULT_API_ENDPOINT = 'https://api.line.me'

    def __init__(
            self, channel_access_token, endpoint=DEFAULT_API_ENDPOINT,
            timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient
    ):
        """Constructor of LineBotApi Client

        Args:
            channel_access_token: Your channel access token
            endpoint: (optional) Default is https://api.line.me
            timeout: How long to wait for the server to send data before giving up,
                as a float, or a :ref:`(connect timeout, readtimeout) <timeouts>` tuple. Default is 5 seconds.
            http_client: (optional) Default is RequestsHttpClient
        """

        self.endpoint = endpoint
        self.headers = {
            'Authorization': 'Bearer ' + channel_access_token,
            'User-Agent': 'line-bot-sdk-python/' + __version__
        }

        if http_client:
            self.http_client = http_client(timeout=timeout)
        else:
            self.http_client = RequestsHttpClient(timeout=timeout)

    def reply_message(self, reply_token, messages, timeout=None):
        """Call reply message API

        https://devdocs.line.me/en/#reply-message

        Respond to events from users, groups, and rooms.

        Webhooks are used to notify you when an event occurs.
        For events that you can respond to, a replyToken is issued for replying to messages.

        Because the replyToken becomes invalid after a certain period of time,
        responses should be sent as soon as a message is received. Reply tokens can only be used once.

        Args:
            reply_token: replyToken received via webhook
            messages: Messages.
                Max: 5
            timeout: (optional) Default is self.http_client.timeout
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        data = {
            'replyToken': reply_token,
            'messages': [message.as_json_dict() for message in messages]
        }
        self._post(
            '/v2/bot/message/reply', data=json.dumps(data), timeout=timeout
        )

    def push_message(self, to, messages, timeout=None):
        """Call push message API

        https://devdocs.line.me/en/#push-message

        Send messages to users, groups, and rooms at any time.

        Args:
            to: ID of the receiver
            messages: Messages.
                Max: 5
            timeout: (optional) Default is self.http_client.timeout
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        data = {
            'to': to,
            'messages': [message.as_json_dict() for message in messages]
        }
        self._post(
            '/v2/bot/message/push', data=json.dumps(data), timeout=timeout
        )

    def get_profile(self, user_id, timeout=None):
        """Call get profile API

        https://devdocs.line.me/en/#bot-api-get-profile

        Get user profile information.

        Args:
            user_id: User ID
            timeout: (optional) Default is self.http_client.timeout

        Returns: Profile class object

        """
        body = self._get(
            '/v2/bot/profile/{user_id}'.format(user_id=user_id),
            timeout=timeout
        )
        return Profile.new_from_json_dict(json.loads(body))

    def get_content_stream(
            self, message_id, chunk_size=1024, timeout=None
    ):
        """Call get content API

        Retrieve image, video, and audio data sent by users.

        https://devdocs.line.me/en/#get-content

        Args:
            message_id: Message ID
            chunk_size: Chunk size
            timeout: (optional) Default is self.http_client.timeout

        Returns: chunk binary content.

        """
        body_stream = self._get_stream(
            '/v2/bot/message/{message_id}/content'.format(
                message_id=message_id),
            chunk_size=chunk_size, timeout=timeout
        )

        return body_stream

    def leave_group(self, group_id, timeout=None):
        """Call leave group API

        Leave a group.

        https://devdocs.line.me/en/#leave

        Args:
            group_id: Group ID
            timeout: (optional) Default is self.http_client.timeout
        """
        self._post(
            '/v2/bot/group/{group_id}/leave'.format(group_id=group_id),
            timeout=timeout
        )

    def leave_room(self, room_id, timeout=None):
        """Call leave room API

        Leave a room.

        https://devdocs.line.me/en/#leave

        Args:
            room_id: Room ID
            timeout: (optional) Default is self.http_client.timeout
        """
        self._post(
            '/v2/bot/room/{room_id}/leave'.format(room_id=room_id),
            timeout=timeout
        )

    def _get(self, path, timeout=None):
        url = self.endpoint + path

        response = self.http_client.get(
            url, headers=self.headers, timeout=timeout
        )

        self.__check_error(response)
        return response.body

    def _get_stream(
            self, path, chunk_size=1024, decode_unicode=False, timeout=None
    ):
        url = self.endpoint + path

        response = self.http_client.get_stream(
            url, headers=self.headers, timeout=timeout,
            chunk_size=chunk_size, decode_unicode=decode_unicode
        )

        self.__check_error(response)
        return response.body_stream

    def _post(self, path, data=None, timeout=None):
        url = self.endpoint + path
        headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.post(
            url, headers=headers, data=data, timeout=timeout
        )

        self.__check_error(response)
        return response.body

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            error = Error.new_from_json_dict(json.loads(response.body))
            raise LineBotApiError(response.status_code, error)
