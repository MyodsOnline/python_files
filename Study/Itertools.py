import itertools

import arr_list
staff_list = arr_list.staff_list
main_staff = arr_list.main_staff_list
obj_list = arr_list.obj_list
letters = arr_list.letter_list
numbers_list = arr_list.numbers_list


print('***count(start, step)***')

for i in itertools.count(2, 2):
  if i > 10:
    break
  print(i, end=' ')
print('\n')

print(list(zip(itertools.count(1), main_staff[0])))
print(list(zip(itertools.count(start=2, step=2), main_staff[2])))


all = list(zip(itertools.count(start=1), obj_list))
for el in all:
  print(el, end=' ')
  
  
print('\n***cycle***')
cnt = 1
for el in itertools.cycle(obj_list):
  if cnt > 10:
    break
  print(cnt, el, end=', ', sep=' - ')
  cnt += 1
  
a = list(zip(itertools.cycle([1,2,3]), obj_list))
print(a)

print('\n***repeat(object, repeat count)***')
rep_cnt = int(input('Enter repeat number - '))
repeat = list(itertools.repeat('a', rep_cnt))
print(f'Repeat {rep_cnt} times - {repeat}')

print('\n***combinations(sequence, number_of_elements)***')

staf_comb = list(itertools.combinations(staff_list, 2))
print(staf_comb)

staf_comb_join = [', '.join(el) for el in itertools.combinations_with_replacement(staff_list, 3)]
print(staf_comb_join)

print('\n***permutations(sequence, number_of_elements)***')
staff_vars = list(','.join(i) for i in itertools.permutations(staff_list, 2))
print(staff_vars)

print('\n***product(sequence1,  sequence2, number_of_elements)***')

shuffle = list(itertools.product('ab', 'cd', repeat=1))
print(shuffle)

print('\n***filterfalse(function, sequence)***')

def bigger_than(incom):
  return incom > rep_cnt
  
not_bigger = list(itertools.filterfalse(bigger_than, numbers_list))
print(f'{not_bigger} <-smaller than {rep_cnt + 1}')
not_bigger = list(itertools.filterfalse(None, numbers_list))
bigger = list(filter(None, numbers_list))
print(not_bigger, '<-false|true ->', bigger)

print('\n***dropwhile/takewhile(function, sequence)***')
dr_wh = list(itertools.dropwhile(bigger_than, numbers_list))
tk_wh = list(itertools.takewhile(bigger_than, numbers_list))
print(dr_wh, tk_wh)

print('\n***compress(sequence, true/false_sequence)***')
compress_list = list(itertools.compress(staff_list, [True, False, False, True, False]))
print(compress_list)

print('\n***accumulate(sequence, [function])***')
acc_list = list(itertools.accumulate(numbers_list[:rep_cnt]))
print(f'{rep_cnt} -> acc = {acc_list}')

def acc_mltply(x, y):
	return x * y
	
acc_list_mltply = list(itertools.accumulate(numbers_list[rep_cnt:], acc_mltply))
print(f'acc_list_mltply -> {acc_list_mltply}')
	
print('\n***chain(sequence, ... [sequence])***')
chain_list = list(itertools.chain(staff_list, main_staff, obj_list))
print(len(chain_list), chain_list)
