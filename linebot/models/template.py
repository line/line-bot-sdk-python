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

from .base import Base
from .send_messages import SendMessage


def _get_action(action):
    action_obj = Base.get_or_new_from_json_dict_with_types(
        action, {
            'postback': PostbackTemplateAction,
            'message': MessageTemplateAction,
            'uri': URITemplateAction,
            'datetimepicker': DatetimePickerTemplateAction,
        }
    )
    return action_obj


def _get_actions(actions):
    new_actions = []
    if actions:
        for action in actions:
            action_obj = _get_action(action)
            if action_obj:
                new_actions.append(action_obj)

    return new_actions


class TemplateSendMessage(SendMessage):
    """TemplateSendMessage.

    https://devdocs.line.me/en/#template-messages

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

    https://devdocs.line.me/en/#buttons

    Template message with an image, title, text, and multiple action buttons.
    """

    def __init__(self, text=None, title=None, thumbnail_image_url=None,
                 image_aspect_ratio=None,
                 image_size=None, image_background_color=None,
                 actions=None, **kwargs):
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
        :param str image_size: Size of the image.
            Specify one of the following values:
            cover: The image fills the entire image area.
                Parts of the image that do not fit in the area are not displayed.
            contain: The entire image is displayed in the image area.
                A background is displayed in the unused areas to the left and right
                of vertical images and in the areas above and below horizontal images.
        :param str image_background_color: Background color of image.
            Specify a RGB color value.
        :param actions: Action when tapped.
            Max: 4
        :type actions: list[T <= :py:class:`linebot.models.template.TemplateAction`]
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
        self.actions = _get_actions(actions)


class ConfirmTemplate(Template):
    """ConfirmTemplate.

    https://devdocs.line.me/en/#confirm

    Template message with two action buttons.
    """

    def __init__(self, text=None, actions=None, **kwargs):
        """__init__ method.

        :param str text: Message text.
            Max: 240 characters
        :param actions: Action when tapped.
            Max: 2
        :type actions: list[T <= :py:class:`linebot.models.template.TemplateAction`]
        :param kwargs:
        """
        super(ConfirmTemplate, self).__init__(**kwargs)

        self.type = 'confirm'
        self.text = text
        self.actions = _get_actions(actions)


class CarouselTemplate(Template):
    """CarouselTemplate.

    https://devdocs.line.me/en/#carousel

    Template message with multiple columns which can be cycled like a carousel.
    """

    def __init__(self, columns=None, image_aspect_ratio=None,
                 image_size=None, **kwargs):
        """__init__ method.

        :param columns: Array of columns.
            Max: 10
        :type columns: list[T <= :py:class:`linebot.models.template.CarouselColumn`]
        :param str image_aspect_ratio: Aspect ratio of the image.
            Specify one of the following values:
            rectangle: 1.51:1
            square: 1:1
        :param str image_size: Size of the image.
            Specify one of the following values:
            cover: The image fills the entire image area.
                Parts of the image that do not fit in the area are not displayed.
            contain: The entire image is displayed in the image area.
                A background is displayed in the unused areas to the left and right
                of vertical images and in the areas above and below horizontal images.
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

    https://devdocs.line.me/en/#image-carousel

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

    https://devdocs.line.me/en/#column-object
    """

    def __init__(self, text=None, title=None, thumbnail_image_url=None,
                 image_background_color=None, actions=None, **kwargs):
        """__init__ method.

        :param str text: Message text.
            Max: 120 characters (no image or title)
            Max: 60 characters (message with an image or title)
        :param str title: Title.
            Max: 40 characters
        :param str thumbnail_image_url: Image URL.
            HTTPS
            JPEG or PNG
            Aspect ratio: 1:1.51
            Max width: 1024px
            Max: 1 MB
        :param str image_background_color: Background color of image.
            Specify a RGB color value.
        :param actions: Action when tapped.
            Max: 3
        :type actions: list[T <= :py:class:`linebot.models.template.TemplateAction`]
        :param kwargs:
        """
        super(CarouselColumn, self).__init__(**kwargs)

        self.text = text
        self.title = title
        self.thumbnail_image_url = thumbnail_image_url
        self.image_background_color = image_background_color
        self.actions = _get_actions(actions)


class ImageCarouselColumn(Base):
    """ImageCarouselColumn.

    https://devdocs.line.me/en/#column-object-for-image-carousel
    """

    def __init__(self, image_url=None, action=None, **kwargs):
        """__init__ method.

        :param str image_url: Image URL.
            HTTPS
            JPEG or PNG
            Aspect ratio: 1:1
            Max width: 1024px
            Max: 1 MB
        :param action: Action when image is tapped
            Max: 5
        :type action: T <= :py:class:`linebot.models.template.TemplateAction`
        :param kwargs:
        """
        super(ImageCarouselColumn, self).__init__(**kwargs)

        self.image_url = image_url
        self.action = _get_action(action)


class TemplateAction(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of TemplateAction."""

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(TemplateAction, self).__init__(**kwargs)

        self.type = None


class PostbackTemplateAction(TemplateAction):
    """PostbackTemplateAction.

    https://devdocs.line.me/en/#template-messages

    When this action is tapped, a postback event is returned
    via webhook with the specified string in the data field.

    If you have included the text field,
    the string in the text field is sent as a message from the user.
    """

    def __init__(self, label=None, data=None, text=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action.
            Max: 20 characters
        :param str data: String returned via webhook in the postback.data property
            of the postback event.
            Max: 300 characters
        :param str text: Text sent when the action is performed.
            Max: 300 characters
        :param kwargs:
        """
        super(PostbackTemplateAction, self).__init__(**kwargs)

        self.type = 'postback'
        self.label = label
        self.data = data
        self.text = text


class MessageTemplateAction(TemplateAction):
    """MessageTemplateAction.

    https://devdocs.line.me/en/#template-messages

    When this action is tapped,
    the string in the text field is sent as a message from the user.
    """

    def __init__(self, label=None, text=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action.
            Max: 20 characters
        :param str text: Text sent when the action is performed.
            Max: 300 characters
        :param kwargs:
        """
        super(MessageTemplateAction, self).__init__(**kwargs)

        self.type = 'message'
        self.label = label
        self.text = text


class URITemplateAction(TemplateAction):
    """URITemplateAction.

    https://devdocs.line.me/en/#template-messages

    When this action is tapped, the URI specified in the uri field is opened.
    """

    def __init__(self, label=None, uri=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
            Max: 20 characters
        :param str uri: URI opened when the action is performed.
            http, https, tel
        :param kwargs:
        """
        super(URITemplateAction, self).__init__(**kwargs)

        self.type = 'uri'
        self.label = label
        self.uri = uri


class DatetimePickerTemplateAction(TemplateAction):
    """DatetimePickerTemplateAction.

    https://devdocs.line.me/en/#template-messages

    When this action is tapped, a postback event is returned via webhook
    with the date and time selected by the user from the date and time selection dialog.
    """

    def __init__(self, label=None, data=None, mode=None,
                 initial=None, max=None, min=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
            Max: 20 characters
        :param str data: String returned via webhook
            in the postback.data property of the postback event
            Max: 300 characters
        :param str mode: 	Action mode
            date: Pick date
            time: Pick time
            datetime: Pick date and time
        :param str initial: Initial value of date or time
        :param str max: Largest date or time value that can be selected.
            Must be greater than the min value.
        :param str min: Smallest date or time value that can be selected.
            Must be less than the max value.
        :param kwargs:
        """
        super(DatetimePickerTemplateAction, self).__init__(**kwargs)

        self.type = 'datetimepicker'
        self.label = label
        self.data = data
        self.mode = mode
        self.initial = initial
        self.max = max
        self.min = min
