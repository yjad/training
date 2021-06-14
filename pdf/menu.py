import tkinter as tk
from tkinter import ttk
import pytesseract
from edit_ocr import review_page, GetFromTo
from pdf_db import update_book



def run_menu():
    root = tk.Tk()
    #root.attributes('-fullscreen', True)
    # root.state('zoome')
    root.attributes('-zoomed', True)
    
    # output = ScrolledText(root, width=150, height = 40, wrap = tk.WORD, background = 'white')
    # output.grid(row=1, column = 0, columnspan = 2, sticky = 'W')
    # set_output_tk(output)
    
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    # file_menu.add_command(label="Load Qradar files", command=lambda: load_db(DATA_FOLDER, output))
    file_menu.add_command(label="1. Load book pages", command= lambda:run_load_book_pages(root))
    file_menu.add_separator()
    
    file_menu.add_command(label="2. Edit Pages", command=lambda:GetFromTo(root))
    file_menu.add_command(label="3. Review Pages", command=lambda:review_page(root))
    file_menu.add_command(label="4. Update Book words", command=update_book)

    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    root.config(menu=menu_bar)    
        
    root.mainloop()

def run_load_book_pages(root):
    app= GetFromTo(root)
    from_page, to_page = app.go_command()
    print (from_page, to_page)


if __name__ == '__main__':
    run_menu()



