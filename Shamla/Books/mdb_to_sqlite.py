#!
# python -m pip install pyodbc --user
def arabic_code_page(instr):
    code_page_720=[0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x00EA,0x00EB,0x0,0x00EF,0x00EE,0x0,0x0,0x0,
                   0x0,0x651,0x652,0x00F4,0x00A4,0x640,0x00FB,0x00F9,0x621,0x622,0x623,0x624,0x00A3,0x65,0x626,0x627,
                   0x628,0x629,0x062A,0x062B,0x062C,0x062D,0x062E,0x062F,0x630,0x631,0x632,0x633,0x634,0x635,0x00AB,0x00BB,
                   0x2591,0x2592,0x2593,0x2502,0x2524,0x2561,0x2562,0x2556,0x2555,0x2563,0x2551,0x2557,0x255D,0x255C,0x255B,0x2510,
                   0x2514,0x2534,0x252C,0x251C,0x2500,0x253C,0x255E,0x255F,0x255A,0x2554,0x2569,0x2566,0x2560,0x550,0x256C,0x2567,
                   0x2568,0x2564,0x2565,0x2559,0x2558,0x2552,0x2553,0x256B,0x256A,0x2518,0x250C,0x2588,0x2584,0x258C,0x2590,0x2580,
                   0x636,0x637,0x638,0x639,0x063A,0x641,0x0B5,0x642,0x643,0x644,0x645,0x646,0x647,0x648,0x649,0x064A,
                   0x2261,0x064B,0x064C,0x064D,0x064E,0x064F,0x650,0x2248,0x00B0,0x2219,0x00B7,0x221A,0x207F,0x00B2,0x25A0,0x00A]
    outstr = ""
    for c in instr:
        if c < 128:
            outstr = outstr + chr(c)
        else:
            outstr = outstr + chr(code_page_720[c-128])
    return outstr

def test_1():
    import csv, pyodbc

    # set up some constants
    MDB = r'D:\Yahia\Yahia\Python\training\Shamla\Books\أول مرة أتدبر القرآن.bok'
    #DRV = '{Microsoft Access Driver (*.mdb)}'
    DRV = 'Microsoft Access Driver (*.mdb)'
    PWD = ''

    # connect to db
    con = pyodbc.connect(f'DRIVER={DRV};DBQ={MDB};PWD={PWD}')
    cur = con.cursor()

    # run a query and get the results
    SQL = 'SELECT * FROM mytable;' # your query goes here
    rows = cur.execute(SQL).fetchall()
    cur.close()
    con.close()

    # you could change the mode from 'w' to 'a' (append) for any subsequent queries
    with open('mytable.csv', 'wb') as fou:
        csv_writer = csv.writer(fou) # default field-delimiter is ","
        csv_writer.writerows(rows)


#!/usr/bin/env python
#
# AccessDump.py
# A simple script to dump the contents of a Microsoft Access Database.
# It depends upon the mdbtools suite:
#   http://sourceforge.net/projects/mdbtools/
def test_2():
    import sys, subprocess, os

    #DATABASE = sys.argv[1]
    DATABASE = r"أول مرة أتدبر القرآن.bok"
    MDB_TOOLS_DIR=r"D:\Yahia\Yahia\Python\mdbtools-win\\"


    # Dump the schema for the DB
    #sys.stdout = open('log.txt', 'w+')
    sql_file = open('log.txt', 'w+b')
    #subprocess.call([MDB_TOOLS_DIR+"mdb-schema", DATABASE, "mysql"])
    schema = subprocess.Popen([MDB_TOOLS_DIR+"mdb-schema", DATABASE, "mysql"],stdout=subprocess.PIPE).communicate()[0]
    #sql_file.write (schema.decode('utf8'))
    sql_file.write (schema)

    # Get the list of table names with "mdb-tables"
    table_names = subprocess.Popen([MDB_TOOLS_DIR+"mdb-tables", "-1", DATABASE],
                                   stdout=subprocess.PIPE).communicate()[0]
    tables = table_names.splitlines()
    #print (tables)



    sql_file.write ("BEGIN;".encode()) # start a transaction, speeds things up when importing
    #sys.stdout.flush()

    # Dump each table as a CSV file using "mdb-export",
    # converting " " in table names to "_" for the CSV filenames.
    for table in tables:
        if table != '':
            #sql1 = subprocess.Popen([MDB_TOOLS_DIR+"MDBICONV=",'"CP1252"', "mdb-export", "-I",  "mysql", "-b", "octal", DATABASE, table.decode()],
            sql1 = subprocess.Popen([MDB_TOOLS_DIR+"mdb-export", "-I",  "mysql", DATABASE, table.decode()],
                            stdout=subprocess.PIPE).communicate()[0]
            #sql2 = arabic_code_page(sql1)
            #sql2 = sql1.decode('iso8859_6', 'ignore')
            sql2 = sql1.decode('utf8', "ignore")
            #print (sql1.decode('utf8', "ignore"))

            sql_file.write (sql2.encode())
            #sql_file.write (sql2.encode('utf8', "ignore"))
    sql_file.write ("COMMIT;".encode()) # end the transaction
    #sys.stdout.flush()

    #sys.stdout.close()
    sql_file.close()

def test_3():
    from poster.encode import multipart_encode
    from poster.streaminghttp import register_openers
    import urllib2

    # Register the streaming http handlers with urllib2
    register_openers()

    # Use multipart encoding for the input files
    datagen, headers = multipart_encode({'files[]': open('example.mdb', 'rb')})

    # Create the request object
    request = urllib2.Request('https://www.rebasedata.com/api/v1/convert', datagen, headers)

    # Do the request and get the response
    # Here the MDB file gets converted to CSV
    response = urllib2.urlopen(request)

    # Check if an error came back
    if response.info().getheader('Content-Type') == 'application/json':
        print
        response.read()
        sys.exit(1)

    # Write the response to /tmp/output.zip
    with open('/tmp/output.zip', 'wb') as local_file:
        local_file.write(response.read())

    print
    ('Conversion result successfully written to /tmp/output.zip!')


def m_yahia():
    import pyodbc
    #import os
    #import rarfile

    # file = rarfile.RarFile('./36097.rar')
    # book_name=file.namelist()[0]
    # file.extractall()
    # os.rename(book_name, '36097.mdb')
    sources = pyodbc.dataSources()
    keys = sources.keys()
    for key in keys:
        print (key)
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=.\Books\4512.mdb;'
    conn_str = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=.\Books\4512.mdb;'
        #r'DRIVER={MS Access Daatbase}; DBQ=.\Books\4512.mdb;'
    )
    cnxn = pyodbc.connect(conn_str)
    crsr = cnxn.cursor()
    for table_info in crsr.tables(tableType='TABLE'):
        print(table_info.table_name)

#m_yahia()
test_2()