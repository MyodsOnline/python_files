import csv
import os

from Top_secret.gen_list import FIELDS

PATH = 'D:/Stydy/my_own_project/python_files/python_files/intensive/tk_app/Top_secret/2811.csv'


def parse_csv(filename):
    with open(filename, encoding='cp1251') as file:
        data_from_file = csv.reader(file, delimiter=';', dialect='excel')
        data_list = list(data_from_file)

        date = f'Analysis for {data_list[0][0][-8:]}'
        data = data_list[2:]
        output_data = []

        for row in data:
            zvk_dict = dict(zip(FIELDS, row))
            output_data.append(zvk_dict)

        return date, output_data


def get_gen_list():
    date, output_data = parse_csv(PATH)
    gen_list = [{k: item[k] for k in ['subject', 'equipment', 'zvk_status']}
                for item in output_data
                if item['complex'] == 'ЭНРГ.Б'
                or item['complex'] == 'ЭНРГ.ТГ']

    # print(gen_list)
    return gen_list


def get_line_list():
    date, output_data = parse_csv(PATH)
    line_list = [{k: item[k] for k in ['subject', 'equipment', 'zvk_status']}
                 for item in output_data
                 if item['complex'] == 'ЛЭП.ЛЭП 330 кВ'
                 or item['complex'] == 'ЛЭП.ЛЭП 750 кВ'
                 and item['mode'] == 'с отключением']

    for el in line_list:
        print(el)
    return line_list


if __name__ == '__main__':
    # parse_csv('D:/Stydy/my_own_project/python_files/python_files/intensive/tk_app/Top_secret/2811.csv')
    get_line_list()
