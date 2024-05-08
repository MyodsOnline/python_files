# def cnt():
# 	gb = {'Susan': [92, 85, 100], 'Eduardo': [83, 95, 79], 'Azizi': [91, 89, 82], 'Pantipa': [97, 91, 92]}
# 	all_grades_total = 0
# 	all_grades_count = 0
# 	for name, grade in gb.items():
# 		total = sum(grade)
# 		print(f'Average for {name} is {total/len(grade):.2f}')
# 		all_grades_total += total
# 		all_grades_count += len(grade)
# 	print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")
#
# cnt()
import random


def get_val():
    return [random.randint(10, 100) for _ in range(0, 24)]

gen = {'uz_tes': get_val(),
      'nw_tes': get_val()}

# print(gen)

'''
Возвращает допустимую токовую нагрузку в зависимости от заданой температуры
'''
# тестовый словарь {температура: ток}
att_11 = {
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

# список температур из словаря
temp_list = [int(k) for k in att_11.keys()]

# получаем тепературу (для теста ввод пользователя)
input_value = input('Temperature: ')

# выбор значений из словаря по ключу: температура
if input_value in att_11.keys():
    print(f'For temperature {input_value} max current is {att_11.get(input_value)} A.')
else:
    nearest_left = None
    nearest_right = None

    for key, val in att_11.items():
        if int(key) < int(input_value):
            nearest_left = int(key), val
        elif int(key) > int(input_value):
            nearest_right = int(key), val
            break

    delta = abs(nearest_right[1] - nearest_left[1])
    length = nearest_right[0] - nearest_left[0]
    step = abs(int(input_value) - nearest_left[0])
    current = nearest_left[1] - delta/length*step

    print(f'{nearest_left}, {nearest_right}\n'
          f'For temperature {input_value} max current is {int(current)} A.')
