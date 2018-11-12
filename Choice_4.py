from tkinter import *
from data import *

def clear():
    for widget in F.winfo_children():
        widget.destroy()

def showall():
    clear()
    food_choice=[]
    for key in price_canteens:
        if key[1] not in food_choice:
            food_choice.append(key[1])
        else:
            pass
    r = 0
    for x in food_choice:
        Label(F, text=x).grid(row=r, columnspan=2,column=0,sticky=W+E)
        r += 1
    Button(F, text='quit', command=new_root.destroy).grid(row=r+2,columnspan=2,column=0,sticky=W+E)

def search():
    clear()
    cant_list = []
    name_raw=E1.get()
    name = ''.join(name_raw.split()).lower()
    for key in price_canteens:
        key_p = ''.join(key[1].split()).lower()
        if name == key_p:
            if key[0] not in cant_list:
                cant_list.append(key[0])
            else:
                pass
        else:
            pass
    Label(F, text="key: "+name_raw).grid(columnspan=2,column=0,sticky=W+E)
    if cant_list == []:
        Label(F, text="The food you have searched doesn't exist.").grid(columnspan=2,column=0,sticky=W+E)
        Button(F, text='quit', command=new_root.destroy).grid(columnspan=2, sticky='s')
    else:
        r = 1
        for x in cant_list:
            Label(F, text=x).grid(row=r, columnspan=2,column=0,sticky=W+E)
            r += 1
        Button(F, text='quit', command=new_root.destroy).grid(row=r + 2, columnspan=2, sticky='s')



new_root = Tk()
new_root.title("SEARCH FOOD BY NAME")
B1 = Button(new_root, text = "show all food choice", command=showall)
B1.grid(row=0,columnspan=2)
L1 = Label(new_root, text="Input Food Name")
L1.grid(row=1,column=0,sticky='e')
E1 = Entry(new_root)
E1.grid(row=1,column=1,sticky='w')
B2 = Button(new_root, text = "search", command=search)
B2.grid(row=2,columnspan=2)
F = Frame(new_root)
F.grid(row=3,columnspan=2)

new_root.mainloop()