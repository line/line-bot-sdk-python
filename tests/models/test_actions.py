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

from __future__ import unicode_literals, absolute_import

import unittest

from linebot.models import (
    PostbackAction,
    MessageAction,
    URIAction,
    DatetimePickerAction,
    CameraRollAction, CameraAction, LocationAction, AltUri)
from linebot.utils import to_camel_case


class TestActions(unittest.TestCase):
    def test_postback(self):
        postback_arg = {
            'type': 'postback',
            'label': 'Buy',
            'data': 'action=buy&id=1',
            'display_text': 'buy'
        }
        self.assertEqual(
            {to_camel_case(k): v for k, v in postback_arg.items()},
            PostbackAction(**postback_arg).as_json_dict()
        )

    def test_message(self):
        message_arg = {
            'type': 'message',
            'label': 'Yes',
            'text': 'yes'
        }
        self.assertEqual(
            message_arg,
            MessageAction(**message_arg).as_json_dict()
        )

    def test_camera(self):
        camera_arg = {
            'type': 'camera',
            'label': 'camera'
        }
        self.assertEqual(
            camera_arg,
            CameraAction(**camera_arg).as_json_dict()
        )

    def test_camera_roll(self):
        camera_roll_arg = {
            'type': 'cameraRoll',
            'label': 'camera roll'
        }
        self.assertEqual(
            camera_roll_arg,
            CameraRollAction(**camera_roll_arg).as_json_dict()
        )

    def test_datetime_picker(self):
        datetime_picker_arg = {
            'type': 'datetimepicker',
            'label': 'Select date',
            'data': 'storeId=12345',
            'mode': 'datetime',
            'initial': '2017-12-25t00:00',
            'max': '2018-01-24t23:59',
            'min': '2017-12-25t00:00'
        }
        self.assertEqual(
            datetime_picker_arg,
            DatetimePickerAction(**datetime_picker_arg).as_json_dict()
        )

    def test_uri(self):
        uri_arg = {
            'type': 'uri',
            'label': 'View detail',
            'uri': 'https://example.com',
            'alt_uri': {'desktop': 'https://example.com'}
        }
        expected = {to_camel_case(k): v for k, v in uri_arg.items()}
        self.assertEqual(
            expected,
            URIAction(**uri_arg).as_json_dict()
        )

        uri_arg['alt_uri'] = AltUri(desktop='https://example.com')
        self.assertEqual(
            expected,
            URIAction(**uri_arg).as_json_dict()
        )

    def test_location(self):
        location_arg = {
            'type': 'location',
            'label': 'Location'
        }
        self.assertEqual(
            location_arg,
            LocationAction(**location_arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
