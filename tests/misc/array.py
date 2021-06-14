def x():
    row = int(input(" input row : "))
    col = int(input(" input col: "))
    od=[]
    td=[]
    v=1

    for x in range(row):
        od.clear()
        for y in range(col):
            od.append(v)
            v += 1
        td.append(od.copy())


    seperator = col * 9 * '-'
    print (seperator)
    for x in range(row):
        s = ''
        for y in range (col):
            s = s + "{:5}".format(td[x][y]) + "   |"
        print (s)
        print (seperator)

x = [1,2 ,3,4,6]
print (x.index(7))