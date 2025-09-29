from Src.Core.validator import validator
from Src.Core.abstract_reference import abstract_reference

###############################################
# Модель группы номенклатуры
class nomenclature_group_model(abstract_reference):
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self.name = name