from Src.Core.validator import validator, argument_exception
from Src.Core.abstract_reference import abstract_reference
from Src.Models.settings_model import settings_model
 
###############################################
# Модель организации
class company_model(abstract_reference):
    __inn: int = 0
    __bic: int = 0
    __corr_account: int = 0
    __account: int = 0
    __ownership: str = ""
    def __init__(self, settings: settings_model = None) -> None:
        super().__init__()
        if settings is not None:
            if not isinstance(settings, settings_model):
                raise argument_exception("Неверный тип параметра settings!")
            if settings.company is not None:
                self.name = settings.company.name
                self.__inn = settings.company.inn
                self.__bic = settings.company.bic
                self.__corr_account = settings.company.corr_account
                self.__account = settings.company.account
                self.__ownership = settings.company.ownership

    # ИНН
    @property
    def inn(self) -> int:
        return self.__inn
    
    @inn.setter
    def inn(self, value: int):
        validator.validate(value, int, 12)
        self.__inn = value

    # БИК
    @property
    def bic(self) -> int:
        return self.__bic

    @bic.setter
    def bic(self, value: int):
        validator.validate(value, int, 9)
        self.__bic = value

    # Корреспондентский счет
    @property
    def corr_account(self) -> int:
        return self.__corr_account
        
    @corr_account.setter
    def corr_account(self, value: int):
        validator.validate(value, int, 11)
        self.__corr_account = value

    # Счет
    @property
    def account(self) -> int:
        return self.__account
    
    @account.setter
    def account(self, value: int):
        validator.validate(value, int, 11)
        self.__account = value

    # Форма собственности
    @property
    def ownership(self) -> str:
        return self.__ownership
    
    @ownership.setter
    def ownership(self, value: str):
        validator.validate(value, str, 5)
        self.__ownership = value.strip()