import sqlite3
from tkinter import (
    DISABLED,
    HORIZONTAL,
    SUNKEN,
    Button,
    Entry,
    Checkbutton,
    END,
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
root.title("Database")
root.geometry("500x500")

# Create a database or connect to one

connection = sqlite3.connect("./db/address_book.db")

# Create cursor
cursor = connection.cursor()

# Create Table
'''
cursor.execute(
    """CREATE TABLE addresses(Id INTEGER,First_Name TEXT,Last_Name TEXT,Address TEXT,City TEXT,State TEXT,Zipcode INTEGER)"""
)
'''

# Create submit function for database
def submit():
    # Create a database or connect to one
    connection = sqlite3.connect("./db/address_book.db")

    # Create cursor
    cursor = connection.cursor()

    # Insert into Table
    cursor.execute(
        """INSERT INTO addresses VALUES(:id, :f_name, :l_name, :address, :city, :state, :zipcode) """,
        {
            "id": id_entry.get(),
            "f_name": fName_entry.get(),
            "l_name": lName_entry.get(),
            "address": address_entry.get(),
            "city": city_entry.get(),
            "state": state_entry.get(),
            "zipcode": zipcode_entry.get(),
        },
    )

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()

    # Clear the text boxes
    id_entry.delete(0, END)
    fName_entry.delete(0, END)
    lName_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)


# Create Query Function
def query():
    # Create a database or connect to one
    connection = sqlite3.connect("./db/address_book.db")

    # Create cursor
    cursor = connection.cursor()

    cursor.execute("""SELECT *, oid FROM addresses """)
    records = cursor.fetchall()
    # print(records)

    print_records = ""
    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()


# Create Function to Delete a Record
def delete():
    # Create a database or connect to one
    connection = sqlite3.connect("./db/address_book.db")

    # Create cursor
    cursor = connection.cursor()

    # Delete a Record
    cursor.execute("""DELETE FROM addresses WHERE id=""" + select_entry.get())

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()


# Create a Edit Function to update a recrod
def edit():
    global editor
    editor = Tk()
    editor.title("Update A Record")
    editor.geometry("450x280")

    # Create a database or connect to one
    connection = sqlite3.connect("./db/address_book.db")

    # Create cursor
    cursor = connection.cursor()

    record_id = select_entry.get()

    cursor.execute("""SELECT * FROM addresses WHERE oid=  """ + record_id)
    records = cursor.fetchall()

    # Create Global variables for text box names
    global id_entry_editor
    global fName_entry_editor
    global lName_entry_editor
    global address_entry_editor
    global city_entry_editor
    global state_entry_editor
    global zipcode_entry_editor

    # Create Text Box
    id_entry_editor = Entry(editor, width=50)
    fName_entry_editor = Entry(editor, width=50)
    lName_entry_editor = Entry(editor, width=50)
    address_entry_editor = Entry(editor, width=50)
    city_entry_editor = Entry(editor, width=50)
    state_entry_editor = Entry(editor, width=50)
    zipcode_entry_editor = Entry(editor, width=50)

    # Create Text Box Labels
    label_id_editor = Label(editor, text="Enter your id number")
    label_fName_editor = Label(editor, text="Enter your first name")
    label_lName_editor = Label(editor, text="Enter your last name")
    label_address_editor = Label(editor, text="Enter your address")
    label_city_editor = Label(editor, text="Enter your home town")
    label_state_editor = Label(editor, text="Enter your state")
    label_zipcode_editor = Label(editor, text="Enter your zipcode")

    # Crate a save button to save edit record
    save_btn = Button(editor, text="Save Changes", command=update)

    # Loop thru results
    for record in records:
        id_entry_editor.insert(0, record[0])
        fName_entry_editor.insert(0, record[1])
        lName_entry_editor.insert(0, record[2])
        address_entry_editor.insert(0, record[3])
        city_entry_editor.insert(0, record[4])
        state_entry_editor.insert(0, record[5])
        zipcode_entry_editor.insert(0, record[6])

    # Shoving it onto the editor window
    id_entry_editor.grid(row=0, column=1, pady=5)
    label_id_editor.grid(row=0, column=0)

    fName_entry_editor.grid(row=1, column=1, pady=5)
    label_fName_editor.grid(row=1, column=0)

    lName_entry_editor.grid(row=2, column=1, pady=5)
    label_lName_editor.grid(row=2, column=0)

    address_entry_editor.grid(row=3, column=1, pady=5)
    label_address_editor.grid(row=3, column=0)

    city_entry_editor.grid(row=4, column=1, pady=5)
    label_city_editor.grid(row=4, column=0)

    state_entry_editor.grid(row=5, column=1, pady=5)
    label_state_editor.grid(row=5, column=0)

    zipcode_entry_editor.grid(row=6, column=1, pady=5)
    label_zipcode_editor.grid(row=6, column=0)

    save_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()


def update():
    # Create a database or connect to one
    connection = sqlite3.connect("./db/address_book.db")

    # Create cursor
    cursor = connection.cursor()

    record_id = select_entry.get()

    cursor.execute(
        """UPDATE addresses SET Id = :id,First_Name = :first,Last_Name = :last,Address = :address,City = :city,State = :state,Zipcode = :zipcode WHERE oid = :oid """,
        {
            "id": id_entry_editor.get(),
            "first": fName_entry_editor.get(),
            "last": lName_entry_editor.get(),
            "address": address_entry_editor.get(),
            "city": city_entry_editor.get(),
            "state": state_entry_editor.get(),
            "zipcode": zipcode_entry_editor.get(),
            "oid": record_id,
        },
    )

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()

    editor.destroy()


# Create Text Box
id_entry = Entry(root, width=50)
fName_entry = Entry(root, width=50)
lName_entry = Entry(root, width=50)
address_entry = Entry(root, width=50)
city_entry = Entry(root, width=50)
state_entry = Entry(root, width=50)
zipcode_entry = Entry(root, width=50)
select_entry = Entry(root, width=35)

# Create Text Box Labels
label_id = Label(root, text="Enter your id number")
label_fName = Label(root, text="Enter your first name")
label_lName = Label(root, text="Enter your last name")
label_address = Label(root, text="Enter your address")
label_city = Label(root, text="Enter your home town")
label_state = Label(root, text="Enter your state")
label_zipcode = Label(root, text="Enter your zipcode")
label_delete = Label(root, text="ID:       ")

# Create Submit Button
submit_btn = Button(root, text="Add Record To DataBase", command=submit)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)

# Create a Delete Button
delete_btn = Button(root, text="Delete Recrod", command=delete)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)


# Shoving it onto the screen
id_entry.grid(row=0, column=1, pady=5)
label_id.grid(row=0, column=0)

fName_entry.grid(row=1, column=1, pady=5)
label_fName.grid(row=1, column=0)

lName_entry.grid(row=2, column=1, pady=5)
label_lName.grid(row=2, column=0)

address_entry.grid(row=3, column=1, pady=5)
label_address.grid(row=3, column=0)

city_entry.grid(row=4, column=1, pady=5)
label_city.grid(row=4, column=0)

state_entry.grid(row=5, column=1, pady=5)
label_state.grid(row=5, column=0)

zipcode_entry.grid(row=6, column=1, pady=5)
label_zipcode.grid(row=6, column=0)

select_entry.grid(row=9, column=1)
label_delete.grid(row=9, column=0)

submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=130)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=130)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=138)

# Commit Changes
connection.commit()

# Close Connection
connection.close()

root.mainloop()
