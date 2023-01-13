from item import Item


class Phone(Item):  # child class for Item class

    all_phones = []

    def __init__(self, name, price, qty, broken_items=0):
        # Call a attrs and methods of super-class
        super().__init__(name, price, qty)
        # Check for curr class
        assert broken_items >= 0, f'Check for broken items failed'
        # Describe unique attrs
        self.broken_items = broken_items

        Phone.all_phones.append(self)