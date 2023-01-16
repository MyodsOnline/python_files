import datetime

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

while True:
    print('Enter year: ')
    response = input('>>> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like "2022"!')
    continue

while True:
    print('Enter a month number (1-12):')
    response = input('>>> ')

    if not response.isdecimal():
        print('Please enter a numeric, like "3 for March"!')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Enter a number from 1 to 12!')


def get_calendar(year, month):
    calText = ''
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '|..Sunday..|..Monday..|.Tuesday..|.Wednesday|.Thursday.|..Friday..|.Saturday.|\n'

    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)

    print(currentDate, currentDate.weekday())

    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator
        day_number_row = ''
        for i in range(7):
            day_number_label = str(currentDate.day).rjust(2)
            day_number_row = '|' + day_number_label + (' ' * 8)
            currentDate += datetime.timedelta(days=1)

        day_number_row += '|\n'
        calText += day_number_row
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

        calText += weekSeparator
        return calText


calText = get_calendar(year, month)
print(calText)
