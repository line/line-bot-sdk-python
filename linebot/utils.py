# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import re
import sys

LOGGER = logging.getLogger('linebot')

PY3 = sys.version_info[0] == 3


def to_snake_case(text):
    """Convert to snake case

    Args:
        text:

    Returns:

    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def to_camel_case(text):
    """Convert to camel case

    Args:
        text:

    Returns:

    """
    split = text.split('_')
    return split[0] + "".join(x.title() for x in split[1:])
