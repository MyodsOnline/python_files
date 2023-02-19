import random
from abc import ABC, abstractmethod

class AbstractSensor():
    """
    an abstract sensor using the implementation of a physical sensor by interface. looks like a box
    """
    def __init__(self, implementor):
        self.implementor = implementor

    def get_value(self):
        return self.implementor.get_value_impl()


class SensorImplementor(ABC):
    """
    abstract sensor interface. looks like a physical sensor
    """
    @abstractmethod
    def get_value_impl(self):
        pass


class BaseSensorImplementator(SensorImplementor):
    """
    the basic interface of the physical sensor
    """
    def __init__(self):
        self.values = [12.3, 12.25, 12.38, 12.18, 12.41, 12.43, 12.37, 12.67]

    def get_value_impl(self):
        return random.choice(self.values)


class BaseSensor(AbstractSensor):
    """
    implementation of a physical sensor
    """
    pass


class AverageSensor(AbstractSensor):
    """
    implementation of a physical average sensor
    """
    def __init__(self, implementor, n):
        super().__init__(implementor)
        self.queue = []
        self.n = n

    def get_average_value(self):
        for _ in range(self.n):
            self.queue.append(self.implementor.get_value_impl())

        if len(self.queue) > self.n:
            self.queue.pop(0)
        return round(sum(self.queue) / len(self.queue))


bs1 = BaseSensor(BaseSensorImplementator())
print(f'base sensor. get random value - {bs1.get_value()}')

as1 = AverageSensor(BaseSensorImplementator(), 5)
print(f'average sensor. get random value - {as1.get_value()}')
print(f'average sensor. get average value - {as1.get_average_value()} for queue {as1.queue}')

#########


class Speedometer(SensorImplementor):
    def __init__(self, min_speed, max_speed):
        self.min_speed = min_speed
        self.max_speed = max_speed

    def get_value_impl(self):
        return round(self.min_speed + random.random()*(self.max_speed - self.min_speed))


sp1 = Speedometer(0, 100)
print(f'Random speed value - {sp1.get_value_impl()}')
a_sp = AverageSensor(Speedometer(5, 100), 5)
print(f'Average speed value - {a_sp.get_average_value()}. Queue - {a_sp.queue}')

#########


class Votlmeter(SensorImplementor):
    def __init__(self):
        self.base_voltage = 12
        self.deviation = 0.3

    def get_value_impl(self):
        return self.base_voltage + random.random() * self.deviation


volt = Votlmeter()
av_volt = AverageSensor(Votlmeter, 5)
print(av_volt.get_average_value())
