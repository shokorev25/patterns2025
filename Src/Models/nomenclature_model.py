from Src.Core.validator import validator, argument_exception
from Src.Core.abstract_reference import abstract_reference
from Src.Models.range_model import range_model
from Src.Models.nomenclature_group_model import nomenclature_group_model

###############################################
# Модель номенклатуры
class nomenclature_model(abstract_reference):
    __full_name: str = ""
    __group: nomenclature_group_model = None
    __unit: range_model = None

    def __init__(self, name: str = "", full_name: str = "", group: nomenclature_group_model = None, unit: range_model = None) -> None:
        super().__init__()
        self.name = name
        self.full_name = full_name
        self.group = group
        self.unit = unit

    @property
    def full_name(self) -> str:
        return self.__full_name
    
    @full_name.setter 
    def full_name(self, value: str):
        validator.validate(value, str, 255)
        self.__full_name = value.strip()

    # Группа номенклатуры
    @property
    def group(self) -> nomenclature_group_model:
        return self.__group
    
    @group.setter
    def group(self, value: nomenclature_group_model):
        if value is not None and not isinstance(value, nomenclature_group_model):
            raise argument_exception("Группа должна быть типа nomenclature_group_model!")
        self.__group = value

    # Единица измерения
    @property
    def unit(self) -> range_model:
        return self.__unit
    
    @unit.setter
    def unit(self, value: range_model):
        if value is not None and not isinstance(value, range_model):
            raise argument_exception("Единица измерения должна быть типа range_model!")
        self.__unit = value