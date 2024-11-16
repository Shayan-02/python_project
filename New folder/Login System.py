from tkinter import *
from tkinter import messagebox
import subprocess


def login():
    user=username.get()
    code=password.get()

    if user=="R" and code=="1":

        #copy and paste your code here
        subprocess.run(['python', 'Bill_Manegment.py'])
        #end of code

    #all alerts , when  someone try to enter wrong username and password
    elif user=="" and code=="":
        messagebox.showerror("Invalid","please enter username and password")
    elif user=="":
        messagebox.showerror("Invalid","username is required")

    elif code=="":
        messagebox.showerror("Invalid","The password filed is required")
    
    elif user!="R" and code!="1":
        messagebox.showerror("Invalid","invalid username and password")

    elif user!="R":
        messagebox.showerror("Invalid,Please enter a valid username ")

    elif code!="1":
        messagebox.showerror("Invalid,Please enter a valid password")


def main_screen():

    global screen
    global username
    global password

    screen=Tk()
    screen.geometry("800x650+150+80")
    screen.configure(bg="#d7dae2")

    #icon
    image_icon=PhotoImage(file="login.png")
    screen.iconphoto(False,image_icon)
    screen.title("Login system")

    lblTitle=Label(text="Login System",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
    lblTitle.pack(pady=50)

    bordercolor=Frame(screen,bg="black",width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text="Username",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=50)
    Label(mainframe,text="password",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=150)
    
    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_password.place(x=400,y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe,text="Login",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=login).place(x=100,y=250)
    Button(mainframe,text="Reset",height="2",width=23,bg="#1089ff",fg="white",bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height="2",width=23,bg="#00db56",fg="white",bd=0,command=screen.destroy).place(x=500,y=250)

    


    screen.mainloop()

main_screen()