import unittest

# тестовый словарь {температура: ток}
application_11 = {
    '-10': 2000,
    '-5': 2000,
    '0': 2000,
    '5': 1800,
    '10': 1700,
    '15': 1650,
    '20': 1500,
    '25': 1400,
    '30': 1300,
}


def permissible_current(input_value):
    '''
    Возвращает допустимую токовую нагрузку в зависимости от заданой температуры
    '''

    # список температур из словаря (не используется)
    temp_list = [int(k) for k in application_11.keys()]

    # расчет значений тока из словаря по ключу температура
    if input_value in application_11.keys():
        # print(f'For temperature {input_value} max current is {att_11.get(input_value)} A.')
        return application_11.get(input_value)
    else:
        nearest_left = None
        nearest_right = None

        for key, val in application_11.items():
            if int(key) < int(input_value):
                nearest_left = int(key), val
            elif int(key) > int(input_value):
                nearest_right = int(key), val
                break

        if nearest_left is None:
            return nearest_right[1]

        if nearest_right is None:
            return nearest_left[1]

        delta = abs(nearest_right[1] - nearest_left[1])
        length = nearest_right[0] - nearest_left[0]
        step = abs(int(input_value) - nearest_left[0])
        current = nearest_left[1] - delta/length*step

        # print(f'{nearest_left}, {nearest_right}\n'
        #       f'For temperature {input_value} max current is {int(current)} A.')
        return int(current)


if __name__ == '__main__':
    print(permissible_current(input('Temperature: '))) # получаем тепературу (для теста ввод пользователя)


# # тестирование функции
# class PermissibleCurrentTestCase(unittest.TestCase):
#     def test_base_values(self):
#         self.assertEqual(permissible_current('0'), 2000)
#         self.assertEqual(permissible_current('-10'), 2000)
#         self.assertEqual(permissible_current('15'), 1650)
#         self.assertEqual(permissible_current('30'), 1300)
#
#     def negative_value_test(self):
#         self.assertEqual(permissible_current('-9'), 2000)
#         self.assertEqual(permissible_current('-1'), 2000)
#
#     def positive_value_test(self):
#         self.assertEqual(permissible_current('1'), 1960)
#         self.assertEqual(permissible_current('6'), 1780)
#         self.assertEqual(permissible_current('9'), 1720)
#         self.assertEqual(permissible_current('17'), 1590)
#
#     def abnormal_value_test(self):
#         self.assertEqual(permissible_current('-90'), 2000)
#         self.assertEqual(permissible_current('100'), 1300)
