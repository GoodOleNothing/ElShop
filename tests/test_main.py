import pytest
from main import Item


example = Item("Смартфон", 10000, 20)

#def test_item_name():
#    assert example.item_name() == None
#
##def test_instantiate_from_csv():
##    assert example.instantiate_from_csv() == 1

def test_calculate_total_price():
    assert example.calculate_total_price() == 200000

def test_apply_discount():
    assert example.apply_discount() == 8500.0



