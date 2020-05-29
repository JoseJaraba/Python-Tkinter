from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import END

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def clickButton(number):
    # entry.delete(0, END)
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def clearButton():
    entry.delete(0, END)


def addButton():
    global first_number
    global math
    math = "addition"
    first_number = int(entry.get())
    entry.delete(0, END)


def subtractButton():
    global first_number
    global math
    math = "subtraction"
    first_number = int(entry.get())
    entry.delete(0, END)


def multiplyButton():
    global first_number
    global math
    math = "multiplication"
    first_number = int(entry.get())
    entry.delete(0, END)


def divideButto():
    global first_number
    global math
    math = "division"
    first_number = int(entry.get())
    entry.delete(0, END)


def equalButton():
    second_number = int(entry.get())
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, first_number + second_number)
    if math == "subtraction":
        entry.insert(0, first_number - second_number)
    if math == "multiplication":
        entry.insert(0, first_number * second_number)
    if math == "division":
        if second_number == 0:
            entry.insert(0, "Syntax Error")
        else:
            entry.insert(0, first_number / second_number)


# Define Buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: clickButton(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: clickButton(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: clickButton(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: clickButton(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: clickButton(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: clickButton(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: clickButton(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: clickButton(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: clickButton(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: clickButton(0))

button_add = Button(root, text="+", padx=40, pady=20, command=addButton)
button_subtract = Button(root, text="-", padx=42, pady=20, command=subtractButton)
button_multiply = Button(root, text="*", padx=42, pady=20, command=multiplyButton)
button_divide = Button(root, text="/", padx=42, pady=20, command=divideButto)

button_equal = Button(root, text="=", padx=90, pady=20, command=equalButton)
button_clear = Button(root, text="clear", padx=80, pady=20, command=clearButton)


# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
