#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

__version__ = ''
with open('linebot/__about__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


def _requirements():
    return [name.strip() for name in open('requirements.txt').readlines()]


def _requirements_test():
    return [name.strip() for name in open('requirements-test.txt').readlines()]


setup(
    name="line-bot-sdk",
    version=__version__,
    author="RyosukeHasebe",
    author_email="hsb.1014@gmail.com",
    maintainer="RyosukeHasebe",
    maintainer_email="hsb.1014@gmail.com",
    url="https://github.com/line/line-bot-sdk-python",
    description="LINE Messaging API SDK for Python",
    long_description="LINE Messaging API SDK for Python",
    packages=[
        "linebot", "linebot.models"
    ],
    install_requires=_requirements(),
    tests_require=_requirements_test(),
    classifiers=[
        "Development Status :: 1 - Planning",
        # "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development"
    ]
)
