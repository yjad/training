import os

data_folder = r'C:\Yahia\Home\Yahia-Dev\Python\vulnerability\data\Qradar\QVM-August-2021'

for folder, subs, files in os.walk(data_folder):
        for f in files:
            filename, file_extension = os.path.splitext(f)
            # print (f'folder: {folder}, subs: {subs}, f:{f}, filename: {filename}')
            print (f' folder: {folder} -  f:{f}')