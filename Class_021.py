from tkinter import Tk
from tkinter import Scale
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
from tkinter import HORIZONTAL
from tkinter import W
from tkinter import E
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Slider")
root.geometry("400x400")


def slide():
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


vertical = Scale(root, from_=0, to=200)
vertical.pack(anchor=W)

horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
horizontal.pack(pady=5)


Button(root, text="Click Me!", command=slide).pack()


root.mainloop()
