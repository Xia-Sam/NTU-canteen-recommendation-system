from tkinter import *
from data import *
import tkinter.scrolledtext as ScrolledText


def clear():
    for widget in F.winfo_children():
        widget.destroy()

def change_price():
    clear()
    key_c_raw = E1.get()
    key_c = ''.join(key_c_raw.split()).lower()
    key_f_raw = E2.get()
    key_f = ''.join(key_f_raw.split()).lower()
    val_p = E3.get()
    try:
        val = float(val_p)
        if val>0:
            mark = 0
            for key, value in price_canteens.items():
                key0p=''.join(key[0].split()).lower()
                key1p=''.join(key[1].split()).lower()
                if key_c == key0p and key_f == key1p:
                    price_canteens[key] = val
                    Label(F, text="You've changed the information successfully").grid()
                    mark = 1
                else:
                    pass
            if mark == 0:
                Label(F, text="The information is wrong, please retry!").grid()
            else:
                pass
        else:
            Label(F, text="The information is wrong, please retry!").grid()
    except ValueError or TypeError:
        Label(F, text="The information is wrong, please retry!").grid()


def del_item():
    clear()
    key_c = E1.get()
    key_f = E2.get()
    key_tup = (key_c,key_f)
    if key_tup in price_canteens:
        del price_canteens[key_tup]
        Label(F, text="You've deleted the item successfully").grid()
    else:
        Label(F, text="The information is wrong, please retry!").grid()


def add_item():
    clear()
    key_c_raw = E1.get()
    key_c = ''.join(key_c_raw.split()).lower()
    key_f_raw = E2.get()
    key_f = ''.join(key_f_raw.split()).lower()
    val_p = E3.get()
    mark = 0
    try:
        val = float(val_p)
        if val>0 and key_c!=None and key_f !=None:
            for key,value in price_canteens.items():
                key0p = ''.join(key[0].split()).lower()
                key1p = ''.join(key[1].split()).lower()
                if key_c==key0p and key_f == key1p and val == value:
                    mark = 1
                else:
                    pass
            if mark == 1:
                Label(F, text="This item already exists, please change your input").grid()
            else:
                price_canteens[(key_c,key_f)]=val
                Label(F, text="You've added the item successfully").grid()
        else:
            Label(F, text="Please input a valid information").grid()
    except ValueError:
        Label(F, text="Please input a valid information").grid()


def refresh():
    clear()
    st = ScrolledText.ScrolledText(F)
    st.pack()
    for key,value in price_canteens.items():
        st.insert(END, key[0]+"\t\t\t\t"+key[1]+"\t\t\t\tS$"+str(value)+"\n")
    print(st.get(1.0, END))



new_root = Tk()
new_root.title("UPDATE INFO")
L_P = Label(new_root, text= 'To change price, please fill all three blanks and click "change price"').grid(row=0,columnspan=4)
L_D = Label(new_root, text= 'To delete item, please fill the "canteen" and "dish", then click "delete item"').grid(row=1,columnspan=4)
L_A = Label(new_root, text= 'To add item, please fill all three blanks and click "add item"').grid(row=2,columnspan=4)
B1 = Button(new_root, text = "change price", command=change_price)
B1.grid(row=3,column=0)
B2 = Button(new_root, text = "delete item", command=del_item)
B2.grid(row=3,column=1)
B3 = Button(new_root, text = "add item", command=add_item)
B3.grid(row=3,column=2)
B4 = Button(new_root, text = "refresh", command=refresh)
B4.grid(row=3,column=3)
L1 = Label(new_root, text = "canteen(e.g.:canteen1)")
L1.grid(row = 4, column =0)
L2 = Label(new_root, text = "dish(e.g.:noodle)")
L2.grid(row = 4, column =1)
L3 = Label(new_root, text = "price(e.g.:3.5)")
L3.grid(row = 4, column =2)
B5 = Button(new_root, text = "quit", command=new_root.destroy)
B5.grid(row=4,column=3)

E1 = Entry(new_root)
E1.grid(row =5, column =0)
E2 = Entry(new_root)
E2.grid(row =5, column =1)
E3 = Entry(new_root)
E3.grid(row =5, column =2)
F = Frame(new_root)
F.grid(row=6,columnspan=3)
refresh()


new_root.mainloop()