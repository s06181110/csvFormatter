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
        # a_string = Jul 12  2019 22:24:46,25,読書,To Do
        if counter < 2:
            counter += 1
            continue
        a_list = a_string.split(',')
        # a_list = [Jul 12  2019 22:24:46, 25, 読書, To Do]
        start_date = datetime.datetime.strptime(a_list[0], '%b %d %Y %H:%M:%S')
        # start_date = 2019-10-14 12:11:45
        if target_day < start_date:
            end_date = start_date + datetime.timedelta(minutes=int(a_list[1]))
            end_date, end_time = str(end_date).split()
            subject = a_list[2]
            start_date, start_time = str(start_date).split()
            write_list.append([subject, start_date, start_time, end_date, end_time])

a_file = os.path.join(home_directory, 'Desktop', 'BeFocused.csv')
with open(a_file, 'w', encoding='utf-8') as a_file:
    a_file.write("Subject,Start Date,Start Time,End Date,End Time\n")
    for a_list in write_list:
        a_file.write(','.join(a_list)+"\n")