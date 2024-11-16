import sqlite3
from tkinter import *
from tkinter import messagebox

# Initialize the Database
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()
cursor.execute(
    """CREATE TABLE IF NOT EXISTS patients (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER,
                  gender TEXT,
                  disease TEXT)"""
)
conn.commit()


# Functions
def add_patient():
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    disease = disease_var.get()

    if name and age and gender and disease:
        cursor.execute(
            "INSERT INTO patients (name, age, gender, disease) VALUES (?, ?, ?, ?)",
            (name, age, gender, disease),
        )
        conn.commit()
        messagebox.showinfo("Success", "Patient added successfully")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")
    refresh_data()


def refresh_data():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM patients")
    for row in cursor.fetchall():
        tree.insert("", END, values=row)


# Tkinter GUI
root = Tk()
root.title("Hospital Management System")

# Input Fields
name_var = StringVar()
age_var = StringVar()
gender_var = StringVar()
disease_var = StringVar()

Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Age").grid(row=1, column=0, padx=10, pady=5)
Entry(root, textvariable=age_var).grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Gender").grid(row=2, column=0, padx=10, pady=5)
Entry(root, textvariable=gender_var).grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Disease").grid(row=3, column=0, padx=10, pady=5)
Entry(root, textvariable=disease_var).grid(row=3, column=1, padx=10, pady=5)

Button(root, text="Add Patient", command=add_patient).grid(
    row=4, column=0, columnspan=2, pady=10
)

# Data Table
from tkinter.ttk import Treeview

tree = Treeview(
    root, columns=("ID", "Name", "Age", "Gender", "Disease"), show="headings"
)
tree.grid(row=5, column=0, columnspan=2, pady=10)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Gender", text="Gender")
tree.heading("Disease", text="Disease")

refresh_data()

root.mainloop()
