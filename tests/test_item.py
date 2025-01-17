"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.exception_class import InstantiateCSVError
from src.item import Item, check_csvfile
from src.phone import Phone
import pytest

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


def test_repr_class():
    n1 = Item('Телефон', 60000, 5)
    assert repr(n1) == "Item('Телефон', 60000, 5)"


def test_str_class():
    m1 = Item('Телефон', 60000, 5)
    assert str(m1) == 'Телефон'


def test_add():
    m1 = Item('Телефон', 60000, 5)
    phone1 = Phone("Смартфон", 10000, 20, 6)
    assert (phone1 + m1) == 25
    with pytest.raises(TypeError):
        m1 + 500
    with pytest.raises(TypeError):
        phone1 + 500

def test_check_csvfile_invalid():
    file_path = "tests/test_csv/invalid_items.csv"
    assert check_csvfile(file_path) == False

def test_check_csvfile_valid():
    file_path = "tests/test_csv/invalid_items.csv"
    assert check_csvfile(file_path) == False
