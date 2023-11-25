import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tkinter widget')
window.geometry('400x400+10+10')
window.resizable(False, False)
# window.config(bg='#FFFFE0')


def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(f'{km_output}')

# label widget
label_title = ttk.Label(master=window, text='Miles to kilometres', font=('Helvetica 24'))
label_title.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left')
button.pack(side='right')
input_frame.pack(pady=10)

# output field
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text='Output', font=('Helvetica 14'), textvariable=output_string)
output_label.pack()

# close window
close = ttk.Button(master=window, text='Quit', command=window.destroy, padding=10)
close.pack()

# start window
window.mainloop()
