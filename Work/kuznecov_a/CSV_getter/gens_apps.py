from csv_getter import parse_data_from_csv
from Work.kuznecov_a.Test.First import csv_parse


def print_data():
    all_apps = csv_parse()
    print('Печорская ГРЭС:')
    for el in all_apps['data']:
        if el['subgect'] == 'Печорская ГРЭС':
            print(f"{el['equipment']:10} - {el['repair_type']:3} - {el['zvk_status']:10} до {el['end_date']}")


print_data()


def get_all_apps():
    apps_list = parse_data_from_csv()
    all_apps = []

    for el in apps_list:
        if el[3] == 'ЭНРГ.Б' or el[3] == 'ЭНРГ.ТГ' or el[3] == 'ЭНРГ.ГГ' or el[3] == 'ЭНРГ.ОО':
            all_apps.append(el)
            # print(el)

    return all_apps


def sort_apps():
    all_apps = get_all_apps()

    kolaes_app = [el for el in all_apps if el[6] == 'Кольская АЭС']
    laes_app = []
    kigres_app = []
    nw_tes_app = ['===== Северо-Западная ТЭЦ =====']
    tes_5_app = ['===== Правобережная ТЭЦ =====']
    tes_21_app = ['===== Южная ТЭЦ =====']
    tes_14_app = ['===== Первомайская ТЭЦ =====']
    uz_tes_app = ['===== Юго-Западная ТЭЦ =====']
    tes_22_app = ['===== Южная ТЭЦ =====']
    novtes_app = ['===== Новгородская ТЭЦ =====']
    psgres_app = ['===== Псковская ГРЭС =====']
    kaltes_app = ['===== Калининградская ТЭЦ =====']
    pechgres_app = ['===== Печорская ГРЭС =====']
    kol_rdu_app = ['===== Кольское РДУ =====']
    kar_rdu_app = ['===== Карельское РДУ =====']
    len_rdu_app = ['===== Ленинградское РДУ =====']
    nov_rdu_app = ['===== Новгородское РДУ =====']
    balt_rdu_app = ['===== Балтийское РДУ =====']
    arh_rdu_app = ['===== Архангельское РДУ =====']
    komi_rdu_app = ['===== Коми РДУ =====']

    sorted_apps = []

    for el in all_apps:
        if el[6] == 'Кольская АЭС':
            if len(el[8]) != 0:
                append_str = f'{el[7]:10}/ {el[8]} - {el[15]} до {el[13]} [{el[0]}]'
            else:
                append_str = f'{el[7]:10} - {el[15]} до {el[13]} [{el[0]}]'

            kolaes_app.append(append_str)
            # kolaes_app.sort()
        elif el[6] == 'Ленинградская АЭС':
            laes_app.append(el)
            laes_app.sort()
        elif el[6] == 'Киришская ГРЭС' and el[3] == 'ЭНРГ.Б':
            append_str = f'{el[7]:10} - {el[15]} до {el[13]} [{el[0]}]'
            kigres_app.append(append_str)
            kigres_app.sort()


    print('===== Кольская АЭС =====')
    for el in kolaes_app:
        print(el)
    print('===== Ленинградская АЭС =====')
    for el in laes_app:
        print(el)
    print('===== Киришская ГРЭС =====')
    for el in kigres_app:
        print(el)


# sort_apps()


def get_kolaes_app():
    all_apps = get_all_apps()
    kolaes_app = [el for el in all_apps if el[6] == 'Кольская АЭС']
    kolaes_list = []

    blok_1 = [el for el in kolaes_app if el[7] == 'Блок 1']
    blok_1_str = str()
    if len(blok_1) != 0:
        for el in blok_1:
            if len(el[8]) != 0:
                blok_1_str = f'{el[7]:10}/ {el[8]} - {el[15]} до {el[13]} [{el[0]}]'
            else:
                blok_1_str = f'{el[7]:10} - {el[15]} до {el[13]} [{el[0]}]'
        kolaes_list.append(blok_1_str)
    else:
        blok_1_str = 'Блок 1'
        kolaes_list.append(blok_1_str)

    blok_2 = [el for el in kolaes_app if el[7] == 'Блок 2']
    blok_2_str = str()
    if len(blok_2) != 0:
        for el in blok_2:
            if len(el[8]) != 0:
                blok_2_str = f'{el[7]:10}/ {el[8]} - {el[15]} до {el[13]} [{el[0]}]'
                kolaes_list.append(blok_2_str)
            else:
                blok_2_str = f'{el[7]:10} - {el[15]} до {el[13]} [{el[0]}]'
                kolaes_list.append(blok_2_str)
    else:
        blok_2_str = 'Блок 2'
        kolaes_list.append(blok_2_str)

    for el in kolaes_app:
        print(el)
    print(kolaes_list)
