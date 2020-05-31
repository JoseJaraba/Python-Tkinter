from tkinter import Tk
from tkinter import IntVar
from tkinter import StringVar
from tkinter import Button
from tkinter import Radiobutton
from tkinter import Label
from tkinter import DISABLED
from tkinter import SUNKEN
from tkinter import W
from tkinter import E
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Radio Buttons")

# response = IntVar()
pizza = StringVar()
pizza.set("Pepperoni")

TOPPINGS = [("Pepperoni", "Pepperoni"), ("Cheese", "Cheese"), ("Mushroom", "Mushroom")]

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def click(value):
    label = Label(root, text=value)
    label.pack()


"""
Radiobutton(
    root,
    text="Option 1",
    variable=response,
    value=1,
    command=lambda: click(response.get()),
).pack()
Radiobutton(
    root,
    text="Option 2",
    variable=response,
    value=2,
    command=lambda: click(response.get()),
).pack()
"""

button = Button(root, text="Click Me !!!", command=lambda: click(pizza.get()))
button.pack()

root.mainloop()
