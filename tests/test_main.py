import pytest
from main import Item

#@pytest.fixture
#def item_data():
#    return ["Смартфон", 10000, 20]

example = Item("Смартфон", 10000, 20)
def test_calculate_total_price():
    assert example.calculate_total_price() == 200000

def test_apply_discount():
    assert example.apply_discount() == 8000.0
