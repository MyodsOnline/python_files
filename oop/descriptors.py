class NonNegative:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if type(value) != int:
            raise TypeError("Invalid data type")
        if value < 0:
            raise ValueError("Negative value!")
        instance.__dict__[self.my_attr] = value

    def __get__(self, instance, owner):
        # print(f'You get {instance} ||| {owner}')
        return instance.__dict__[self.my_attr]
        # return getattr(instance, self.my_attr)


class Worker:
    MAX_RATE = 1000

    hours = NonNegative()
    rate = NonNegative()

    @classmethod
    def validate_max_rate(cls, arg):
        if arg < cls.MAX_RATE:
            return True

    def __init__(self, name: str, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = 0
        if self.validate_max_rate(rate):
            self.rate = rate
        else:
            self.rate = self.MAX_RATE

    def total_profit(self, bonus=0):
        return self.rate * self.hours + bonus


w_1 = Worker('10', 10, 1999)
print(w_1.__dict__)
print(w_1.total_profit(10))


# descriptor for port number
class Port:
    def __set__(self, instance, value):
        if not 1023 < value < 65536:
            print(f'Incorrect port number {value}')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class ServerPort():
    port = Port()

    def __init__(self, address:str, port):
        self.address = address
        self.port = port
        print(f'Port {self.address}:{self.port} created')

    def init_port(self):
        pass


# port_1 = ServerPort('127.0.0.1', 1022)


class Rect:
    _width = NonNegative()
    _height = NonNegative()

    def __init__(self, w, h):
        self._width = w
        self._height = h

    @property
    def area(self):
        return self._width * self._height


def properties():
    print(Rect.__dict__['area'])
    r_1 = Rect(2, 3)
    print(r_1.__dict__, r_1.area, r_1._height, sep=' ||| ')


if __name__ == '__main__':
    properties()