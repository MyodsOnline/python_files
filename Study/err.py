num_char = len(input('Type any word: '))
print(f'your word has {num_char} letters')


ans = sum([int(b) for b in list(str(input('Enter your number: ')))])
print(ans)

def sum_num(user_int):
    user_list = list(user_int)
    for i in user_list:
        a = f'{user_list[int(i)]} +'
        print(a)
    ans = (sum([int(b) for b in list(user_int)]))
    print(f'{user_list} = {ans}')


sum_num(input('Enter your number: '))

a_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


modernized_a = [el for el in a_1 if (el < 5)]
print(modernized_a)

gen_list = list(set([el for el in a_1 if el in a_2]))
print(gen_list)

set_list = list(set(a_1) & set(a_2))
print(set_list)

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(int(input()))

def triangle_area(height:int, lenght:int):
    print(height * lenght / 2)

triangle_area(height=int(input('height: ')), lenght=int(input('lenght: ')))