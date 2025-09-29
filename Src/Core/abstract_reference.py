from abc import ABC
import uuid
from Src.Core.validator import validator, argument_exception

class abstract_reference(ABC):
    __unique_code: str
    __name: str = ""

    def __init__(self) -> None:
        super().__init__()
        self.__unique_code = uuid.uuid4().hex

    """
    Уникальный код
    """
    @property
    def unique_code(self) -> str:
        return self.__unique_code
    
    @unique_code.setter
    def unique_code(self, value: str):
        validator.validate(value, str)
        self.__unique_code = value.strip()
    
    """
    Наименование (ограничено 50 символами)
    """
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str):
        validator.validate(value, str, 50)
        self.__name = value.strip()
    
    """
    Перегрузка штатного варианта сравнения
    """
    def __eq__(self, other) -> bool:
        if isinstance(other, abstract_reference):
            return self.__unique_code == other.unique_code
        return False