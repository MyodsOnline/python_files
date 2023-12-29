import csv


def get_data_from_csv():
    with open('тмп_Приложение 8_upd.csv', 'r', encoding='utf-8') as file:
        data = csv.reader(file, delimiter=";")
        header = next(data, None)
        out = []
        m_1 = str()
        m_2 = str()
        m_1_list = []
        m_2_list = []
        for row in data:
            if row[0]:
                m_1 = row[0]
                m_1_list.append(m_1)
            elif row[1]:
                m_2 = row[1]
                if m_2 not in m_2_list:
                    m_2_list.append(m_2)
                else:
                    continue
            else:
                row[0] = m_1
                row[1] = m_2
                out.append(row)
    # print(m_1_list)
    # for i in m_2_list:
    #     print(i)
    # for i in out:
    #     print(i)
    return out, m_1_list, m_2_list, header


def check_220():
    data, m_1_list, m_2_list, header = get_data_from_csv()
    """
        data - все значимые строки файла
        m_1_list - список ремонтных схем первого порядка
        m_2_list - список ремонтных схем второго порядка
    """
    for el in data, m_1_list, m_2_list, header:
        print(el)


def add_330(mmm):
    pass


if __name__ == '__main__':
    check_220()
    # get_data_from_csv()
