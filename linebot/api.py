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
from .models.responses import Profile, MemberIds, MessageContent, RichMenu


class LineBotApi(object):
    """LineBotApi provides interface for LINE messaging API."""

    DEFAULT_API_ENDPOINT = 'https://api.line.me'

    def __init__(self, channel_access_token, endpoint=DEFAULT_API_ENDPOINT,
                 timeout=HttpClient.DEFAULT_TIMEOUT, http_client=RequestsHttpClient):
        """__init__ method.

        :param str channel_access_token: Your channel access token
        :param str endpoint: (optional) Default is https://api.line.me
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is linebot.http_client.HttpClient.DEFAULT_TIMEOUT
        :type timeout: float | tuple(float, float)
        :param http_client: (optional) Default is
            :py:class:`linebot.http_client.RequestsHttpClient`
        :type http_client: T <= :py:class:`linebot.http_client.HttpClient`
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
        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
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
        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
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

    def get_rich_menu(self, rich_menu_id, timeout=None):
        """Call get rich menu API.

        https://developers.line.me/en/docs/messaging-api/reference/#get-rich-menu

        Get rich menu object through a given rich_menu_id

        :param str rich_menu_id: ID of the rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: RichMenu instance
        :type RichMenu: T <= :py:class:`linebot.models.reponse.RichMenu`
        """
        response = self._get(
            '/v2/bot/richmenu/{rich_menu_id}'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

        return RichMenu.new_from_json_dict(response.json)

    def delete_rich_menu(self, rich_menu_id, timeout=None):
        """Call delete rich menu API.

        https://developers.line.me/en/docs/messaging-api/reference/#delete-rich-menu

        Delete rich menu object through a given rich_menu_id

        :param str rich_menu_id: ID of the rich menu
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: An empty RichMenu instance
        :type RichMenu: T <= :py:class:`linebot.models.reponse.RichMenu`
        """
        response = self._delete(
            '/v2/bot/richmenu/{rich_menu_id}'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

        return RichMenu.new_from_json_dict(response.json)

    def create_rich_menu(self, data, timeout=None):
        """Call delete rich menu API.

        https://developers.line.me/en/docs/messaging-api/reference/#create-rich-menu

        Create a rich menu object through a group of given data

        :param data: Inquired to create a rich menu.
        :type data: T <= :py:class:`linebot.models.template.RichMenuTemplate`
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :return: An RichMenu instance with a rich menu id
        :type RichMenu: T <= :py:class:`linebot.models.reponse.RichMenu`
        """
        response = self._post(
            '/v2/bot/richmenu', data=data.as_json_string(), timeout=timeout
        )

        return RichMenu.new_from_json_dict(response.json)

    def link_rich_menu_to_user(self, user_id, rich_menu_id, timeout=None):
        """Call link rich menu to user API.

        https://developers.line.me/en/docs/messaging-api/reference/#link-rich-menu-to-user

        Links a rich menu to a user. Only one rich menu can be linked to a user at one time.

        :param str user_id: ID of an uploaded rich menu
        :param str rich_menu_id: ID of the user
        :type timeout: float | tuple(float, float)
        :return: An empty RichMenu instance
        :type RichMenu: T <= :py:class:`linebot.models.reponse.RichMenu`
        """
        response = self._post(
            '/v2/bot/user/{user_id}/richmenu/{rich_menu_id}'.format(
                user_id=user_id,
                rich_menu_id=rich_menu_id
            ),
            timeout=timeout
        )

        return RichMenu.new_from_json_dict(response.json)

    def get_rich_menu_list(self, timeout=None):
        """Call get rich menu list API.

        https://developers.line.me/en/docs/messaging-api/reference/#get-rich-menu-list

        Gets a list of all uploaded rich menus.

        :return: An list of RichMenu instances
        :type RichMenu: T <= :py:class:`linebot.models.reponse.RichMenu`
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        response = self._get(
            '/v2/bot/richmenu/list',
            timeout=timeout
        )

        lst_result = []
        for richmenu in response.json['richmenus']:
            lst_result.append(RichMenu.new_from_json_dict(richmenu))

        return lst_result

    def upload_rich_menu_image(self, rich_menu_id, path_to_image, timeout=None):
        """Call upload rich menu image API.

        https://developers.line.me/en/docs/messaging-api/reference/#upload-rich-menu-image

        Uploads and attaches an image to a rich menu.

        :param str rich_menu_id: IDs of the rechmenu
        :param str path_to_image: path to the image to upload,
                                  only allow jpeg or png due to content type limitation
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        # check content type by file header, and add it into header dict
        with open(path_to_image, 'rb') as image:
            image_content = image.read()

            if image_content[0:3] == b'\xff\xd8\xff':
                self.headers['Content-Type'] = 'image/jpeg'
            elif image_content[0:8] == b'\x89PNG\r\n\x1a\n':
                self.headers['Content-Type'] = 'image/png'

        # send request
        self._post(
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            data=open(path_to_image, 'rb').read(),
            timeout=timeout
        )

        # remove added header to avoid side effect in other apis
        del self.headers['Content-Type']

    def get_rich_menu_id_of_user(self, user_id, timeout=None):
        """Call get rich menu ID of user API.

        https://developers.line.me/en/docs/messaging-api/reference/#get-rich-menu-id-of-user

        Gets the ID of the rich menu linked to a user.

        :param str user_id: IDs of the user
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        response = self._get(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )

        return RichMenu.new_from_json_dict(response.json)

    def unlink_rich_menu_from_user(self, user_id, timeout=None):
        """Call unlink rich menu from user API.

        https://developers.line.me/en/docs/messaging-api/reference/#unlink-rich-menu-from-user

        Unlinks a rich menu from a user.

        :param str user_id: ID of the user
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._delete(
            '/v2/bot/user/{user_id}/richmenu'.format(user_id=user_id),
            timeout=timeout
        )

    def download_rich_menu_image(self, rich_menu_id, timeout=None):
        """Call download rich menu image API.

        https://developers.line.me/en/docs/messaging-api/reference/#download-rich-menu-image

        Downloads an image associated with a rich menu.

        :param str rich_menu_id: ID of the rich menu with the image to be downloaded
        :param str path_to_image: path to stroe the image download from remote
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        response = self._get(
            '/v2/bot/richmenu/{rich_menu_id}/content'.format(rich_menu_id=rich_menu_id),
            timeout=timeout
        )

        return MessageContent(response)

    def multicast(self, to, messages, timeout=None):
        """Call multicast API.

        https://devdocs.line.me/en/#multicast

        Send messages to multiple users at any time.

        :param to: IDs of the receivers
            Max: 150 users
        :type to: list[str]
        :param messages: Messages.
            Max: 5
        :type messages: T <= :py:class:`linebot.models.send_messages.SendMessage` |
            list[T <= :py:class:`linebot.models.send_messages.SendMessage`]
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        if not isinstance(messages, (list, tuple)):
            messages = [messages]

        data = {
            'to': to,
            'messages': [message.as_json_dict() for message in messages]
        }

        self._post(
            '/v2/bot/message/multicast', data=json.dumps(data), timeout=timeout
        )

    def get_profile(self, user_id, timeout=None):
        """Call get profile API.

        https://devdocs.line.me/en/#bot-api-get-profile

        Get user profile information.

        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/profile/{user_id}'.format(user_id=user_id),
            timeout=timeout
        )

        return Profile.new_from_json_dict(response.json)

    def get_group_member_profile(self, group_id, user_id, timeout=None):
        """Call get group member profile API.

        https://devdocs.line.me/en/#get-group-room-member-profile

        Gets the user profile of a member of a group that
        the bot is in. This can be the user ID of a user who has
        not added the bot as a friend or has blocked the bot.

        :param str group_id: Group ID
        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/group/{group_id}/member/{user_id}'.format(group_id=group_id, user_id=user_id),
            timeout=timeout
        )

        return Profile.new_from_json_dict(response.json)

    def get_room_member_profile(self, room_id, user_id, timeout=None):
        """Call get room member profile API.

        https://devdocs.line.me/en/#get-group-room-member-profile

        Gets the user profile of a member of a room that
        the bot is in. This can be the user ID of a user who has
        not added the bot as a friend or has blocked the bot.

        :param str room_id: Room ID
        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/room/{room_id}/member/{user_id}'.format(room_id=room_id, user_id=user_id),
            timeout=timeout
        )

        return Profile.new_from_json_dict(response.json)

    def get_group_member_ids(self, group_id, start=None, timeout=None):
        """Call get group member IDs API.

        https://devdocs.line.me/en/#get-group-room-member-ids

        Gets the user IDs of the members of a group that the bot is in.
        This includes the user IDs of users who have not added the bot as a friend
        or has blocked the bot.

        :param str group_id: Group ID
        :param str start: continuationToken
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MemberIds`
        :return: MemberIds instance
        """
        params = None if start is None else {'start': start}

        response = self._get(
            '/v2/bot/group/{group_id}/members/ids'.format(group_id=group_id),
            params=params,
            timeout=timeout
        )

        return MemberIds.new_from_json_dict(response.json)

    def get_room_member_ids(self, room_id, start=None, timeout=None):
        """Call get room member IDs API.

        https://devdocs.line.me/en/#get-group-room-member-ids

        Gets the user IDs of the members of a group that the bot is in.
        This includes the user IDs of users who have not added the bot as a friend
        or has blocked the bot.

        :param str room_id: Room ID
        :param str start: continuationToken
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MemberIds`
        :return: MemberIds instance
        """
        params = None if start is None else {'start': start}

        response = self._get(
            '/v2/bot/room/{room_id}/members/ids'.format(room_id=room_id),
            params=params,
            timeout=timeout
        )

        return MemberIds.new_from_json_dict(response.json)

    def get_message_content(self, message_id, timeout=None):
        """Call get content API.

        https://devdocs.line.me/en/#get-content

        Retrieve image, video, and audio data sent by users.

        :param str message_id: Message ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.MessageContent`
        :return: MessageContent instance
        """
        response = self._get(
            '/v2/bot/message/{message_id}/content'.format(message_id=message_id),
            stream=True, timeout=timeout
        )

        return MessageContent(response)

    def leave_group(self, group_id, timeout=None):
        """Call leave group API.

        https://devdocs.line.me/en/#leave

        Leave a group.

        :param str group_id: Group ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
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
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        """
        self._post(
            '/v2/bot/room/{room_id}/leave'.format(room_id=room_id),
            timeout=timeout
        )

    def _get(self, path, params=None, stream=False, timeout=None):
        url = self.endpoint + path

        response = self.http_client.get(
            url, headers=self.headers, params=params, stream=stream, timeout=timeout
        )

        self.__check_error(response)
        return response

    def _post(self, path, data=None, timeout=None):
        url = self.endpoint + path
        headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.post(
            url, headers=headers, data=data, timeout=timeout
        )

        self.__check_error(response)
        return response

    def _delete(self, path, data=None, timeout=None):
        url = self.endpoint + path
        headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = self.http_client.delete(
            url, headers=headers, data=data, timeout=timeout
        )

        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            error = Error.new_from_json_dict(response.json)
            raise LineBotApiError(response.status_code, error)
