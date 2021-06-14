import tkinter 
from tkinter import filedialog


def get_file_path(initialDir=".", DialogTitle="select File", fileTypeText = "all Files", fileType = "*.*"):
    root = tkinter.Tk()
    root.withdraw()
    file_path: str

    file_path = filedialog.askopenfilename(initialdir = initialDir, title = DialogTitle,filetypes = ((fileTypeText,fileType),("all files","*.*")))

    return file_path





