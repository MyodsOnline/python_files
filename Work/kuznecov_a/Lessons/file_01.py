
class UV_Upask:
    def __init__(self, title: str, value: float, mode=False):
        self.title = title
        self.value = value
        self.mode = mode
        print(f'UPASK "{title}" created')

    def pa_value(self):
        return f'{self.title}: {self.value}'

    def upask_on(self):
        self.mode = True
        return f'The "{self.title} is ON"'

    def upask_info(self):
        print(f'The {self.title} is {"OFF" if {self.mode} == False else "ON"}')


upask = UV_Upask('ПРД/ПРМ ПКУС по ВОЛС (№2) РП 330 кВ Каменный Бор – ПС 330 кВ Кондопога', 300, False)
# upask.upask_on()

upask.upask_info()


class UV_Upasc_child(UV_Upask):
    def __init__(self, title, value, mode, commands):
        super().__init__(title, value, mode)
        self.commands = commands

    def child_info(self):
        print(f'child {type(self.child_info())}')


init_1 = UV_Upasc_child('ffff', 1000, True, 'First')
print(init_1)
