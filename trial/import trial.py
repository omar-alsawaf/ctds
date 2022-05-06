def ctd5():
    import ctd5

def ctd4():
    import ctd4

from tkinter import *
root=Tk()
root.title("misssion 3.2")
root.geometry('1000x1000')
Button(root, text ="ctd5", command= ctd5 , height=3 ,width=10).place(x=50, y=150)
Button(root, text ="ctd4", command= ctd4 , height=3 ,width=10).place(x=150, y=150)
root.mainloop()