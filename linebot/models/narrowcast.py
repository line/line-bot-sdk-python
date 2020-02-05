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


from __future__ import unicode_literals

from functools import wraps

from .base import Base


class NarrowCastModel(Base):
    def __init__(self, messages, recipient=None, filter=None, limit=None, **kwargs):
        super(NarrowCastModel, self).__init__(**kwargs)
        self.messages = messages
        self.recipient = self.get_or_new_from_json_dict_with_types(
            recipient, {
                'operator': Operator,
                'audience': Audience,
                'gender': Gender,
                'age': Age,
                'appType': App,
                'area': Area,
                'subscriptionPeriod': SubscriptionPeriod
            }
        )
        self.filter = self.get_or_new_from_json_dict(filter, NarrowCastDemographic)
        self.limit = self.get_or_new_from_json_dict(limit, NarrowCastLimit)


class NarrowCastDemographic(Base):
    def __init__(self, demographic=None, **kwargs):
        super(NarrowCastDemographic, self).__init__(**kwargs)
        self.demographic = self.get_or_new_from_json_dict_with_types(
            demographic, {
                'operator': Operator,
                'audience': Audience,
                'gender': Gender,
                'age': Age,
                'appType': App,
                'area': Area,
                'subscriptionPeriod': SubscriptionPeriod
            }
        )


class NarrowCastLimit(Base):
    """Limit."""

    def __init__(self, max=None, **kwargs):
        """__init__ method.

        :param int max: Limit of send message.
        """
        super(NarrowCastLimit, self).__init__(**kwargs)
        self.max = max


class NarrowCast(Base):
    """NarrowCast.

    https://developers.line.biz/en/reference/messaging-api/#container

    A container is the top-level structure of a Flex Message.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(NarrowCast, self).__init__(**kwargs)

        self.type = None


def operator_initialize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs.get('and'):
            kwargs['AND'] = kwargs['and']
        if kwargs.get('or'):
            kwargs['OR'] = kwargs['or']
        if kwargs.get('not'):
            kwargs['NOT'] = kwargs['not']
        return func(*args, **kwargs)

    return wrapper


class Operator(NarrowCast):
    """Operator."""

    @operator_initialize
    def __init__(self, AND=None, OR=None, NOT=None, **kwargs):
        super(Operator, self).__init__(**kwargs)
        self.type = 'operator'
        new_and = []
        if AND:
            for condition in AND:
                new_and.append(self.get_or_new_from_json_dict_with_types(
                    condition, {
                        'operator': Operator,
                        'audience': Audience,
                        'gender': Gender,
                        'age': Age,
                        'appType': App,
                        'area': Area,
                        'subscriptionPeriod': SubscriptionPeriod
                    }
                ))
        self.AND = new_and if new_and else None
        new_or = []
        if OR:
            for condition in OR:
                new_or.append(self.get_or_new_from_json_dict_with_types(
                    condition, {
                        'operator': Operator,
                        'audience': Audience,
                        'gender': Gender,
                        'age': Age,
                        'appType': App,
                        'area': Area,
                        'subscriptionPeriod': SubscriptionPeriod
                    }
                ))
        self.OR = new_or if new_or else None

        self.NOT = self.get_or_new_from_json_dict_with_types(
            NOT, {
                'audience': Audience,
                'gender': Gender,
                'age': Age,
                'appType': App,
                'area': Area,
                'subscriptionPeriod': SubscriptionPeriod
            }
        )


class Audience(NarrowCast):
    """Audience."""

    def __init__(self, audience_group_id=None, request_id=None, **kwargs):
        super(Audience, self).__init__(**kwargs)

        self.type = 'audience'
        self.audience_group_id = audience_group_id


class Age(NarrowCast):
    """Age."""

    def __init__(self, gte=None, lt=None, **kwargs):
        super(Age, self).__init__(**kwargs)
        self.type = 'age'
        self.gte = gte
        self.lt = lt


class Gender(NarrowCast):
    """Gender."""

    def __init__(self, one_of=None, **kwargs):
        super(Gender, self).__init__(**kwargs)
        self.type = 'gender'
        self.one_of = one_of


class App(NarrowCast):
    """App."""

    def __init__(self, one_of=None, **kwargs):
        super(App, self).__init__(**kwargs)
        self.type = 'appType'
        self.one_of = one_of


class Area(NarrowCast):
    """Area."""

    def __init__(self, one_of=None, **kwargs):
        super(Area, self).__init__(**kwargs)
        self.type = 'area'
        self.one_of = one_of


class SubscriptionPeriod(NarrowCast):
    """SubscriptionPeriod."""

    def __init__(self, gte=None, lt=None, **kwargs):
        super(SubscriptionPeriod, self).__init__(**kwargs)
        self.type = 'subscriptionPeriod'
        self.gte = gte
        self.lt = lt
