#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ソースコードディストリビューション（sdist）のための設えです。
$ python setup.py sdist
"""

__author__ = 'Enomoto Yoshiki'
__version__ = '1.0.1'
__date__ = '2018/12/7 (Created: 2018/10/19)'

from distutils.core import setup

setup( \
    name='csvFormatter', \
    version=__version__, \
    description='csvFormatter written by Python 3.7.5', \
    author=__author__, \
    author_email='s06181110.cac@gmail.com', \
    license='MIT License', \
    long_description='このプログラムはBe Focused Proで生成されるCSVファイルをGoogleカレンダーにエクスポートできる形式に変更するプログラムです。', \
    platforms='macOS (10.15.1) Catalina', \
    packages='jp', \
)
