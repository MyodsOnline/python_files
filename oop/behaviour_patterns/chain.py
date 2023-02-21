from abc import ABC, abstractmethod
from random import choice, random


class ChainMaster(ABC):
    def get_next(self, next):
        self.next = next
        return self.next

    @abstractmethod
    def handler(self, request):
        if self.next is not None:
            return self.next.handler(request)


class Request:
    data = [
        'generation switch off',
        'generation switch on',
        'element switch off',
        'signal',
    ]

    def get_data(self):
        return choice(self.data)

# dd = Request()
# print(dd.get_data())


class Operator(ChainMaster):
    probability = 0.75

    def __init__(self, name):
        self.name = name

    def busy(self):
        return random() < self.probability

    def handler(self, request):
        if self.busy():
            print(f'Dispatcher {self.name} is busy')
            super().handler(request)
        else:
            print(f'Dispatcher {self.name} impacting on {request.get_data()}')


class OperatorBusy(ChainMaster):
    def __init__(self):
        self.request = None

    def handler(self, request):
        if self.request == request:
            print('All dispatchers are busy, please wait')
        else:
            self.request = request

        super().handler(request)


handler = OperatorBusy()
handler.get_next(Operator('mike')).get_next(Operator('leo')).get_next(Operator('alex')).get_next(handler)


for _ in range(3):
    handler.handler(Request())


print('------------NEXT EXAMPLE-----------')
#### Decoder

class DecodeHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class Decoder(DecodeHandler):
    def __init__(self):
        self.next = None
        self.encoding = None

    def set_next(self, handler):
        self.next = handler
        return handler

    def handle(self, request):
        try:
            print(f'try to decode "{self.encoding}"')
            print(f'result --> {request.decode(self.encoding)}')
        except UnicodeDecodeError:
            print(f'--> fail decode {request} in "{self.encoding}"')
            if self.next:
                return self.next.handle(request)


class Cp1251(Decoder):
    def __init__(self):
        super().__init__()
        self.encoding = 'cp1251'


class UTF8(Decoder):
    def __init__(self):
        super().__init__()
        self.encoding = 'utf-8'


class Final(Decoder):
    def handle(self, request):
        return f'--->cant decode {request}'


data = [b'\xff\xff\xff', b'\x78']

cp = Cp1251()
utf = UTF8()
fin = Final()

utf.set_next(cp).set_next(fin)

for el in data:
    utf.handle(el)
