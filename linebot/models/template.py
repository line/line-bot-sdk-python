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


def _get_actions(actions):
    new_actions = []
    if actions:
        for action in actions:
            action_obj = Base.get_or_new_from_json_dict_with_types(
                action, {
                    'postback': PostbackTemplateAction,
                    'message': MessageTemplateAction,
                    'uri': URITemplateAction
                }
            )
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
                'carousel': CarouselTemplate
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


class CarouselTemplate(Base):
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
