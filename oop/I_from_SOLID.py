# interface segregation principle:
#
import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


class PlottableMixin(abc.ABC):
    @abc.abstractmethod
    def plot(self):
        pass


class Circle(Figure, PlottableMixin):
    def draw(self):
        print('Drawing circle')

    def plot(self):
        print('Printing circle')


class GuideLine(Figure):
    def draw(self):
        print('Drawing guideline')
