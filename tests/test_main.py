import pytest
from main import Item


example = Item("Смартфон", 10000, 20)
example2 = Item("Тест", 10000.5, 20.0)

def test_item_name():
    assert example.item_name == 'Смартфон'
    #assert example2.item_name == None

def test_instantiate_from_csv():
    assert example.instantiate_from_csv() == None

def test_is_integers():
    assert example.is_integers(5.5, 5.1) == False
    assert example.is_integers(5, 5) == True

def test_calculate_total_price():
    assert example.calculate_total_price() == 200000

def test_apply_discount():
    assert example.apply_discount() == 8500.0



