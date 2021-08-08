import os
import xml.etree.ElementTree as ET 
from lxml import etree
import re

from DB import insert_row_dict, open_db, close_db, exec_db_cmd, query_to_list, OUT_FOLDER, \
    print_tk, clear_tk, print_query, trim, query_to_dict_list, query_to_excel

def get_ns(root): 
    ns = re.match(r'{.*}', root.tag)
    if ns:
        return ns.group(0)
    else:
        print ("file has no NameSpace")
        return ''
        
def load_ACH():   
    # clear_tk()
    # file_path = filedialog.askopenfilename(title="Select file",multiple=False,
                                           # filetypes=(("Excel files", "*,xlsx"), ("Excel files", "*.xlsx")))
    # if not file_path:
        # return  # no files selected

    
    # file_name = r"C:\Yahia\HDB\HDB-CBP\3- Execution\Interfaces\IRDs\ACH\0002\booking\ACH sample\29_4003076817_BOOKING_8034_1.xml"
    # file_name = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\29_PACS008_2021080309241818109.XML"
    file_name = r"C:\Yahia\Python\src\HDB\training\xml\ACH\29_PACS008_2021080309241818109.XML"
    parse_pacs_file(file_name)
    

def local_name(tag_text):
    return etree.QName(tag_text).localname
    
    
def parse_pacs_file(file_name):
    
    tree = ET.parse(file_name) 

    root = tree.getroot()
    conn, cursor = open_db()
    
    ns = get_ns(root)
      
    if ns:
        grp_header = root[0].find(f"./{ns}GrpHdr")
    else:
        grp_header = root.find(f"./{ns}GrpHdr")

    # print (xml_to_dict(grp_header))
    exec_db_cmd('delete from GrpHdr')
    exec_db_cmd('delete from trx')
    rec = load_ach_GrpHdr(grp_header)

    insert_row_dict(conn, cursor, "GrpHdr", rec)

    msg_id = rec.get('MsgId')
    trans_grp_tag = "CdtTrfTxInf"
    trxs = root[0].findall(f"./{ns}{trans_grp_tag}")
    for trx in trxs:
        rec_0 = load_CdtTrfTxInf(trx, msg_id)
        print (rec)
        rec = { 'MsgId': msg_id}
        rec.update(rec_0)
        insert_row_dict(conn, cursor, "trx", rec)
                

    conn.commit()
    close_db(cursor)
    
    
def load_ach_GrpHdr(xml_item):   
    
    rec = xml_to_dict(xml_item).get('GrpHdr')    
    grp_header = {'MsgId':rec.get('MsgId'),
    'CreDtTm':rec.get('CreDtTm'),
    'NbOfTxs': rec.get('NbOfTxs'),
    'TtlIntrBkSttlmAmt': rec.get('TtlIntrBkSttlmAmt'),
    # 'TtlIntrBkSttlmCcy': rec.get('TtlIntrBkSttlmAmt'),
    'IntrBkSttlmDt': rec.get('IntrBkSttlmDt'),
    'SttlmMtd': rec.get('SttlmInf').get('SttlmMtd'),
    'ClrSysId': rec['SttlmInf']['ClrSys']['ClrSysId'],
    'InstrPrty': rec.get('PmtTpInf').get('InstrPrty'),
    'ClrChanl': rec.get('PmtTpInf').get('ClrChanl'),
    'CtgyPurp': rec.get('PmtTpInf').get('CtgyPurp')
    }
    return grp_header

def load_CdtTrfTxInf(xml_item, msg_id):   
    
    rec = xml_to_dict(xml_item).get('CdtTrfTxInf')  
    trx_rec_dict = {
    'MsgId':msg_id,
    'InstrId':rec['PmtId'].get('InstrId'),
    'EndToEndId':rec['PmtId'].get('EndToEndId'),
    'IntrBkSttlmAmt':rec.get('IntrBkSttlmAmt'),
    'IntrBkSttlmCcy':'TBD',
    'ChrgBr':rec.get('ChrgBr'),
    'DbtrNm':rec['Dbtr'].get('Nm'),
    'DbtrAcctId':rec['DbtrAcct']['Id']['PrtryAcct'].get('Id'),
    'DbtrAgtBIC':rec['DbtrAgt']['FinInstnId'].get('BIC'),
    'CdtrAgtBrnchId':rec['DbtrAgt']['BrnchId'].get('Id'),
    'CdtrNm': rec['Cdtr'].get('Nm'),
    'CdtrAcctId': rec['CdtrAcct']['Id']['PrtryAcct'].get('Id'),
    'CdtrAcctTp': rec['CdtrAcct']['Tp'].get('Cd'),
    'Purp': rec['Purp'].get('Cd'),
    'RmtInfUstrd': rec['RmtInf'].get('Ustrd')
    }
    return trx_rec_dict

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
            if dic.get(t):  # key alreay exist
                for i in range(100):
                    if not dic.get(f"{t}_{i}"):
                        dic.update ({f"{t}_{i}":L0.text})
                        break
            else:
                dic.update({t:L0.text})
        else:
            # print ("sub -->", L0)
            dic_sub = xml_to_dict(L0)      # recursive
            dic.update(dic_sub)

    return {local_name(element.tag):dic}
    
if __name__ == '__main__':
    
    load_ACH()
