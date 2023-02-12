import csv
import json
import os
import datetime

from Top_secret.gen_list import FIELDS

PATH = os.path.dirname(__file__)


def csv_parse():
    with open('../Test_data/all.csv', encoding='utf-8') as file_data:
        data_from_file = csv.reader(file_data, delimiter=';', dialect='excel')
        data_list = list(data_from_file)

        date = data_list[0][0][-8:]
        data = data_list[2:]

        output_data = []
        # gen_app = []

        for row in data:
            zvk_dict = dict(zip(FIELDS, row))
            output_data.append(zvk_dict)

    # with open('all_apps.json', 'w+', encoding='utf-8') as zvk_json:
    #     for row in data:
    #         zvk_dict = dict(zip(FIELDS, row))
    #         print(zvk_dict)
    #         output_data.append(zvk_dict)
    #         tmp = json.dumps(zvk_dict, ensure_ascii=False, indent=4)
    #         zvk_json.write(tmp)
    #         # json.dump(zvk_dict, zvk_json, ensure_ascii=False, indent=4)
    #     print(f'\033[34mCurrent date: {datetime.date.today().strftime("%d.%m.%y")} \nApplication date: {date}')

    return {'date': date, 'data': output_data}


def all_status_apps():
    all_apps = csv_parse()

    opened_apps = []
    approved_apps = []
    viewed_apps = []
    not_viewed_apps = []
    error_parsed_apps = []

    for row in all_apps['data']:
        if row['zvk_status'] == 'Открытая':
            opened_apps.append(row)
        elif row['zvk_status'] == 'Разрешенная':
            approved_apps.append(row)
        elif row['zvk_status'] == 'Рассмотренная':
            viewed_apps.append(row)
        elif row['zvk_status'] == 'Не рассмотренная':
            not_viewed_apps.append(row)
        else:
            error_parsed_apps.append(row)

    # opened_apps = [el for el in all_apps['data'] if el['zvk_status'] == 'Открытая']
    # approved_apps = [el for el in all_apps['data'] if el['zvk_status'] == 'Разрешенная']
    # viewed_apps = [el for el in all_apps['data'] if el['zvk_status'] == 'Рассмотренная']
    # not_viewed_apps = [el for el in all_apps['data'] if el['zvk_status'] == 'Рассмотренная']

    return {'opened_apps': opened_apps, 'approved_apps': approved_apps, 'viewed_apps': viewed_apps,
            'not_viewed_apps': not_viewed_apps}


if __name__ == '__main__':
    all_status_apps()
