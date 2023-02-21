from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


class MachineOperation(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(self.name)


class CompositeOperation(Component):
    def __init__(self):
        self.children = set()

    def operation(self):
        for child in self.children:
            child.operation()

    def add_children(self, component):
        self.children.add(component)

    def remove(self, component):
        self.children.discard(component)


comp_1 = CompositeOperation()
comp_2 = CompositeOperation()
op_1 = MachineOperation('m1')
op_2 = MachineOperation('m2')
op_3 = MachineOperation('m3')
op_4 = MachineOperation('m4')

comp_1.add_children(op_1)
comp_1.add_children(op_2)
comp_1.add_children(op_3)
comp_2.add_children(op_4)

comp_1.add_children(comp_2)

print('_______')
a = comp_1.operation()
print('_______')
comp_2.operation()

