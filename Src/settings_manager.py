import Src
from Src.Models.company_model import company_model, Settings
import os
import json

####################################################
# Менеджер настроек.
# Предназначен для управления настройками и хранения параметров приложения
class settings_manager:
    __file_name: str = ""
    __company: company_model = None
    __settings: Settings = None


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.set_default()

    @property
    def company(self) -> company_model:
        return self.__company

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, value: str):
        if value.strip() == "":
            return

        abs_path = os.path.abspath(value)
        if os.path.exists(abs_path):
            self.__file_name = abs_path
        else:
            raise Exception(f"Не найден файл настроек: {abs_path}")

    
    @property
    def settings(self) -> Settings:
        return self.__settings

    def load(self) -> bool:
        if self.__file_name.strip() == "":
            raise Exception("Не найден файл настроек!")

        try:
            with open(self.__file_name.strip(), 'r', encoding="utf-8") as file_instance:
                data = json.load(file_instance)

                if "company" in data.keys():
                    self.convert(data["company"])
                    return True
            return False
        except Exception as ex:
            print(f"Ошибка загрузки: {ex}")
            return False

    def convert(self, data: dict):
        s = Settings()
        s.name = data["name"]
        s.inn = data["inn"]
        s.account = data["account"]
        s.corr_account = data["corr_account"]
        s.bik = data["bik"]
        s.ownership = data["ownership"]
        self.__settings = s

    def set_default(self):
        self.__company = company_model()
        self.__company.name = "Рога и копыта"
        self.__settings = None
