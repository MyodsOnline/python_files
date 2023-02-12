import datetime
import logging


def current_smena():
    """Выбор смены в зависимости от текущего времени"""
    CURRENT_DATE = datetime.datetime.now()
    # if int(datetime.datetime.now().time().strftime('%H')) in range(0, 20):
    #     START_TIME = datetime.datetime.combine(CURRENT_DATE, datetime.time(hour=8, minute=0)).strftime('%H:%M %d.%m.%y')
    #     END_TIME = datetime.datetime.combine(CURRENT_DATE, datetime.time(hour=22, minute=0)).strftime('%H:%M %d.%m.%y')
    # else:
    #     START_TIME = datetime.datetime.combine(CURRENT_DATE, datetime.time(hour=20, minute=0)).strftime('%H:%M %d.%m.%y')
    #     END_TIME = datetime.datetime.combine(CURRENT_DATE, datetime.time(hour=22, minute=0)).strftime('%H:%M %d.%m.%y')
    #
    # TEST_TIME = datetime.datetime(2022, 12, 26, 9, 36).strftime('%H:%M %d.%m.%y')
    #
    # TIMEDELTA = END_TIME - START_TIME
    #
    # print(START_TIME, END_TIME, TEST_TIME)

    NEXT_DATE = CURRENT_DATE + datetime.timedelta(days=1)
    smena = f'Дневная смена c 8:00 по 20:00 {CURRENT_DATE.strftime("%d.%m.%y")}.' \
        if int(CURRENT_DATE.strftime('%H')) in range(8, 20) \
        else f'Ночная смена c 20:00 {CURRENT_DATE.strftime("%d.%m.%y")} по 08:00 {NEXT_DATE.strftime("%d.%m.%y")}.'

    return smena


def log_to_file(data):

    with open('text.txt', 'w', encoding='utf-8') as f:
        f.write(data)


# subprocess.call('calc.exe')

"""
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'Software'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'Hardware'}


people = [bob, sue]

for person in people:
    print(person['name'], person['pay'], sep=', ')
    if person['name'].__contains__('Jo'):
        print(person['name'], person['age'], sep=' - ')

db = {}
db['bob'] = bob
db['sue'] = sue
"""

if __name__ == '__main__':
    log_to_file(current_smena())
