import csv
# class A:
#     def __init__ (self, file_name):
#         print (file_name)
#
# class B(A):
#     print ('I am in calss B')
#
#
# x =B('file_name')

file_path = r'D:\Yahia\Yahia\Python\training\reservation\مميزة 2 uploud.csv'
try:
    csv_file = open(file_path, mode='r', newline="\n", encoding='utf-8')
except:
    print(f'Error opening file: {file_path}')

ws = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
if ws == None:
    print(f'reading csv file: {file_path}')

try:
    print (next(ws))
except:
    pass
# for r in ws:
#     print (r)