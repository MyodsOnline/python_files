import csv
import json
import os.path

PATH = os.path.join('Work/kuznecov_a/Test_data/', 'all.csv')


def parse_data_from_csv():
    with open('../Test_data/all.csv') as file_data:
        data_from_file = csv.reader(file_data, delimiter=';', dialect='excel')
        data_list = list(data_from_file)

        col = []
        for i in range(len(data_list)):
            col.append(data_list[i][7])
        print(set(col))

        # return data_list


"""
        opened = []
        allowed = []
        viewed = []
        not_viewed = []

        # status = []
        # komplex = []

        for i in range(len(data_list)):
            # status.append(data_list[i][5])
            # komplex.append(data_list[i][3])

            if data_list[i][5] == 'Открытая':
                opened.append(data_list[i])
            elif data_list[i][5] == 'Разрешенная':
                allowed.append(data_list[i])
            elif data_list[i][5] == 'Рассмотренная':
                viewed.append(data_list[i])
            elif data_list[i][5] == 'Не рассмотренная':
                not_viewed.append(data_list[i])
"""


def opened_app():
    opened = []
    all_apps = parse_data_from_csv()
    for row in all_apps:
        if row[5] == 'Открытая':
            opened.append(row)

    return opened


def generator_app():
    gen_opened = []
    gen_opened_apps = opened_app()
    title = '==== Открытые заявки getted now===='.upper()
    gen_opened.append(title)
    for row in gen_opened_apps:
        if row[3] == 'ЭНРГ.Б' or row[3] == 'ЭНРГ.ТГ' or row[3] == 'ЭНРГ.ГГ' or row[3] == 'ЭНРГ.ОО':

            if len(row[8]) != 0:
                row_str = f'{row[6]:25} || {row[8]:10} ==> {row[15]:5}'
            else:
                row_str = f'{row[6]:25} || {row[7][:8]:10} ==> {row[15]:5}'

            gen_opened.append(row_str)
            gen_opened.sort()

    for el in gen_opened:
        print(el)

            # row_str = row[0] + '    ' + row[6] + row[7][:17] + '    ' + row[15] + '/' + row[16].lower()
            # print(f'{row[0]} \t {row[6]} [{row[7][:17]}] \t {row[15]}/{row[16].lower()}')
            # gen_opened.append(row_str)

    # print('==== Открытые заявки ===='.upper())
    # for el in gen_opened:
    #     print(el)

    with open('text.csv', 'w', encoding='utf-8') as f:
        f.write('\n'.join(gen_opened))
        # for line in gen_opened:
        #     f.write(f'{line}\n')


# opened_app(parse_data_from_csv())

if __name__ == '__main__':
    parse_data_from_csv()




"""
    for row in data_list:
        # print(row)
        if row['Состояние заявки'] == 'Открытая':
            if row['Комплекс'] == 'ЭНРГ.Б':
            # print(f"{row['№ свой']} - {row['Объект']} - {row['Оборудование'][:20]} [{row['Категория']}/{row['Ремонт']}]"
            #       f" до {row['Разрешенное время -  конец'].split()[-1]} {row['Разрешенное время -  конец'].split()[0]}")
                allowed.append(row)
        print(allowed)
"""

