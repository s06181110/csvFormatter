#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Be focused pro で取得したCSVファイルをGoogleカレンダーのフォーマットに変換して出力するプログラムである。
進捗報告でカレンダーを見せる際に重宝しています。
"""

import datetime
import io
import os

__author__ = 'Enomoto Yoshiki'
__version__ = '1.0.2'
__date__ = '2019/12/7 (Created: 2019/10/19)'

def main():
	"""
	CSVファイルをフォーマットするメインプログラム。
	before: Start Date, Duration, Assigned task, Task state
	after : Subject, Start Date, StartTime, End Date, End Time
	"""

	# 読み込みを行う
	lines = read()
	# 読み込んだ情報を都合よく整形する
	a_list = formatted(lines)
	# 整形されたリストをcsv形式で書き込む
	write(a_list)
	print("Successful")

def read():
	"""
	ダウンロードディレクトリにある「BeFocused.csv」を読み込んで、行のリストを応答します。
	"""
	# 読み込むファイルのパスを決める
	home_directory = os.environ['HOME']
	target_file = os.path.join(home_directory, 'Downloads', 'BeFocused.csv')

	# 全部を読み込んだ後、'\r'で分割する
	buffer = io.StringIO()
	with open(target_file, 'r', encoding='utf-8') as a_file:
		try:
			for line in a_file:
				# 復帰改行コードを削除した文字列で読む
				a_string = line.rstrip('\r\n')
				# 復帰コードを挿入して文字列にする
				buffer.write(a_string)
				buffer.write('\r')
		except UnicodeDecodeError:
			pass
		contents = buffer.getvalue()
	lines = contents.split('\r')

	# 行のリストを応答する
	return lines

def formatted(lines):
	"""
	CSVの形式を変換する関数。
	Googleカレンダーフォーマットにして応答します。
	1週間に限定していますが、自由に変更してください。
	"""
	formatted_list = []
	# 今日の日付を取る
	today = datetime.datetime.today()
	# 1週間前の日付を求める
	target_day = today - datetime.timedelta(days=7)

	# 最初2行(ヘッダー)と最後の余分なレコードを飛ばして読み込む
	for a_string in lines[2:-1]:
		a_list = a_string.split(',') # [Oct 14  2019 12:11:45, 25, 読書, To Do]
		start_date = datetime.datetime.strptime(a_list[0], '%b %d %Y %H:%M:%S') # 2019-10-14 12:11:45
		if target_day < start_date:
			end_date = start_date + datetime.timedelta(minutes=int(a_list[1])) # 2019-10-14 12:36:45
			end_date, end_time = str(end_date).split() # [2019-10-14, 12:36:45]
			subject = a_list[2] # 読書
			start_date, start_time = str(start_date).split() # [2019-10-14, 12:11:45]
			formatted_list.append([subject, start_date, start_time, end_date, end_time])

	# 整形されたリストを返す
	return formatted_list

def write(a_list):
	"""
	CSVのヘッダーと受け取ったリストを書き込んだものをデスクトップに書き込む関数。
	"""
	# 書き込むファイルのパスを決める
	home_directory = os.environ['HOME']
	a_file = os.path.join(home_directory, 'Desktop', 'BeFocused.csv')
	with open(a_file, 'w', encoding='utf-8') as a_file:
		# ヘッダー部分を書き込む
		a_file.write("Subject,Start Date,Start Time,End Date,End Time\n")
		for a_list in a_list:
			a_file.write(','.join(a_list)+"\n")


#  このスクリプトファイルが直接実行されただけ、以下の部分を実行する。
if __name__ == '__main__':

	import sys

	# このモジュールのmain()を呼び出して結果を得て、Pythonシステムに終わりを告げる。
	sys.exit(main())
