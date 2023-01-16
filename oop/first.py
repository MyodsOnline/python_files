# import os

class PCUS:
    """
    I will deal with that issue later.
    """
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def PCUS_on(self):
        print(f'{self.name} is on')

    def PCUS_off(self):
        print(f'{self.name} is off')


first_PCUS = PCUS(123, 'PS Vostocnaya')
first_PCUS.PCUS_on()
