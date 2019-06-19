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
    CameraRollAction,
    CameraAction,
    URIAction,
    LocationAction,
    DatetimePickerAction,
    AltUri,
)
from tests.models.serialize_test_case import SerializeTestCase


class TestActions(SerializeTestCase):
    def test_postback(self):
        arg = {
            'type': 'postback',
            'label': 'Buy',
            'data': 'action=buy&id=1',
            'display_text': 'buy'
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            PostbackAction(**arg).as_json_dict()
        )

    def test_message(self):
        arg = {
            'type': 'message',
            'label': 'Yes',
            'text': 'yes'
        }
        self.assertEqual(
            arg,
            MessageAction(**arg).as_json_dict()
        )

    def test_camera(self):
        arg = {
            'type': 'camera',
            'label': 'camera'
        }
        self.assertEqual(
            arg,
            CameraAction(**arg).as_json_dict()
        )

    def test_camera_roll(self):
        arg = {
            'type': 'cameraRoll',
            'label': 'camera roll'
        }
        self.assertEqual(
            arg,
            CameraRollAction(**arg).as_json_dict()
        )

    def test_datetime_picker(self):
        arg = {
            'type': 'datetimepicker',
            'label': 'Select date',
            'data': 'storeId=12345',
            'mode': 'datetime',
            'initial': '2017-12-25t00:00',
            'max': '2018-01-24t23:59',
            'min': '2017-12-25t00:00'
        }
        self.assertEqual(
            arg,
            DatetimePickerAction(**arg).as_json_dict()
        )

    def test_uri(self):
        arg = {
            'type': 'uri',
            'label': 'View detail',
            'uri': 'https://example.com',
            'alt_uri': AltUri(desktop='https://example.com')
        }
        self.assertEqual(
            self.serialize_as_dict(arg),
            URIAction(**arg).as_json_dict()
        )

    def test_location(self):
        arg = {
            'type': 'location',
            'label': 'Location'
        }
        self.assertEqual(
            arg,
            LocationAction(**arg).as_json_dict()
        )


if __name__ == '__main__':
    unittest.main()
