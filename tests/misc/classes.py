import csv

class A:
    a= 'from A'


class B(A):
    print ('from B')
    a= 'from B'
    b = 'from B'

class X(A):
    a = 'from X'
    print (a)
    x='from X'

class Y(X,B):
    def __init__(self):
        self.a = 'a from Y'
        self.b = 'b from Y'
        self.x = 'x from Y'


r = Y()
print (r.a, r.b, r.x)

csv_file = open(r'E:\Yahia\python\training\reservation\data\x.csv', mode='r', newline="\n", encoding='utf-8')
csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for ws in csv_reader:
    print (ws)
    for f in ws:
        v = f
        print(f, ': ' ,type(v))
