sber_string = '5 сентября 2024 01:53:36'
description_string = 'Комиссия банку за карту'

month_dict = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12',
}


def convert_date_time(date_time_str, descript_str):
    date_part, month_part, year_part, time_part = date_time_str.split()
    time_part = time_part.replace(":", "-")
    month = month_dict[month_part.lower()]
    description = descript_str.replace(" ", "_")
    result = f"{year_part}-{month}-{date_part}__{time_part}__{description}"
    return result


if __name__ == '__main__':
    print(convert_date_time(sber_string, description_string))
