"""
Репозиторий данных
"""
class reposity:
    """
    Простой репозиторий-обёртка над словарём.
    Хранит коллекции по ключам.
    """
    def __init__(self):
        # инициализация экземпляра
        self.__data = {}

    @property
    def data(self):
        return self.__data

    # Ключ для единиц измерения
    @staticmethod
    def range_key():
        return "range_model"

    # Ключ для групп номенклатуры
    @staticmethod
    def group_key():
        return "group_model"

    # Ключ для номенклатуры
    @staticmethod
    def nomenclature_key():
        return "nomenclature_model"

    # Ключ для рецептов
    @staticmethod
    def receipts_key():
        return "receipts"
