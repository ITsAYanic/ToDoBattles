from tkinter import *;
import tkinter as tk;

def kill():
    print("I FUCKING WORK!")

root = Tk()
frm = tk.Frame(root).pack()
label = tk.Label(root, text="Do I work?")
label.pack()
button = tk.Button(root, text="I'm a button", command=kill)
checkbutton = tk.Checkbutton(root)
input_field = tk.Entry(root)
input_field.pack()
checkbutton.pack()
button.pack()
label.pack()
root.mainloop()

