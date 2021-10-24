from xml.etree.ElementTree import iterparse
#from cElementTree import iterparse
import pandas as pd

# file_path = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\tttt\29_PACS002_2021080108055236720.XML"
# file_path = r"C:\Yahia\HDB\HDB-CBP\3- Execution\Interfaces\IRDs\ACH\0002\booking\ACH sample\29_4003076817_BOOKING_8034_1.xml"
file_path = r"C:\Yahia\Home\Yahia-Dev\Python\training\xml\ACH\8_8_2021\29_PACS008_20160802191205682107.xml"
dict_list = []

for event, elem in iterparse(file_path, events=("start","end",)):
    print (f"{event}, tag: {elem.tag}, text: {elem.text}, aatrib: {elem.attrib}")
    # if elem.tag == "row":
    #     dict_list.append({'rowId': elem.attrib['Id'],
    #                       'UserId': elem.attrib['UserId'],
    #                       'Name': elem.attrib['Name'],
    #                       'Date': elem.attrib['Date'],
    #                       'Class': elem.attrib['Class'],
    #                       'TagBased': elem.attrib['TagBased']})

    #     # dict_list.append(elem.attrib)      # ALTERNATIVELY, PARSE ALL ATTRIBUTES

    elem.clear()

df = pd.DataFrame(dict_list)