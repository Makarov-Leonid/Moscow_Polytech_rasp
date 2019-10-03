#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from contextlib import closing
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
    # -----------------
    connect = connection_db()
    sql ="INSERT INTO rasp(day,time_,teacher,subject,date_from,date_to,auditories) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    info = (data['day'],data['time'],data['teacher'],
            data['subject'],data['date_from'],data['date_to'],data['auditories'])
    try:
        cursor = connect.cursor()
        cursor.execute(sql,info)
        print('subject')
        connect.commit()
    finally:
        connect.close()

# TODO: Убрать\вынести в отдельный файл
#пусть пока полежит здесь
# CREATE TABLE rasp(
#   day INT NOT NULL,
#   time_ INT NOT NULL,
#   teacher CHAR(255) NOT NULL,
#   subject CHAR(255) NOT NULL,
#   date_from DATE NOT NULL,
#   date_to DATE NOT NULL,
#   auditories CHAR(255) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;


def structure_data():
    rasp = get_data()
    for grup in rasp:
        grup_title = grup["group"]['title']
        grid = grup["grid"]
        # elem день недели, value расписание на этот день
        # TODO: проверить всегда ли расписание лежит в value[0]
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
                            'day':day,
                            'time':time,
                            'teacher':teacher,
                            'subject':subject,
                            'date_from':date_from,
                            'date_to':date_to,
                            'auditories':auditories,
                         }
                write_data(result)
                # print([v for v in result.values()])

def main():
    print(structure_data())

if __name__ == '__main__':
    main()
