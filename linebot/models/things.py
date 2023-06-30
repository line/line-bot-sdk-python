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

"""linebot.models.things module."""


from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Things(with_metaclass(ABCMeta, Base)):
    """Abstract Base Class of Things."""

    def __init__(self, device_id=None, **kwargs):
        """__init__ method.

        :param str device_id: Device ID.
        :param kwargs:
        """
        super(Things, self).__init__(**kwargs)
        self.device_id = device_id


class DeviceLink(Things):
    """DeviceLink.

    https://developers.line.biz/en/reference/messaging-api/#device-link-event

    Indicates that a user linked a device with LINE.
    """

    def __init__(self, device_id=None, **kwargs):
        """__init__ method.

        :param str device_id: Device ID of the device that has been linked with LINE.
        :param kwargs:
        """
        super(DeviceLink, self).__init__(device_id=device_id, **kwargs)

        self.type = 'link'


class DeviceUnlink(Things):
    """DeviceUnlink.

    https://developers.line.biz/en/reference/messaging-api/#device-unlink-event

    Indicates that the user unlinked a device from LINE.
    """

    def __init__(self, device_id=None, **kwargs):
        """__init__ method.

        :param str device_id: Device ID of the device that was unlinked from LINE.
        :param kwargs:
        """
        super(DeviceUnlink, self).__init__(device_id=device_id, **kwargs)

        self.type = 'unlink'


class ScenarioResult(Things):
    """ScenarioResult.

    https://developers.line.biz/en/reference/messaging-api/#scenario-result-event

    Indicates that an automatic communication scenario has been executed.
    """

    def __init__(self, device_id=None, result=None, **kwargs):
        """__init__ method.

        :param str device_id: Device ID of the device that executed the scenario.
        :param str result: ScenarioResultPayload object.
        :param kwargs:
        """
        super(ScenarioResult, self).__init__(device_id=device_id, **kwargs)

        self.type = 'scenarioResult'
        self.result = self.get_or_new_from_json_dict(
            result, ScenarioResultPayload
        )


class ScenarioResultPayload(Base):
    """ScenarioResultPayload."""

    def __init__(self, scenario_id=None, revision=None, start_time=None,
                 result_code=None, end_time=None, action_results=None,
                 ble_notification_payload=None, error_reason=None, **kwargs):
        """__init__ method.

        :param str scenario_id: Scenario ID executed.
        :param long revision: Revision number.
        :param long start_time: Timestamp for when execution of scenario
            action started (milliseconds).
        :param long end_time: Timestamp for when execution of scenario
            was completed (milliseconds).
        :param str result_code: Scenario execution completion status.
        :param action_results: Array of actions specified in a scenario.
        :type action_results: list[T <= :py:class:`linebot.models.things.ActionResult`]
        :param str ble_notification_payload: Data contained in notification.
        :param str error_reason: Error response.
        :param kwargs:
        """
        super(ScenarioResultPayload, self).__init__(**kwargs)

        self.scenario_id = scenario_id
        self.revision = revision
        self.start_time = start_time
        self.end_time = end_time
        self.result_code = result_code
        self.action_results = [self.get_or_new_from_json_dict(it, ActionResult)
                               for it in action_results]
        self.ble_notification_payload = ble_notification_payload
        self.error_reason = error_reason


class ActionResult(Base):
    """ActionResult.

    Execution result of individual operations specified in action
    """

    def __init__(self, type=None, data=None, **kwargs):
        """__init__ method.

        :param str type: Type of the executed action.
        :param str data: Base64-encoded binary data.
        :param kwargs:
        """
        super(ActionResult, self).__init__(**kwargs)

        self.type = type
        self.data = data
