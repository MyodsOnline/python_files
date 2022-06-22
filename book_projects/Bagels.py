import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    """
    Bagels - a deductive logic game. I am thinking a 3-digits number. Try to guess what is it.
    """
    while True:
        secret_num = get_secret_num()
        print(f'Secret number is ready! Number contains {NUM_DIGITS} unique digits')
        print(f'You have {MAX_GUESSES} attempts')

        guesses_cnt = 1

        while guesses_cnt <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{guesses_cnt}')
                guess = input('>>> ')

            clues = get_clue(guess, secret_num)
            print(clues)
            guesses_cnt += 1

            if guess == secret_num:
                break
            if guesses_cnt > MAX_GUESSES:
                print(f'You run out of guesses. The secret number was: {secret_num}')

        print('Do you want to play again? (yes / no)')
        if not input('>>> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_num():
    digit_list = list('0123456789')
    random.shuffle(digit_list)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(digit_list[i])
    return secret_num


def get_clue(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'

    return ' '.join(clues)


if __name__ == '__main__':
    main()
