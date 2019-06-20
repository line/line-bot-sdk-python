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

"""linebot.models.template module."""

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .actions import get_action, get_actions
from .base import Base
from .send_messages import SendMessage


class TemplateSendMessage(SendMessage):
    """TemplateSendMessage.

    https://developers.line.biz/en/reference/messaging-api/#template-messages

    Template messages are messages with predefined layouts which you can customize.
    There are three types of templates available
    that can be used to interact with users through your bot.
    """

    def __init__(self, alt_text=None, template=None, **kwargs):
        """__init__ method.

        :param str alt_text: Alternative text for unsupported devices.
        :param template: Object with the contents of the template.
        :type template: T <= :py:class:`linebot.models.template.Template`
        :param kwargs:
        """
        super(TemplateSendMessage, self).__init__(**kwargs)

        self.type = 'template'
        self.alt_text = alt_text
        self.template = self.get_or_new_from_json_dict_with_types(
            template, {
                'buttons': ButtonsTemplate,
                'confirm': ConfirmTemplate,
                'carousel': CarouselTemplate,
                'image_carousel': ImageCarouselTemplate
            }
        )


class Template(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Template."""

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Template, self).__init__(**kwargs)

        self.type = None


class ButtonsTemplate(Template):
    """ButtonsTemplate.

    https://developers.line.biz/en/reference/messaging-api/#buttons

    Template message with an image, title, text, and multiple action buttons.
    """

    def __init__(self, text=None, title=None, thumbnail_image_url=None,
                 image_aspect_ratio=None,
                 image_size=None, image_background_color=None,
                 actions=None, default_action=None, **kwargs):
        """__init__ method.

        :param str text: Message text.
            Max: 160 characters (no image or title).
            Max: 60 characters (message with an image or title)
        :param str title: Title.
            Max: 40 characters
        :param str thumbnail_image_url: Image URL.
            HTTPS
            JPEG or PNG
            Aspect ratio: 1:1.51
            Max width: 1024px
            Max: 1 MB
        :param str image_aspect_ratio: Aspect ratio of the image.
            Specify one of the following values:
            rectangle: 1.51:1
            square: 1:1
        :param str image_size: Size of the image. Specify ``cover`` or ``contain``.
        :param str image_background_color: Background color of image.
            Specify a RGB color value.
        :param actions: Action when tapped.
            Max: 4
        :type actions: list[T <= :py:class:`linebot.models.actions.Action`]
        :param default_action: Action when image is tapped;
            set for the entire image, title, and text area
        :type default_action: T <= :py:class:`linebot.models.actions.Action`
        :param kwargs:
        """
        super(ButtonsTemplate, self).__init__(**kwargs)

        self.type = 'buttons'
        self.text = text
        self.title = title
        self.thumbnail_image_url = thumbnail_image_url
        self.image_aspect_ratio = image_aspect_ratio
        self.image_size = image_size
        self.image_background_color = image_background_color
        self.actions = get_actions(actions)
        self.default_action = get_action(default_action)


class ConfirmTemplate(Template):
    """ConfirmTemplate.

    https://developers.line.biz/en/reference/messaging-api/#confirm

    Template message with two action buttons.
    """

    def __init__(self, text=None, actions=None, **kwargs):
        """__init__ method.

        :param str text: Message text.
            Max: 240 characters
        :param actions: Action when tapped.
            Max: 2
        :type actions: list[T <= :py:class:`linebot.models.actions.Action`]
        :param kwargs:
        """
        super(ConfirmTemplate, self).__init__(**kwargs)

        self.type = 'confirm'
        self.text = text
        self.actions = get_actions(actions)


class CarouselTemplate(Template):
    """CarouselTemplate.

    https://developers.line.biz/en/reference/messaging-api/#carousel

    Template message with multiple columns which can be cycled like a carousel.
    """

    def __init__(self, columns=None, image_aspect_ratio=None,
                 image_size=None, **kwargs):
        """__init__ method.

        :param columns: Array of columns.
            Max: 10
        :type columns: list[T <= :py:class:`linebot.models.template.CarouselColumn`]
        :param str image_aspect_ratio: Aspect ratio of the image.
            Specify ``rectangle`` or ``square``.
        :param str image_size: Size of the image. Specify ``cover`` or ``contain``.
        :param kwargs:
        """
        super(CarouselTemplate, self).__init__(**kwargs)

        self.type = 'carousel'

        new_columns = []
        if columns:
            for column in columns:
                new_columns.append(self.get_or_new_from_json_dict(
                    column, CarouselColumn
                ))
        self.columns = new_columns
        self.image_aspect_ratio = image_aspect_ratio
        self.image_size = image_size


class ImageCarouselTemplate(Template):
    """ImageCarouselTemplate.

    https://developers.line.biz/en/reference/messaging-api/#image-carousel

    Template message with multiple images columns which can be cycled like as carousel.
    """

    def __init__(self, columns=None, **kwargs):
        """__init__ method.

        :param columns: Array of columns.
            Max: 10
        :type columns: list[T <= :py:class:`linebot.models.template.ImageCarouselColumn`]
        :param kwargs:
        """
        super(ImageCarouselTemplate, self).__init__(**kwargs)

        self.type = 'image_carousel'

        new_columns = []
        if columns:
            for column in columns:
                new_columns.append(self.get_or_new_from_json_dict(
                    column, ImageCarouselColumn
                ))
        self.columns = new_columns


class CarouselColumn(Base):
    """CarouselColumn.

    https://developers.line.biz/en/reference/messaging-api/#column-object
    """

    def __init__(self, text=None, title=None,
                 thumbnail_image_url=None, image_background_color=None,
                 actions=None, default_action=None, **kwargs):
        """__init__ method.

        :param str text: Message text.
            Max: 120 characters (no image or title)
            Max: 60 characters (message with an image or title)
        :param str title: Title.
            Max: 40 characters
        :param str thumbnail_image_url: Image URL (HTTPS). JPEG or PNG. Aspect ration is 1:1.51.
            Max width: 1024px, Max: 1 MB.
        :param str image_background_color: Background color of image.
            Specify a RGB color value.
        :param actions: Action when tapped.
            Max: 3
        :type actions: list[T <= :py:class:`linebot.models.actions.Action`]
        :param default_action: Action when image is tapped;
            set for the entire image, title, and text area
        :type default_action: T <= :py:class:`linebot.models.actions.Action`
        :param kwargs:
        """
        super(CarouselColumn, self).__init__(**kwargs)

        self.text = text
        self.title = title
        self.thumbnail_image_url = thumbnail_image_url
        self.image_background_color = image_background_color
        self.actions = get_actions(actions)
        self.default_action = get_action(default_action)


class ImageCarouselColumn(Base):
    """ImageCarouselColumn.

    https://developers.line.biz/en/reference/messaging-api/#column-object-for-image-carousel
    """

    def __init__(self, image_url=None, action=None, **kwargs):
        """__init__ method.

        :param str image_url: Image URL (HTTPS). JPEG or PNG. Aspect ration is 1:1.
            Max width: 1024px, Max: 1 MB.
        :param action: Action when image is tapped. Max: 5.
        :type action: T <= :py:class:`linebot.models.actions.Action`
        :param kwargs:
        """
        super(ImageCarouselColumn, self).__init__(**kwargs)

        self.image_url = image_url
        self.action = get_action(action)
