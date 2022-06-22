import random
import os

TITLE = 'ИЗУЧАТЕЛЬ ТАБЛИЦЫ УМНОЖЕНИЯ'
HELP = 'help - для вывода справки'
ASK = '? - если не знаешь ответа и хочешь подсмотреть'
EXIT = '! - для завершения программы'
DEVIDER = "*" * 26
ATTEMPT = 9


def get_tip(int_a):
    print(f'{DEVIDER}\n  ТАБЛИЦА УМНОЖЕНИЯ НА {int_a}')
    for i in range(1, 10):
        print(f'\t{int_a} * {i} = {int_a * i}')
    print(DEVIDER)

def question(a):
    attempt = ATTEMPT
    correct_answers = 0
    os.system('clear')
    digit_list = list('123456789')
    random.shuffle(digit_list)

    while attempt > 0:
        random_int = int(digit_list.pop())
        user_ans = input(f'{a} * {random_int} = ')
        correct_ans = a * random_int
        if user_ans == '?':
            print(f'\nПравильный ответ - {correct_ans}\n')
        elif user_ans == '!':
            close()
            break
        else:
            try:
                user_ans = int(user_ans)
                if user_ans == correct_ans:
                    print(f'{user_ans} - Правильный ответ!')
                    correct_answers += 1
                else:
                    print(f'\n{user_ans} - Неверный ответ.\t{a} * {random_int} = {correct_ans}\n')
            except ValueError:
                print(f'\nПохоже ты ввел не цифру, будь внимательнее!\n')
        attempt -= 1
    print(f'Ты правильно ответил на {correct_answers} вопросов из {ATTEMPT}\n')


def close():
    os.system('clear')
    print('Заходи ещё!!!')


def main():
    print(f'\n{DEVIDER}\n{TITLE}\n{HELP}\n{EXIT}\n{DEVIDER}\n')

    while True:
        user_choise = input('Умножение на какую цифру будем изучать? ')
        if user_choise == '!':
            close()
            break
        else:
            try:
                user_choise_int = int(user_choise)
                if user_choise_int in range(1, 10):
                    get_tip(user_choise_int)
                    go = input('\nГотов проверить свою память?'
                          '\nНажми "Enter" чтобы начать тест,'
                          '\nили "!" чтобы закрыть программу.')
                    if go == '!':
                        close()
                        break
                    else:
                        question(user_choise_int)
                else:
                    print('\n\tДумаю, пока рано умножать такие числа!'
                          '\n\tДавай закрепим базу (от 1 до 9).\n')
            except ValueError:
                print('\t', DEVIDER, '\n\tПохоже ты ввел не цифру, будь внимательнее!')


if __name__ == '__main__':
    main()