import tkinter as tk
from tkinter import ttk, filedialog
import os

from csv_parse import parse_csv


window = tk.Tk()
window.geometry('600x800+100+100')
window.title('Tkinter apps app')
window.minsize(600, 800)
# window.overrideredirect(True)


# definitions
def open_path():
    file_name = filedialog.askopenfilename()
    entry_path.insert(tk.END, file_name)


def get_file_name():
    output_label.config(text=f'{parse_csv(path.get())} from file "{os.path.basename(path.get())}"')
    entry_path.delete(0, 'end')
    path.set('')


# file input area
path = tk.StringVar()

file_input_area = ttk.Labelframe(
    master=window,
    text='View apps file',
    padding=5)
file_input_area.pack(side='top', fill='x', padx=5, pady=5)
file_input_area.columnconfigure(1, weight=1)

ttk.Label(master=file_input_area, text='File path', anchor='nw', padding=(-3, 0, 3, 0)).grid(row=0, column=0, pady=2, sticky='w')
entry_path = ttk.Entry(master=file_input_area, textvariable=path)
entry_path.grid(row=0, column=1, sticky='ew', pady=2, padx=2)
open_path_btn = ttk.Button(
    master=file_input_area,
    text='Browse',
    command=open_path,
    style='W.TButton')
open_path_btn.grid(row=0, column=2, sticky='ew', pady=2, padx=2)
parse_file = ttk.Button(
    master=file_input_area,
    text='Parse',
    command=get_file_name)
parse_file.grid(row=0, column=3, sticky='ew', pady=2, padx=2)


# parsed file data
output_area = ttk.Labelframe(
    master=window,
    text='View file data',
    padding=5)
output_area.pack(fill='x', padx=5, pady=5)
output_area.columnconfigure(1, weight=1)

output_label = ttk.Label(master=output_area, anchor='c', font='TkTextFont 12')
output_label.grid(row=0, column=0, sticky='w')


# service buttons area
serv_btn = ttk.Frame(master=window)
serv_btn.pack(padx=12, fill='x')
info_btn = ttk.Button(master=serv_btn, command=window.destroy, text='Quit')
info_btn.pack(side='right', padx=2)
close_btn = ttk.Button(master=serv_btn, command=window.destroy, text='Info')
close_btn.pack(side='right', padx=2)

window.mainloop()
