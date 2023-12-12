import tkinter as tk
from tkinter import ttk
from random import choice


# main window
window = tk.Tk()
window.geometry('600x800+50+50')
window.title('Combobox widget')

# data
first_names = ['SLKJ', 'aslkdj', 'sdkjfh', 'askldj', 'qweqw', 'qweasd']
last_names = ['234', '345346', '2342', '2345345', '122', '3242']




# treeview
table = ttk.Treeview(window, columns=('first', 'last', 'email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Last name')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@email.com'
    data = (first, last, email)
    table.insert(parent='', index=0, values=data)


# events
def item_select(event):
    # print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])


table.bind('<<TreeviewSelect>>', item_select)

# items


# starter
window.mainloop()
