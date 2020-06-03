from tkinter import Tk
from tkinter import Toplevel
from tkinter import filedialog
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
root.title("Open Files")


def open_files():
    global image

    root.filename = filedialog.askopenfilename(
        initialdir="./img",
        title="Select A File",
        filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")),
    )

    image = ImageTk.PhotoImage(
        Image.open(root.filename).resize((250, 250), Image.ANTIALIAS)
    )

    label = Label(root, image=image)
    label.grid(row=1, column=0, columnspan=2)


btn_open = Button(root, text="Open Files", command=open_files)
btn_open.grid(row=0, column=0, padx=5)

btn_exit = Button(root, text="Exit", command=root.destroy)
btn_exit.grid(row=0, column=1)


root.mainloop()
