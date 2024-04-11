# This Python file uses the following encoding: utf-8

import sqlite3
from logger.Logger import Logger

logger = Logger()


class SQL:

    __CONNECTION: sqlite3.Connection = None
    __cursor: sqlite3.Cursor = None
    c = 1

    def __enter__(self):
        SQL.__CONNECTION = sqlite3.connect('../diplom.db', isolation_level=None)
        SQL.__cursor = SQL.__CONNECTION.cursor()
        logger.info("Connection opened")
        return SQL.__CONNECTION

    def __exit__(self, exc_type, exc_val, exc_tb):
        if SQL.__CONNECTION:
            SQL.__cursor.close()
            SQL.__CONNECTION.close()
            logger.info("Connection closed")

    @staticmethod
    def execute(statement: str):
        SQL.__cursor.execute(statement)

    @staticmethod
    def select(statement: str):
        SQL.__cursor.execute(statement)
