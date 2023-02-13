# This Python file uses the following encoding: utf-8

import sqlite3


class SQL:
    __CONNECTION = sqlite3.Connection('')
    c = 1

    @staticmethod
    def connect(func):
        def wrapper(*args, **kwargs):
            SQL.__CONNECTION = sqlite3.connect('diplom.db')
            res = func(*args, **kwargs)
            SQL.__CONNECTION.close()
            return res

        return wrapper

    @staticmethod
    def insert(statement: str):
        cursor = SQL.__CONNECTION.cursor()
        cursor.execute(statement)
        print(SQL.c, 'inserted')
        SQL.c += 1
        SQL.__CONNECTION.commit()
