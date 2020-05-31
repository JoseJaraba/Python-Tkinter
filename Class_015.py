from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import DISABLED
from tkinter import SUNKEN
from tkinter import W
from tkinter import E
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title("Flowers Album")
# root.iconbitmap("Path of the .ico")


img_1 = ImageTk.PhotoImage(
    Image.open("img/Flower_1.jpg").resize((250, 250), Image.ANTIALIAS)
)
img_2 = ImageTk.PhotoImage(
    Image.open("img/Flower_2.jpg").resize((250, 250), Image.ANTIALIAS)
)
img_3 = ImageTk.PhotoImage(
    Image.open("img/Flower_3.jpg").resize((250, 250), Image.ANTIALIAS)
)
img_4 = ImageTk.PhotoImage(
    Image.open("img/Flower_4.jpg").resize((250, 250), Image.ANTIALIAS)
)
img_5 = ImageTk.PhotoImage(
    Image.open("img/Flower_5.jpg").resize((250, 250), Image.ANTIALIAS)
)

img_list = [img_1, img_2, img_3, img_4, img_5]

status = Label(
    root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E
)
label = Label(root, image=img_1,)


def forward(image_number):
    global label
    global button_back
    global button_front
    global status

    label.grid_forget()
    label = Label(root, image=img_list[image_number - 1])
    button_front = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))
    status = Label(
        root,
        text="Image " + str(image_number) + "of " + str(len(img_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E,
    )

    if image_number == 5:
        button_front = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_front.grid(row=1, column=2)

    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def backward(image_number):
    global label
    global button_back
    global button_front

    label.grid_forget()
    label = Label(root, image=img_list[image_number - 1])
    button_front = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: backward(image_number - 1))
    status = Label(
        root,
        text="Image " + str(image_number) + "of " + str(len(img_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E,
    )

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_front.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=backward, state=DISABLED)
button_front = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="Exit Program", command=root.quit)

label.grid(row=0, column=0, columnspan=3)

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_front.grid(row=1, column=2, pady=10)

status.grid(row=2, column=0, columnspan=3, sticky=W + E)


root.mainloop()
