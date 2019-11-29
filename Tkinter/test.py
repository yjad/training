# import tkinter as tk
#
#
# class HelloWorld(tk.Frame):
#     def __init__(self, parent):
#         super(HelloWorld, self).__init__(parent)
#         self.label = tk.Label(self, text="Hello, World!")
#         self.label.pack(padx=40, pady=30)
#
#
# c
# if __name__ == "__main__":
#      root = tk.Tk()
#      main = HelloWorld(root)
#      main.pack(fill="both", expand=True)
#      root.mainloop()

import tkinter as tk

def click():
    #entered_text

def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()



button = tk.Button(frame, text="QUIT", fg="red", command=quit)
    #.grid(row=1,column=2)
button.pack(side=tk.RIGHT)
slogan = tk.Button(frame, text="File ...")
#.grid(row=2,column=2)
slogan.pack(side=tk.RIGHT)

T = tk.Text(root, height=4, width=30)
T.pack(side=tk.LEFT)
T.insert(tk.END, "Just a text Widget\nin two lines\n")


root.mainloop()