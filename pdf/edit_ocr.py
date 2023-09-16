import os
import tkinter as tk
import tkinter.font
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# import pyperclip
from PIL import Image, ImageTk

from pdf_db import (get_db_page, get_page_dict, rebuild_page_text,
                    update_book_word)


def review_page(root):    
    app = DisplayImageLabelPlace(root)

# def get_from_to_page_no(root):
#     app  = GetFromTo(root)
#     return app.from_page_no_var.get(), app.to_page_no_var.get()

    

class DisplayImageLabelPlace():
    def __init__(self, master, **kwargs):

        self.word_edited = 0    # false
        self.master = master
        frame = tk.Frame(master)
        frame.configure(bg='#dddddd')
        frame.grid()

        self.img_lbl = tk.Label(self.master, width = 400, height = 6, bg="light gray")  
        self.img_lbl.place(anchor='nw', relwidth=0.35, relheight = 0.94)
        self.page_no_var = tk.IntVar()

        text_font = tkinter.font.Font( family = "Calibri (Body)", size = 13, weight = "normal")

        self.page_raw = ScrolledText(self.master, width=50, height = 16, wrap = tk.WORD, background = 'white')
        self.page_raw.tag_configure('tag-right', justify='right')
        self.page_raw.configure(font = text_font)
        # self.page_raw.config (state ='disabled')
        self.page_raw.place(relx=0.36, rely = 0)

        self.page_edited = ScrolledText(self.master, width = 50, height = 16, wrap=tk.WORD, background = 'light gray')
        self.page_edited.tag_configure('tag-right', justify='right')
        self.page_edited.configure(font = text_font)
        self.page_edited.place(relx=0.36, rely = .47)

        
        cols = ('#','pdf', 'Dic', 'Type')
        self.listBox = ttk.Treeview(self.master, columns=cols, show='headings', height = 25, selectmode="browse")
        self.listBox.column("#", minwidth=0, width=40, stretch=tk.NO)
        self.listBox.column("pdf", minwidth=0, width=90, stretch=tk.NO)
        self.listBox.column("Dic", minwidth=0, width=90, stretch=tk.NO)
        self.listBox.column("Type", minwidth=0, width=100, stretch=tk.NO)
        self.listBox.place(relx=0.73, rely = 0)
        for col in cols:
            self.listBox.heading(col, text=col)  
       
        verscrlbar = ttk.Scrollbar(self.master, 
                           orient ="vertical", 
                           command = self.listBox.yview)
        verscrlbar.place(relx=0.97, rely = 0, height=530)
        self.listBox.configure(yscrollcommand = verscrlbar.set)
        
        self.listBox.bind("<Double-1>", self.listBox_OnDoubleClick)
        self.listBox.bind("<ButtonRelease-1>", self.listBox_OnClick)
        self.listBox.bind("<KeyRelease-Up>", self.listBox_UpArrow)
        self.listBox.bind("<KeyRelease-Down>", self.listBox_DownArrow)
        
        self.edit_word_var = tk.StringVar()
        self.dict_entry = tk.Entry(self.master, textvariable = self.edit_word_var, width=20, justify='right').place(relx=0.74, rely=0.80)
        
        self.word_pdf_type = tk.IntVar()
        tk.Radiobutton(self.master, text='Specific', variable = self.word_pdf_type, value=0).place(relx=0.85, rely=0.80)
        tk.Radiobutton(self.master, text='Dict', variable = self.word_pdf_type, value=1).place(relx=0.85, rely=0.84)
    
        tk.Button(self.master, text="Save  ", fg="red", command=self.save_dict_word).place(relx=0.95, rely=0.80)
        tk.Button(self.master, text="Save Page", fg="red", command=self.save_dict_page).place(relx=0.95, rely=0.94)

        tk.Button(self.master, text="GO", command=self.draw_page).place(relx=0.2, rely=0.94)
        tk.Button(self.master, text="Prev  ", command=self.prev_page).place(relx=0.25, rely=0.94)
        tk.Entry(self.master, textvariable = self.page_no_var, width=4).place(relx=0.3, rely=0.94)
        tk.Button(self.master, text="Next  ", command=self.next_page).place(relx=0.33, rely=0.94)    
        tk.Button(self.master, text="Copy  ", command=self.copy_clipboard).place(relx=0.37, rely=0.94)    
        tk.Button(self.master, text="reEdit  ", command=self.reedit_page).place(relx=0.41, rely=0.94)    
        tk.Button(self.master, text="Quit  ", fg="red", command=quit).place(relx=0.55, rely=0.94)

        self.page_no_var.set(4)
        self.draw_page()

    def draw_page(self):
        
        self.word_edited = 0    # False
        page_no = self.page_no_var.get()
        page = 'ABH-'+ format(page_no, '03') + '.png'
        
        # image_path = f'.\\data\\books\\ABH\\pages\\{page}'
        image_path = os.path.join('.', 'data', 'books', 'ABH', 'pages', page)

        img_file  = Image.open(image_path)
        img_file.thumbnail((600,650), Image.ANTIALIAS)
        self.img_lbl.img  = ImageTk.PhotoImage(img_file) 
        self.img_lbl.config(image = self.img_lbl.img)

        # words= str(((pytesseract.image_to_string(Image.open(image_path), lang='ara'))))
        page_raw, page_edited = get_db_page(page_no)

        self.page_raw.config (state ='normal') 
        self.page_raw.delete('1.0', 'end')   # clear text
        self.page_raw.insert('end', page_raw, 'tag-right')    
        self.page_raw.config (state ='disabled')  
         
        self.page_edited.config (state ='normal') 
        self.page_edited.delete('1.0', 'end')   # clear text
        self.page_edited.insert('end', page_edited, 'tag-right')  
        self.page_edited.config (state ='disabled')  

        self.word_pdf_type.set(0)   # default Specific
        
        for i in self.listBox.get_children():
            self.listBox.delete(i)   # clear text
        rows  = get_page_dict(page_no)
        for i, row in enumerate (rows, start = 1):
            self.listBox.insert("", "end", iid = i, values=(i, row[0], row[1], (row[3] if row[3]!=None else ''), 0))
        
        self.listBox.selection_set(['1'])   # select first line

    def next_page(self):
        if self.word_edited:
            if tk.messagebox.askyesno("Save?", "Save Changes?"):
                self.save_dict_page()
        
        self.page_no_var.set(self.page_no_var.get()+ 1)
        self.draw_page()
        
        
    def prev_page(self):
        if self.word_edited:
            if tk.messagebox.askyesno("Save?", "Save Changes?"):
                self.save_dict_page()
        self.page_no_var.set(self.page_no_var.get() - 1)
        self.draw_page()

    def copy_clipboard(self):
        pyperclip.copy(self.page_edited.get("1.0",tk.END))


    def reedit_page(self):
        page_no = self.page_no_var.get()
        page_reedited = rebuild_page_text(page_no)
        # page_raw, page_reedited = get_db_page(page_no)
        self.page_edited.config (state ='normal') 
        self.page_edited.delete('1.0', 'end')   # clear text
        self.page_edited.insert('end', page_reedited, 'tag-right')  
        self.page_edited.config (state ='disabled')  


    def listBox_DictLineChange(self, event):
        # item = self.self.listBox.item(item,"values")
        item = self.listBox.focus()
        # print (event,":", item, self.listBox.selection(), self.listBox.item(item,"values"))
        
        items = self.listBox.item(item,"values")
        self.edit_word_var.set(items[2])
        if items[3] in ['', 'Specific', 'None']:
            self.word_pdf_type.set(0)
        else:
            self.word_pdf_type.set(1)
        
        
    def listBox_OnClick(self, event):
        self.listBox_DictLineChange(event)

    def listBox_OnDoubleClick(self, event):
        self.listBox_DictLineChange(event)

    def listBox_UpArrow(self, event):
        self.listBox_DictLineChange(event)
        
    def listBox_DownArrow(self, event):
        self.listBox_DictLineChange(event)
        
    def save_dict_word(self):   # update on the TreeView 
        self.word_edited = 1
        word_types = ['Specific', 'Dict']
        
        # item = self.listBox.focus()
        word_type = word_types[self.word_pdf_type.get()]
        word_dict = self.edit_word_var.get()
        selected = self.listBox.focus()
        temp = self.listBox.item(selected, 'values')
       
        self.listBox.item(selected, values=(temp[0], temp[1], word_dict, word_type, 1))

        
    def save_dict_page(self):   # save changes in the page's dict to DB
        
        page_edited = False
        for w in self.listBox.get_children():
            row = self.listBox.item(w, 'values')
            if int(row[4]):  # row got modified
                # update_book_word(pdf_word, dict_word, page_no, word_type)
                update_book_word(row[1], row[2], self.page_no_var.get(), row[3])
                page_edited = True
        self.word_edited = 0
        if page_edited: # refresh edited page text
            page_reedited = rebuild_page_text(self.page_no_var.get())
            self.page_edited.config (state ='normal') 
            self.page_edited.delete('1.0', 'end')   # clear text
            self.page_edited.insert('end', page_reedited, 'tag-right')  
            self.page_edited.config (state ='disabled')  
        

class GetFromTo():
    def __init__(self, master, **kwargs):

        self.master = master
        frame = tk.Frame(master)
        frame.configure(bg='#dddddd')
        frame.grid()

        self.from_page_no_var = tk.IntVar()
        self.to_page_no_var = tk.IntVar()

        tk.Label(self.master, text = 'From Page:').place(x = 10, y = 10)
        tk.Entry(self.master, textvariable = self.from_page_no_var, width=4).place(x=100, y=10)

        tk.Label(self.master, text = 'to Page  :').place(x = 10, y = 50)
        tk.Entry(self.master, textvariable = self.to_page_no_var, width=4).place(x=100, y=50)

        tk.Button(self.master, text="GO", command=self.go_command).place(x=200, y=10)

        
        # self.draw()

    def go_command(self):
        return self.from_page_no_var.get(),self.to_page_no_var.get()
    


    def load_pages(self):
        for page_no in range(self.from_page_no_var.get(),self.to_page_no_var.get()+1):
            edit_page_text(page_no)
