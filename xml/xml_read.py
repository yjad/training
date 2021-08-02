import xml.etree.ElementTree as ET 
from lxml import etree
import csv

def parse_fullSync():
# Pass the path of the xml document 
    tree = ET.parse('fullSync.xml') 
    root = tree.getroot()

    print_xml_sample(root.findall("./Profile"))
    # print_sample(root, 3)
   

    # for country in root.findall('country'):

def local_name(tag_text):
    return etree.QName(tag_text).localname

def print_xml_sample_level(elmt, level, seq , sample_count=1):
    
    if seq >= sample_count : return
    attrib = f", attrib: {elmt.attrib}" if elmt.attrib else ""
    text = f", text: {elmt.text}" if elmt.text else ""
    print (level * '\t', f"{seq}- L{level}: tag: {local_name(elmt.tag)}{attrib}{text}")
    # print (level * '\t', f"{seq}- L{level}: tag: {local_name(elmt.tag)}, attrib: {elmt.attrib}, text: {elmt.text}")
    if len(elmt) > 0:
        for i,sub in enumerate(elmt):
            if i > sample_count: break
            print_xml_sample_level(sub, level+1, i , sample_count)

def print_xml_sample(root, sample_count=1):
    sample_count = sample_count -1
    for i, child in enumerate(root):
        if i> sample_count : break
        print_xml_sample_level(child, 0, i , sample_count)

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


def parse_pacs():
    file_name = r"C:\Yahia\HDB\HDB-CBP\3- Execution\Interfaces\IRDs\ACH\0002\booking\ACH sample\29_4003076817_BOOKING_8034_1.xml"
    # tree = ET.parse("29_PACS008_20160802191205682107.xml") 
    tree = ET.parse(file_name) 

    f_keys = open ('trx_keys.txt', 'w')
    root = tree.getroot()
    print_xml_sample(root,10)
    keys_writen = True
    with open("trx.txt", 'wt', encoding='utf8') as f:   
        for e in root[0]:      # transactions
            trx_dict = xml_to_dict(e)
            f.writelines(str(trx_dict)+"\n")
            if trx_dict.get("GrpHdr"):
                f_keys.writelines(str(trx_dict.keys()) + "\n")
            elif not keys_writen:
                f_keys.writelines(str(trx_dict.keys()) + "\n")
                keys_writen = True
            else:
                f_keys.writelines(str(trx_dict.keys()) + "\n")

    f_keys.close()
    
    return

def xml_to_dict(element):
    dic = {local_name(element.tag):element.text}
    for L0 in element:
        if type(L0.text) == str:
            dic.update ({local_name(L0.tag):L0.text})
        else:
            for L1 in L0:
                if type(L1.text) == str:
                    dic.update ({local_name(L1.tag):L1.text})
                else:
                    for L2 in L1:
                        if type(L2.text) == str:
                            dic.update ({local_name(L2.tag):L2.text})
                        else:
                            for L3 in L2:
                                if type(L3.text) == str:
                                    dic.update ({local_name(L3.tag):L3.text})
                                else:
                                    for L4 in L3:
                                        if type(L4.text) == str:
                                            dic.update ({local_name(L4.tag):L4.text})
                                        else:
                                            print (L4.tag, L4.text) # for more than 4 levels, print 
    return dic

    
if __name__ == '__main__':
    # parse_fullSync()
    parse_pacs()