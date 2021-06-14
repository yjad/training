def test_1(root):
    # root = tk.Tk()
    root.geometry('1500x800')
    # root.geometry('500x500')
    root.resizable(1, 1)
    root.config()
    root.title('Edit OCR')
    frame = tk.Frame(root)
    frame.grid()
    # frame.configure(bg='#dddddd')
    page_no=13
    page_no_var = tk.IntVar()
    page_no_var.set(14)
    image_path = ''
    image_obj = None

    def display_page():
        global image_path
        global image_obj
        # page_no = page_no_var.get()
        # page = 'ABH-'+format(page_no, '03') + '.png'
        
        # image_path = f'.\\data\\ABH pages\\{page}'
        # img_file  = Image.open(image_path)
        # img_file.thumbnail((600,650), Image.ANTIALIAS)
        # img = ImageTk.PhotoImage(img_file) 

        
        # image_obj= canvas.create_image(0, 0, anchor=tk.NW, image=img) 

        # time.wait()
        # text.insert('end', image_path+"ccc") 

        # canvas.delete(image_obj)
        # x = len(image_path)
        # text.insert('end', '\n'+str(len(img)), 'tag-right')  

        # text_file_path = f".\\out\\{page.split('.')[0]}.txt"
        # with open(text_file_path, "r", encoding='utf-8') as page_text_file:
        #     page_text = page_text_file.read()
        # text_file = f".\\out\\{page.split('.')[0]}.txt"
        # text.delete('1.0', 'end')   # clear text
        # text.insert('end', page_text, 'tag-right')    

        # text.insert('end', '\n'+str(len(img)), 'tag-right')  
        # coord = 10, 50, 240, 210
        # arc = canvas.create_arc(coord, start=0, extent=150, fill="red")
        # time.wait(3)
        # canvas.delete(arc)

    def next_page():
        page_no = page_no_var.get() 
        page_no += 1
        page_no_var.set(page_no)
        # display_page()
        
        
    def prev_page():
        page_no = page_no_var.get()
        page_no -= 1
        page_no_var.set(page_no)
        # display_page()

    
    # canvas = tk.Canvas(root, width = 470, height = 650, bg="gray")  
    # canvas.grid(row=0, column=0, sticky= 'w')
    # image_path = f'.\\data\\ABH pages\\ABH-012.png'
    # page = 'ABH-'+format(page_no_var.get(), '03') + '.png'
    # image_path = f'.\\data\\ABH pages\\{page}'
    # print (image_path)
    # img_file  = Image.open(image_path)
    # img_file.thumbnail((600,650), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img_file) 
    # canvas = tk.Canvas(root, width = 470, height = 650, bg="blue")  
    # canvas.grid(row=0, column=0, sticky= 'w')
    # x =canvas.create_image(0, 0, anchor=tk.NW, image=img) 
    
    # text = tk.Text(root, width = 70, height = 35, wrap=tk.WORD, yscrollcommand = 1, xscrollcommand = 1)
    # text.tag_configure('tag-right', justify='right')
    # text.grid(row=0, column=6, sticky= 'w')
    
    # image_path = f'.\\data\\ABH pages\\ABH-012.png'
    # img_file  = Image.open(image_path)
    # img_file.thumbnail((600,650), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img_file) 
    # canvas.create_image(0, 0, anchor=tk.NW, image=img) 

    # tk.Label(root, text="Page No: ").grid(row=2,column=1, sticky='ew')
    # tk.Entry(root, textvariable = page_no_var, width=4).grid(row=1,column=1, sticky='w')
    # tk.Button(root, text="GO", command=display_page).grid(row=1,column=2, sticky= 'ew',padx=5)
    # tk.Button(root, text="Next  ", command=next_page).grid(row=1,column=3, sticky= 'ew',padx=5)
    # tk.Button(root, text="Prev  ", command=prev_page).grid(row=1,column=4, sticky='ew',padx=5)
    # tk.Button(root, text="Quit  ", fg="red", command=quit).grid(row=1,column=5, sticky='ew',padx=5)

    
    
        
    # canvas.place(x=0, y=0)
    
    # img_file  = Image.open(image_path)
    # img_file.thumbnail((600,650), Image.ANTIALIAS)
    # img = ImageTk.PhotoImage(img_file) 
    # canvas.create_image(0, 0, anchor=tk.NW, image=img) 

   
    app = DisplayImageLabel(root)
    
    root.mainloop()

class DisplayImage(object):
    def __init__(self, master, **kwargs):
        self.master = master
        # self.filename = filename
        self.text = tk.Text(self.master, width = 70, height = 35, wrap=tk.WORD, yscrollcommand = 1, xscrollcommand = 1)
        self.text.tag_configure('tag-right', justify='right')
        self.text.grid(row=0, column=6, sticky= 'w')

        self.canvas = tk.Canvas(self.master, width = 470, height = 650, bg="gray")  
        self.canvas.grid(row=0, column=0, sticky= 'w')
        self.page_no_var = tk.IntVar()

        # tk.Entry(self.master, textvariable = self.page_no_var, width=4).grid(row=1,column=1, sticky='w')
        # tk.Button(self.master, text="GO", command=self.draw).grid(row=1,column=2, sticky= 'ew',padx=5)
        # tk.Button(self.master, text="Next  ", command=next_page).grid(row=1,column=3, sticky= 'ew',padx=5)
        # tk.Button(self.master, text="Prev  ", command=prev_page).grid(row=1,column=4, sticky='ew',padx=5)
        # tk.Button(self.master, text="Quit  ", fg="red", command=quit).grid(row=1,column=5, sticky='ew',padx=5)

        # self.update = self.draw().__next__
        # master.after(100, self.update)
        
        self.draw()

    def draw(self):
        page_no = self.page_no_var.get()
        page = 'ABH-'+format(page_no, '03') + '.png'
        
        image_path = f'.\\data\\ABH pages\\{page}'
        img_file  = Image.open(image_path)
        img_file.thumbnail((600,650), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img_file) 
        canvas_obj = self.canvas.create_image(0, 0, anchor=tk.NW, image=img) 
        # arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")


class DisplayImageLabel():
    def __init__(self, master, **kwargs):

        self.master = master
        frame = tk.Frame(master)
        frame.configure(bg='#dddddd')
        frame.grid()
        self.text = tk.Text(self.master, width = 70, height = 35, wrap=tk.WORD, yscrollcommand = 1, xscrollcommand = 1)
        self.text.tag_configure('tag-right', justify='right')
        self.text.grid(row=0, column=6, sticky= 'w')

        self.img_lbl = tk.Label(self.master, width = 470, height = 650, bg="gray")  
        self.img_lbl.grid(row=0, column=0, sticky= 'w')
        self.page_no_var = tk.IntVar()

        tk.Entry(self.master, textvariable = self.page_no_var, width=4).grid(row=1,column=1, sticky='w')
        tk.Button(self.master, text="GO", command=self.draw).grid(row=1,column=2, sticky= 'ew',padx=5)
        tk.Button(self.master, text="Next  ", command=self.next_page).grid(row=1,column=3, sticky= 'ew',padx=5)
        tk.Button(self.master, text="Prev  ", command=self.prev_page).grid(row=1,column=4, sticky='ew',padx=5)
        tk.Button(self.master, text="Quit  ", fg="red", command=quit).grid(row=1,column=5, sticky='ew',padx=5)

        self.page_no_var.set(4)
        self.draw()

    def draw(self):
        page_no = self.page_no_var.get()
        page = 'ABH-'+ format(page_no, '03') + '.png'
        
        image_path = f'.\\data\\books\\ABH\\pages\\{page}'

        img_file  = Image.open(image_path)
        img_file.thumbnail((600,650), Image.ANTIALIAS)
        self.img_lbl.img  = ImageTk.PhotoImage(img_file) 
        self.img_lbl.config(image = self.img_lbl.img)

        # words= str(((pytesseract.image_to_string(Image.open(image_path), lang='ara'))))
        page_raw, page_edited = get_db_page(page_no)

        self.text.delete('1.0', 'end')   # clear text
        self.text.insert('end', page_edited, 'tag-right')    
        
    def next_page(self):
        page_no = self.page_no_var.get() 
        self.page_no_var.set(page_no+1)
        self.draw()
        
        
    def prev_page(self):
        page_no = self.page_no_var.get()
        self.page_no_var.set(page_no - 1)
        self.draw()