from Src.Core.abstract_model import abstact_model
from Src.Core.validator import validator

"""
Модели для описания рецептов:
 - ingredient_model: ингредиент + количество (строка)
 - step_model: пошаговое описание шага
 - recipe_model: рецепт в целом
"""

class ingredient_model(abstact_model):
    __name: str = ""
    __amount: str = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        self.__name = value.strip()

    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, value: str):
        validator.validate(value, str)
        self.__amount = value.strip()


class step_model(abstact_model):
    __description: str = ""

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        validator.validate(value, str)
        self.__description = value.strip()


class recipe_model(abstact_model):
    __name: str = ""
    __ingredients: list = None
    __steps: list = None
    __source: str = ""

    def __init__(self):
        super().__init__()
        self.__ingredients = []
        self.__steps = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        self.__name = value.strip()

    @property
    def ingredients(self) -> list:
        return self.__ingredients

    def add_ingredient(self, ing: ingredient_model):
        validator.validate(ing, ingredient_model)
        self.__ingredients.append(ing)

    @property
    def steps(self) -> list:
        return self.__steps

    def add_step(self, st: step_model):
        validator.validate(st, step_model)
        self.__steps.append(st)

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, value: str):
        if value is None:
            self.__source = ""
            return
        validator.validate(value, str)
        self.__source = value.strip()
