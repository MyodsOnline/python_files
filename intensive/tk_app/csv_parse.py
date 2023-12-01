import csv
import os

from Top_secret.gen_list import FIELDS


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

        # gen_list = [item for item in output_data if item['complex'] == 'ЭНРГ.Б' or item['complex'] == 'ЭНРГ.ТГ']
        gen_list = [{k: item[k] for k in ['subject', 'equipment', 'zvk_status']}
                    for item in output_data
                    if item['complex'] == 'ЭНРГ.Б'
                    or item['complex'] == 'ЭНРГ.ТГ']
        print(gen_list)
        # gen_list.sort() # make sorting
        # for el in gen_list:
        #     print(el['subject'], el['equipment'])

        # return f'Analysis of application for {date}'
        return date, gen_list


if __name__ == '__main__':
    parse_csv('D:/Stydy/my_own_project/python_files/python_files/intensive/tk_app/Top_secret/2811.csv')