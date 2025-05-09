import timeit
from typing import List, Tuple






def measure_execution_time(func):
    """
    Декоратор для измерения времени выполнения функции с использованием timeit.

    :param func: Функция, время выполнения которой нужно измерить
    :return: Обернутая функция с измерением времени
    """

    def wrapper(*args, **kwargs):
        # Используем timeit для измерения времени выполнения
        execution_time = timeit.timeit(lambda: func(*args, **kwargs), number=10000)
        print(f"Время выполнения функции {func.__name__}: {execution_time:.6f} секунд")
        return func(*args, **kwargs)

    return wrapper


@measure_execution_time
def Andrei(canal: List[Tuple[int, int]]) -> bool:
    """
    Функция возвращает False, если хотя бы в одном кортеже из списка canal оба элемента равны нулю.
    В противном случае возвращает True.

    :param canal: Список из двух кортежей, каждый кортеж содержит два элемента (int, int)
    :return: False, если хотя бы один кортеж состоит из двух нулей, иначе True
    """
    if (canal[0][0] == 0 and canal[0][1] == 0) \
            or (canal[1][0] == 0 and canal[1][1] == 0):
        return False
    return True


@measure_execution_time
def Antonina(canal: List[Tuple[int, int]]) -> bool:
    """
    Функция возвращает True, если хотя бы в одном кортеже из списка canal есть элемент, равный 1.
    Логика описана примитивно, без использования оператора `in`.

    :param canal: Список из двух кортежей, каждый кортеж содержит два элемента (int, int)
    :return: True, если хотя бы один элемент равен 1, иначе False
    """
    if (canal[0][0] == 1 or canal[0][1] == 1) \
            and (canal[1][0] == 1 or canal[1][1] == 1):
        return True
    return False


# Пример использования
formatted_data = [(0, 1), (1, 0)]

# Проверка первой функции (проверка нулей)
result_zeros = Andrei(formatted_data)
print(f"Результат проверки нулей: {result_zeros}")

# Проверка второй функции (проверка единиц)
result_ones = Antonina(formatted_data)
print(f"Результат проверки единиц: {result_ones}")

# Сравнение времени выполнения
time_zeros = timeit.timeit(lambda: Andrei(formatted_data), number=1)
time_ones = timeit.timeit(lambda: Antonina(formatted_data), number=1)
time_diff = abs(time_zeros - time_ones)

print(f"Разница во времени выполнения: {time_diff:.6f} секунд")

# Определение, какая функция выполняется быстрее
if time_zeros < time_ones:
    print("Функция Andrei выполняется быстрее.")
elif time_ones < time_zeros:
    print("Функция Antonina выполняется быстрее.")
else:
    print("Обе функции выполняются за одинаковое время.")

print('\n', '\n', '\n', '\n', '\n')
