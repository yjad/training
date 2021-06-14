import sqlite3
from sqlite3 import Error
import datetime


def create_connection(db_file, conn):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     #if conn:
    #     #   conn.close()


# if __name__ == '__main__':
#     create_connection(r"D:\Yahia\Yahia\Python\training\db\vezeeta.db")

def save_list():
    db_file = r"D:\Yahia\Yahia\Python\training\db\DateTime.sqlite"
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    #finally:
        #create_connection(db_name, conn)
    d = {'id': 132430,
         'date_added': '2019-05-24',
         'view_count': 4662,
         'time_stamp'
         'tags': '',
         'rar_link': 'http://shamela.ws/books/1324/132429.rar',
         'pdf_link': 'http://waqfeya.com/book.php?bid=11070',
         'online_link': 'http://shamela.ws/browse.php/book-132429',
         'epub_link': 'http://d.shamela.ws/epubs/132/132429.epub'}

    cursor = conn.cursor()
    # cursor.execute(f'CREATE TABLE IF NOT EXISTS "TABLE_SHAMELA_OFFICIAL"'
    #                '(id INTEGER NOT NULL PRIMARY KEY,'
    #                'time_stamp TEXT ,'
    #                'view_count INTEGER,'
    #                'date_added TEXT,'
    #                'tags TEXT,'
    #                'rar_link TEXT,'
    #                'pdf_link TEXT,'
    #                'online_link TEXT,'
    #                'epub_link TEXT)')
    cursor.execute("INSERT INTO " + "TABLE_SHAMELA_OFFICIAL" + " VALUES("
                                                        ":id,"
                                                        ":DATETIME('now'), "
                                                        ":view_count,"
                                                        ":date_added,"
                                                        ":rar_link, "
                                                        ":pdf_link, "
                                                        ":tags,"
                                                        ":online_link, " 
                                                        ":epub_link"
                                                        ")"
                   , dict(d))
    #cur = conn.cursor()
    # try:
    #     cur.execute(sql)
    # except Error as e:
    #     print ('Error executing insert: ', e, sql)

    #cur.execute('insert into ')
    conn.commit()
    conn.close()
    # for d in doctors_list:
    #     #print('from save List: ', d)
    #     try:
    #         cur.execute(sql, d)
    #     except Error as e:
    #         print ('error Inserting record: ', e)
    #         return
    #     print ('last inserted record ID: ',cur.lastrowid)
    # try:
    #     conn.commit()
    #     conn.close()
    # except Error as e:
    #     print ('Error closing conn/cursor: ', e)
save_list()