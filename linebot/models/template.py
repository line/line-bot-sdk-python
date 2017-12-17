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

    def __init__(self, text=None, title=None, thumbnail_image_url=None, actions=None, **kwargs):
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

    def __init__(self, columns=None, **kwargs):
        """__init__ method.

        :param columns: Array of columns.
            Max: 5
        :type columns: list[T <= :py:class:`linebot.models.template.CarouselColumn`]
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


class ImageCarouselTemplate(Template):
    """ImageCarouselTemplate.

    https://devdocs.line.me/en/#image-carousel

    Template message with multiple images columns which can be cycled like as carousel.
    """

    def __init__(self, columns=None, **kwargs):
        """__init__ method.

        :param columns: Array of columns.
            Max: 5
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

    def __init__(self, text=None, title=None, thumbnail_image_url=None, actions=None, **kwargs):
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
        :param actions: Action when tapped.
            Max: 3
        :type actions: list[T <= :py:class:`linebot.models.template.TemplateAction`]
        :param kwargs:
        """
        super(CarouselColumn, self).__init__(**kwargs)

        self.text = text
        self.title = title
        self.thumbnail_image_url = thumbnail_image_url
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


class RichMenuTemplate(with_metaclass(ABCMeta, Base)):
    """RichMenuTemplate.

    https://developers.line.me/en/docs/messaging-api/reference/#rich-menu-object

    This is the template to create a richmenu before posting to remote server,
    or a template to receive rich menu query result from remote server.
    """

    def __init__(self, size=None, selected=None, name=None, chatBarText=None,
                 areas=None, **kwargs):
        """__init__ method.

        :param size: size object which describe the rich menu displayed in the chat.
                      Rich menu images must be one of the following sizes: 2500x1686, 2500x843.
        :type size: T <= :py:class:`linebot.models.template.RichMenuBoundTemplate`
        :param bool selected: true to display the rich menu by default. Otherwise, false.
        :param str name: Name of the rich menu.
                         Maximum of 300 characters.
        :param str chatBarText: Text displayed in the chat bar.
                                Maximum of 14 characters.
        :param areas: Array of area objects which define coordinates and size of tappable areas.
                      Maximum of 20 area objects.
        :type areas: T <= :py:class:`linebot.models.template.RichMenuAreaTemplate`
        :param kwargs:
        """
        super(RichMenuTemplate, self).__init__(**kwargs)

        self.size = size  # RichMenuBoundTemplate
        self.selected = selected
        self.name = name
        self.chatBarText = chatBarText
        self.areas = []
        if not isinstance(areas, (list, tuple)):
            areas = [areas]

        self.areas = [area.as_json_dict() for area in areas]  # RichMenuAreaTemplate


class RichMenuBoundTemplate(with_metaclass(ABCMeta, Base)):
    """RichMenuBoundTemplate.

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
        super(RichMenuBoundTemplate, self).__init__(id=id, **kwargs)

        self.x = x
        self.y = y
        self.width = width
        self.height = height


class RichMenuAreaTemplate(with_metaclass(ABCMeta, Base)):
    """RichMenuAreaTemplate.

    https://developers.line.me/en/docs/messaging-api/reference/#area-object

    Array of area objects which define the coordinates and size of tappable areas.
    """

    def __init__(self, bounds=None, action=None, **kwargs):
        """__init__ method.

        :param bounds: Object describing the boundaries of the area in pixels.
        :type areas: T <= :py:class:`linebot.models.template.RichMenuBoundTemplate`
        :param action: Action performed when the area is tapped.
        :type action: T <= :py:class:`linebot.models.template.PostbackTemplateAction` |
                      T <= :py:class:`linebot.models.template.MessageTemplateAction` |
                      T <= :py:class:`linebot.models.template.URITemplateAction` |
                      T <= :py:class:`linebot.models.template.DatetimePickerTemplateAction`
        :param kwargs:
        """
        super(RichMenuAreaTemplate, self).__init__(id=id, **kwargs)

        action = _get_action(action)  # {Action}Template
        self.action = action
        self.bounds = bounds  # RichMenuBoundTemplate
