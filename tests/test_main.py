from workshop.item import Item
from workshop.phone import Phone
from workshop.keyboard import Keyboard, Mixing
from workshop.instantiatecsverror import InstantiateCSVError

example = Item("Смартфон", 10000, 20)
example2 = Phone("iPhone 14", 120_000, 5, 2)
example3 = Keyboard('Dark Project KD87A', 9600, 5)

def test_item_name():
    assert example.item_name == 'Смартфон'

def test_instantiate_from_csv():
    assert Item.instantiate_from_csv() == Item.initiated_examples

def test_is_integers():
    assert example.is_integers(5.5) == False
    assert example.is_integers(5) == True

def test_calculate_total_price():
    assert example.calculate_total_price() == 200000

def test_apply_discount():
    assert example.apply_discount() == 8500.0

def test_repr():
    assert example.__repr__() == "Item('Смартфон', '10000', '20')"

def test_str():
    assert example.__str__() == 'Смартфон'

def test_number_of_sim():
    assert example2.number_of_sim == 2

def test_add():
    assert example + example2 == 25

def test_change_lang():
    assert example3.language == 'EN'
    example3.change_lang()
    assert example3.language == 'RU'
    example3.change_lang()
    assert example3.language == 'EN'

#def test_instantiatecsverror():
#    pass