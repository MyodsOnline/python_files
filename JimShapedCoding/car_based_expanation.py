
class Car:

    def __init__(self, brand, model, year):
        assert 1900 <= year >= 2023, "It's impossible for now"

        self.brand = brand
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.brand} {self.model} {self.year}'

    def car_goes_left(self):
        print(f'The {self.brand} {self.model} turns left')


car_1 = Car('Foton', 'Mat', 1982)

print(car_1)
car_1.car_goes_left()
