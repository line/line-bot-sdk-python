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

"""linebot.api module."""

from __future__ import unicode_literals

import json

from .__about__ import __version__
from .exceptions import LineBotApiError
from .http_client import HttpClient, RequestsHttpClient
from .models.error import Error
from .models.responses import Profile


class LineBotApi(object):
    """LineBotApi provides interface for LINE messaging API."""

    DEFAULT_API_ENDPOINT = 'https://api.line.me'

    def __init__(self, channel_access_token, endpoint=DEFAULT_API_ENDPOINT,
                 timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient):
        """__init__ method.

        :param str channel_access_token: Your channel access token
        :param str endpoint: (optional) Default is https://api.line.me
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is linebot.http_client.HttpClient.DEFAULT_TIMEOUT
        :param T <= linebot.http_client.HttpClient: (optional) Default is RequestsHttpClient
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
        """Call reply message API.

        https://devdocs.line.me/en/#reply-message

        Respond to events from users, groups, and rooms.

        Webhooks are used to notify you when an event occurs.
        For events that you can respond to, a replyToken is issued for replying to messages.

        Because the replyToken becomes invalid after a certain period of time,
        responses should be sent as soon as a message is received.

        Reply tokens can only be used once.

        :param str reply_token: replyToken received via webhook
        :param T <= linebot.models.Message|list[T <= linebot.models.Message] messages: Messages.
            Max: 5
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is self.http_client.timeout
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
        """Call push message API.

        https://devdocs.line.me/en/#push-message

        Send messages to users, groups, and rooms at any time.

        :param str to: ID of the receiver
        :param T <= linebot.models.Message|list[T <= linebot.models.Message] messages: Messages.
            Max: 5
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is self.http_client.timeout
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
        """Call get profile API.

        https://devdocs.line.me/en/#bot-api-get-profile

        Get user profile information.

        :param str user_id: User ID
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is self.http_client.timeout
        :rtype: linebot.models.Profile
        :return:

        """
        body = self._get(
            '/v2/bot/profile/{user_id}'.format(user_id=user_id),
            timeout=timeout
        )
        return Profile.new_from_json_dict(json.loads(body))

    def get_content_stream(self, message_id, chunk_size=1024, timeout=None):
        """Call get content API.

        https://devdocs.line.me/en/#get-content

        Retrieve image, video, and audio data sent by users.

        :param message_id: Message ID
        :param int chunk_size: Chunk size
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is self.http_client.timeout
        :rtype: iterator
        :return:

        """
        body_stream = self._get_stream(
            '/v2/bot/message/{message_id}/content'.format(
                message_id=message_id),
            chunk_size=chunk_size, timeout=timeout
        )

        return body_stream

    def leave_group(self, group_id, timeout=None):
        """Call leave group API.

        https://devdocs.line.me/en/#leave

        Leave a group.

        :param str group_id: Group ID
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is self.http_client.timeout
        """
        self._post(
            '/v2/bot/group/{group_id}/leave'.format(group_id=group_id),
            timeout=timeout
        )

    def leave_room(self, room_id, timeout=None):
        """Call leave room API.

        https://devdocs.line.me/en/#leave

        Leave a room.

        :param str room_id: Room ID
        :param float|tuple(float, float) timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, readtimeout) float tuple.
            Default is self.http_client.timeout
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

    def _get_stream(self, path, chunk_size=1024, decode_unicode=False, timeout=None):
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
