#!/usr/bin/python
# -*- coding: utf-8 -*-
from contextlib import closing
import pymysql
from pymysql import Error

def connection_db():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='qaz')
    return connection

def create_db():
    connect = connection_db()
    try:
        cursor = connect.cursor()
        cursor.execute("create database schedule")
    except Error as e:
        if e.args[0] == 1007:
            pass
    finally:
        connect.close()
def create

def main():
    create_db()

if __name__ == '__main__':
    main()
