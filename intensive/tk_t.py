import tkinter as tk
from tkinter import ttk, filedialog
import subprocess


def open_path():
    file_name = filedialog.askopenfilename()
    entry_path.insert(tk.END, file_name)


window = tk.Tk()
window.geometry('600x400')
window.title('Tkinter app')

path = tk.StringVar()

top_label = ttk.Labelframe(master=window, text='View apps file', padding=(20, 10, 5, 5))
top_label.pack(side='top', fill='x', padx=10)
top_label.columnconfigure(1, weight=1)

ttk.Label(master=top_label, text='Path').grid(row=0, column=0, padx=2, pady=2, sticky='ew')
entry_path = ttk.Entry(master=top_label, textvariable=path)
entry_path.grid(row=0, column=1, sticky='ew', pady=2, padx=2)
open_path_btn = ttk.Button(master=top_label, text='Browse', command=open_path, style='W.TButton')
open_path_btn.grid(row=0, column=2, sticky='ew', pady=2, padx=2)
parse_file = ttk.Button(master=top_label, text='Parse', command=lambda: print(path.get()))
parse_file.grid(row=0, column=3, sticky='ew', pady=2, padx=2)



# run window
window.mainloop()
