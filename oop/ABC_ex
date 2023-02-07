import abc
from typing import List  # useful method


class Figure(abc.ABC):
    @abc.abstractmethod
    def draw(self):
        pass


class Circle(Figure):
    def draw(self):
        print('Draw circles')


class Triangle(Figure):
    def draw(self):
        print('Draw triangles')


class Square(Figure):
    def draw(self):
        print('Draw square')


class CAD:
    @classmethod
    def drew_all(cls, figures: List[Figure]):
        for figure in figures:
            figure.draw()

    @classmethod
    def drew_all_sorted(cls, figures: List[Figure], comparator):  # comparator - useful thing
        sorted_figures = sorted(figures, key=comparator)
        cls.drew_all(sorted_figures)


class FigureComparators:
    @staticmethod
    def compare_circle_first(figure):
        if isinstance(figure, Circle):
            return 0
        elif isinstance(figure, Square):
            return 1
        elif isinstance(figure, Triangle):
            return 2
        else:
            return 3


data = [Triangle(), Square(), Circle(), Triangle(), Triangle(), Square(), Circle()]

cad = CAD()
cad.drew_all_sorted(data, FigureComparators.compare_circle_first)
