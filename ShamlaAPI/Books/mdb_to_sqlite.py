#! mdb_to_sqlite.py
import sys, subprocess, os
import sqlite3
from sqlite3 import Error
import time

MDB_TOOLS_DIR = r".\mdbtools-win\\"

def mdb_2_sqlite(DB_file_name):

    db_file = DB_file_name.split(".")[0]
    db_file = db_file + ".sqlite"
    os.remove(db_file)  # remove DB if exists
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    # Dump the schema for the DB
    schema = subprocess.Popen([MDB_TOOLS_DIR +"mdb-schema", "--drop-table", "--no-indexes", "--no-relations", DB_file_name, "mysql"],
                              stdout=subprocess.PIPE).communicate()[0]

    cur = conn.cursor()
    sql = 'BEGIN TRANSACTION;\n' + schema.decode('utf8') + "\nCommit"
    cur.executescript(sql)

    # Get the list of table names with "mdb-tables"
    table_names = subprocess.Popen([MDB_TOOLS_DIR +"mdb-tables", "-1", DB_file_name],
                                   stdout=subprocess.PIPE).communicate()[0]
    tables = table_names.splitlines()

    # Dump each table as a CSV file using "mdb-export",
    for table in tables:
        t= time.time()
        if table != '':
            print (f'insert into {table}')

            sql1 = subprocess.Popen([MDB_TOOLS_DIR +"mdb-export", "-I", "mysql", DB_file_name, table.decode()],
                                    stdout=subprocess.PIPE).communicate()[0]
            sql = sql1.decode('CP1256').encode('utf8')
            sql = 'BEGIN TRANSACTION;\n' + sql.decode('utf8') + "\nCommit"
            cur.executescript(sql)
            print ("\n Time Taken: %.3f sec" % (time.time() - t))
    try:
        conn.close()
    except Error as e:
        print ('Error closing conn/cursor: ', e)

mdb_2_sqlite(r"aa.mdb")