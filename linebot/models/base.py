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

"""linebot.models.base module."""

from __future__ import unicode_literals

import json

from .. import utils


class Base(object):
    """Base class of model.

    Suitable for JSON base data.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        pass

    def __str__(self):
        """__str__ method.

        :return:
        """
        return self.as_json_string()

    def __repr__(self):
        """__repr__ method.

        :return:
        """
        return str(self)

    def __eq__(self, other):
        """__eq__ method.

        :param other:
        :return:
        """
        return other and self.as_json_dict() == other.as_json_dict()

    def __ne__(self, other):
        """__ne__ method.

        :param other:
        :return:
        """
        return not self.__eq__(other)

    def as_json_string(self):
        """Return JSON string from this object.

        :rtype: str
        :return:
        """
        return json.dumps(self.as_json_dict(), sort_keys=True)

    def as_json_dict(self):
        """Return dictionary from this object.

        :return: dict
        """
        data = {}
        for key in self.__dict__.keys():
            camel_key = utils.to_camel_case(key)
            if isinstance(getattr(self, key, None), (list, tuple, set)):
                data[camel_key] = list()
                for sub_obj in getattr(self, key, None):
                    if getattr(sub_obj, 'as_json_dict', None):
                        data[camel_key].append(sub_obj.as_json_dict())
                    else:
                        data[camel_key].append(sub_obj)

            elif getattr(getattr(self, key, None), 'as_json_dict', None):
                data[camel_key] = getattr(self, key).as_json_dict()

            else:
                data[camel_key] = getattr(self, key, None)

        return data

    @classmethod
    def new_from_json_dict(cls, data):
        """Create a new instance from a dict.

        :param data: JSON dict
        :rtype:
        :return:
        """
        new_data = {utils.to_snake_case(key): value
                    for key, value in data.items()}

        return cls(**new_data)

    @staticmethod
    def get_or_new_from_json_dict(data, cls):
        """Helper function.

        If data is instance of cls, return data.
        Else if data is instance of dict, create instance from dict.
        Else, return None.

        :param data:
        :param cls:
        :rtype: object
        :return:
        """
        if isinstance(data, cls):
            return data
        elif isinstance(data, dict):
            return cls.new_from_json_dict(data)

        return None

    @staticmethod
    def get_or_new_from_json_dict_with_types(
            data, cls_map, type_key='type'
    ):
        """Helper function.

        If data is instance of one of cls, return data.
        Else if data is instance of dict, create instance from dict.
        Else, return None.

        :param data:
        :param cls_map:
        :param type_key:
        :rtype: object
        :return:
        """
        if isinstance(data, tuple(cls_map.values())):
            return data
        elif isinstance(data, dict):
            type_val = data[type_key]
            if type_val in cls_map:
                return cls_map[type_val].new_from_json_dict(data)

        return None
