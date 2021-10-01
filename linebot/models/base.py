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
        """__str__ method."""
        return self.as_json_string()

    def __repr__(self):
        """__repr__ method."""
        return str(self)

    def __eq__(self, other):
        """__eq__ method.

        :param other:
        """
        return other and self.as_json_dict() == other.as_json_dict()

    def __ne__(self, other):
        """__ne__ method.

        :param other:
        """
        return not self.__eq__(other)

    def as_json_string(self):
        """Return JSON string from this object.

        :rtype: str
        """
        return json.dumps(self.as_json_dict(), sort_keys=True)

    def as_json_dict(self):
        """Return dictionary from this object.

        :return: dict
        """
        data = {}
        for key, value in self.__dict__.items():
            camel_key = utils.to_camel_case(key)
            if isinstance(value, (list, tuple, set)):
                data[camel_key] = list()
                for item in value:
                    if hasattr(item, 'as_json_dict'):
                        data[camel_key].append(item.as_json_dict())
                    else:
                        data[camel_key].append(item)

            elif hasattr(value, 'as_json_dict'):
                data[camel_key] = value.as_json_dict()
            elif value is not None:
                data[camel_key] = value

        return data

    @classmethod
    def new_from_json_dict(cls, data):
        """Create a new instance from a dict.

        :param data: JSON dict
        """
        new_data = {utils.to_snake_case(key): value
                    for key, value in data.items()}

        return cls(**new_data)

    @staticmethod
    def get_or_new_from_json_dict(data, cls):
        """Get `cls` object w/ deserialization from json if needed.

        If data is instance of cls, return data.
        Else if data is instance of dict, create instance from dict.
        Else, return None.

        :param data:
        :param cls:
        :rtype: object
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
        """Get `cls` object w/ deserialization from json by using type key hint if needed.

        If data is instance of one of cls, return data.
        Else if data is instance of dict, create instance from dict.
        Else, return None.

        :param data:
        :param cls_map:
        :param type_key:
        :rtype: object
        """
        if isinstance(data, tuple(cls_map.values())):
            return data
        elif isinstance(data, dict):
            type_val = data[type_key]
            if type_val in cls_map:
                return cls_map[type_val].new_from_json_dict(data)

        return None
