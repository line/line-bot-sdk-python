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


from abc import ABCMeta

from future.utils import with_metaclass

from .actions import get_action
from .base import Base


class RichMenu(with_metaclass(ABCMeta, Base)):
    """RichMenu.

    https://developers.line.me/en/docs/messaging-api/reference/#rich-menu-object
    """

    def __init__(self, size=None, selected=None, name=None, chat_bar_text=None,
                 areas=None, **kwargs):
        """__init__ method.

        :param size: size object which describe the rich menu displayed in the chat.
            Rich menu images must be one of the following sizes: 2500x1686, 2500x843.
        :type size: :py:class:`linebot.models.rich_menu.RichMenuSize`
        :param bool selected: true to display the rich menu by default. Otherwise, false.
        :param str name: Name of the rich menu.
            Maximum of 300 characters.
        :param str chatBarText: Text displayed in the chat bar.
                                Maximum of 14 characters.
        :param areas: Array of area objects which define coordinates and size of tappable areas.
                      Maximum of 20 area objects.
        :type areas: list[T <= :py:class:`linebot.models.rich_menu.RichMenuArea`]
        :param kwargs:
        """
        super(RichMenu, self).__init__(**kwargs)

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


class RichMenuSize(with_metaclass(ABCMeta, Base)):
    """RichMenuSize.

    https://developers.line.me/en/docs/messaging-api/reference/#size-object
    """

    def __init__(self, width=None, height=None, **kwargs):
        """__init__ method.

        :param int width: Width of the rich menu. Must be 2500.
        :param int height: Height of the rich menu. Possible values: 1686, 843.
        :param kwargs:
        """
        super(RichMenuSize, self).__init__(**kwargs)

        self.width = width
        self.height = height


class RichMenuArea(with_metaclass(ABCMeta, Base)):
    """RichMenuArea.

    https://developers.line.me/en/docs/messaging-api/reference/#area-object
    """

    def __init__(self, bounds=None, action=None, **kwargs):
        """__init__ method.

        :param bounds: Object describing the boundaries of the area in pixels. See bounds object.
        :type bounds: :py:class:`linebot.models.rich_menu.RichMenuBound`
        :param action: Action performed when the area is tapped. See action objects.
        :type action: T <= :py:class:`linebot.models.actions.Action`
        :param kwargs:
        """
        super(RichMenuArea, self).__init__(**kwargs)

        self.bounds = self.get_or_new_from_json_dict(bounds, RichMenuBounds)
        self.action = get_action(action)


class RichMenuBounds(with_metaclass(ABCMeta, Base)):
    """RichMenuBounds.

    https://developers.line.me/en/docs/messaging-api/reference/#bounds-object
    """

    def __init__(self, x=None, y=None, width=None, height=None, **kwargs):
        """__init__ method.

        :param int x: Horizontal position relative to the top-left corner of the area.
        :param int y: Vertical position relative to the top-left corner of the area.
        :param int width: Width of the area.
        :param int height: Height of the area.
        :param kwargs:
        """
        super(RichMenuBounds, self).__init__(**kwargs)

        self.x = x
        self.y = y
        self.width = width
        self.height = height


class RichMenuAlias(with_metaclass(ABCMeta, Base)):
    """RichMenuAlias.

    https://developers.line.biz/en/reference/messaging-api/#create-rich-menu-alias
    """

    def __init__(self, rich_menu_alias_id=None, rich_menu_id=None, **kwargs):
        """__init__ method.

        :param string rich_menu_alias_id: Rich menu alias ID,
         which can be any ID, unique for each channel.
        :param string rich_menu_id: The rich menu ID to be associated with the rich menu alias.
        :param kwargs:
        """
        super(RichMenuAlias, self).__init__(**kwargs)

        self.rich_menu_alias_id = rich_menu_alias_id
        self.rich_menu_id = rich_menu_id
