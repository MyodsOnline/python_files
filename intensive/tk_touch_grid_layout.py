import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('800x800')
window.title('Tkinter grid layout')


# commands
def toggle_label_place():
    global label_visibility
    if label_visibility:
        label_1.grid_forget()
        label_visibility = False
    else:
        label_visibility = True
        label_1.grid(row=0, column=0, sticky='nesw')


# useful variables
label_visibility = True

# widgets
label_1 = ttk.Label(window, text='label 1', background='#F0E68C')
label_2 = ttk.Label(window, text='label 2', background='#E0FFFF')
label_3 = ttk.Label(window, text='label 3', background='#808080')
label_4 = ttk.Label(window, text='label 4', background='#7CFC00')
button_1 = ttk.Button(window, text='Toggle lable', command=toggle_label_place)
button_2 = ttk.Button(window, text='Button 2', command=window.destroy)
entry = ttk.Entry(window)

# define a grid
window.columnconfigure((0, 1, 2), weight=1)
window.columnconfigure(3, weight=4)
window.rowconfigure((0, 1, 2), weight=1)
window.rowconfigure(3, weight=4)

# place a widget
label_1.grid(row=0, column=0, sticky='nesw')
label_2.grid(row=1, column=1, sticky='we', columnspan=2)
label_3.grid(row=2, column=2, sticky='ns', rowspan=3)
label_4.grid(row=3, column=3, sticky='nesw')
button_1.place(x=10, y=10)
button_2.grid(row=2, column=2, sticky='n')

# run
window.mainloop()
