#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Be focused pro で取得したCSVファイルを
Googleカレンダーのフォーマットに変換して出力する
"""

import os, datetime

home_directory = os.path.expanduser('~')
a_file = os.path.join(home_directory, 'Downloads', 'BeFocused.csv')
today = datetime.datetime.combine(datetime.date.today(), datetime.time())
target_day = today - datetime.timedelta(days=7)


write_list = []
with open(a_file, 'r', encoding='utf-8') as a_file:
    counter = 0
    for a_string in a_file:
        if counter < 2:
            counter += 1
            continue
        a_list = a_string.split(',')
        start_time = datetime.datetime.strptime(a_list[0], '%b %d %Y %H:%M:%S')
        if target_day < start_time:
            end_time = start_time + datetime.timedelta(minutes=int(a_list[1]))
            write_list.append([a_list[2], ','.join(str(start_time).split()), ','.join(str(end_time).split())])

a_file = os.path.join(home_directory, 'Desktop', 'BeFocused.csv')
with open(a_file, 'w', encoding='utf-8') as a_file:
    a_file.write("Subject,Start Date,Start Time,End Date,End Time\n")
    for a_list in write_list:
        a_file.write(','.join(a_list)+"\n")