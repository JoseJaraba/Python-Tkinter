from tkinter import (
    DISABLED,
    HORIZONTAL,
    SUNKEN,
    Button,
    Checkbutton,
    E,
    IntVar,
    Label,
    OptionMenu,
    Radiobutton,
    Scale,
    StringVar,
    Tk,
    Toplevel,
    W,
    filedialog,
    messagebox,
)

from PIL import Image, ImageTk

root = Tk()
root.title("Dropdown Menus")


options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

variable = StringVar()
variable.set(options[0])


def show():
    Label(root, text=variable.get()).pack()


# Drop Down Boxes

drop = OptionMenu(root, variable, *options)
drop.pack()

button = Button(root, text="Show selection", command=show)
button.pack()

root.mainloop()
