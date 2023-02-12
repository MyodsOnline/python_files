import unittest


class Rectangle:
    __slots__ = ('_width', '_height')

    def __init__(self, width, height):
        super().__setattr__('_width', width)
        super().__setattr__('_height', height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, key, value):
        raise AttributeError('Attributes are immutable')

    @property
    def area(self):
        return self._height * self._width


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)


class TestRectangle(unittest.TestCase):
    def test(self):
        rectangle = Square(10)
        self.assertEqual(rectangle.area, 100)

        with self.assertRaises(AttributeError):
            rectangle.width = 100
