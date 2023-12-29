import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('800x800')
window.title('Combined layout')
window.minsize(800, 800)

menu_frame = ttk.Frame(window)
main_frame = ttk.Frame(window)

# main place layout
menu_frame.place(x=0, y=0, relwidth=0.2, relheight=1)
main_frame.place(relx=0.2, y=0, relwidth=0.8, relheight=1)

# menu widgets
menu_btn_1 = ttk.Button(menu_frame, text='Button 1')
menu_btn_2 = ttk.Button(menu_frame, text='Button 2')
menu_btn_3 = ttk.Button(menu_frame, text='Button 3')

menu_slider_1 = ttk.Scale(menu_frame, orient='vertical')
menu_slider_2 = ttk.Scale(menu_frame, orient='vertical')

toggle_frame = ttk.Frame(menu_frame)
menu_toggle_1 = ttk.Checkbutton(toggle_frame, text='check 1')
menu_toggle_2 = ttk.Checkbutton(toggle_frame, text='check 2')

entry = ttk.Entry(menu_frame)

# menu layout
menu_frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
menu_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

menu_btn_1.grid(row=0, column=0, sticky='nswe', columnspan=2)
menu_btn_2.grid(row=0, column=2, sticky='nswe', columnspan=1)
menu_btn_3.grid(row=1, column=0, sticky='nswe', columnspan=3)

menu_slider_1.grid(row=2, column=0, rowspan=2, sticky='nsew', pady=20)
menu_slider_2.grid(row=2, column=2, rowspan=2, sticky='nsew', pady=20)

# toggle layout
toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew')
menu_toggle_1.pack(side='left', expand=True)
menu_toggle_2.pack(side='left', expand=True)

# entry layout
entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor='center')

# main widgets
entry_frame_1 = ttk.Frame(main_frame)
main_label_1 = ttk.Label(entry_frame_1, text='label 1', background='#F0E68C')
main_btn_1 = ttk.Button(entry_frame_1, text=' Button 1')

entry_frame_2 = ttk.Frame(main_frame)
main_label_2 = ttk.Label(entry_frame_2, text='label 2', background='#808080')
main_btn_2 = ttk.Button(entry_frame_2, text=' Button 2')

# main layout
entry_frame_1.pack(side='left', expand=True, fill='both', padx=20, pady=20)
entry_frame_2.pack(side='left', expand=True, fill='both', padx=20, pady=20)

main_label_1.pack(expand=True, fill='both')
main_btn_1.pack(expand=True, fill='both', pady=10)
main_label_2.pack(expand=True, fill='both')
main_btn_2.pack(expand=True, fill='both', pady=10)

window.mainloop()
