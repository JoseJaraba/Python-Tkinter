from tkinter import Tk
from tkinter import Label

root = Tk()

# Creating a Label Widget
myLabelOne = Label(root, text="Hello World!")
myLabelTwo = Label(root, text="My Name Is Jose Jaraba")

# Shoving it onto the screen
myLabelOne.grid(row=0, column=0)
myLabelTwo.grid(row=1, column=1)

root.mainloop()
