x = 'abcabcabc'
y='c'
z=[]
p=0
while True:
    try:
        if x[p] == y:
            z = z + [p]
    except IndexError:
        break
    p +=1
print (z)
exit(1)

import datetime

t= False
x = 'yahia' if t else 'no'
print (x)

link = ['link','2ndlink']
item = dict()
item['id']=100
item['repository'] = 'reText'
a = (1,2)
b = (3,4,5)
print (a+b)

print (datetime.datetime.now())

# print("INSERT OR REPLACE INTO pdf_links(link_text,link_value,book_id,repository) values(?,?,?,?)",
#       link + (item['id'], item['repository']))


