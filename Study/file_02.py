"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
"""


def abbrev_name(name):
    # return f'{name.split()[0][0].upper()}.{name.split()[1][0].upper()}'
    return '.'.join(i[0] for i in name.split()).upper()


# print(abbrev_name('john smith first'))

"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""


def simple_multiplication(number):
    try:
        number = int(number)
        return number * 8 if (number % 2 == 0) else number * 9
    except ValueError:
        return 'wrong data'


# print(simple_multiplication(262))

"""
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
"""


def paperwork(n, m):
    return 0 if (n < 0 or m < 0) else n * m


# print(paperwork(4, -4))

"""
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.
"""

# def count_positives_sum_negatives(arr):
#     final = []
#     if arr:
#         final.append(len([x for x in arr if x > 0]))
#         final.append(sum([x for x in arr if x < 0]))
#     return final
#
#
# print(count_positives_sum_negatives([1, 2, 3, 4, -1, -6, 0, 0, 2]))

"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""

# def even_or_odd(number):
#     return 'Even' if number % 2 == 0 else 'Odd'

"""
You get an array of numbers, return the sum of all of the positives ones.
"""

# def positive_sum(arr):
#     return sum([x for x in arr if x > 0])

"""
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
"""

# def invert(lst):
#     return [-x for x in lst]

"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""

# def move_zeros(array):
#     zeros, others = [], []
#     for i in array:
#         if i == 0:
#             zeros.append(i)
#         else:
#             others.append(i)
#     array = others + zeros
#     return array

"""
Create a countdown timer.
"""

import time


def countdown(time_sec):
    while time_sec:
        mins, sec = divmod(time_sec, 60)
        timeformat = f'{mins:02d}:{sec:02d}'
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1

    print('Timer ended!')


# countdown(3)


"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):
    # noob way:
    # set_string = set(string.lower())
    # if len(set_string) == len(string):
    #     return True
    # else:
    #     return False

    # master way:
    return len(string) == len(set(string.lower()))

    # another way
    # new_string = string.lower()
    # for letter in new_string:
    #     if letter.count(new_string) > 1:
    #         return False
    # return True


# is_isogram('Uuto')

"""
Take 2 strings s1 and s2 including only letters from ato z. 
Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
"""


def longest(a1, a2):
    return "".join(sorted(set(a1) | set(a2)))


a1 = "xyaabbbccccdefww"
a2 = "xxxxyyyyabklmopq"

# longest(a1, a2)

"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string.
"""


def fake_bin(x):
    # # noob way
    # output = str()
    # for el in x:
    #     if int(el) < 5:
    #         output += '0'
    #     else:
    #         output += '1'
    # return output

    # # master way
    return ''.join('0' if int(el) < 5 else '1' for el in x)


# fake_bin('1345478554')

"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.
"""


def pig_latin(text):
    # # noob way
    # list_string = text.split(" ")
    # pig_string = list()
    # exception_list = [',', '.', '!', '?', ':']
    # for word in list_string:
    #     if word in exception_list:
    #         pig_string.append(word)
    #     else:
    #         word = word[1:] + word[0] +'ay'
    #         pig_string.append(word)
    # return ' '.join(pig_string)

    # master way
    lst = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

"""

"""


def same_structure_as(original, other):
    if len(original) != len(other):
        return False
    for el in range(0, len(original)):
        if type(original[el]) != type(other[el]):
            return False
        elif type(original[el]) == type(other[el]) == list:
            if len(original[el]) != len(other[el]):
                return False
            else:
                continue
        else:
            continue
    return True


#same_structure_as([1, [1, 1], 1], [2, [2, 2], 2])

"""
Ways to convert a Boolean to a String
"""


def boolean_to_string_1(b):
    return str(b)

def boolean_to_string_2(b):
    return 'True' if b else 'False'

def boolean_to_string_3(b):
    if b:
        return "True"
    return "False"

def boolean_to_string_4(b):
    return ('False', 'True')[b]

def boolean_to_string_5(b):
    if b == True or b == False:
        return str(b)

boolean_to_string_6 = lambda x: "True" if x else "False"

def boolean_to_string_7(b):
    d = {True: "True", False: "False"}
    return d[b]

# print(boolean_to_string_4(True))

"""
Complete the solution so that the function will break up camel casing, using a space between words.
"""

def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])

# print(solution('someText'))

"""
create a decorator for calculating the runtime of a function
"""

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        value = func(*args)
        finish = time.time()
        print(f'time for function "{func.__name__}": {round(finish - start, 2)} sec.')
        return value
    return wrapper


@timer
def list_make_1(idx):
    list_1 = []
    for i in range(idx):
        list_1.append(i)
    return list_1


@timer
def list_make_2(idx):
    return [i for i in range(idx)]


val = 10 ** 6

if __name__ == '__main__':
    list_make_1(val)
    list_make_2(val)
