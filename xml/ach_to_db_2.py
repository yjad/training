import os, json
from sqlite3.dbapi2 import Cursor
import xml.etree.ElementTree as ET 
from tkinter import filedialog
from DB import exec_query, insert_row_dict, open_db, close_db, exec_db_cmd, query_to_list, OUT_FOLDER, \
    print_tk, clear_tk, print_query, trim, query_to_dict_list, query_to_excel
from ach_to_db import get_ns, xml_to_dict, local_name


def xml_to_sqlite(file_name):

    print (file_name)
    tree = ET.parse(file_name) 
    root = tree.getroot()
    f = open (".\\out\\parse_xml.txt", 'w', encoding = "UTF8")
    conn, cursor = open_db()

    for L0 in root:
        
        f.writelines (f"====== L0: {local_name(L0.tag)} {len(L0)} ===============\n")
        for L1 in L0:
            L1_rec = dict_to_1L_dict(xml_to_dict(L1))
            if L1_rec: 
                if local_name(L1.tag) == "GrpHdr":
                    table_name = 'GrpHdr'
                    MsgId = L1_rec.get('GrpHdr_MsgId')
                    rec = {'pacsId':local_name(root[0].tag), "filename":file_name}
                    rec.update(L1_rec)
                    
                    insert_rec(conn, cursor, rec, table_name)
                else:
                    table_name = local_name(L0.tag).replace('.', '_')
                    L1_rec.update({'MsgId':MsgId})
                    insert_rec(conn, cursor, L1_rec, table_name)
                
                f.writelines (f"L1: {local_name(L1.tag)}, {len(L1)}, {20* '-'}, \n, {json.dumps(L1_rec, indent=4)}\n")

    conn.commit()
    close_db(cursor)
    f.close()


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


def parse_pacs_file(file_name, conn, cursor, fexception):
    
    tree = ET.parse(file_name) 
    root = tree.getroot()
    
    # print (file_name)
    # print_xml_sample(root,10,"trx.txt")
        
    ns = get_ns(root)
    pacs_type = ns[32:47]   # pacs.004.001.01
    # print (pacs_type)
    
    # if pacs_type == '008.001.01':
        # print ('rejection record, skip it: ', file_name, ns)
        # return 
    # print (file_name)
    # print (file_name, pacs_type)
    # return 
    
    if ns:
        grp_header = root[0].find(f"./{ns}GrpHdr")
    else:
        grp_header = root.find(f"./{ns}GrpHdr")

    # print (xml_to_dict(grp_header))
    rec_org = xml_to_dict(grp_header).get('GrpHdr')
    rec = dict_to_1L_dict(rec_org)       
    rec.update({'file_name':file_name})
    create_tables(rec, "GrpHdr_auto")
    ret = insert_row_dict(conn, cursor, "GrpHdr_auto", rec)
    if ret == -1:
        fexception.writelines(f"Error inserting GrpHdr record: {str(rec)}\n {50*'-'}\n")
    
    
    # if pacs_type in ["002.001.01"]:
    #     load_pacs_002_trx(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    # if pacs_type in ["002.001.02"]:
    #     load_pacs_002_001_02(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    # elif pacs_type in ["004.001.01"]:
    #     load_pacs_004_trx(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    # elif pacs_type == "008.001.01":  
    #     load_pacs_008_trx(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    # else:
    #     print (f"New pacs_type: {file_name} - {pacs_type}")

def table_exists(table_name, cursor):
    cmd  = f"SELECT 1 FROM sqlite_master WHERE type = 'table' AND name= '{table_name}'"
    row = exec_query(cursor, cmd)
    return len(row) # new table

def insert_rec(conn, cursor, rec, table):
    
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


def load_ACH_folder():   
    # clear_tk()
    # data_folder = filedialog.askdirectory(initialdir=".", title="select data folder", mustexist =True)
    # if not data_folder:
    #     return  # no files selected

    
    # file_name = r"C:\Yahia\HDB\HDB-CBP\3- Execution\Interfaces\IRDs\ACH\0002\booking\ACH sample\29_4003076817_BOOKING_8034_1.xml"
    # file_name = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\29_PACS008_2021080309241818109.XML"
    # file_name = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\29_PACS008_2021080309241818109.XML"
    # file_name = r"C:\Users\Yahia\Documents\ACH sample\29_4003076817_BOOKING_8034_1.xml"
    
    # data_folder = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH"
    data_folder = r"C:\Yahia\Python\src\HDB\training\xml\ACH\tttt"
    fexception = open (r".\out\exceptions.txt", "wt", encoding = "UTF8")
    
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
    
    # parse_xml(file_name)
    # return

    # parse_pacs_file(file_name, conn, cursor, fexception)
    # return 
    for folder, subs, files in os.walk(data_folder):
        for f in files:
            filename, file_extension = os.path.splitext(f)
            if file_extension.upper() != ".XML":
                continue
                
            # parse_pacs_file(os.path.join(os.path.join(folder, f)), conn, cursor, fexception)
            xml_to_sqlite(os.path.join(os.path.join(folder, f)))
    
    
    # fexception.close()
        
# print (json.dumps((rec), indent=4))
# rec_l1 = dict_to_1L_dict(rec)
# print (50*"-", json.dumps(rec_l1, indent=4))
# print (rec_l1.keys())

if __name__ == '__main__':
    load_ACH_folder()