import tkinter as tk
from tkinter import ttk


# main window
window = tk.Tk()
window.geometry('500x800+50+50')
window.title('Combobox widget')

# combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar()
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
combo.pack()

combo_label = ttk.Label(window, text='Chose what you want')
combo_label.pack()

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text=f'Selected value: {food_string.get()}'))

# spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(
    window,
    from_=3,
    to=20,
    increment=3,
    textvariable=spin_int,
    command=lambda: print(spin_int.get())
)
spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('down'))
# spin['values'] = (1, 2, 3, 4, 5)
spin.pack()

# starter
window.mainloop()
