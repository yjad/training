import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pdf_db import get_db_page



def test_1():
    root = tk.Tk()
    # root.geometry('1500x800')
    root.geometry('500x500')
    # root.resizable(1, 1)
    # root.config()
    root.title('Edit OCR')
    frame = tk.Frame(root)
    frame.grid()
    # frame.configure(bg='#dddddd')

    # for r in range(1,5):

    #     self.words_raw = ScrolledText(self.master, width = 16, height = 32, wrap=tk.WORD, background = 'white')
    #     self.words_raw.tag_configure('tag-right', justify='right')
    #     self.words_raw.configure(font = text_font)
    #     self.words_raw.place(relx=0.73, rely = 0)

   
    # root = Tk()

    height = 30
    width = 5
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Entry(root, text="")
            b.grid(row=i, column=j)

    # mainloop()
    # app = DisplayImageLabelPlace(root)
    
    root.mainloop()
# test_1()




def test_2():
    def show():

        tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5'],
        ['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5'],
        ['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]
        tempList.sort(key=lambda e: e[1], reverse=True)

        for i in listBox.get_children():
            listBox.delete(i)

        for i, (name, score) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, name, score))

    def OnDoubleClick(event):
            item = listBox.selection()[0]
            print("you clicked on", listBox.item(item,"values")[1])

    scores = tk.Tk() 
    label = tk.Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)
    # create Treeview with 3 columns
    cols = ('Position', 'Name', 'Score')
    listBox = ttk.Treeview(scores, columns=cols, show='headings')
    # set column headings
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.grid(row=1, column=0, columnspan=2)

    listBox.bind("<Double-1>", OnDoubleClick)

    showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
    closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

    scores.mainloop()

    

test_2()