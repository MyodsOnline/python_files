import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('800x1000+50+50')
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

# Repair Scheme Selection area
scheme_selection_area = ttk.Labelframe(
    master=window, text='Выбор опций для расчета', padding=5
)
scheme_selection_area.pack(fill='x', padx=5, pady=5)
scheme_selection_area.columnconfigure(1, weight=1)

dependencies = ttk.Frame(master=scheme_selection_area)
dependencies.grid(row=0, column=0)
dependencies_title = ttk.Label(master=dependencies, text='Отметить схемы', font='TkTextFont 12 bold', justify='left')
dependencies_title.pack()

variable = tk.StringVar()

for k, v in dependencies_dict.items():
    ttk.Radiobutton(dependencies, variable=variable, text=v, value=k, command=lambda: print(variable.get()))\
        .pack(anchor='w', fill='x')

repair = ttk.Frame(master=scheme_selection_area)
repair.grid(row=0, column=1)
repair_title = ttk.Label(master=repair, text='Где переключаемся', font='TkTextFont 12 bold',)
repair_title.pack()


def foo():
    check_grid_option.config(text='Транзит 220 кВ замкнут') \
        if 'selected' in check_grid_option.state() \
        else check_grid_option.config(text='Транзит 220 кВ разомкнут')


check_grid_option = ttk.Checkbutton(repair, text='Состояние транзита 220 кВ', command=foo)
check_grid_option.pack()

lines = tk.StringVar()
combo = ttk.Combobox(repair, textvariable=lines)
combo['values'] = operations_list
combo.pack()


window.mainloop()
