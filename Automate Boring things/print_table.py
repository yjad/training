#! print_table

def print_table():

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

    rows = 3
    columns= len(tableData[0])

    max_len = 0
    for i in range(rows):
        for j in range (columns):
            if len(tableData[i][j]) > max_len:
                max_len = len(tableData[i][j])
    sep = '-' * (((max_len +1 ) * columns) + 2)
    for i in range(rows):
        row_text = '| '
        print (sep)
        for j in range (columns):
            row_text = row_text + tableData[i][j].rjust(max_len) + '|'
        print (row_text)
    print(sep)


