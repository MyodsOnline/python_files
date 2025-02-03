def string_converter(phone: str) -> str:
    """
    Очистка и форматирование номера телефона.

    Функция убирает из строки все символы, кроме цифр,
    добавляет в начало цифру 9 и форматирует номер,
    разбивая его на группы по 3 цифры, разделенные пробелами.

    Args:
        phone (str): Исходная строка с номером телефона

    Returns:
        str: Отформатированная строка с номером телефона
    """
    cleaned_str = ''.join([_ for _ in phone if _.isdigit()])
    cleaned_str_with_nine = f'9{cleaned_str}'
    formatted = ' '.join([cleaned_str_with_nine[i:i+3] for i in range(0, len(cleaned_str_with_nine), 3)])
    print(formatted)
    return cleaned_str_with_nine


while True:
    input_phone = input('Phone number (or "q" for quit program): ')
    if input_phone.lower() == 'q':
        break
    try:
        cleaned_phone = string_converter(input_phone)
        print(cleaned_phone)
    except TypeError as e:
        print(f'Error {e}, check your input')
