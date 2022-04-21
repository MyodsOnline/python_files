"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
"""

# def abbrev_name(name):
#     # return f'{name.split()[0][0].upper()}.{name.split()[1][0].upper()}'
#     return '.'.join(i[0] for i in name.split()).upper()
#
#
# print(abbrev_name('john smith first'))

"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""

# def simple_multiplication(number):
#     try:
#         number = int(number)
#         return number * 8 if (number % 2 == 0) else number * 9
#     except ValueError:
#         return 'wrong data'
#
#
# print(simple_multiplication(262))

"""
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.
"""

# def paperwork(n, m):
#     return 0 if (n < 0 or m < 0) else n * m
#
#
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


def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'

"""

"""