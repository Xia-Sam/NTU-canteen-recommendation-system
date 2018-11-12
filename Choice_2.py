from tkinter import *
from function import  *
from data import *
import tkinter.scrolledtext as ScrolledText


def clear():
    for widget in F.winfo_children():
        widget.destroy()

def result():
    clear()
    lower_str = E1.get()
    higher_str = E2.get()
    for widget in F.winfo_children():
        widget.destroy()

    try:
        higher = float(higher_str)
        lower = float(lower_str)
        if lower < 0:
            l3 = Label(F, text="Wrong value! Please retry")
            l3.pack()
        elif higher>10:
            l3 = Label(F, text="Wrong value! Please retry")
            l3.pack()
        elif lower>higher:
            l3 = Label(F, text="Wrong value! Please retry")
            l3.pack()

        else:
            price = (lower,higher)
            food_list = search_by_price(price,price_canteens)
            try:
                st = ScrolledText.ScrolledText(F)
                st.grid(sticky=W+E)
                for item in food_list:
                    st.insert(END, item+'\n')
                print(st.get(1.0, END))
            except TypeError:
                Label(F, text="No corresponding food!").grid(sticky='n')
                Button(F, text='close', command=new_root.destroy).grid(sticky='s')
    except ValueError:
        l=Label(F, text="Wrong data type! Please retry")
        l.pack()

new_root = Tk()
new_root.title("SEARCH FOOD BY PRICE")
L1 = Label(new_root, text="Please enter number from 0 to 10.").grid(row=0, columnspan=2)
L2 = Label(new_root, text="Lowest Price:").grid(row=1,column=0)
E1 = Entry(new_root, bd=5)
E1.grid(row=1,column=1)
L3 = Label(new_root, text="Highest Price:").grid(row=2,column=0)
E2 = Entry(new_root, bd=5)
E2.grid(row=2,column=1)
B1 = Button(new_root, text="search", command=result).grid(row=3,column=0)
B2 = Button(new_root, text="quit", command=new_root.destroy).grid(row=3,column=1)
F = Frame(new_root)
F.grid(row=4, column=0, columnspan=2)

new_root.mainloop()
