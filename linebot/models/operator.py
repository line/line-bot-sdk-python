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

from __future__ import unicode_literals

from abc import ABCMeta

from future.utils import with_metaclass

from .base import Base


class Operator(with_metaclass(ABCMeta, Base)):
    """Operator.

    https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter

    A operator is the top-level structure of a demographic element.
    """

    def __init__(self, **kwargs):
        """__init__ method.

        :param kwargs:
        """
        super(Operator, self).__init__(**kwargs)

        self.type = "operator"


class AND(Operator):
    """AND
    """

    def __init__(self, *args, **kwargs):
        """__init__ method.

        :param args:
        :param kwargs:
        """
        super(AND, self).__init__(**kwargs)

        setattr(self, 'and', args)


class OR(Operator):
    """OR
    """

    def __init__(self, *args, **kwargs):
        """__init__ method.

        :param args:
        :param kwargs:
        """
        super(OR, self).__init__(**kwargs)

        setattr(self, 'or', args)


class NOT(Operator):
    """NOT
    """

    def __init__(self, arg, **kwargs):
        """__init__ method.

        :param arg:
        :param kwargs:
        """
        super(NOT, self).__init__(**kwargs)

        setattr(self, 'not', arg)
