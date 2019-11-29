from pathlib import Path


def list_files(parent_folder:str):
    path = Path(parent_folder)
    for file in path.glob('*'):
        print (file)

def list_files_abs(parent_folder:str):
    path = Path(parent_folder)
    print (path.absolute())


def create_folder(folder_name:str):
# print all file
    path = Path(folder_name)
    path.mkdir()


# execute functions
list_files('.')
#list_files('c:')
#list_files_abs('e:')
#create_folder('email')