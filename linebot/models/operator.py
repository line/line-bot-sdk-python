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

"""linebot.models.filter module."""


from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Operator(with_metaclass(ABCMeta, Base)):
    """Operator.

    https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter

    Use logical AND, OR, and NOT operators to combine multiple recipient objects or
    demographic filter objects together.
    You can specify up to 10 recipient objects or demographic filter objects per request.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Operator, self).__init__(**kwargs)

        self.type = "operator"


class And(Operator):
    """And.

    Create a new recipient object or demographic filter object by taking the
    logical conjunction (AND) of the specified array of objects.
    """

    def __init__(self, *args, **kwargs):
        """__init__ method.

        :param args:
        :param kwargs:
        """
        super(And, self).__init__(**kwargs)

        setattr(self, 'and', args)


class Or(Operator):
    """Or.

    Create a new recipient object or demographic filter object by taking the
    logical disjunction (OR) of the specified array of objects.
    """

    def __init__(self, *args, **kwargs):
        """__init__ method.

        :param args:
        :param kwargs:
        """
        super(Or, self).__init__(**kwargs)

        setattr(self, 'or', args)


class Not(Operator):
    """Not.

    Create a new recipient object or demographic filter object that excludes
    in the specified object.
    """

    def __init__(self, arg, **kwargs):
        """__init__ method.

        :param arg:
        :param kwargs:
        """
        super(Not, self).__init__(**kwargs)

        setattr(self, 'not', arg)
