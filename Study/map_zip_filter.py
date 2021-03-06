arr = [1, 2, 3, 4, 5]
arr_10 = [el for el in range(10, 70, 10)]
arr_100 = [el * 10 for el in arr_10[:-3]]
new_arr_gen = [el for el in arr if el % 2 == 0]
word_arr = ('a', 'aa', 'aaa', 'aaaa', 'aaaaa')

print('**** Examples with MAP(). Returns iterable object. **** \n')


def func(elem):
    return elem + 10


print(f'apply map to arr - {list(map(func, arr))}')


def func1(elem):
    return f'{elem} + 100 = {elem + 100}'


lambda_func = lambda x, y: x + y
lambda_res = list(map(lambda_func, arr, arr_10))
print(f'lambda + map - {lambda_res}')

print(f'result = {list(map(func1, new_arr_gen))}')


def func2(e1, e2, e3):
    return e1 + e2 + e3


print(f'map() with arrays of different lenghts - {tuple(map(func2, arr, arr_10, arr_100))} -- smaller length is taken')

print(f'count len() with map() - {list(map(len, word_arr))}')
print(f'apply .upper to array - {list(map(str.upper, word_arr))}')

print('\n**** Examples with ZIP() ****\n')

print(f'zip() for different arrays - {list(zip(arr, arr_10, arr_100))}')

zip_arr = [x + y + z for (x, y, z) in zip(arr, arr_10, arr_100)]
print(f'sum for elements in zip - {zip_arr}')

print('\n**** Examples with FILTER() ****\n')


def even(data):
    return data >= 3


filtered_arr = list(filter(even, arr))
print(filtered_arr)

filtered_arr = [i for i in arr if even(i)]
print(filtered_arr)

is_even = lambda x: x % 2 == 0
filtered_with_lambda_arr = list(filter(is_even, arr))
print(f'filtered_with_lambda_arr - {filtered_with_lambda_arr}')

filtered_with_lambda_arr_odd = list(filter(lambda x: x % 2 == 1, arr))
print(f'almost same thing - {filtered_with_lambda_arr_odd}')
