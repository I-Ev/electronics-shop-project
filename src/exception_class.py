class InstantiateCSVError(Exception):
    """ класс-исключение для проверки повреждения файла CSV"""
    def __init__(self, *args, **kwargs):
            self.message = "Файл item.csv поврежден"


