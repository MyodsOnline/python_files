import tkinter as tk
from tkinter import ttk


def btn_function():
    if entry.get():
        label.config(text=entry.get())
        entry.config(state='disabled')
    else:
        label.config(text='You should add text')


# create the window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x500+10+10')

# tkinter variable
string_var = tk.StringVar(value='')

# widgets
label = ttk.Label(master=window, text='Some text')
entry = ttk.Entry(master=window, width=50, textvariable=string_var)
button = ttk.Button(master=window, text='Submit', width=50, command=btn_function)
var_label = ttk.Label(master=window, text='basic text', textvariable=string_var)

# pack the widgets
label.pack(pady=5)
entry.pack()
button.pack(pady=5)
var_label.pack()

# run the window
window.mainloop()
