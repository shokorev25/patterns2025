###############################################
# Модель организации
class company_model:
    __name: str = ""
    __inn: int = 0
    __account: int = 0
    __corr_account: int = 0
    __bik: int = 0

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Наименование не может быть пустым!")
        self.__name = value.strip()

    # ИНН
    @property
    def inn(self) -> int:
        return self.__inn

    @inn.setter
    def inn(self, value: int):
        value_str = str(value)
        if len(value_str) != 12 or not value_str.isdigit():
            raise ValueError("ИНН должен содержать 12 цифр!")
        self.__inn = int(value)

    # Счёт
    @property
    def account(self) -> int:
        return self.__account

    @account.setter
    def account(self, value: int):
        value_str = str(value)
        if len(value_str) != 11 or not value_str.isdigit():
            raise ValueError("Счёт должен содержать 11 цифр!")
        self.__account = int(value)

    # Корреспондентский счёт
    @property
    def corr_account(self) -> int:
        return self.__corr_account

    @corr_account.setter
    def corr_account(self, value: int):
        value_str = str(value)
        if len(value_str) != 11 or not value_str.isdigit():
            raise ValueError("Корреспондентский счёт должен содержать 11 цифр!")
        self.__corr_account = int(value)

    # БИК
    @property
    def bik(self) -> int:
        return self.__bik

    @bik.setter
    def bik(self, value: int):
        value_str = str(value)
        if len(value_str) != 9 or not value_str.isdigit():
            raise ValueError("БИК должен содержать 9 цифр!")
        self.__bik = int(value)


#################################################
# Настройки организации
class Settings:
    __ownership: str = ""

    @property
    def ownership(self) -> str:
        return self.__ownership

    @ownership.setter
    def ownership(self, value: str):
        if len(value) != 5:
            raise ValueError("Вид собственности должен содержать 5 символов!")
        self.__ownership = value
