#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.


import re
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

__version__ = ''
with open('linebot/__about__.py', 'r') as fd:
    reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
    for line in fd:
        m = reg.match(line)
        if m:
            __version__ = m.group(1)
            break


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


def _requirements_test():
    with open('requirements-test.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('_README.rst', 'r') as fd:
    long_description = fd.read()

setup(
    name="line-bot-sdk",
    version=__version__,
    author="RyosukeHasebe",
    author_email="hsb.1014@gmail.com",
    maintainer="RyosukeHasebe",
    maintainer_email="hsb.1014@gmail.com",
    url="https://github.com/line/line-bot-sdk-python",
    description="LINE Messaging API SDK for Python",
    long_description=long_description,
    license='Apache License 2.0',
    packages=[
        "linebot", "linebot.models"
    ],
    install_requires=_requirements(),
    tests_require=_requirements_test(),
    cmdclass={'test': PyTest},
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
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development"
    ]
)
