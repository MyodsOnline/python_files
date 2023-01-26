from abc import ABC, abstractmethod


class Car:

    def __init__(self, brand, model, year):
        assert year <= 2023, "It's impossible for now"

        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.brand} {self.model} {self.year}'

    def car_goes_left(self):
        print(f'The {self.brand} {self.model} turns left')


car_1 = Car('Foton', 'Mat', 2000)

print(car_1)
car_1.car_goes_left()


class SerialPort(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class Charger(ABC):
    @abstractmethod
    def charge(self):
        pass

# class COM_port(SerialPort):
#     pass
#
# com_port_1 = COM_port()
# >>> TypeError: Can't instantiate abstract class COM_port with abstract methods read, write


class COM_port(SerialPort):
    def read(self):
        print('Read')

    def write(self):
        print('Write')


com_port_2 = COM_port()
com_port_2.read()
com_port_2.write()


class USB_port(SerialPort, Charger):
    def read(self):
        print('USB Read')

    def write(self):
        print('USB Write')

# usb_port_1 = USB_port()
# >>> TypeError: Can't instantiate abstract class USB_port with abstract method charge

    def charge(self):
        print('USB Charge')

usb_port_2 = USB_port()
