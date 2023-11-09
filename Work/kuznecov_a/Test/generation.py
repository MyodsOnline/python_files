import datetime
import pprint
import os
from tabulate import tabulate

"""
Используются модули:
First - функция csv_parse - разбор csv, генерация json
Zero - выбор смены в зависимости от текущего времени
"""

from Top_secret.gen_list import *
from First import csv_parse, all_status_apps
from Zero import current_smena

power_plants_apps = power_plants
gen_app_complex = gen_app_complex

delimiter = f'{"-" * 60}'

current_shift = current_smena()


def get_all_gen_apps():
    print(current_shift)
    print(delimiter)
    all_apps = csv_parse()
    all_gen_apps = {}

    for el in all_apps['data']:
        for station in power_plants_apps.keys():
            if station == el['subject'] and el['complex'] in gen_app_complex and el['repair_type'] != 'ОГР':
                power_plants_apps[station].append(el)
    sorted(all_gen_apps)

    with open(os.path.join(my_folder, 'all_gen_apps.txt'), 'w+', encoding='utf-8', newline='\n') as file:
        file.write(f'{current_shift}\nПо генерации - {len(power_plants_apps)} заявок')

        for key, val in power_plants_apps.items():
            file.write(f'\n{delimiter}\n')
            file.write(f"{key.upper()} ({len(val)})\n")
            if len(val) > 0:
                print(f">>> {key.upper()} ({len(val)})\n", end='')

            for el in power_plants_apps[key]:
                if el['zvk_status'] == 'Открытая':
                    file.write(f"{el['self_number']:5}) {el['equipment']:10} {el['equipment_detail']} {el['repair_type']} "
                               f"{el['zvk_status']:10} до {el['end_date']}\n")
                    print(f"{el['self_number']:5}) {el['equipment']:10} {el['equipment_detail']} {el['repair_type']} "
                               f"{el['zvk_status']:10} до {el['end_date']}\n", end='')
                elif el['zvk_status'] == 'Разрешенная':
                    file.write(f"{el['self_number']:5}) {el['equipment']:10} {el['equipment_detail']} {el['repair_type']} "
                               f"{el['zvk_status']:10} c {el['start_date']}\n")
                else:
                    file.write(f"{el['self_number']:5}) {el['equipment']:10} {el['equipment_detail']} {el['repair_type']} "
                               f"{el['zvk_status']:10} c {el['asked_start_date']}\n")


if __name__ == '__main__':
    get_all_gen_apps()
