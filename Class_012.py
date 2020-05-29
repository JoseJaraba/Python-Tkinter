from tkinter import Tk
from tkinter import Label
from tkinter import Button

root = Tk()


def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=myClick, fg="blue", bg="white")
myButton.pack()

root.mainloop()
