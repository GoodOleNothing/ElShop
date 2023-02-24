class Item:
    pay_rate = 0.85
    examples_data = []

    def __init__(self, item_name, item_price, amount):
        self.item_name = item_name
        self.item_price = item_price
        self.amount = amount
        self.examples_data.append([item_name, item_price, amount])

    def calculate_total_price(self):
        return self.item_price * self.amount

    def apply_discount(self):
        return self.item_price * self.pay_rate


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8

print(item1.apply_discount())
print(item2.item_price)
print(item1.examples_data)
print(item1.examples)
