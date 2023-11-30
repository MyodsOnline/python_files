import tkinter as tk
from tkinter import ttk
import textwrap

from fff import repair_dict


window = tk.Tk()
window.geometry('800x415+50+50')
window.title('Сечение Невское')


operations_list = [
    'ВЛ 330 кВ Ленинградская АЭС – Восточная',
    'ВЛ 330 кВ Ленинградская – Колпино I цепь',
    'ВЛ 330 кВ Ленинградская – Колпино II цепь',
    'КВЛ 330 кВ Восточная – Колпино I цепь',
    'ВЛ 330 кВ Восточная – Колпино II цепь',
    'ВЛ 330 кВ Восточная – Звёздная',
    'ВЛ 330 кВ Киришская ГРЭС – Чудово',
    'ВЛ 330 кВ Ленинградская – Чудово',
    'КВЛ 330 кВ Киришская ГРЭС – Восточная I цепь',
    'ВЛ 750 кВ Ленинградская АЭС – Ленинградская',
    'Выключатели'
]

operations_dict = {
    '1': 'ВЛ 330 кВ Ленинградская АЭС – Восточная',
    '2': 'ВЛ 330 кВ Ленинградская – Колпино I цепь',
    '3': 'ВЛ 330 кВ Ленинградская – Колпино II цепь',
    '4': 'КВЛ 330 кВ Восточная – Колпино I цепь',
    '5': 'ВЛ 330 кВ Восточная – Колпино II цепь',
    '6': 'ВЛ 330 кВ Восточная – Звёздная',
    '7': 'ВЛ 330 кВ Киришская ГРЭС – Чудово',
    '8': 'ВЛ 330 кВ Ленинградская – Чудово',
    '9': 'КВЛ 330 кВ Киришская ГРЭС – Восточная I цепь',
    '10': 'ВЛ 750 кВ Ленинградская АЭС – Ленинградская',
    '11': 'Выключатели'
}

dependencies_dict = {
    '0': 'Нормальная',
    '1': 'Ремонт ВЛ 330 кВ Ленинградская – Колпино I цепь',
    '2': 'Ремонт ВЛ 330 кВ Ленинградская – Колпино II цепь',
    '3': 'Ремонт или не в транзите ВЛ 330 кВ Восточная – Звёздная',
    '4': 'Ремонт КВЛ 330 кВ Восточная – Колпино I цепь',
    '5': 'Ремонт ВЛ 330 кВ Восточная – Колпино II цепь',
    '6': 'Ремонт или не в транзите ВЛ 330 кВ Киришская ГРЭС – Чудово',
    '7': 'Ремонт или не в транзите ВЛ 330 кВ Ленинградская АЭС – Восточная',
    '8': 'Ремонт ВЛ 750 кВ Ленинградская АЭС – Ленинградская'
}

main_grid_options = ('Замкнут',
                     'Разомкнут')


def update_out_by_220():
    check_grid_option.config(text='Транзит 220 кВ замкнут') \
        if 'selected' in check_grid_option.state() \
        else check_grid_option.config(text='Транзит 220 кВ разомкнут')
    output[1] = check_220_var.get()
    test_output()


def update_out_by_dependencies():
    output[2] = variable.get()
    test_output()


def update_out_by_lines(event):
    output[0] = operations_list.index(combo.get())
    count_btn.config(state='enabled')
    test_output()


def test_output():
    for el in output:
        print(el, type(el))


def count():
    string = str()
    for i in output:
        string += str(i)
    print(string)

    for key, value in repair_dict.items():
        if key == string:
            print(value)
            insert_row(value)


def wrap(string, length=35):
    return '\n'.join(textwrap.wrap(string, length))


def insert_row(value):
    table.delete(*table.get_children())
    table.insert(parent='', index=0, values=list(map(wrap, value)))


# Repair Scheme Selection area
scheme_selection_area = ttk.Labelframe(
    master=window, text='Выбор опций для расчета', padding=5
)
scheme_selection_area.pack(fill='x', padx=5, pady=5,)
scheme_selection_area.columnconfigure(1, weight=1)

dependencies = ttk.Frame(master=scheme_selection_area)
dependencies.grid(row=0, column=0)
dependencies_title = ttk.Label(master=dependencies, text='Отметить схемы', font='TkTextFont 12 bold', justify='left')
dependencies_title.pack()

variable = tk.IntVar()

for k, v in dependencies_dict.items():
    ttk.Radiobutton(dependencies, variable=variable, text=v, value=k, command=update_out_by_dependencies)\
        .pack(anchor='w', fill='x')

repair = ttk.Frame(master=scheme_selection_area)
repair.grid(row=0, column=1,)
repair_title = ttk.Label(master=repair, text='Где переключаемся', font='TkTextFont 12 bold',)
repair_title.pack(side='top', fill="x", anchor='n')


check_220_var = tk.IntVar()
check_grid_option = ttk.Checkbutton(
    repair,
    text='Состояние транзита 220 кВ',
    command=update_out_by_220,
    width=100,
    variable=check_220_var,
)
check_grid_option.pack()

lines = tk.StringVar()
combo = ttk.Combobox(repair, textvariable=lines, width=58, height=15)
combo['values'] = operations_list
combo.pack()
combo.bind('<<ComboboxSelected>>', update_out_by_lines)

count_btn = ttk.Button(master=repair, text='Расчет', state='disabled', command=count)
count_btn.pack(side='right', padx=1)


# business logic
output = [lines.get() if lines.get() else None, check_220_var.get(), variable.get()]

# calculation result
calculation_result = ttk.Labelframe(master=window, text='Результат расчета', padding=5)
calculation_result.pack(fill='x', padx=5, pady=5,)
scheme_selection_area.columnconfigure(1, weight=1)

table = ttk.Treeview(calculation_result, columns=('first', 'last', 'third'), show='headings', height=3)
table.heading('first', text='Отключение линии')
table.heading('last', text='Операции с выключателями')
table.heading('third', text='Примечания')
table.pack(fill='both', expand=True)

ttk.Button(master=window, text='Выход', command=window.destroy).pack(side='right', padx=10)


window.mainloop()
