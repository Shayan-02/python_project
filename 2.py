from calendar import *
from tkinter import *


def show_calender():
    year = y_ent.get()
    month = m_ent.get()
    c_lbl.configure(calendar(year, month))
    

root = Tk()

y_lbl = Label(root, text="year").place(x=5, y=10)
y_ent = Entry(root)
y_ent.place(x=40, y=10)

m_lbl = Label(root, text="month").place(x=5, y=40)
m_ent = Entry(root)
m_ent.place(x=40, y=40)

c_btn = Button(root, text="click me", command=show_calender).place(x=40, y=100)

c_lbl = Label(root, text="")

root.mainloop()