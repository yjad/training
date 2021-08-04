import enum
import xml.etree.ElementTree as ET 
from lxml import etree
import re
import csv

def parse_fullSync():
    # Pass the path of the xml document 
    tree = ET.parse('fullSync.xml') 
    root = tree.getroot()

    print_xml_sample(root.findall("./Profile"))
    # print_sample(root, 3)
   

    # for country in root.findall('country'):




def print_xml_sample(root, sample_count=1, file_name = None):
    def print_xml_sample_level(elmt, level, seq , sample_count=1, fp=None):
        if seq >= sample_count : return
        attrib = f", attrib: {elmt.attrib}" if elmt.attrib else ""
        text = f", text: {elmt.text}" if elmt.text else ""
        line = level * '\t' + f"{seq}- L{level}: tag: {local_name(elmt.tag)}{attrib}{text}"
        if fp:
            fp.writelines(line + "\n")
        else:
            print (line)
            # print (level * '\t', f"{seq}- L{level}: tag: {local_name(elmt.tag)}{attrib}{text}")
        
        if len(elmt) > 0:
            for i,sub in enumerate(elmt):
                if i >= sample_count: break
                print_xml_sample_level(sub, level+1, i , sample_count, fp)  # recursive


    sample_count = sample_count 
    if file_name:
        f = open(file_name, 'w', encoding='utf8')
    else:
        f = None
    for i, child in enumerate(root):
        if i>= sample_count : break
        print_xml_sample_level(child, 0, i , sample_count, f)

    if file_name: f.close()


def print_xml_sample_0(root, sample_count=1):
    sample_count = sample_count -1
    
    for i, child in enumerate(root):
        if i> sample_count : break
       
        print (f"{i} - L0: tag: {local_name(child.tag)}, attrib: {child.attrib}, text: {child.text}")
        if len(child) > 0:
            for j, l1 in enumerate(child):
                if j> sample_count : break
                print (f"\t {j}- L1: tag: {local_name(l1.tag)}, attrib: {l1.attrib}, text: {l1.text}")
                # print (l1.tag.keys())
                if len (l1) > 0:    # go into next level
                    for k,l2 in enumerate(l1):
                        if k> sample_count : break
                        print (f"\t\t {k}- L2: tag: {local_name(l2.tag)}, attrib: {l2.attrib}, text: {l2.text}")
                        # print (f"\t\t  tag - keys: {l2.keys()}")
                        if len (l1) > 0:    # go into next level
                            for m,l3 in enumerate(l2):
                                if m> sample_count : break
                                print (f"\t\t\t {m}- L3: tag: {local_name(l3.tag)}, attrib: {l3.attrib}, text: {l3.text}")


def local_name(tag_text):
    return etree.QName(tag_text).localname

def get_ns(root): 
    ns = re.match(r'{.*}', root.tag)
    if ns:
        return ns.group(0)
    else:
        print ("file has no NameSpace")
        return ''

def parse_pacs():
    # file_name = r"C:\Yahia\HDB\HDB-CBP\3- Execution\Interfaces\IRDs\ACH\0002\booking\ACH sample\29_4003076817_BOOKING_8034_1.xml"
    file_name = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\29_PACS008_2021080309241818109.XML"
    # file_name  = "29_PACS008_20160802191205682107.xml"
    tree = ET.parse(file_name) 

    root = tree.getroot()
    # print (root.tag)
    # print_xml_sample(root,3)
    print_xml_sample(root,999,"trx.txt")
    ns = get_ns(root)
        
    # print ("ns: ", ns)
    if ns:
        grp_header = root[0].find(f"./{ns}GrpHdr")
    else:
        grp_header = root.find(f"./{ns}GrpHdr")

    print ("GrpHdr", xml_to_dict(grp_header))
    # trans_grp_tag = "PmtTx"
    trans_grp_tag = "CdtTrfTxInf"
    one_trx = root[0].find(f"./{ns}{trans_grp_tag}")
    print ("CdtTrfTxInf", xml_to_dict(one_trx))
    # trans_grp_tag = "CdtTrf"
    trxs = root[0].findall(f"./{ns}{trans_grp_tag}")
    # 
    # print (("CdtTrfTxInf", xml_to_dict(trx)) for trx in trxs)
    for trx in trxs:
        dic = xml_to_dict(trx)
        print (dic, "\n","\n ----------------------")

    
    # print ("CdtTrfTxInf", xml_to_dict(trxs[0]))
    # print ("CdtTrfTxInf", xml_to_dict(trxs))
    # xml_to_dict(root)

    return

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

# def xml_to_dict_00(element):    # not used
#     if type(element) == list:
#         print ("Error - use One Element at a time")
#         return None 
#     dic = xml_to_dict(element)
#     return dic


# def xml_to_dict_0(element):
#     dic = {local_name(element.tag):element.text}
#     for L0 in element:
#         if type(L0.text) == str:
#             dic.update ({local_name(L0.tag):L0.text})
#         else:
#             for L1 in L0:
#                 if type(L1.text) == str:
#                     dic.update ({local_name(L1.tag):L1.text})
#                 else:
#                     for L2 in L1:
#                         if type(L2.text) == str:
#                             dic.update ({local_name(L2.tag):L2.text})
#                         else:
#                             for L3 in L2:
#                                 if type(L3.text) == str:
#                                     dic.update ({local_name(L3.tag):L3.text})
#                                 else:
#                                     for L4 in L3:
#                                         if type(L4.text) == str:
#                                             dic.update ({local_name(L4.tag):L4.text})
#                                         else:
#                                             print (L4.tag, L4.text) # for more than 4 levels, print 
#     return dic

    
if __name__ == '__main__':
    # parse_fullSync()
    parse_pacs()