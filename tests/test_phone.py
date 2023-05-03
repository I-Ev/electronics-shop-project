from src.item import Item
from src.phone import Phone

assert issubclass(Phone, Item) == True

phone1 = Phone("Смартфон", 10000, 20, 6)

assert phone1.number_of_sim == 6
assert repr(phone1) == "Phone('Смартфон', 10000, 20, 6)"
