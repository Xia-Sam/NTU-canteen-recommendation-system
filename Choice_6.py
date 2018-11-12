from tkinter import *
from data import *

def clear():
    for widget in F.winfo_children():
        widget.destroy()


def display():
    clear()
    find = 0
    str = E1.get()
    str_a = ''.join(str.split())
    str_a = str_a.lower()
    for key,value in service_time_info.items():
        key_j = ''.join(key.split())
        if str_a == key_j:
            Label(F, text=str+": "+value).grid()
            find = 1
        else:
            pass
    if find == 0:
        Label(F, text="The information is wrong, please retry!").grid()

new_root = Tk()
new_root.title("OPENING HOUR")
L_P = Label(new_root, text= 'Input the name of canteen you want to search.').grid(row=0)

L1 = Label(new_root, text = "canteen name: (e.g.:canteen1)")
L1.grid(row = 1, column =0)
E1 = Entry(new_root)
E1.grid(row =2, column =0)
B1 = Button(new_root, text = "search", command=display)
B1.grid(row=3,column=0)
F = Frame(new_root)
F.grid(row=4)
Button(new_root, text='close', command=new_root.destroy).grid(sticky='s')
mainloop()


