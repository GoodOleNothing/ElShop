import pytest
from main import Item


example = Item("Смартфон", 10000, 20)

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



