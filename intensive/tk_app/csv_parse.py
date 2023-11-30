import csv
import os

from Top_secret.gen_list import FIELDS


def parse_csv(filename):
    with open(filename, encoding='cp1251') as file:
        data_from_file = csv.reader(file, delimiter=';', dialect='excel')
        data_list = list(data_from_file)

        date = data_list[0][0][-8:]
        data = data_list[2:]
        output_data = []

        for row in data:
            zvk_dict = dict(zip(FIELDS, row))
            output_data.append(zvk_dict)

        print(output_data)
        return f'Analysis of application for {date}'
