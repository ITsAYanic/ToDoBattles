from crud import testmessage;
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
ttk.Label(frm, text="Hello World!").pack()
ttk.Button(frm, text="Quit", command=root.destroy).pack()
root.mainloop()