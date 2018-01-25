from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("калкуляторус")
root.resizable(0, 0)

# calc logic
def calc(key):
    global memory
    if key == "=":
        # Remove letters from input
        str1 = "-+*/0123456789."
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, 'First letter is not number')
            messagebox.showerror( 'err', 'First letter is not number' )
        # counting
        try:
            result = eval( calc_entry.get() )
            calc_entry.insert( END, "="+str(result) )
        except:
            calc_entry.insert( END, "error" )
            messagebox.showerror( 'err', 'First letter is not number' )
    # clear input
    elif key == "C":
        calc_entry.delete(0, END)
    # changing - +
    elif key == "+/-":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == '-':
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, '-')
        except IndexError:
            pass
    else:
        if '=' in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# create all buttons
btn_list = [ 
    '7', '8', '9', '+', '-',
    '4', '5', '6', '*', '/',
    '1', '2', '3', '+/-', '=',
    '0', '.', 'C', '', ''
]

r = 1
c = 0
for i in btn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r,column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)
        
root.mainloop()