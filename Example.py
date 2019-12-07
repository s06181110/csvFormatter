#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Be Focused Pro で取得したCSVファイルを
Googleカレンダーのフォーマットに変換して出力する
"""

__author__ = 'Enomoto Yoshiki'
__version__ = '1.0.2'
__date__ = '2019/12/7 (Created: 2019/10/19)'

# exit関数に利用。
import sys

import jp.ac.kyoto_su.g1744221.Formatter as Formatter

# このスクリプトファイルが直接実行されただけ、以下の部分を実行する。
if __name__ == '__main__':

	# Formatterモジュールのmain()を呼び出して、Pythonシステムに終わりを告げる。
	sys.exit(Formatter.main())
