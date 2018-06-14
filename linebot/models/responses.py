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

"""linebot.models.responses module."""

from __future__ import unicode_literals

from .base import Base
from .rich_menu import RichMenuSize, RichMenuArea


class Profile(Base):
    """Profile.

    https://devdocs.line.me/en/#bot-api-get-profile
    """

    def __init__(self, display_name=None, user_id=None, picture_url=None,
                 status_message=None, **kwargs):
        """__init__ method.

        :param str display_name: Display name
        :param str user_id: User ID
        :param str picture_url: Image URL
        :param str status_message: Status message
        :param kwargs:
        """
        super(Profile, self).__init__(**kwargs)

        self.display_name = display_name
        self.user_id = user_id
        self.picture_url = picture_url
        self.status_message = status_message


class MemberIds(Base):
    """MemberIds.

    https://devdocs.line.me/en/#get-group-room-member-ids
    """

    def __init__(self, member_ids=None, next=None, **kwargs):
        """__init__ method.

        :param member_ids: List of user IDs of the members in the group or room.
            Max: 100 user IDs
        :type member_ids: list[str]
        :param str next: continuationToken.
            Only returned when there are more user IDs remaining in memberIds.
        :param kwargs:
        """
        super(MemberIds, self).__init__(**kwargs)

        self.member_ids = member_ids
        self.next = next


class Content(object):
    """MessageContent.

    https://devdocs.line.me/ja/#get-content
    """

    def __init__(self, response):
        """__init__ method.

        :param response: HttpResponse object
        :type response: T <= :py:class:`linebot.http_client.HttpResponse`
        """
        self.response = response

    @property
    def content_type(self):
        """Get Content-type header value.

        :rtype: str
        :return: content-type header value
        """
        return self.response.headers.get('content-type')

    @property
    def content(self):
        """Get content.

        If content size is large, should use iter_content.

        :rtype: binary
        """
        return self.response.content

    def iter_content(self, chunk_size=1024):
        """Get content as iterator (stream).

        If content size is large, should use this.

        :param chunk_size: Chunk size
        :rtype: iterator
        :return:
        """
        return self.response.iter_content(chunk_size=chunk_size)


class RichMenuResponse(Base):
    """RichMenuResponse.

    https://developers.line.me/en/docs/messaging-api/reference/#rich-menu-response-object
    """

    def __init__(self, rich_menu_id=None, size=None, selected=None, name=None,
                 chat_bar_text=None, areas=None, **kwargs):
        """__init__ method.

        :param str id: Rich Menu ID
        :param size: size object which describe the rich menu displayed in the chat.
            Rich menu images must be one of the following sizes: 2500x1686, 2500x843.
        :type size: :py:class:`linebot.models.rich_menu.RichMenuSize`
        :param bool selected: true to display the rich menu by default. Otherwise, false.
        :param str name: Name of the rich menu.
            Maximum of 300 characters.
        :param str chat_bar_text: Text displayed in the chat bar.
            Maximum of 14 characters.
        :param areas: Array of area objects which define coordinates and size of tappable areas.
            Maximum of 20 area objects.
        :type areas: list[T <= :py:class:`linebot.models.rich_menu.RichMenuArea`]
        :param kwargs:
        """
        super(RichMenuResponse, self).__init__(**kwargs)

        self.rich_menu_id = rich_menu_id
        self.size = self.get_or_new_from_json_dict(size, RichMenuSize)
        self.selected = selected
        self.name = name
        self.chat_bar_text = chat_bar_text

        new_areas = []
        if areas:
            for area in areas:
                new_areas.append(
                    self.get_or_new_from_json_dict(area, RichMenuArea)
                )
        self.areas = new_areas
