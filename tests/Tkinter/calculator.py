from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, StringVar, DoubleVar


class MyFirstGUI():
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master, pack_or_grid):
        self.master = master
        master.title ('A Simple GUI')
        self.label = Label(master, text="This is our first GUI!")

        if pack_or_grid == 'P':
            self.label_index = 0
            self.label_text = StringVar()
            self.label_text.set(self.LABEL_TEXT[self.label_index])
            self.label = Label(master, textvariable=self.label_text)
            self.label.bind("<Button-1>", self.cycle_label_text)
            self.label.pack()

            self.greet_button = Button(master, text="Greet", command=self.greet)
            self.greet_button.pack()

            self.close_button = Button(master, text="Close", command=master.quit)
            self.close_button.pack()
            # self.label.pack()
            # self.greet_button.pack(side=LEFT)
            # self.close_button.pack(side=RIGHT)
        else:
            self.greet_button = Button(master, text="Greet", command=self.greet)
            self.test_button = Button(master, text="Test", command=self.test)
            self.close_button = Button(master, text="Close", command=master.quit)
            self.label.grid(columnspan=2, sticky = W)
            self.greet_button.grid(row=1)
            self.test_button.grid(row=1, column = 2)
            self.close_button.grid(row=1, column = 3)

    def greet(self):
        print("Greetings!")

    def test(self):
        print("Tesssssssst!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT)  # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])


class Calculator():
    def __init__(self, master):
        self.master = master
        master.title ('Calculator')
        self.total = 0.0
        self.entered_number = 0.0

        self.total_label_text = DoubleVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate)  # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master,      text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master,    text="Clear", command=lambda: self.update("reset"))
        self.multiply_button = Button(master, text="*", command=lambda: self.update("multiply"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W + E)

        self.add_button.grid(row=2, column=0, sticky=W + E)
        self.subtract_button.grid(row=2, column=1, sticky=W + E)
        self.reset_button.grid(row=2, column=2, sticky=W + E)
        self.multiply_button.grid(row=3, column=1, sticky=W + E)

    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_number = 0.0
            return True
        try:
            self.entered_number = float(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "multiply":
            self.total *= self.entered_number
        else:  # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
#my_gui = MyFirstGUI(root, 'P')
my_gui = Calculator(root)
root.mainloop()