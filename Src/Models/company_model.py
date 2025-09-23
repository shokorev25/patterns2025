###############################################
# Модель организации
class company_model:
    __name: str = ""
    __inn: str = ""

    # Наименование
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() != "":
            self.__name = value.strip()


#################################################
# Настройки организации
class Settings:
    __name: str = ""
    __inn: str = ""
    __account: str = ""
    __corr_account: str = ""
    __bik: str = ""
    __ownership: str = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Наименование не может быть пустым!")
        self.__name = value.strip()

    # ИНН
    @property
    def inn(self) -> str:
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if len(value) != 12:
            raise ValueError("ИНН должен содержать 12 символов!")
        self.__inn = value

    # Счёт
    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, value: str):
        if len(value) != 11:
            raise ValueError("Счёт должен содержать 11 символов!")
        self.__account = value

    # Корреспондентский счёт
    @property
    def corr_account(self) -> str:
        return self.__corr_account

    @corr_account.setter
    def corr_account(self, value: str):
        if len(value) != 11:
            raise ValueError("Корреспондентский счёт должен содержать 11 символов!")
        self.__corr_account = value

    # БИК
    @property
    def bik(self) -> str:
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if len(value) != 9:
            raise ValueError("БИК должен содержать 9 символов!")
        self.__bik = value

    # Вид собственности
    @property
    def ownership(self) -> str:
        return self.__ownership

    @ownership.setter
    def ownership(self, value: str):
        if len(value) != 5:
            raise ValueError("Вид собственности должен содержать 5 символов!")
        self.__ownership = value
