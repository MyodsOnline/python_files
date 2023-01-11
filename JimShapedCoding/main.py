import csv


class Item:
    pay_rate = 0.2  # pay rate after 20% discount
    all_items = []

    # class attributes
    def __init__(self, name: str, price: int or float, qty=0):

        # validation to the received arguments
        assert price > 0, f'Price {price} is not valid'
        assert qty >= 0, f'Quantity {qty} is not valid'

        # assign to self object
        self.name = name
        self.price = price
        self.qty = qty

        # print(f'I am created with parameters - name:{name}, price:{price}, qty:{qty}.')

        Item.all_items.append(self)

    # class methods
    def apply_discount(self):
        self.price = self.price * (1 - self.pay_rate) if self.pay_rate > 0 else self.price

    def calculate_total_price(self):
        return self.price * self.qty

    @classmethod
    def instance_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                qty=int(item.get('qty')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'Item("{self.name}, {self.price}, {self.qty}")'


# Item.instance_from_csv()
# print(Item.all_items)

print(Item.is_integer(7.0))
