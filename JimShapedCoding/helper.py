from item import Item
from phone import Phone

# Item.instance_from_csv()
#
# print(Item.all_items)

item_1 = Item('MyItem', 750)
print(item_1.name)

item_1.name = 'OtherItem'
print(item_1.name)

item_1.name = 'OtherMyItem'  # Will raise Exception
print(item_1.name)
