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

"""linebot.models.actions module."""


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
            'datetimepicker': DatetimePickerAction,
            'camera': CameraAction,
            'cameraRoll': CameraRollAction,
            'location': LocationAction,
            'richmenuswitch': RichMenuSwitchAction,
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

    def __init__(
        self,
        label=None,
        data=None,
        display_text=None,
        text=None,
        input_option=None,
        fill_in_text=None,
        **kwargs
    ):
        """__init__ method.

        :param str label: Label for the action.
        :param str data: String returned via webhook
            in the postback.data property of the postback event.
        :param str display_text: Text displayed in the chat as a message sent by
            the user when the action is performed.
        :param str text: Deprecated. Text displayed in the chat as a message sent by
            the user when the action is performed. Returned from the server through a webhook.
        :param kwargs:
        """
        super(PostbackAction, self).__init__(**kwargs)

        self.type = 'postback'
        self.label = label
        self.data = data
        self.display_text = display_text
        self.text = text
        self.input_option = input_option
        self.fill_in_text = fill_in_text


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

    def __init__(self, label=None, uri=None, alt_uri=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
            Max: 20 characters
        :param str uri: URI opened when the action is performed.
        :param alt_uri: URI opened when the desktop app.
        :type alt_uri: T <= :py:class:`linebot.models.actions.AltUri`
        :param kwargs:
        """
        super(URIAction, self).__init__(**kwargs)

        self.type = 'uri'
        self.label = label
        self.uri = uri
        self.alt_uri = self.get_or_new_from_json_dict(alt_uri, AltUri)


class AltUri(with_metaclass(ABCMeta, Base)):
    """AltUri.

    https://github.com/line/line-bot-sdk-python/issues/155

    URI opened when the desktop app.
    """

    def __init__(self, desktop=None, **kwargs):
        """__init__ method.

        :param str desktop: URI opened on LINE for macOS and Windows
            when the action is performed.
            If the altUri.desktop property is set,
            the uri property is ignored on LINE for macOS and Windows.
        :param kwargs:
        """
        super(AltUri, self).__init__(**kwargs)

        self.desktop = desktop


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


class CameraAction(Action):
    """CameraAction.

    https://developers.line.me/en/reference/messaging-api/#camera-action

    This action can be configured only with quick reply buttons.
    When a button associated with this action is tapped,
    the camera screen in the LINE app is opened.
    """

    def __init__(self, label=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
        :param kwargs:
        """
        super(CameraAction, self).__init__(**kwargs)

        self.type = 'camera'
        self.label = label


class CameraRollAction(Action):
    """CameraRollAction.

    https://developers.line.me/en/reference/messaging-api/#camera-roll-action

    This action can be configured only with quick reply buttons.
    When a button associated with this action is tapped,
    the camera roll screen in the LINE app is opened.
    """

    def __init__(self, label=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
        :param kwargs:
        """
        super(CameraRollAction, self).__init__(**kwargs)

        self.type = 'cameraRoll'
        self.label = label


class LocationAction(Action):
    """LocationRollAction.

    https://developers.line.me/en/reference/messaging-api/#location-action

    This action can be configured only with quick reply buttons.
    When a button associated with this action is tapped,
    the location screen in the LINE app is opened.
    """

    def __init__(self, label=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
        :param kwargs:
        """
        super(LocationAction, self).__init__(**kwargs)

        self.type = 'location'
        self.label = label


class RichMenuSwitchAction(Action):
    """RichMenuSwitchAction.

    https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action

    This action can be configured only with rich menus.
    It can't be used for Flex Messages or quick replies.
    When you tap a rich menu associated with this action,
    you can switch between rich menus,
    and a postback event including the rich menu alias ID selected
     by the user is returned via a webhook.
    """

    def __init__(self, label=None, rich_menu_alias_id=None, data=None, **kwargs):
        """__init__ method.

        :param str label: Label for the action
        :param str rich_menu_alias_id: Rich menu alias ID to switch to.
        :param str data: String returned by the postback.data property
         of the postback event via a webhook
        :param kwargs:
        """
        super(RichMenuSwitchAction, self).__init__(**kwargs)

        self.type = 'richmenuswitch'
        self.label = label
        self.rich_menu_alias_id = rich_menu_alias_id
        self.data = data
