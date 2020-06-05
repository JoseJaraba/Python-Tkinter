from tkinter import Tk
from tkinter import Scale
from tkinter import Toplevel
from tkinter import filedialog
from tkinter import IntVar
from tkinter import StringVar
from tkinter import Button
from tkinter import Checkbutton
from tkinter import messagebox
from tkinter import Radiobutton
from tkinter import Label
from tkinter import DISABLED
from tkinter import SUNKEN
from tkinter import HORIZONTAL
from tkinter import W
from tkinter import E
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Checkboxes")
root.geometry("500x500")

var = StringVar()


def show():
    Label(root, text=var.get()).pack(pady=5)


checkbox = Checkbutton(
    root, text="Check this box", variable=var, onvalue="On", offvalue="Off"
)
checkbox.deselect()
checkbox.pack()


Button(root, text="Show Selection", command=show).pack()


root.mainloop()
