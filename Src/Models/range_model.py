from Src.Core.entity_model import entity_model
from Src.Core.validator import validator, argument_exception

"""
Модель единицы измерения
"""
class range_model(entity_model):
    __value:int = 1
    __base:'range_model' = None

    """
    Значение коэффициента пересчета (целое)
    """
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        validator.validate(value, int)
        if value <= 0:
             raise argument_exception("Некорректный аргумент!")
        self.__value = value

    """
    Базовая единица измерения
    """
    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        # база может быть None либо range_model
        if value is not None:
            validator.validate(value, range_model)
        self.__base = value

    """
    Фабрики для распространённых единиц
    """
    @staticmethod
    def create_kill():
        """
        Киллограмм (килограмм): база грамм, коэффициент 1000
        """
        gramm = range_model.create_gramm()
        item = range_model.create("киллограмм", gramm)
        item.value = 1000
        return item

    @staticmethod
    def create_gramm():
        item = range_model.create("грамм")
        item.value = 1
        return item

    @staticmethod
    def create(name:str, base=None):
        validator.validate(name, str)
        inner_base = None
        if base is not None:
            validator.validate(base, range_model)
            inner_base = base
        item = range_model()
        item.name = name
        item.base = inner_base
        return item
