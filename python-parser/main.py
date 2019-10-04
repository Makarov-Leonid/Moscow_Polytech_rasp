# -*- coding: utf-8 -*-
import json
import pymysql
from pymysql.cursors import DictCursor
#-------
# TODO: Добавить requirements.txt

def get_data():
    with open("stu_mami.json","r", encoding="utf8") as reader:
        data = json.load(reader)
        rasp = data['contents']
    return rasp

def connection_db():

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='qaz',
                                 db='schedule',
                                 charset='utf8',
                                 cursorclass=DictCursor)
    return connection

def write_data(data):
    # input data keys
    # -----------------
    # 'day'
    # 'time'
    # 'teacher'
    # 'subject'
    # 'date_from'
    # 'date_to'
    # 'auditories'
    # 'group'
    # -----------------
    connect = connection_db()
    sql ="INSERT INTO rasp(day,time_,teacher,subject,date_from,date_to,auditories,group_) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    info = (data['day'],data['time'],data['teacher'],
            data['subject'],data['date_from'],data['date_to'],
            data['auditories'],data['group'])
    try:
        cursor = connect.cursor()
        cursor.execute(sql,info)
        connect.commit()
    finally:
        connect.close()

def read_data():
    connect = connection_db()
    sql =   '''
                SELECT day, time_, auditories, group_ FROM rasp
                WHERE NOW() >= date_from AND NOW() <= date_to AND
                teacher=%s
                ORDER BY day, time_
            '''
    finding_teacher = 'Никишина Ирина Николаевна'
    try:
        cursor = connect.cursor()
        cursor.execute(sql, finding_teacher) #finding_teacher
        for row in cursor:
            print(row)
    finally:
        connect.close()


def structure_data():
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
                write_data(result)

def main():
    read_data()

if __name__ == '__main__':
    main()
