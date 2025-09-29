from Src.Models.settings_model import settings_model
from Src.Core.validator import argument_exception, operation_exception
from Src.Core.validator import validator
from Src.Models.company_model import company_model
import os
import json

####################################################
# Менеджер настроек.
# Предназначен для управления настройками и хранения параметров приложения
class settings_manager:

    __full_file_name: str = ""
    __settings: settings_model = None


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance 
    
    def __init__(self):
        self.set_default()


    @property
    def settings(self) -> settings_model:
        return self.__settings


    @property
    def file_name(self) -> str:
        return self.__full_file_name

    @file_name.setter
    def file_name(self, value: str):
        validator.validate(value, str)
        full_file_name = os.path.abspath(value)        
        if os.path.exists(full_file_name):
            self.__full_file_name = full_file_name.strip()
        else:
            raise argument_exception(f'Не найден файл настроек {full_file_name}')


    def open(self, file_name: str) -> bool:
        self.file_name = file_name
        return self.load()


    def load(self) -> bool:
        if self.__full_file_name == "":
            raise operation_exception("Не найден файл настроек!")

        try:
            with open(self.__full_file_name, 'r') as file_instance:
                settings = json.load(file_instance)

                if "company" in settings.keys():
                    data = settings["company"]
                    return self.convert(data)

            return False
        except Exception as e:
            raise operation_exception(f"Ошибка при загрузке настроек: {str(e)}")
        

    def convert(self, data: dict) -> bool:
        validator.validate(data, dict)

        fields = list(filter(lambda x: not x.startswith("_"), dir(self.__settings.company))) 
        matching_keys = list(filter(lambda key: key in fields, data.keys()))

        try:
            for key in matching_keys:
                setattr(self.__settings.company, key, data[key])
        except Exception as e:
            raise operation_exception(f"Ошибка при преобразовании данных: {str(e)}")

        return True


    def set_default(self):
        company = company_model()
        company.name = "Рога и копыта"
        company.inn = -1
        
        self.__settings = settings_model()
        self.__settings.company = company