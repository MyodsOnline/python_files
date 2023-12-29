import tkinter as tk
from tkinter import ttk
import textwrap

from csv_getter import get_data_from_csv


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.geometry(f'{size[0]}x{size[1]}')
        self.title(title)
        self.minsize(size[0], size[1])

        # data
        self.out, self.m_1_list, self.m_2_list, self.header = get_data_from_csv()

        # widgets
        self.menu = Menu(self)

        # run app
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ttk.Label(self, background='#F0E68C').pack(expand=True, fill='both')
        self.place(x=0, y=0, relwidth=1, relheight=0.7)
        self.out, self.m_1_list, self.m_2_list, self.header = get_data_from_csv()
        self.create_widgets()

    def wrap(string, length=35):
        return '\n'.join(textwrap.wrap(string, length))

    def create_widgets(self):
        scheme_selection_area = ttk.Labelframe(
            master=self, text='Выбор опций для расчета', padding=5
        )
        scheme_selection_area.columnconfigure(0, weight=1, uniform='a')
        scheme_selection_area.columnconfigure((1, 2), weight=2, uniform='a')
        scheme_selection_area.rowconfigure(0, weight=1, uniform='a')
        scheme_selection_area.rowconfigure(1, weight=int(len(self.m_2_list)), uniform='a')
        scheme_selection_area.pack(fill='x', padx=5, pady=5, )

        label_m_1_list = ttk.Label(scheme_selection_area, background='#F0E68C', text='First')
        label_m_2_list = ttk.Label(scheme_selection_area, background='#E0E68C', text='Second')
        label_m_3_list = ttk.Label(scheme_selection_area, background='#A0E68C', text='Third')

        label_m_1_list.grid(row=0, column=0)
        label_m_2_list.grid(row=0, column=1)
        label_m_3_list.grid(row=0, column=2)

        table = ttk.Treeview(scheme_selection_area, columns=('first',), show='headings', height=3)
        table.heading('first', text='Учитываемые элементы:')
        table.grid(row=1, column=2, sticky='nsew')

        frame_220_unit = ttk.Frame(scheme_selection_area)
        frame_220_unit.grid(row=1, column=0, sticky='nsew')

        for el in self.m_1_list:
            ttk.Radiobutton(frame_220_unit, text=f'{self.wrap(el)}', value=f'{el}').pack(anchor='w', fill='x')

        frame_operation_unit = ttk.Frame(scheme_selection_area)
        frame_operation_unit.grid(row=1, column=1, sticky='nsew')

        for el in self.m_2_list:
            ttk.Radiobutton(frame_operation_unit, text=f'{el}', value=f'{el}').pack(anchor='w', fill='x')


# create an App instance
App('Class based app', (1200, 600))