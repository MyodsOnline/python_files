import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Tab widget')

# tab widget
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
label_1 = ttk.Label(tab1, text='Text in tab 1')
label_1.pack()

tab2 = ttk.Frame(notebook)
label_2 = ttk.Label(tab2, text='Text in tab 2')
label_2.pack()

notebook.add(tab1, text='Gen list')
notebook.add(tab2, text='Line list')
notebook.pack()

window.mainloop()
