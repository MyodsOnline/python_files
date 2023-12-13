import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('600x400')
window.title('Layout intro')

# widgets
label_1 = ttk.Label(window, text='label 1', background='#F0E68C', padding=(10, 5, 10, 5))
label_2 = ttk.Label(window, text='label 2', background='#E0FFFF', padding=(10, 5, 10, 5))
label_3 = ttk.Label(window, text='label 3', background='#808080')
label_4 = ttk.Label(window, text='label 4', background='#7CFC00')
button_1 = ttk.Button(window, text='Button 1', command=window.destroy)
button_2 = ttk.Button(window, text='Button 2', command=window.destroy)

# # pack
# label_1.pack(side='left', expand=True, fill='both')
# label_2.pack(side='left', expand=True, fill='x')

# # grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=2)
# window.rowconfigure(0, weight=1)
# window.rowconfigure(1, weight=1)
#
# label_1.grid(row=0, column=1, sticky='nsew')
# label_2.grid(row=1, column=1, sticky='nsew', columnspan=2)

# # place
# label_1.place(x=100, y=200, width=200, height=100)
# label_2.place(relx=0.6, rely=0.4, relwidth=1, anchor='center')

# layout with pack
label_1.pack(side='top', fill='x')
label_2.pack(side='top')
label_3.pack(side='left', fill='both', ipadx=20)
button_1.pack(side='bottom', anchor='ne', fill='x')

window.mainloop()
