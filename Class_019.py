from tkinter import Tk
from tkinter import Toplevel
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
root.title("New Windows")


def open():
    global image

    top = Toplevel()
    top.title("Flowers")

    image = ImageTk.PhotoImage(
        Image.open("img/Flower_1.jpg").resize((250, 250), Image.ANTIALIAS)
    )
    label = Label(top, image=image)
    label.pack()

    btn_close = Button(top, text="Close Windo", command=top.destroy)
    btn_close.pack()


btn_new = Button(root, text="Open Second Windo", command=open)
btn_new.pack(pady=5)

btn_close = Button(root, text="Exit", command=root.destroy)
btn_close.pack()

root.mainloop()
