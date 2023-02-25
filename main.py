import csv


class Item:
    pay_rate = 0.85
    examples_data = []
    initiated_examples = []

    def __init__(self, item_name: str, item_price: int, amount: int):
        self.__item_name = item_name
        self.item_price = item_price
        self.amount = amount

    @property
    def item_name(self) -> str:
        """проверка, что при задании названия товара длина его не превышает 10 символов.
        При привышении - исключение"""
        return self.__item_name

    @item_name.setter
    def item_name(self, value: str) -> None:
        if len(value) <= 10:
            self.__item_name = value
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls) -> 'Item':
        """метод класса, выполняющий альтернативный способ создания объектов-товаров. Из csv-файла"""
        with open('items.csv') as csvitems:
            csvreader = csv.DictReader(csvitems)
            for i in csvreader:
                cls.examples_data.append([i['name'], i['price'], i['quantity']])
                item_name, item_price, amount = (i['name'], i['price'], i['quantity'])
                cls.initiated_examples.append(cls(item_name, item_price, amount))

    def calculate_total_price(self):
        return int(self.item_price) * int(self.amount)

    def apply_discount(self):
        return float(self.item_price) * self.pay_rate






#item1 = Item("Смартфон", 10000, 20)
#item2 = Item("Ноутбук", 20000, 5)
#print(item1.calculate_total_price())
#print(item2.calculate_total_price())
#Item.pay_rate = 0.8
#print(item1.apply_discount())
#print(item2.item_price)
#print(item1.examples_data)
#print(item1.examples)
#print(item1._item_name)

#item = Item('Телефон', 10000, 5)
#item.item_name = 'Смартфон'
#print(item.item_name)
#item.item_name = 'СуперСмартфон'

Item.instantiate_from_csv()
print(len(Item.initiated_examples))
item1 = Item.initiated_examples[0]
print(item1.item_name)


