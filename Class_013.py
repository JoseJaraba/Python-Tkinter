from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry

root = Tk()

entry = Entry(root, width=50, borderwidth=5, bg="blue", fg="white")
entry.pack()
entry.insert(0, "Enter Your Name ")


def myClick():
    greet = "Hello! " + entry.get()
    myLabel = Label(root, text=greet)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name!", command=myClick, fg="blue", bg="white")
myButton.pack()


root.mainloop()
