# dependency inversion principle
import abc


class ItemInterface(abc.ABC):
    @abc.abstractmethod
    def get_price(self):
        pass


class SimpleItem(ItemInterface):
    def get_price(self):
        pass


class PerfectItem(ItemInterface):
    def get_price(self):
        pass


class GetOrder():
    total = 0

    def add(self, item):
        if isinstance(item, ItemInterface):
            self.total += 1
            print('Added to chart')
        else:
            print('Unsupportable item')
