import csv
from workshop.instantiatecsverror import InstantiateCSVError


class Item:
    pay_rate = 0.85
    examples_data = []
    initiated_examples = []

    def __init__(self, item_name: str, item_price: int, amount: int):
        self.__item_name = item_name
        self.item_price = item_price
        self.amount = amount
        self.is_integers

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
    def instantiate_from_csv(cls, file_name='items.csv') -> 'Item':
        """метод класса, выполняющий альтернативный способ создания объектов-товаров. Из csv-файла"""
        try:
            with open(file_name) as csv_items:
                csvreader = csv.DictReader(csv_items)
                for i in csvreader:
                    if list(i.keys()) == ['name', 'price', 'quantity']:
                        static_func = cls.is_integers(i['price'])
                        if static_func is True:
                            item_name, item_price, quantity = (i['name'], float(i['price']), i['quantity'])
                            cls.examples_data.append([item_name, int(item_price), quantity])
                            cls.initiated_examples.append(cls(item_name, int(item_price), quantity))
                        else:
                            item_name, item_price, quantity = (i['name'], float(i['price']), i['quantity'])
                            cls.examples_data.append([item_name, item_price, quantity])
                            cls.initiated_examples.append(cls(item_name, item_price, quantity))
                        return cls.initiated_examples
                    else:
                        raise InstantiateCSVError  #выдача ошибки повреждённого файла
        except FileNotFoundError:  #ошибка ненайденного файла
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def is_integers(item_price_type) -> bool:
        """Статический метод, который проверяет, является ли число, полученое из csv-файла целым"""
        if float(item_price_type) % 1 == 0 or float(item_price_type) % 1 == 0.0:
            return True
        else:
            return False

    def calculate_total_price(self):
        return int(self.item_price) * int(self.amount)

    def apply_discount(self):
        return float(self.item_price) * self.pay_rate

    def __repr__(self) -> str:
        """Вохвращает содержание класса"""
        return f"{self.__class__.__name__}('{self.__item_name}', '{self.item_price}', '{self.amount}')"

    def __str__(self) -> str:
        """Возвращает название товара"""
        return f'{self.__item_name}'

    def __add__(self, other):
        """Сложение экземпляров класса `Phone` и `Item`по количеству товара в магазине.
        Нельзя сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов"""
        if not isinstance(other, Item):
            raise ValueError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов')
        return self.amount + other.amount


