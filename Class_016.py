from tkinter import Tk
from tkinter import Frame
from tkinter import LabelFrame
from tkinter import Button
from tkinter import Label
from tkinter import DISABLED
from tkinter import SUNKEN
from tkinter import W
from tkinter import E
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Frames")

frame = LabelFrame(root, padx=50, pady=50)  # padding inside of the Frame
frame.pack(padx=10, pady=10)  # padding outside of the Frame

button_1 = Button(frame, text="Don't Click Here !!!")
button_2 = Button(frame, text="... Or Here !!!")

button_1.grid(row=0, column=0, pady=5)
button_2.grid(row=1, column=1)


root.mainloop()
