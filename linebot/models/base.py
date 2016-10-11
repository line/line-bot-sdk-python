# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from .. import utils


class Base(object):
    """Base class of model.

    Suitable for JSON base data.
    
    """

    def __init__(self, **kwargs):
        pass

    def __str__(self):
        return self.as_json_string()

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return other and self.as_json_dict() == other.as_json_dict()

    def __ne__(self, other):
        return not self.__eq__(other)

    def set_attrs(self, param_defaults, kwargs):
        for (param, default) in param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def as_json_string(self):
        """Return JSON string from this object."""

        return json.dumps(self.as_json_dict(), sort_keys=True)

    def as_json_dict(self):
        """Return dictionary from this object."""

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

        Args:
            data: dict

        Returns:
            New instance from dict.
        """
        new_data = {utils.to_snake_case(key): value
                    for key, value in data.items()}

        return cls(**new_data)

    @staticmethod
    def get_or_new_from_json_dict(data, cls):
        if isinstance(data, cls):
            return data
        elif isinstance(data, dict):
            return cls.new_from_json_dict(data)

        return None

    @staticmethod
    def get_or_new_from_json_dict_with_types(
            data, cls_map, type_key='type'
    ):
        if isinstance(data, tuple(cls_map.values())):
            return data
        elif isinstance(data, dict):
            type_val = data[type_key]
            if type_val in cls_map:
                return cls_map[type_val].new_from_json_dict(data)

        return None
