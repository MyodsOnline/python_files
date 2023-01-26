class NonNegative:
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value!")
        instance.__dict__[self.my_attr] = value

    def __get__(self, instance, owner):
        print(f'You get {instance} ||| {owner}')
        return instance.__dict__[self.my_attr]


class Worker:
    hours = NonNegative()
    rate = NonNegative()

    def __init__(self, name: str, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def total_profit(self, bonus=0):
        return self.rate * self.hours + bonus


w_1 = Worker('12', 10, 100)
print(w_1.total_profit(10))