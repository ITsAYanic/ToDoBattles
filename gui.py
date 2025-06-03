from tkinter import *;
import tkinter as tk;

def kill():
    print("I FUCKING WORK!")

root = Tk()
frm = tk.Frame(root).pack()
label = tk.Label(root, text="Do I work?").pack()
button = tk.Button(frm, text="I'm a button", command=kill).pack()


root.mainloop()

