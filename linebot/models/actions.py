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


def get_action(action):
    """Get action."""
    action_obj = Base.get_or_new_from_json_dict_with_types(
        action, {
            'postback': PostbackAction,
            'message': MessageAction,
            'uri': URIAction,
            'datetimepicker': DatetimePickerAction
        }
    )
    return action_obj


def get_actions(actions):
    """Get actions."""
    new_actions = []
    if actions:
        for action in actions:
            action_obj = get_action(action)
            if action_obj:
                new_actions.append(action_obj)

    return new_actions


class Action(with_metaclass(ABCMeta, Base)):
    """Abstract base class of Action."""

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Action, self).__init__(**kwargs)

        self.type = None


class PostbackAction(Action):
    """PostbackAction.

    https://developers.line.me/en/docs/messaging-api/reference/#postback-action

    When a control associated with this action is tapped,
    a postback event is returned via webhook with the specified string in the data property.
    """

    def __init__(self, label=None, data=None, text=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action.
        :param str data: String returned via webhook
            in the postback.data property of the postback event.
        :param str text: Text displayed in the chat as a message sent by
            the user when the action is performed. Returned from the server through a webhook.
        :param kwargs:
        """
        super(PostbackAction, self).__init__(**kwargs)

        self.type = 'postback'
        self.label = label
        self.data = data
        self.text = text


class MessageAction(Action):
    """MessageAction.

    https://developers.line.me/en/docs/messaging-api/reference/#message-action

    When a control associated with this action is tapped,
    the string in the text property is sent as a message from the user.
    """

    def __init__(self, label=None, text=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action.
        :param str text: Text sent when the action is performed.
        :param kwargs:
        """
        super(MessageAction, self).__init__(**kwargs)

        self.type = 'message'
        self.label = label
        self.text = text


class URIAction(Action):
    """URIAction.

    https://developers.line.me/en/docs/messaging-api/reference/#uri-action

    When a control associated with this action is tapped,
    the URI specified in the uri property is opened.
    """

    def __init__(self, label=None, uri=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
            Max: 20 characters
        :param str uri: URI opened when the action is performed.
        :param kwargs:
        """
        super(URIAction, self).__init__(**kwargs)

        self.type = 'uri'
        self.label = label
        self.uri = uri


class DatetimePickerAction(Action):
    """DatetimePickerAction.

    https://developers.line.me/en/docs/messaging-api/reference/#datetime-picker-action

    When a control associated with this action is tapped,
    a postback event is returned via webhook with the date and time
    selected by the user from the date and time selection dialog.
    The datetime picker action does not support time zones.
    """

    def __init__(self, label=None, data=None, mode=None,
                 initial=None, max=None, min=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
        :param str data: String returned via webhook
            in the postback.data property of the postback event
        :param str mode: Action mode
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
        super(DatetimePickerAction, self).__init__(**kwargs)

        self.type = 'datetimepicker'
        self.label = label
        self.data = data
        self.mode = mode
        self.initial = initial
        self.max = max
        self.min = min
