from tkinter import Tk
from tkinter import IntVar
from tkinter import StringVar
from tkinter import Button
from tkinter import messagebox
from tkinter import Radiobutton
from tkinter import Label
from tkinter import DISABLED
from tkinter import SUNKEN
from tkinter import W
from tkinter import E
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Message Box")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World!")
    # Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()


button = Button(root, text="Popup", command=popup)
button.pack()

root.mainloop()
