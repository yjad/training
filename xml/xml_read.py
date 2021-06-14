import xml.etree.ElementTree as ET 
import csv

# Pass the path of the xml document 
tree = ET.parse('fullSync.xml') 

# get the parent tag 
root = tree.getroot() 

# print the root (parent) tag along with its memory location 
# print('root: ', root) 

# print the attributes of the first tag  
# r = root[0]
# print('root[0].tag:', r.tag) 
# print('root[0].attrib:', r.attrib) 
# print ('r: ', r)
# for i,s in enumerate(r):
    # print (i, s.tag, s.attrib)
# print the text contained within first subtag of the 5th tag from the parent 
# print('root[5][0].text: ', root[5][0].text) 

with open('t24Shre.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['#', 'name', 'type', 'upload/Download', 'source', 'dest'])
    for i,e in enumerate(root, start=1):
        # for k,d in e.attrib.items():
            # print (f'Key: {k}, data: {d}')
        # for i,x in enumerate(e):
            # print (i, x.tag, x.attrib)
        name = e.attrib['name']
        typ = e.attrib['type']
        source = e[2].attrib['uri']
        dest = e[3].attrib['uri'] 
        # print (i, name, typ, source, dest)
        if source[:5] == 'file:':
            upload = 'Upload'
        else:
            upload = 'Download'
        writer.writerow([i, name, typ, upload, source, dest])