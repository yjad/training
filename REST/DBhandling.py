#! DB Handling

ERROR_OPENING_DB = -1
ERROR_READINGS_RECS = -2
ERROR_CLOSING_CONN = -3

import sqlite3
from sqlite3 import Error

DB_FILE_NAME = r".\Books\main.sqlite"
def get_categories_db(cmd):
    try:
        conn = sqlite3.connect(DB_FILE_NAME)
    except Error as e:
        print(f'error opening database: {e}')
        return None, ERROR_OPENING_DB

    try:
        categs = conn.execute(cmd)
    except Error as e:
        print ('error reading record: ', e)
        conn.close()
        return None, ERROR_READINGS_RECS

    categ_list = categs.fetchall()
    num_of_rows = categs.rowcount
    try:
        conn.close()
    except Error as e:
        print ('Error closing conn/cursor: ', e)
        return None, ERROR_CLOSING_CONN
    return categ_list, num_of_rows


def add_todo_db_record(rec):
    sql = 'INSERT INTO todo (title, desc, status) VALUES(?,?,?)'

    try:
        conn = sqlite3.connect(DB_FILE_NAME)
    except Error as e:
        print(f'error opening database: {e}')
        conn.close()
        return None, -1

    cur = conn.cursor()
    try:
        tasks = cur.execute(sql, rec)
    except Error as e:
        print ('error inserting record: ', e)
        conn.close()
        return -4

    inserted_rec_id = cur.lastrowid
    try:
        conn.commit()
        conn.close()
    except Error as e:
        print ('Error closing conn/cursor: ', e)
        return -5
    return inserted_rec_id

def update_todo_db_record(rec):

    sql = f"update todo set title = '{rec[1]}', desc = '{rec[2]}', status = '{rec[3]}' where ID = {rec[0]}"
    print (sql)
    try:
        conn = sqlite3.connect(DB_FILE_NAME)
    except Error as e:
        print(f'error opening database: {e}')
        conn.close()
        return None, -1

    cur = conn.cursor()
    try:
        tasks = cur.execute(sql)
    except Error as e:
        print ('error updating record: ', e)
        conn.close()
        return -6   # error updating rec

    if cur.rowcount == 0:
        conn.close()
        return -7   # record not found

    try:
        conn.commit()
        conn.close()
    except Error as e:
        print ('Error closing conn/cursor: ', e)
        return -5
    return 0

def delete_todo_db_record(task_id):

    sql = f"delete from todo where ID = {task_id}"
    print (sql)
    try:
        conn = sqlite3.connect(DB_FILE_NAME)
    except Error as e:
        print(f'error opening database: {e}')
        conn.close()
        return None, -1

    cur = conn.cursor()
    try:
        tasks = cur.execute(sql)
    except Error as e:
        print ('error deleting record: ', e)
        conn.close()
        return -8   # error updating rec

    no_deleted_records = cur.rowcount
    if cur.rowcount == 0:
        conn.close()
        return -7   # record not found

    try:
        conn.commit()
        conn.close()
    except Error as e:
        print ('Error closing conn/cursor: ', e)
        return -5
    return no_deleted_records

"""
rec = [8,'updated title', 'updated desc', 'Done']
status = delete_todo_db_record(8)
print (status)
"""