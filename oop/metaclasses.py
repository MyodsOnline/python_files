"""
__prepare__
__new__
__init__
__call__
"""

class DocMeta(type):
    def __init__(self, classname, bases, classdict):
        for key, value in classdict.items():
            if key.startswith("__"):
                continue
            if not hasattr(value, "__call__"):
                continue
            if not getattr(value, "__doc__"):
                raise TypeError(f"Method {key} should have a docstring")


class MyClass(metaclass=DocMeta):
    def method_1(self):
        """docstring"""
        print(f"{self.__class__} is done")

    def method_2(self):
        """docstring"""
        print(f"{self.__class__} is done")

my_obj = MyClass()
my_obj.method_1()
my_obj.method_2()


