import pytest

from src.keyboard import Keyboard


def test_keyboard():
    k = Keyboard('Logitech K380', 50, 90)
    assert k.language == 'EN'
    assert k.name == 'Logitech K380'
    assert k.price == 50
    assert k.quantity == 90

    k.change_lang()
    assert k.language == 'RU'

    with pytest.raises(AttributeError):
        k.language = 'CH'
