import os, json
from sqlite3.dbapi2 import Cursor
import xml.etree.ElementTree as ET 
from lxml import etree
import re
from tkinter import filedialog
from DB import exec_query, insert_row_dict, open_db, close_db, exec_db_cmd, query_to_list, OUT_FOLDER, \
    print_tk, clear_tk, print_query, trim, query_to_dict_list, query_to_excel


def load_ACH_folder():   
    # clear_tk()
    data_folder = filedialog.askdirectory(initialdir=".", title="select data folder", mustexist =True)
    if not data_folder:
        return  # no files selected

    # data_folder = r"C:\Yahia\Python\src\HDB\training\xml\ACH\tttt"

    _, cursor = open_db()

    if table_exists("GrpHdr", cursor) > 0:
        exec_db_cmd('delete from GrpHdr')
    # exec_db_cmd('delete from trx')
    if table_exists("pacs_008_001_01", cursor) > 0: 
        exec_db_cmd('delete from pacs_008_001_01')
    if table_exists("pacs_002_001_02", cursor) > 0: 
        exec_db_cmd('delete from pacs_002_001_02')
    if table_exists("pacs_004_001_01", cursor) > 0:
        exec_db_cmd('delete from pacs_004_001_01')

    close_db(cursor)
    
    for folder, subs, files in os.walk(data_folder):
        for f in files:
            filename, file_extension = os.path.splitext(f)
            if file_extension.upper() != ".XML":
                continue
            xml_to_sqlite(os.path.join(os.path.join(folder, f)))

def xml_to_sqlite(file_name):

    print (file_name)
    tree = ET.parse(file_name) 
    root = tree.getroot()
    # f = open (".\\out\\parse_xml.txt", 'w', encoding = "UTF8")
    conn, cursor = open_db()

    for i,L0 in enumerate(root):
        
        # f.writelines (f"====== L0: {local_name(L0.tag)} {len(L0)} ===============\n")
        print (f"{i} - len(L0): {len(L0)}, {local_name(L0.tag)}")
        for L1 in L0:
            L1_rec = dict_to_1L_dict(xml_to_dict(L1))
           
            if L1_rec: 
                if local_name(L1.tag) == "GrpHdr":
                    table_name = 'GrpHdr'
                    MsgId = L1_rec.get('GrpHdr_MsgId')
                    rec = {'pacsId':local_name(root[0].tag), "filename":file_name}
                    rec.update(L1_rec)
                    insert_db_rec(conn, cursor, rec, table_name)
                else:
                    table_name = local_name(L0.tag).replace('.', '_')
                    L1_rec.update({'MsgId':MsgId})
                    insert_db_rec(conn, cursor, L1_rec, table_name)
                conn.commit()
                # f.writelines (f"L1: {local_name(L1.tag)}, {len(L1)}, {20* '-'}, \n, {json.dumps(L1_rec, indent=4)}\n")

    
    close_db(cursor)
    # f.close()


def table_exists(table_name, cursor):
    cmd  = f"SELECT 1 FROM sqlite_master WHERE type = 'table' AND name= '{table_name}'"
    row = exec_query(cursor, cmd)
    return len(row) # new table


def insert_db_rec(conn, cursor, rec, table):
    
    if table_exists(table, cursor) == 0 : # new table
        cmd = f"CREATE TABLE IF NOT EXISTS {table} ( {' TEXT,'.join(rec.keys())} )"
        # print (cmd)
        exec_db_cmd(cmd)
    else:
        check_col_names(rec, table, conn, cursor)

    insert_row_dict(conn, cursor, table, rec)


def check_col_names(rec, table, conn, cursor):
    get_column_names = conn.execute(f"SELECT * FROM {table} LIMIT 1")
    col_names = [c[0] for c in get_column_names.description]
    for key in rec.keys():
        if key not in col_names:
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {key}")
            conn.commit()

def get_ns(root): 
    ns = re.match(r'{.*}', root.tag)
    if ns:
        return ns.group(0)
    else:
        print ("file has no NameSpace")
        return ''
        
def local_name(tag_text):
    return etree.QName(tag_text).localname


def dict_to_1L_dict(rec, parent=''):
    dic = {}
    
    for L0 in rec.items():
        
        # print (L0, L0[0], type (L0))
        
        if type(L0[1]) == str:
            if parent:
                L0_dict = {parent + '_'+ L0[0] :L0[1]}
            else:
                L0_dict = {L0[0] :L0[1]}
            # print (L0_dict)
            dic.update(L0_dict)
        else:
            if parent:
                parent_s = parent + '_' + list(L0)[0] 
            else:
                parent_s = list(L0)[0]
            dic_sub = dict_to_1L_dict(L0[1], parent_s)      # recursive
            
            dic.update(dic_sub)
            # print ("-----------", dic)
    return dic
    
    
def xml_to_dict(element):

    if type(element) == list:
        print ("Error - use One Element at a time")
        return None 
    elif element is None:
        print ("Error - element is None")
        return None

    dic = {}
    for L0 in element:
        # print ("element->:", L0)
        if type(L0.text) == str:
            t = local_name(L0.tag)
            dic.update({t:L0.text})
        else:
            dic_sub = xml_to_dict(L0)      # recursive
            dic.update(dic_sub)

    return {local_name(element.tag):dic}
    
    
if __name__ == '__main__':
    load_ACH_folder()