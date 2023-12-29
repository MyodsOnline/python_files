import textwrap
import copy
import tkinter as tk
from tkinter import ttk

from csv_getter import get_data_from_csv

window = tk.Tk()
window.geometry('1200x800')
window.title('Подготовка режима в сечении Невское')


out, m_1_list, m_2_list, header = get_data_from_csv()
calc_mask = ['a', 'b']


def wrap(string, length=60):
    return '\n'.join(textwrap.wrap(string, length))


def press_m_1_list():
    m_1_list_value = variable_m_1_list.get()
    if calc_mask[0] == 'a':
        calc_mask.pop(0)
        calc_mask.insert(0, m_1_list_value)
    else:
        calc_mask.pop(0)
        calc_mask.insert(0, m_1_list_value)
    if len(calc_mask) == 2 and calc_mask[0] != 'a' and calc_mask[1] != 'b':
        chose_m_3_list(calc_mask)


def press_m_2_list():
    m_2_list_value = variable_m_2_list.get()
    if calc_mask[1]:
        calc_mask.pop(1)
    calc_mask.insert(1, m_2_list_value)
    if len(calc_mask) == 2 and calc_mask[0] != 'a' and calc_mask[1] != 'b':
        chose_m_3_list(calc_mask)


def chose_m_3_list(calc_mask):
    csv_data = out
    frame_repair_unit = ttk.Frame(scheme_selection_area)

    for el in csv_data:
        if el[0] == calc_mask[0] and el[1] == calc_mask[1]:
            # print(el)
            frame_repair_unit.grid(row=1, column=2, sticky='nsew')
            ttk.Radiobutton(
                frame_repair_unit,
                text=f'{wrap(el[2], 66)}',
                value=el[2],
                variable=variable_m_3_list,
                style='TRadiobutton',
                command=press_m_3_list,
            ).pack(anchor='w', fill='x', padx=2)
    # ttk.Button(master=frame_repair_unit, text='Расчет', command=window.destroy).pack(side='bottom')


def press_m_3_list():
    m_3_list_value = variable_m_3_list.get()
    full_calc_mask = [itm for itm in calc_mask]
    if len(full_calc_mask) > 2:
        full_calc_mask.pop(2)
    full_calc_mask.append(m_3_list_value)
    draw_table(full_calc_mask)


def draw_table(full_calc_mask):
    calc_list = []
    for el in out:
        if el[0] == full_calc_mask[0] and el[1] == full_calc_mask[1] and el[2] == full_calc_mask[2]:
            calc_list = el[3:6]
            table.delete(*table.get_children())
            table.insert(parent='', index=0, values=list(map(wrap, calc_list)))


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
style.configure('TRadiobutton', anchor='nw', padding=3)
style.map('TRadiobutton', background=[('selected', 'lightblue')])

variable_m_1_list = tk.StringVar()
variable_m_2_list = tk.StringVar()
variable_m_3_list = tk.StringVar()

frame_220_unit = ttk.Frame(scheme_selection_area)
frame_220_unit.grid(row=1, column=0, sticky='nsew')
for el in m_1_list:
    ttk.Radiobutton(
        frame_220_unit,
        text=f'{wrap(el, 35)}',
        variable=variable_m_1_list,
        style='TRadiobutton',
        value=el,
        # command=lambda x=el: press_m_1_list(x)
        command=press_m_1_list,
    ).pack(anchor='nw', fill='x', pady=2)

frame_operation_unit = ttk.Frame(scheme_selection_area)
frame_operation_unit.grid(row=1, column=1, sticky='nsew')
for el in m_2_list:
    ttk.Radiobutton(
        frame_operation_unit,
        text=f'{wrap(el, 66)}',
        value=el,
        variable=variable_m_2_list,
        style='TRadiobutton',
        command=press_m_2_list,
    ).pack(anchor='w', fill='x', padx=2)

calculation_selection_area = ttk.Labelframe(master=window, text='Результаты расчета допустимого перетока при операциях', padding=5)
calculation_selection_area.pack(fill='x', padx=5, pady=5, )

table = ttk.Treeview(calculation_selection_area, columns=('first', 'last', 'third'), show='headings', height=3, padding=(5, 0))
table.heading(
    'first',
    text=f'{wrap("с отдельными выключателями и разъединителями")}', anchor='nw')
table.heading(
    'last',
    text=f'{wrap("по отключению сетевых элементов  (ЛЭП, АТ, СШ)")}', anchor='nw')
table.heading(
    'third',
    text='Примечания')
table.pack(fill='both', expand=True)

# run
window.mainloop()
