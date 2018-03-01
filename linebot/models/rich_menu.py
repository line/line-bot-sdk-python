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

"""linebot.models.rich_menu module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class RichMenu(with_metaclass(ABCMeta, Base)):
    """RichMenu.

    https://developers.line.me/en/docs/messaging-api/reference/#rich-menu-object

    This is the template to create a richmenu before posting to remote server,
    or a template to receive rich menu query result from remote server.
    """

    def __init__(self, size=None, selected=None, name=None, chatBarText=None,
                 areas=None, **kwargs):
        """__init__ method.

        :param size: size object which describe the rich menu displayed in the chat.
                      Rich menu images must be one of the following sizes: 2500x1686, 2500x843.
        :type size: T <= :py:class:`linebot.models.rich_menu.RichMenuBound`
        :param bool selected: true to display the rich menu by default. Otherwise, false.
        :param str name: Name of the rich menu.
                         Maximum of 300 characters.
        :param str chatBarText: Text displayed in the chat bar.
                                Maximum of 14 characters.
        :param areas: Array of area objects which define coordinates and size of tappable areas.
                      Maximum of 20 area objects.
        :type areas: T <= :py:class:`linebot.models.rich_menu.RichMenuArea`
        :param kwargs:
        """
        super(RichMenu, self).__init__(**kwargs)

        self.size = size  # RichMenuBound
        self.selected = selected
        self.name = name
        self.chatBarText = chatBarText
        self.areas = []
        if not isinstance(areas, (list, tuple)):
            areas = [areas]

        self.areas = [area.as_json_dict() for area in areas]  # RichMenuArea


class RichMenuBound(with_metaclass(ABCMeta, Base)):
    """RichMenuBound.

    https://developers.line.me/en/docs/messaging-api/reference/#bounds-object
    https://developers.line.me/en/docs/messaging-api/reference/#size-object

    This is the template to describe the boundaries of the area in pixels.
    If x and y are equal to default value, the bound object is equal to size object.
    """

    def __init__(self, x=None, y=None, width=None, height=None, **kwargs):
        """__init__ method.

        :param int x: Horizontal position relative to the top-left corner of the area.
        :param int y: Vertical position relative to the top-left corner of the area.
        :param int width: Width of the area.
        :param int height: Height of the area.
        :param kwargs:
        """
        super(RichMenuBound, self).__init__(id=id, **kwargs)

        self.x = x
        self.y = y
        self.width = width
        self.height = height


class RichMenuArea(with_metaclass(ABCMeta, Base)):
    """RichMenuArea.

    https://developers.line.me/en/docs/messaging-api/reference/#area-object

    Array of area objects which define the coordinates and size of tappable areas.
    """

    def __init__(self, bounds=None, action=None, **kwargs):
        """__init__ method.

        :param bounds: Object describing the boundaries of the area in pixels.
        :type areas: T <= :py:class:`linebot.models.template.RichMenuBound`
        :param action: Action performed when the area is tapped.
        :type action: T <= :py:class:`linebot.models.template.PostbackTemplateAction` |
                      T <= :py:class:`linebot.models.template.MessageTemplateAction` |
                      T <= :py:class:`linebot.models.template.URITemplateAction` |
                      T <= :py:class:`linebot.models.template.DatetimePickerTemplateAction`
        :param kwargs:
        """
        super(RichMenuArea, self).__init__(id=id, **kwargs)

        self.action = action
        self.bounds = bounds  # RichMenuBound
