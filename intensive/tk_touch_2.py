import tkinter as tk
from tkinter import ttk, filedialog
import os


# simple function
def btn_foo():
    entry_text = entry.get()
    print(entry_text)


def check_status():
    btn.config(state='enabled') if 'selected' in check.state() else btn.config(state='disabled')
    print(check_var.get())


# create the window
window = tk.Tk()
window.title('Window and widgets')
window.geometry('800x800+10+10')

# create a ttk widget
label = ttk.Label(master=window, text='Simple notepad')
label.pack()

# create widgets
text_widget = tk.Text(master=window)
text_widget.pack(pady=10)

# ttk entry
entry = ttk.Entry(master=window, width=106)
entry.pack()

# ttk buttons -> button, checkbox, radiobutton

buttons_frame = ttk.Frame(master=window, padding=(495, 10, 0, 10))
options_frame = ttk.Frame(master=window)

btn = ttk.Button(master=buttons_frame, text='Submit', command=btn_foo, state='disabled')
exit_btn = ttk.Button(master=buttons_frame, text='Quit', command=window.destroy)

check_var = tk.BooleanVar()
check = ttk.Checkbutton(options_frame, text='Checkbox_1', command=check_status, variable=check_var)

radio_var = tk.StringVar()
radio_1 = ttk.Radiobutton(
    options_frame,
    text='Radiobutton 1',
    value='type 1',
    variable=radio_var,
    command=lambda: print(radio_var.get()),
)
radio_2 = ttk.Radiobutton(
    options_frame,
    text='Radiobutton 2',
    value='type 2',
    variable=radio_var,
    command=lambda: print(radio_var.get())
)

buttons_frame.pack()
exit_btn.pack(side='right')
btn.pack(side='right')

options_frame.pack()
check.pack()
radio_1.pack()
radio_2.pack()


# file input
def open_file():
    file_name = filedialog.askopenfilename()
    entry_path.insert(tk.END, file_name)


file_path = tk.StringVar()

file_input_frame = ttk.Labelframe(master=window,
                                  text='File view module',
                                  padding=(10, 5, 10, 5))
file_input_frame.pack(side='top', fill='x', padx=10)
file_input_frame.columnconfigure(1, weight=2)

style = ttk.Style()
style.map("C.TButton",
          foreground=[('pressed', 'red'), ('active', 'blue')],
          background=[('pressed', '!disabled', 'black'), ('active', 'white')]
          )

ttk.Label(master=file_input_frame, text='File path').grid(row=0, column=0, sticky='ew')
entry_path = ttk.Entry(master=file_input_frame, textvariable=file_path)
entry_path.grid(row=0, column=1, sticky='ew', padx=3)
open_file_btn = ttk.Button(
    master=file_input_frame,
    text='Browse',
    command=open_file)
open_file_btn.grid(row=0, column=2, sticky='ew')
parse_file = ttk.Button(
    master=file_input_frame,
    text='Parse',
    style='C.TButton',
    command=lambda: print(file_path.get())
)
parse_file.grid(row=0, column=3, sticky='ew')

# run the window
window.mainloop()
