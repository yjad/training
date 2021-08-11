import os
import xml.etree.ElementTree as ET 
from lxml import etree
import re
from xml_read import print_xml_sample

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
    # file_name = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\29_PACS008_2021080309241818109.XML"
    file_name = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\tttt\29_PACS002_2021080108055236720.XML"
    
    data_folder = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH"
    fexception = open (r".\out\exceptions.txt", "wt", encoding = "UTF8")
    
    conn, cursor = open_db()
    exec_db_cmd('delete from GrpHdr')
    exec_db_cmd('delete from trx')
    exec_db_cmd('delete from pacs_002_004')
    parse_pacs_file(file_name, conn, cursor, fexception)
    return 
    for folder, subs, files in os.walk(data_folder):
        for f in files:
            filename, file_extension = os.path.splitext(f)
            if file_extension.upper() != ".XML":
                continue
                
            parse_pacs_file(os.path.join(os.path.join(folder, f)), conn, cursor, fexception)
    
    conn.commit()
    close_db(cursor)
    
    fexception.close()
    
def local_name(tag_text):
    return etree.QName(tag_text).localname
    
    
def parse_pacs_file(file_name, conn, cursor, fexception):
    
    tree = ET.parse(file_name) 
    root = tree.getroot()
    print (root[0].tag)
    
    # print (file_name)
    # print_xml_sample(root,10,"trx.txt")
    
    
    ns = get_ns(root)
    pacs_type = ns[37:47]   # 004.001.01
    
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
 
    rec = load_ach_GrpHdr(pacs_type, grp_header)
    rec.update({'file_name':file_name})
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
        
        
def load_pacs_008_trx(root, conn, cursor, ns, msg_id, fexception):
        
        trans_grp_tag = "CdtTrfTxInf"
        trxs = root[0].findall(f"./{ns}{trans_grp_tag}")
        for trx in trxs:
            rec_0 = load_CdtTrfTxInf(trx, msg_id)
            # print (rec)
            rec = { 'MsgId': msg_id}
            rec.update(rec_0)
            ret_code = insert_row_dict(conn, cursor, "trx", rec)
            if ret_code == -1:
                 fexception.writelines(f"Error inserting trx record: {str(rec)}\n {50*'-'}\n")
                    
    
def load_ach_GrpHdr(pacs_type, xml_item):   
    
    rec = xml_to_dict(xml_item).get('GrpHdr')    
    SttlmMtd =  rec.get('SttlmInf')
    if SttlmMtd: SttlmMtd = SttlmMtd.get('SttlmMtd') 
    
    ClrSysId =  rec.get('SttlmInf')
    if ClrSysId: ClrSysId = ClrSysId.get('ClrSys')
    if ClrSysId:  ClrSysId = ClrSysId.get('ClrSysId', '')

    InstrPrty = rec.get('PmtTpInf')
    if InstrPrty: InstrPrty = InstrPrty.get('InstrPrty', '')
     
    ClrChanl = rec.get('PmtTpInf')
    if ClrChanl: ClrChanl = ClrChanl.get('ClrChanl', '')
     
    CtgyPurp = rec.get('PmtTpInf')
    if CtgyPurp: CtgyPurp = CtgyPurp.get('CtgyPurp', '')
    
    grp_header = {'pacs_type': pacs_type,
    'MsgId':rec.get('MsgId'),
    'CreDtTm':rec.get('CreDtTm'),
    'NbOfTxs': rec.get('NbOfTxs'),
    'TtlIntrBkSttlmAmt': rec.get('TtlIntrBkSttlmAmt'),
    # 'TtlIntrBkSttlmCcy': rec.get('TtlIntrBkSttlmAmt'),
    'IntrBkSttlmDt': rec.get('IntrBkSttlmDt'),
    'SttlmMtd': SttlmMtd,
    'ClrSysId': ClrSysId,
    'InstrPrty': InstrPrty,
    'ClrChanl': ClrChanl,
    'CtgyPurp': CtgyPurp
    }
    return grp_header

def load_CdtTrfTxInf(xml_item, msg_id):   
    
    rec = xml_to_dict(xml_item).get('CdtTrfTxInf')  
    DbtrAgtBrnchId = rec['DbtrAgt'].get('BrnchId','')
    if type(DbtrAgtBrnchId) != str: # case debitor has no branch number
        DbtrAgtBrnchId = DbtrAgtBrnchId.get('Id', '')
        
    CdtrAcctTp= rec['CdtrAcct'].get('Tp', '')
    CdtrAcctTp = CdtrAcctTp.get('Cd') if type (CdtrAcctTp) != str else ''
    Purp = rec.get('Purp', '')
    Purp = Purp.get('Cd') if type (Purp) != str else ''
    trx_rec_dict = {
    'MsgId':msg_id,
    'InstrId':rec['PmtId'].get('InstrId'),
    'EndToEndId':rec['PmtId'].get('EndToEndId'),
    'TxId':rec['PmtId'].get('TxId'),
        'IntrBkSttlmAmt':rec.get('IntrBkSttlmAmt'),
    'IntrBkSttlmCcy':'TBD',
    'ChrgBr':rec.get('ChrgBr'),
    'DbtrNm':rec['Dbtr'].get('Nm'),
    'DbtrAcctId':rec['DbtrAcct']['Id']['PrtryAcct'].get('Id'),
    'DbtrAgtBIC':rec['DbtrAgt']['FinInstnId'].get('BIC'),
    'DbtrAgtBrnchId':DbtrAgtBrnchId,
    'CdtrAgtBIC':rec['CdtrAgt']['FinInstnId'].get('BIC'),
    'CdtrAgtBrnchId':rec['CdtrAgt']['BrnchId'].get('Id'),
    'CdtrNm': rec['Cdtr'].get('Nm'),
    'CdtrAcctId': rec['CdtrAcct']['Id']['PrtryAcct'].get('Id'),
    'CdtrAcctTp': CdtrAcctTp,
    'Purp': Purp,
    'RmtInfUstrd': rec['RmtInf'].get('Ustrd')
    }
    return trx_rec_dict

def load_pacs_004_trx(root, conn, cursor, ns, msg_id, fexception):
    
    org_grp_info = xml_to_dict(root[0].find(f"./{ns}{'OrgnlGrpInf'}")).get('OrgnlGrpInf')
    # print ("---------> ",org_grp_info, "OrgnlMsgId:", org_grp_info.get('OrgnlMsgId'))
    trx_info = xml_to_dict(root[0].find(f"./{ns}{'TxInf'}")).get('TxInf')
    # print (trx_info)
    return_reason_info = xml_to_dict(root[0].find(f".//{ns}{'RtrRsnInf'}")).get('RtrRsnInf')
    # print ("----------->",return_reason_info)
    # print (return_reason_info.get('RtrRsn'))
    # rec = xml_to_dict(xml_item)
    
    trx_dict = {
    'MsgId': msg_id,
    'OrgnlMsgId': org_grp_info.get('OrgnlMsgId'),
    'OrgnlMsgNmId': org_grp_info.get('OrgnlMsgNmId'),
    'TrxRtrId': trx_info.get('RtrId'),
    'OrgnlEndToEndId': trx_info.get('OrgnlEndToEndId'),
    'OrgnlTxId': trx_info.get('OrgnlTxId'),
    'RtrdIntrBkSttlmAmt': trx_info.get('RtrdIntrBkSttlmAmt'),
    'RtrdIntrBkSttlmCcy': '', #trx_info.get('RtrdIntrBkSttlmCcy'),
    'RtrRsn': return_reason_info.get('RtrRsn').get('Prtry')
    }
    insert_row_dict(conn, cursor, "pacs_002_004", trx_dict)
    return trx_dict
    
def load_pacs_002_trx(root, conn, cursor, ns, msg_id, fexception):
    
    org_grp_info = xml_to_dict(root[0].find(f"./{ns}{'OrgnlGrpInfAndSts'}")).get('OrgnlGrpInfAndSts')
    # print ("---------> ",org_grp_info, "OrgnlMsgId:", org_grp_info.get('OrgnlMsgId'))
    trx_info = xml_to_dict(root[0].find(f"./{ns}{'TxInfAndSts'}")).get('TxInfAndSts')
    # print (trx_info)
    return_reason_info = xml_to_dict(root[0].find(f".//{ns}{'StsRsnInf'}")).get('StsRsnInf')
    # print ("----------->",return_reason_info)
    # print (return_reason_info.get('RtrRsn'))
    # rec = xml_to_dict(xml_item)
    
    trx_dict = {
    'MsgId': msg_id,
    'OrgnlMsgId': org_grp_info.get('OrgnlMsgId'),
    'OrgnlMsgNmId': org_grp_info.get('OrgnlMsgNmId'),
    'GrpSts': org_grp_info.get('GrpSts'),
    'TrxRtrId': trx_info.get('RtrId'),
    'OrgnlEndToEndId': trx_info.get('OrgnlEndToEndId'),
    'OrgnlTxId': trx_info.get('OrgnlTxId'),
    'RtrdIntrBkSttlmAmt': trx_info.get('RtrdIntrBkSttlmAmt'),
    'RtrdIntrBkSttlmCcy': '', #trx_info.get('RtrdIntrBkSttlmCcy'),
    'RtrRsn': return_reason_info.get('RtrRsn').get('Prtry')
    }
    insert_row_dict(conn, cursor, "pacs_002_004", trx_dict)
    return trx_dict
    
def load_pacs_002_001_02(root, conn, cursor, ns, msg_id, fexception):
    
    org_grp_info = xml_to_dict(root[0].find(f"./{ns}{'OrgnlGrpInfAndSts'}")).get('OrgnlGrpInfAndSts')
    # print ("---------> ",org_grp_info, "OrgnlMsgId:", org_grp_info.get('OrgnlMsgId'))
    trx_info = xml_to_dict(root[0].find(f"./{ns}{'TxInfAndSts'}")).get('TxInfAndSts')
    # print (trx_info)
    # return_reason_info = xml_to_dict(root[0].find(f".//{ns}{'StsRsnInf'}")).get('StsRsnInf')
    # print ("----------->",return_reason_info)
    # print (return_reason_info.get('RtrRsn'))
    # rec = xml_to_dict(xml_item)
    
    trx_dict = {
    'MsgId': msg_id,
    'OrgnlMsgId': org_grp_info.get('OrgnlMsgId'),
    'OrgnlMsgNmId': org_grp_info.get('OrgnlMsgNmId'),
    'GrpSts': org_grp_info.get('GrpSts'),
    
    'TrxRtrId': trx_info.get('StsId'),
    # 'OrgnlEndToEndId': trx_info.get('OrgnlEndToEndId'),
    'OrgnlTxId': trx_info.get('StsRsnInf').get('OrgnlTxId'),
    # 'RtrdIntrBkSttlmAmt': trx_info.get('RtrdIntrBkSttlmAmt'),
    # 'RtrdIntrBkSttlmCcy': '', #trx_info.get('RtrdIntrBkSttlmCcy'),
    'RtrRsn': trx_info.get('StsRsnInf').get('StsRsn').get('Prtry'),
    'AddtlStsRsnInf': trx_info.get('StsRsnInf').get('AddtlStsRsnInf')
    }
    insert_row_dict(conn, cursor, "pacs_002_004", trx_dict)
    return trx_dict
    
    
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

if __name__ == '__main__':
    
    load_ACH()
