"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item1.pay_rate = 0.5


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    item1.apply_discount()
    assert item1.price == 5000
