from passwordGenerator import password
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("random password")
root.iconbitmap(r'key.ico')
root.geometry("275x50+500+500")
var = StringVar()
label = Label(root, textvariable = var, font="Helvetica 12")
var.set(password())
label.pack(padx = 0.5, pady = 5, anchor = CENTER)

root.mainloop()
