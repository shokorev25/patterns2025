from Src.Core.validator import validator, argument_exception
from Src.Models.company_model import company_model

######################################
# Модель настроек приложения
class settings_model: 
    __company: company_model = None

    # Текущая организация
    @property
    def company(self) -> company_model:
        return self.__company
    
    @company.setter
    def company(self, value: company_model):
        if value is not None and not isinstance(value, company_model):
            raise argument_exception("Компания должна быть типа company_model!")
        self.__company = value