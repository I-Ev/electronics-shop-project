"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item1.pay_rate = 0.5


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 5000


def test_name_getter():
    assert item1.name == 'Смартфон'


def test_name_setter():
    item1.name = 'Tesla'
    assert item1.name == 'Tesla'
    item1.name = 'TERRRRRRRRRRRRRRRRRRRRRR'
    assert item1.name == 'Tesla'

def test_strint_to_number():
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
