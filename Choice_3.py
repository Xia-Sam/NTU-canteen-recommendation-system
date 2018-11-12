from tkinter import *
from function import *
from data import *

def clear():
    for widget in F.winfo_children():
        widget.destroy()


def check_rank():
    clear()
    ratelist=rate(ranklist)
    r = 0
    for x in ratelist:
        Label(F, text=x).grid(row=r, sticky="w")
        r += 1
    Button(F, text='close', command=new_root.destroy).grid(sticky='s')

def update_rank():
    clear()
    name_raw = E1.get()
    name = ''.join(name_raw.split()).lower()
    rate_str = E2.get()
    mark = 0
    try:
        rate = float(rate_str)
        if 0<=rate<=5:
            for key,value in ranklist.items():
                key_j = ''.join(key.split()).lower()
                if name == key_j:
                    value.append(rate)
                    Label(F, text="We have received your rate. Thank you!").grid()
                    mark = 1
                else:
                    pass
            if mark == 0:
                Label(F, text="The canteen doesn't exist or your input have something wrong. Please try again").grid()
            else:
                pass
        else:
            Label(F, text="Please input a rate between 0 to 5!").grid()
    except ValueError or TypeError:
        Label(F, text="Please give a number").grid()
    finally:
        Button(F, text='close', command=new_root.destroy).grid(sticky='s')


new_root=Tk()
new_root.title("RATE OF CANTEENS")
B1 = Button(new_root, text = "Rate the Canteen", command=update_rank)
B1.grid(row=0,column=0)
B2 = Button(new_root, text = "Check Ranklist", command=check_rank)
B2.grid(row=0,column=1)
L1 = Label(new_root, text="canteen(e.g.:canteen1)")
L1.grid(row=1, column=0)
L2 = Label(new_root, text="rate(from 0 to 5)")
L2.grid(row=1, column=1)
E1 = Entry(new_root)
E1.grid(row=2, column=0)
E2 = Entry(new_root)
E2.grid(row=2, column=1)
F = Frame(new_root)
F.grid(row=3, column=0, columnspan=2)



new_root.mainloop()
