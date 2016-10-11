#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup

__version__ = ''
with open('line_bot/__about__.py', 'r') as fd:
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
    name="line-bot-sdk-python",
    version=__version__,
    author="Ryosuke Hasebe",
    author_email="ryosuke.hasebe@linecorp.com",
    url="https://github.com/line/line-bot-sdk-python",
    description="LINE Messaging API SDK for Python",
    packages=[
        "line_bot"
    ],
    install_requires=_requirements(),
    tests_require=_requirements_test(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
        "Topic :: Software Development"
    ]
)
