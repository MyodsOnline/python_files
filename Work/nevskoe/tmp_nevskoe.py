import textwrap
import tkinter as tk
from tkinter import ttk

from csv_getter import get_data_from_csv

window = tk.Tk()
window.geometry('1200x800')
window.title('Подготовка режима в сечении Невское')


out, m_1_list, m_2_list, header = get_data_from_csv()


def wrap(string, length=35):
    return '\n'.join(textwrap.wrap(string, length))


def press_m_1_list(value):
    m_1_list_value = value
    frame_operation_unit = ttk.Frame(scheme_selection_area)
    frame_operation_unit.grid(row=1, column=1, sticky='nsew')
    for el in m_2_list:
        ttk.Button(frame_operation_unit, text=f'{wrap(el, 66)}', style='Kim.TButton', command=lambda x=el: press_m_2_list(x)) \
            .pack(anchor='nw', fill='x', padx=2)
    return m_1_list_value


def press_m_2_list(value):

    print(value)


scheme_selection_area = ttk.Labelframe(master=window, text='Выбор опций для расчета', padding=5)
scheme_selection_area.columnconfigure(0, weight=1, uniform='a')
scheme_selection_area.columnconfigure((1, 2), weight=2, uniform='a')
scheme_selection_area.rowconfigure(0, weight=1, uniform='a')
scheme_selection_area.rowconfigure(1, weight=int(len(m_2_list)), uniform='a')
scheme_selection_area.pack(fill='x', padx=5, pady=5, )

ttk.Label(scheme_selection_area, background='#F0E68C', text='First').grid(row=0, column=0)
ttk.Label(scheme_selection_area, background='#E0E68C', text='Second').grid(row=0, column=1)
ttk.Label(scheme_selection_area, background='#A0E68C', text='Third').grid(row=0, column=2)

style = ttk.Style()
style.configure('Kim.TButton', foreground='black', anchor='nw', padding=3)
style.map('Kim.TButton', background=[('pressed', 'red')])

variable = tk.StringVar()

frame_220_unit = ttk.Frame(scheme_selection_area)
frame_220_unit.grid(row=1, column=0, sticky='nsew')
for el in m_1_list:
    ttk.Button(frame_220_unit, text=f'{wrap(el)}', style='Kim.TButton', command=lambda x=el: press_m_1_list(x))\
        .pack(anchor='nw', fill='x', pady=2)


# for el in m_2_list:
#     ttk.Button(frame_operation_unit, text=f'{wrap(el, 66)}', style='Kim.TButton', command=lambda x=el: press(x))\
#         .pack(anchor='nw', fill='x', padx=2)
#     # ttk.Radiobutton(frame_operation_unit, text=f'{wrap(el, 66)}', value=f'{el}').pack(anchor='w', fill='x', padx=2)

# table = ttk.Treeview(scheme_selection_area, columns=('first',), show='headings', height=3)
# table.heading('first', text='Учитываемые элементы:')
table = ttk.Treeview(scheme_selection_area, columns=('first',), height=2)
table.grid(row=1, column=2, sticky='nsew')

# run
window.mainloop()
