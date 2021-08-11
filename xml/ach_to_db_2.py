import json
from DB import insert_row_dict, open_db, close_db, exec_db_cmd, query_to_list, OUT_FOLDER, \
    print_tk, clear_tk, print_query, trim, query_to_dict_list, query_to_excel
    
# rec = {'PmtId': {'InstrId': 'FT21220WVT2C', 'EndToEndId': 'FT21220WVT2C', 'TxId': 'FT21220WVT2C'}
# , 
    # 'IntrBkSttlmAmt': '75000.00', 'ChrgBr': 'SLEV', 
    # 'Dbtr': {'Nm': 'Ahmed AAAAlsayed Mohammed'}, 
    # 'DbtrAcct': {'Id': {'PrtryAcct': {'Id': 'EG130038008800000880000003160'}}}, 
    # 'DbtrAgt': {'FinInstnId': {'BIC': 'HDBKEGCAXXX'}, 'BrnchId': {'Id': '0088'}},
    # 'CdtrAgt': {'FinInstnId': {'BIC': 'CIBEEGCX'}, 'BrnchId': {'Id': '0039'}}, 
    # 'Cdtr': {'Nm': 'حامد مصطفي البسيونى'}, 
    # 'CdtrAcct': {'Id': {'PrtryAcct': {'Id': '100036556352'}}, 'Tp': {'Cd': 'CACC'}}, 
    # 'Purp': {'Cd': 'CASH'}, 
    # 'RmtInf': {'Ustrd': 'شحصى شراء موبيليات'}
    # }

def dict_to_1L_dict(rec, parent=''):
    dic = {}
    
    for L0 in rec.items():
        
        # print (L0, L0[0], type (L0))
        
        if type(L0[1]) == str:
            if parent:
                L0_dict = {parent + '.'+ L0[0] :L0[1]}
            else:
                L0_dict = {L0[0] :L0[1]}
            # print (L0_dict)
            dic.update(L0_dict)
        else:
            if parent:
                parent_s = parent + '.' + list(L0)[0] 
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
    pacs_type = ns[32:47]   # 004.001.01
    print (pacs_type)
    
    # if pacs_type == '008.001.01':
        # print ('rejection record, skip it: ', file_name, ns)
        # return 
    # print (file_name)
    print (file_name, pacs_type)
    # return 
    
    if ns:
        grp_header = root[0].find(f"./{ns}GrpHdr")
    else:
        grp_header = root.find(f"./{ns}GrpHdr")

    # print (xml_to_dict(grp_header))
    rec_org = xml_to_dict(xml_item).get('GrpHdr')
    rec = dict_to_1L_dict(rec_org)       
    rec.update({'file_name':file_name})
    create_tables(rec, "GrpHdr_auto")
    ret = insert_row_dict(conn, cursor, "GrpHdr", rec)
    if ret == -1:
        fexception.writelines(f"Error inserting GrpHdr record: {str(rec)}\n {50*'-'}\n")
    
    
    if pacs_type in ["002.001.01"]:
        load_pacs_002_trx(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    if pacs_type in ["002.001.02"]:
        load_pacs_002_001_02(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    elif pacs_type in ["004.001.01"]:
        load_pacs_004_trx(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    elif pacs_type == "008.001.01":  
        load_pacs_008_trx(root, conn, cursor, ns, rec.get('MsgId'), fexception)
    else:
        print (f"New pacs_type: {file_name} - {pacs_type}")
        
def create_tables(rec, table):
    cmd = f"CREATE TABLE IF NOT EXIST {table} ("
    
    for key in rec.keys():
        cmd = cmd + f"{key} TEXT, "
    if table == "GrpHdr_auto":
        cmd = cmd + "PRIMARY KEY("MsgId"))"
    else:
        pass
        
    exec_db_cmd(cmd)
    
        
print (json.dumps((rec), indent=4))
rec_l1 = dict_to_1L_dict(rec)
print (50*"-", json.dumps(rec_l1, indent=4))
print (rec_l1.keys())