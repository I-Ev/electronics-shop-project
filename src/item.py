import csv
from src.exception_class import InstantiateCSVError


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        item_list = []
        csv_file_path = r'C:\PythonProjects\HoweWorks\electronics-shop-project\src\items.csv'
        try:
            with open(csv_file_path, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                if check_csvfile(csv_file_path):
                    for row in reader:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        item_list.append(Item(name, price, quantity))
                else:
                    raise InstantiateCSVError("Файл item.csv поврежден")
                cls.all = item_list
        except FileNotFoundError:
            print('Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError

def check_csvfile(file_path):
    """ Возвращает True если в csv файле 3 столбца, иначе False """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Получаем заголовки
        if len(headers) == 3:  # Проверяем длину заголовков
            for row in reader: # Проходимся уже по строкам данных
                if len(row) == 3:
                    return True
    return False
