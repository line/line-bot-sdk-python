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

import sys
import unittest
from numbers import Number

from linebot.models import (
    Base,
)
from linebot.utils import to_camel_case

PY3 = sys.version_info[0] == 3


class SerializeTestCase(unittest.TestCase):
    def serialize_as_dict(self, obj):
        if isinstance(obj, Base):
            return obj.as_json_dict()
        elif isinstance(obj, dict):
            return {
                to_camel_case(k): self.serialize_as_dict(v)
                for k, v in obj.items()
            }
        elif isinstance(obj, list):
            return [self.serialize_as_dict(elem) for elem in obj]
        else:
            if PY3:
                self.assertIsInstance(obj, (str, bool, Number))
            else:
                self.assertIsInstance(obj, (basestring, bool, Number))
            return obj
