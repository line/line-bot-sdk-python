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

"""linebot.models.imagemap module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base
from .send_messages import SendMessage


class ImagemapSendMessage(SendMessage):
    """ImagemapSendMessage.

    https://devdocs.line.me/en/#imagemap-message

    Imagemaps are images with one or more links. You can assign one link for the entire image
    or multiple links which correspond to different regions of the image.
    """

    def __init__(self, base_url=None, alt_text=None, base_size=None, actions=None, **kwargs):
        """__init__ method.

        :param str base_url: Base URL of image.
            HTTPS
        :param str alt_text: Alternative text
        :param base_size: Width and height of base image
        :type base_size: :py:class:`linebot.models.imagemap.BaseSize`
        :param actions: Action when tapped
        :type actions: list[T <= :py:class:`linebot.models.imagemap.ImagemapAction`]
        :param kwargs:
        """
        super(ImagemapSendMessage, self).__init__(**kwargs)

        self.type = 'imagemap'
        self.base_url = base_url
        self.alt_text = alt_text
        self.base_size = self.get_or_new_from_json_dict(
            base_size, BaseSize
        )

        new_actions = []
        if actions:
            for action in actions:
                action_obj = self.get_or_new_from_json_dict_with_types(
                    action, {
                        'uri': URIImagemapAction,
                        'message': MessageImagemapAction
                    }
                )
                if action_obj:
                    new_actions.append(action_obj)
        self.actions = new_actions


class BaseSize(Base):
    """BaseSize.

    https://devdocs.line.me/en/#imagemap-message
    """

    def __init__(self, width=None, height=None, **kwargs):
        """__init__ method.

        https://devdocs.line.me/en/#imagemap-message

        :param int width: Width of base image (set to 1040px）
        :param int height: Height of base image（set to the height
            that corresponds to a width of 1040px
        :param kwargs:
        """
        super(BaseSize, self).__init__(**kwargs)

        self.width = width
        self.height = height


class ImagemapAction(with_metaclass(ABCMeta, Base)):
    """ImagemapAction.

    https://devdocs.line.me/en/#imagemap-message
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(ImagemapAction, self).__init__(**kwargs)

        self.type = None


class URIImagemapAction(ImagemapAction):
    """URIImagemapAction.

    https://devdocs.line.me/en/#imagemap-message
    """

    def __init__(self, link_uri=None, area=None, **kwargs):
        """__init__ method.

        :param str link_uri: Webpage URL
        :param area: Defined tappable area
        :type area: :py:class:`linebot.models.imagemap.ImagemapArea`
        :param kwargs:
        """
        super(URIImagemapAction, self).__init__(**kwargs)

        self.type = 'uri'
        self.link_uri = link_uri
        self.area = self.get_or_new_from_json_dict(area, ImagemapArea)


class MessageImagemapAction(ImagemapAction):
    """MessageImagemapAction.

    https://devdocs.line.me/en/#imagemap-message
    """

    def __init__(self, text=None, area=None, **kwargs):
        """__init__ method.

        :param str text: Message to send
        :param area: Defined tappable area
        :type area: :py:class:`linebot.models.imagemap.ImagemapArea`
        :param kwargs:
        """
        super(MessageImagemapAction, self).__init__(**kwargs)

        self.type = 'message'
        self.text = text
        self.area = self.get_or_new_from_json_dict(area, ImagemapArea)


class ImagemapArea(Base):
    """ImagemapArea.

    https://devdocs.line.me/en/#imagemap-area-object

    Defines the size of the full imagemap with the width as 1040px.
    The top left is used as the origin of the area.
    """

    def __init__(self, x=None, y=None, width=None, height=None, **kwargs):
        """__init__ method.

        :param int x: Horizontal position of the tappable area
        :param int y: Vertical position of the tappable area
        :param int width: Width of the tappable area
        :param int height: Height of the tappable area
        :param kwargs:
        """
        super(ImagemapArea, self).__init__(**kwargs)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
