pr = '**********'
#help(test)
print(test.__doc__, test.test.__doc__)
print(f'{"*"*10}')
print(input.__doc__)


d = {'x':1, 'y':2}
for key in d:
	print(key, d[key])


print(pr)	
sum_1 = 70 + 8
for i in [1, 70, 8]:
	print((sum_1 - i), end=' ')
print(f'\n')
sum_2 = 10 - 8
for i in [20, 10, 90]:
	print((sum_2 + i), end=' ')

arr = [1, 2, 3]
for i in arr:
	i *= 2
print(arr)

for i in range(len(arr)):
	arr[i] *= 2
print(arr)


my_list = list('abcdefghij')
for i, val in enumerate(my_list, 1):
	print(f'{i} - {val}')


for i in range(1, 21):
	if 4 < i < 11:
		continue
	print(i)


i = 0

while True:
	us_num = input('enter: ')
	if us_num == 'stop':
		print(f'final sum - {i}')
		break
	else:
		try:
			us_num_int = int(us_num)
			i += us_num_int
			print(i)
		except ValueError:
			print('its NaN')


arr = ['my', 'live', 'is', 'empty']
arr_j = '=>'.join(arr)
arr_dr = str(arr_j).replace('=>', '-')
print(arr_j, arr_dr)


arr_str = arr_j.split('=>')
print(arr_str)


import random
arr = ', '.join(str(i) for i in random.sample(range(300), 5))
for i, val in enumerate( arr.split(', '), 65 ):
	print(f'{i} - {val}', end='\n\n')
