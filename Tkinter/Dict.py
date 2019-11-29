#import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E, PhotoImage, WORD, Text


class Glossary:
    my_dict = {'One': 'One definition', 'Two': 'Two Definition'}

    def __init__(self, master):
        self.master = master
        master.title("My Computer Science Dictionary")
        master.configure (background = 'black')

        photo1 = PhotoImage (file = 'image1.gif')
        Label (master, image = photo1).grid(row=0, column = 0, sticky = E)

        Label(master, text='Enter the work you want its definitio:',  fg='black',
              font='none 12 bold').grid(row=1, column=0, sticky = W)

        self.textentry = Entry(master, width=20, bg='white')
        self.textentry.grid(row=2, column=0, sticky = W)

        Button(master, text = 'SUBMIT', width = 6, command=self.click).grid(row=3, column = 0, sticky = W, )

        Label(master, text='\nDefinintion',  fg='black', font='none 12 bold').grid(row=4, column=0, sticky = W)

        self.output = Text(master, width=75, height = 6, wrap = WORD, background = 'white')
        self.output.grid(row=5, column = 0, columnspan = 2, sticky = 'W')

        Button(master, text='Exit', width=6, command= master.quit).grid(row=3, column=2, sticky=E )

    def click(self):
        entered_text = self.textentry.get()
        self.output.delete(0.0, END)
        try:
            definition = self.my_dict[entered_text]
        except:
            definition = 'Invalid key'

        self.output.insert(END, definition)

root = Tk()
my_glossary = Glossary(root)
root.mainloop()