from tkinter import Tk
from tkinter import Label

root = Tk()

# Creating a Label Widget
myLabel = Label(root, text="Hello World!")
# Shoving it onto the screen
myLabel.pack()

root.mainloop()
