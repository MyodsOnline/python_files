from typing import Union

ordered_list = [1, 2, 3, 4, 5, 6, 7, 8]
unordered_list = [4, 6, 8, 7, 3, 5, 2, 1]


def binary_search(array: list, target: int) -> int:
    """
    Выполняет бинарный поиск целевого числа в отсортированном списке.

    Args:
        array (list): Отсортированный список целых чисел.
        target (int): Целое число, которое требуется найти.

    Returns:
        int: Индекс целевого числа в списке, если оно найдено, иначе -1.
    """
    left, right = 0, len(array) -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

#print(f'Target value index – {binary_search(ordered_list, 6)}')


def find_smallest_index(arr: list) -> int:
    """
    Ищет индекс минимального значения в списке.

    Args:
        arr (list): Исходный список чисел.

    Returns:
        int: Индекс минимального значения в списке.
    """
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i
    return smallest_index


def sorted_array(arr: list) -> list:
    """Сортирует список методом выбора.

    Args:
        arr (list): Исходный список чисел.

    Returns:
        list: Отсортированный список.
    """
    new_arr = []
    original_arr = arr.copy()

    while original_arr:
        smallest_index = find_smallest_index(original_arr)
        new_arr.append(original_arr.pop(smallest_index))

    return new_arr


#print(f'Unsorted array – {unordered_list}')
#print(f'Sorted array – {sorted_array(unordered_list)}')


def countdown(i: int):
    if i <= 0:
        print(i)
        return
    else:
        print(i, end=', ')
        countdown(i - 1)


#countdown(3)


def fact(x: int) -> Union[int, None]:
    """
    Вычисляет факториал числа x.
    Если число меньше или равно нулю, возвращается None.

    Args:
        x (int): Число, для которого вычисляется факториал

    Returns:
        int: Факториал числа x или None, если x <= 0
    """
    if x == 1:
        return 1
    elif x <= 0:
        return None
    else:
        return x * fact(x - 1)


# print(fact(3))


def say_recursion_hello(hello: str) -> None:
    """
    Рекурсивная функция, которая выводит переданную строку и вызывает себя снова,
    убирая последний символ строки, пока строка не станет пустой.

    :param hello: Строка, которую нужно вывести и обработать рекурсией.
    :return: None
    """
    print(hello)
    if len(hello) <= 0:
        return None
    else:
        say_recursion_hello(hello[:-1])


#say_recursion_hello('Hello!')


def count_elements(arr: list):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_elements(arr[:-1])


#print(count_elements(unordered_list))


def find_max_val(arr: list) -> int:
    """
    Рекурсивная функция для нахождения максимального значения в списке.

    Args:
        arr (list): Список целых чисел.

    Returns:
        int: Максимальное значение в переданном списке.
    """
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] <= arr[1]:
            arr.pop(0)
            return find_max_val(arr)
        else:
            arr.pop(1)
            return find_max_val(arr)

print(find_max_val(unordered_list))
