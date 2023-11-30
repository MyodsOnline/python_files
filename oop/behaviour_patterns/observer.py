"""
The Observer pattern is a software design pattern in which an object, called the Subject (Observable),
manages a list of dependents, called Observers, and notifies them automatically of any internal state changes
by calling one of their methods.
"""
from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def notify(self, order, service):
        pass


class Publisher(ABC):
    @abstractmethod
    def subscribe(self, courier):
        pass

    @abstractmethod
    def unsubscribe(self, courier):
        pass


class Courier(Subscriber):
    def __init__(self, name):
        self.name = name

    def notify(self, order, service):
        print(f'Courier {self.name} takes stuff {order}')
        service.subscribe()
        print(f'Courier {self.name} goes')


class Restauraunt(Publisher):
    def __init__(self):
        self.couriers = set()

    def subscribe(self, courier):
        self.couriers.add(courier)

    def unsubscribe(self, courier):
        self.couriers.discard(courier)

    def dispatch(self, message):
        if len(self.couriers) == 0:
            print(f'Have not free couriers')
        else:
            for courier in self.couriers:
                courier.notify(message, self)


pizza = Restauraunt()
ivan = Courier('Ivan')
tom = Courier('Tom')

pizza.subscribe(ivan)
pizza.subscribe(tom)

pizza.dispatch(pizza)
