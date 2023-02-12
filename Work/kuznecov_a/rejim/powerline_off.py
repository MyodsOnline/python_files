

questions_list = {
    'rejim': 'is ok?',
    'fuuuuck': 'fuuuuck',
}


def agrrr(agr):
    if isinstance(agr, dict):
        for key, val in questions_list.items():
            print(f"{key}?")
            a = int(input(f'{val}'))
            if a == 0:
                print(f"{key} is skipped, becouse {val}")
            elif a == 1:
                print('Alarm')
            else:
                pass
    else:
        raise ValueError


agrrr(questions_list)
