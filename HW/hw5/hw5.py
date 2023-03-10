import sqlite3

from sqlite3 import Error as error

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except:
        print(error)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except error:
        print(error)

def create_student(conn, user):
    sql = """INSERT INTO user(name, age, marks, status)
    VALUES (?, ?, ?, ?)
    """
    try:
        cursor = conn.cursor()
        conn.execute(sql, user)
        conn.commit()
    except error:
        print(error)

def read(conn):
    try:
        sql = '''SELECT * FROM user'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except error:
        print(error)

def update(conn, id, age, marks):
    sql = '''UPDATE user SET age=?, marks=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id, age, marks))
        conn.commit()
    except error:
        print(error)


sql_create = """
CREATE TABLE user(
name VARCHAR(20) NOT NULL,
age DATE,
marks DOUBLE (2,1) NOT NULL DEFAULT 0.0,
status VARCHAR(20) NOT NULL
);
"""

database = r'hw.db'

connection = create_db(database)

if connection is not None:
    print('все отлично')
    # create_table(connection, sql_create)
    # create_student(connection, ('emir', '2007-10-12', 3.9, 'student'))
    update(connection, 3, '2009-12-10', 4.5)

read(connection)