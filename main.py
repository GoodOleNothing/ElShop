from workshop.item import Item
from workshop.phone import *

#item1 = Item("Смартфон", 10000, 20)
#item2 = Item("Ноутбук", 20000, 5)
#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
#Item.pay_rate = 0.8
#print(item1.apply_discount())
#print(item2.item_price)
#print(item1.examples_data)
#print(item1.initiated_examples)
#print(item1._item_name)

#item = Item('Телефон', 10000, 5)
#item.item_name = 'Смартфон'
#print(item.item_name)
##item.item_name = 'СуперСмартфон'
#
#Item.instantiate_from_csv()
#print(len(Item.initiated_examples))
#item1 = Item.initiated_examples[0]
#print(item1.item_name)
#
#print(Item.is_integers(5))
#print(Item.is_integers(5.0))
#print(Item.is_integers(5.5))

#item1 = Item("Смартфон", 10000, 20)
##item1
#print(item1)

phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("iPhone 14", 120_000, 3)
print(phone1)
print(repr(phone1))
print(phone1 + item1)
phone1.number_of_sim = 0
