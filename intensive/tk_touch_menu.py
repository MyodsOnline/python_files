import tkinter as tk
from tkinter import ttk


window = tk.Tk()
height = window.winfo_screenheight()
window.geometry(f'600x{height-92}+0+0')
window.title('Tkinter menu')
window.attributes('-topmost', True)

window.bind('<Escape>', lambda event: window.quit())

# menu
menu = tk.Menu(window)

# sub_menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command=lambda: print('New file'))
file_menu.add_command(label='Open', command=lambda: print('Open file'))

file_menu.add_separator()
file_menu.add_command(label='Quit', command=window.destroy)

# another sub_menu
options_menu = tk.Menu(menu, tearoff=False)
options_menu.add_command(label='Label')
options_menu.add_separator()
option_1_check_string = tk.StringVar()
option_2_check_string = tk.StringVar()
option_3_check_string = tk.StringVar()
options_menu.add_checkbutton(label='check 1', onvalue='on', offvalue='off', variable=option_1_check_string)
options_menu.add_checkbutton(label='check 2', onvalue='on', offvalue='off', variable=option_2_check_string)
options_menu.add_checkbutton(label='check 3', onvalue='on', offvalue='off', variable=option_3_check_string)

menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Options', menu=options_menu)

window.configure(menu=menu)

# menu button
menu_btn = ttk.Menubutton(window, text='Menu button')
menu_btn.pack()

sub_menu_btn = tk.Menu(menu_btn, tearoff=False)
sub_menu_btn.add_command(label='Position 1', command=lambda: print('Position 1'))
sub_menu_btn.add_command(label='Position 2', command=lambda: print('Position 2'))
menu_btn.configure(menu=sub_menu_btn)


window.mainloop()
