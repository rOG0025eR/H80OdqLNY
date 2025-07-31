# 代码生成时间: 2025-08-01 05:47:11
import sqlite3
from sqlite3 import Error

"""
A Python script using sqlite3 to demonstrate SQL injection protection.
This script connects to a SQLite database, creates a table,
inserts data, and queries the data safely using parameterized queries."""

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn):
    """ create a table in the SQLite database if it doesn't exist """
    try:
        c = conn.cursor()
        # Using parameterized queries to prevent SQL injection
        c.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );""")
    except Error as e:
        print(e)


def insert_user(conn, user):
    """ Insert a new user into the users table """
    sql = ''' INSERT INTO users(username,password)
              VALUES(?,?) '''
    try:
        c = conn.cursor()
        c.execute(sql, user)
        conn.commit()
        return c.lastrowid
    except Error as e:
        print(e)
        return None


def select_user(conn, username):
    "