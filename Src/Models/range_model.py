from Src.Core.validator import validator, argument_exception
from Src.Core.abstract_reference import abstract_reference

###############################################
# Модель единицы измерения
class range_model(abstract_reference):
    __base_unit: 'range_model' = None
    __conversion_factor: float = 1.0

    def __init__(self, name: str = "", conversion_factor: float = 1.0, base_unit: 'range_model' = None) -> None:
        super().__init__()
        self.name = name
        self.conversion_factor = conversion_factor
        self.base_unit = base_unit


    @property
    def base_unit(self) -> 'range_model':
        return self.__base_unit
    
    @base_unit.setter
    def base_unit(self, value: 'range_model'):
        if value is not None and not isinstance(value, range_model):
            raise argument_exception("Базовая единица измерения должна быть типа range_model!")
        self.__base_unit = value


    @property 
    def conversion_factor(self) -> float:
        return self.__conversion_factor
    
    @conversion_factor.setter
    def conversion_factor(self, value: float):
        validator.validate(value, float)
        if value <= 0:
            raise argument_exception("Коэффициент пересчета должен быть больше 0!")
        self.__conversion_factor = value