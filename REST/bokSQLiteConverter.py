import pyodbc
import os
import rarfile


# file = rarfile.RarFile('./36097.rar')
# book_name=file.namelist()[0]
# file.extractall()
# os.rename(book_name, '36097.mdb')
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=.\36097.mdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
for table_info in crsr.tables(tableType='TABLE'):
    print(table_info.table_name)