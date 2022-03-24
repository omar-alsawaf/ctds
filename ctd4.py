from tkinter import *
from tkinter import messagebox
import hashlib
import string
invalidcharacters= set(string.punctuation)
def hashing(k):
    y=hashlib.md5(k.encode('utf-8')).hexdigest()
    return y;

def message():
    username=e1.get()
    password0=e2.get()  
    if (username=="" or password0==""):
        messagebox.showinfo("","MISSING USERNAME OR PASSWORD")
    elif any(char in invalidcharacters for char in password0 ):
        messagebox.showinfo("","PASSSWORD HAS SPECIAL CHARACTERS")
    elif any(char in invalidcharacters for char in username ):
        messagebox.showinfo("","USERNAME HAS SPECIAL CHARACTERS")
    else:
        password0=hashing(e2.get())
        if (username=="guest" and password0=="804c46cfec3d10628803370cfbc46b36"):
            messagebox.showinfo("","LOGIN SUCCESSFUL")
            root.destroy()
        else:
            messagebox.showinfo("","INCORRECT USERNAME OR PASSWORD")
        
    
root= Tk()
root.title("                                     Login")
root.geometry('500x400')
global e1
global e2
Label(root, text="Username:").place(x=10, y=10)
Label(root, text="Password:").place(x=10, y=80)
e1 = Entry(root)
e1.place(x=140, y=10)
e2 = Entry(root)
e2.place(x=140, y=80)
e2.config(show="*")
Button(root, text ="Login", command= message , height=3 ,width=10).place(x=50, y=150)

root.mainloop()
