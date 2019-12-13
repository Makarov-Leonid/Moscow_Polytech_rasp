# -*- coding: utf-8 -*-
import json
import datetime

def get_data():
    with open("stu_mami.json","r", encoding="utf8") as reader:
        data = json.load(reader)
        rasp = data['contents']
    return rasp

def read_data():
    rasp = get_data()
    for grup in rasp:
        grup_title = grup["group"]['title']
        grid = grup["grid"]
        # elem день недели, value расписание на этот день
        for elem, value in grid.items():
            day = elem
            for time_l, param in value.items():
                if param == []:
                    continue
                time = time_l
                param = param[0]
                teacher     = param["teacher"]
                subject     = param["subject"]
                date_from   = param["date_from"]
                date_to     = param["date_to"]
                auditories  = param["auditories"][0]["title"]
                #наверно, это можно сделать по другому
                result = {
                            'group':grup_title,
                            'day':day,
                            'time':time,
                            'teacher':teacher,
                            'subject':subject,
                            'date_from':date_from,
                            'date_to':date_to,
                            'auditories':auditories,
                         }
                yield result

def print_data(result, teacher):
    day = {'1':'Понедельник', '2':'Вторник', '3':'Среда', '4':'Четверг', '5':'Пятница', '6':'Суббота', '7':'Воскреcенье'}
    time = {'1':'9:00 - 10:30', '2':'10:40 - 12:10', '3':'12:20 - 13:50', '4':'14:30 - 16:00', '5':'16:10 - 17:40', '6':'17:50 - 19:20', '7':'19:30 - 21:00'}
    time_ = str(datetime.datetime.now())[:10]
    for row in result:
        if row['date_from'] <= time_ and row['date_to'] >= time_ and row['teacher'] == teacher:
            print('{:11} {:13} {:10} {}'.format(day[row['day']], time[row['time']], row['auditories'], row['subject']))


def main(teacher = 'Чувашев Юрий Иванович'):
    print(teacher)
    print_data(read_data(), teacher)

if __name__ == '__main__':
    main()
