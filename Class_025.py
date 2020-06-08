import numpy as np
import matplotlib.pyplot as plt
from tkinter import (
    DISABLED,
    END,
    HORIZONTAL,
    SUNKEN,
    Button,
    Checkbutton,
    E,
    Entry,
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
root.title("Matplotlib Charts")
root.geometry("500x500")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()


Button(root, text="Graph It!", command=graph).pack()


root.mainloop()
