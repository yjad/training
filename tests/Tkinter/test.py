
import tkinter as tk
from tkinter import ttk


global save_rec
global print_save_rec

def save_cmd():

    global print_save_rec
    save_rec_txt = ''
    for a,b in save_rec.items():
        save_rec_txt = save_rec_txt + f" {a}:{b.get()}, "
     
    print_save_rec.set(save_rec_txt)
   

def test_1():

    global save_rec
    global print_save_rec
    
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.grid()
    frame.configure(bg='#dddddd')

    print_save_rec = tk.StringVar()
    save_rec={'name':tk.StringVar(), 
                'job':tk.StringVar(),
                'title':tk.StringVar(),
                'gender':tk.IntVar(),
                'language':tk.StringVar(),
                'month':tk.StringVar(),
                }    

    # def CurSelet(event):
    #     widget = event.widget
    #     selection=widget.curselection()
    #     save_rec['language'].set(widget.get(selection[0]))

    tk.Label(frame, text="Name: ").grid(row=1, column=1, sticky='w')
    tk.Label(frame, text="Title: ").grid(row=2, column=1, sticky='w')
    tk.Label(frame, text="Job: ").grid(row=3, column=1, sticky='w')

    tk.Entry(frame, textvariable = save_rec['name']).grid(row=1, column=2, sticky= 'w')
    tk.Entry(frame, textvariable = save_rec['title']).grid(row=2, column=2, sticky= 'w')
    tk.Entry(frame, textvariable = save_rec['job']).grid(row=3, column=2, sticky= 'w')

    save_rec['gender'].set(1)   # set default

    rb_box = tk.LabelFrame(frame, text='Gender Frame: ', fg= 'red')
    rb_box.grid(row=4, column=1, sticky= 'ew')

    tk.Radiobutton(rb_box, text='male', variable = save_rec['gender'], value=1).grid(row=2, column=1, sticky='w')
    tk.Radiobutton(rb_box, text='female', variable = save_rec['gender'], value=2).grid(row=3, column=1, sticky='w')

    tk.Label(frame, text="Language: ").grid(row=5, column=1, sticky='w')

    langs=("Python", "Perl", "C", "PHP", "JSP", "Ruby")
    lang_cb = ttk.Combobox(frame, textvariable=save_rec['language'])
    lang_cb['values'] = langs
    lang_cb['state'] = 'readonly'  # normal
    lang_cb.grid(row=5, column = 2, sticky = 'w', pady=10)

    # Lb1 = tk.Listbox(frame,height=6, width=10, selectmode = 'single')
    # Lb1.insert(1, "Python")
    # Lb1.insert(2, "Perl")
    # Lb1.insert(3, "C")
    # Lb1.insert(4, "PHP")
    # Lb1.insert(5, "JSP")
    # Lb1.insert(6, "Ruby")
     
    # Lb1.bind('<<ListboxSelect>>',CurSelet)
    # Lb1.select_set(0)
    # Lb1.curselection()
    # save_rec['language'].set(Lb1.get(0))
    # Lb1.grid(row=5, column=2, sticky= 'w')

    
# --------------------------------------
# Combo Box
#---------------------------------------
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    
    tk.Label(frame, text="Month: ").grid(row=6, column=1, sticky='w')
    # selected_month = tk.StringVar()

    month_cb = ttk.Combobox(frame, textvariable=save_rec['month'])
    month_cb['values'] = months
    month_cb['state'] = 'readonly'  # normal
    month_cb.grid(row=6, column = 2, sticky = 'w', pady=10)

    # month_cb.bind('<<ComboboxSelected>>', month_changed)
#-----------------------
    tk.Label(frame, text = '          ').grid(row=1, column=3)

    tk.Label(frame, textvariable=print_save_rec, wraplength=300).grid(row=8, column=1, padx=50, sticky='w')

    tk.Button(frame, text="Save  ", fg="red", command = save_cmd).grid(row=1,column=4, sticky='ew',padx=5)
    tk.Button(frame, text="Edit  ", fg="red").grid(row=2,column=4, sticky= 'ew',padx=5)
    tk.Button(frame, text="Insert", fg="red").grid(row=3,column=4, sticky='ew',padx=5)
    tk.Button(frame, text="Quit  ", fg="red", command=quit).grid(row=4,column=4, sticky='ew',padx=5)

    root.mainloop()


test_1()