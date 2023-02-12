import os

from Top_secret.gen_list import *
from First import csv_parse, all_status_apps
from Zero import current_smena


delimiter = f'{"-" * 60}'

current_shift = current_smena()

all_apps = csv_parse()
all_grid_apps = []
opened_grid_apps = []
approved_grid_apps = []

# dc_all = dc_ru + dc_eu
dc_all = [dc_ru, dc_eu]


def get_all_grid_apps(dc_el):

    for el in all_apps['data']:
        if el['complex'] in grid_app_complex and el['mode'] == 'с отключением' and el['zvk_giver'] in dc_el:
            if el['zvk_status'] == 'Открытая':
                opened_grid_apps.append(el)
            elif el['zvk_status'] == 'Разрешенная':
                approved_grid_apps.append(el)
            else:
                all_grid_apps.append(el)

    # print(all_grid_apps[0].keys())

    if opened_grid_apps:
        with open(os.path.join(my_folder, 'all_grid_apps.txt'), 'w', encoding='utf-8', newline='\n') as file:
            file.write(current_shift)
            file.write(f'\n{delimiter}\n{("Открытые заявки -").upper()} {len(opened_grid_apps)}\n')
            for open_app in opened_grid_apps:
                file.write(f"{open_app['self_number']:5}|{open_app['repair_type']:3}|{open_app['zvk_type']:3}| - "
                           f"{open_app['equipment']:46} до {open_app['end_date']} АГ:{open_app['ag']}\n")

    if approved_grid_apps:
        with open(os.path.join(my_folder, 'all_grid_apps.txt'), 'a+', encoding='utf-8', newline='\n') as file:
            file.write(f'\n{delimiter}\n{("Разрешенные заявки -").upper()}{len(approved_grid_apps)}\n')
            for approved_app in approved_grid_apps:
                file.write(f"{approved_app['self_number']:5}|{approved_app['repair_type']:3}|{approved_app['zvk_type']:3}| "
                           f"- {approved_app['equipment']} c {approved_app['asked_start_date']}\n")

    with open(os.path.join(my_folder, 'all_grid_apps.txt'), 'a+', encoding='utf-8', newline='\n') as file:
        file.write(f'\n{delimiter}\n{("Прочие заявки -").upper()}{len(all_grid_apps)}\n')
        for string in all_grid_apps:
            file.write(f"{string['self_number']:05}|{string['repair_type']:03}|{string['zvk_type']:03}|"
                       f"{string['zvk_status']:16}| - {string['equipment']} с {string['asked_start_date']}\n")


if __name__ == '__main__':
    # get_all_grid_apps(dc_ru)
    for el in dc_all:
        get_all_grid_apps(el)
