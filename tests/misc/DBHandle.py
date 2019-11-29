import sqlite3
from sqlite3 import Error


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

def save_list(doctors_list):
    db_file = r"D:\Yahia\Yahia\Python\training\db\vezeeta.db"
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    #finally:
        #create_connection(db_name, conn)
    sql = ''' INSERT INTO doctors(name, address, short_desc, fees, image_url, rating, no_of_visitors, waiting_time)
                  VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute('delete from doctors')
    for d in doctors_list:
        #print('from save List: ', d)
        try:
            cur.execute(sql, d)
        except Error as e:
            print ('error Inserting record: ', e)
            return
        print ('last inserted record ID: ',cur.lastrowid)
    try:
        conn.commit()
        conn.close()
    except Error as e:
        print ('Error closing conn/cursor: ', e)