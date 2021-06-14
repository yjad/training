import tkinter as tk

my_dict = {'algorithm': 'algorism definition',
           'bug': 'bug definition'}

output:tk.Text = None

def click():
    txt = textentry.get()
    #clear_text()
    definition = ''
    try:
        definition = my_dict[txt]
    except:
        output = 'key does not exist'
    output.insert = (tk.END, definition)


root = tk.Tk()
root.title('My computer science dictionary')
root.configure(background='gray')
# photo1=tk.PhotoImage(file='image1.gif')
# tk.Label(root, image=photo1, bg='black').grid(row=0, column=0, sticky=tk.W)

label1= tk.Label(root, text='Enter the work you would like a definition for:', bg = 'black', fg='white', font='Arial 12')
label1.grid(column=0, row=1, sticky=tk.W)

textentry = tk.Entry(root, width=20, bg= 'white')
textentry.grid(column=0, row=2, sticky=tk.W)

tk.Button(root, text='submit', width=6, bg= 'white',command=click).grid(column=0, row=4, sticky=tk.W)

label2= tk.Label (root, text='\n Definition:', bg = 'black', fg='white', font='none 12 bold')
label1.grid(column=0, row=5, sticky=tk.W)

output = tk.Text(root, width=75, height=6, wrap= tk.WORD, bg= 'white')
output.grid(row=5, column =0, columnspan=2, sticky =tk.W)

root.mainloop()


# def clear_text():
#     output.delete(0.0, tk.END)
#
# def get_text():
#     return textentry.get()
#
# def insert_text(definition):

