#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymysql
from pymysql import Error

def connection_mySQL():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='qaz')
    return connection

def create_table():
    connect = connection_mySQL()
    try:
        cursor = connect.cursor()
        cursor.execute("use schedule")

        cursor.execute('''
                        CREATE TABLE rasp(
                        day INT NOT NULL,
                        time_ INT NOT NULL,
                        teacher CHAR(255) NOT NULL,
                        subject CHAR(255) NOT NULL,
                        date_from DATE NOT NULL,
                        date_to DATE NOT NULL,
                        auditories CHAR(255) NOT NULL,
                        group_ CHAR(255) NOT NULL
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                       '''
                      )
        print('tables complete')
    except:
        print('error table creater')
    finally:
        connect.close()

def create_db():
    connect = connection_mySQL()
    try:
        cursor = connect.cursor()
        cursor.execute("create database schedule")
        print('db complete')
        create_table()
    except Error as e:
        if e.args[0] == 1007:
            pass
    finally:
        connect.close()

def main():
    create_db()

if __name__ == '__main__':
    main()
