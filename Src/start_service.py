from Src.reposity import reposity
from Src.Models.range_model import range_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.recipe_model import recipe_model, ingredient_model, step_model

class start_service:
    __repo: reposity = reposity()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        data = self.__repo.data
        data.setdefault(reposity.range_key(), [])
        data.setdefault(reposity.group_key(), [])
        data.setdefault(reposity.nomenclature_key(), [])
        data.setdefault(reposity.receipts_key(), [])

    def __create_ranges(self):
        data = self.__repo.data
        if len(data[reposity.range_key()]) == 0:
            data[reposity.range_key()].append(range_model.create_gramm())
            data[reposity.range_key()].append(range_model.create_kill())

    def __create_groups(self):
        """
        Создаёт группы номенклатуры.
        """
        data = self.__repo.data
        if len(data[reposity.group_key()]) == 0:
            g1 = group_model(); g1.name = "Мука и крупы"
            g2 = group_model(); g2.name = "Сладкое"
            g3 = group_model(); g3.name = "Масла и жиры"
            g4 = group_model(); g4.name = "Яйца"
            data[reposity.group_key()].extend([g1, g2, g3, g4])

    def __create_nomenclature(self):
        """
        Создаёт номенклатуру — добавляет ингредиенты, используемые в рецепте.
        """
        data = self.__repo.data
        if len(data[reposity.nomenclature_key()]) > 0:
            return  # уже есть данные

        grams = None
        if len(data[reposity.range_key()]) > 0:
            grams = data[reposity.range_key()][0]

        groups = data[reposity.group_key()]
        def add_item(name: str, grp_index: int):
            item = nomenclature_model()
            item.name = name
            if grams is not None:
                item.range = grams
            if 0 <= grp_index < len(groups):
                item.group = groups[grp_index]
            data[reposity.nomenclature_key()].append(item)

        add_item("Пшеничная мука", 0)   # Мука и крупы
        add_item("Сахар", 1)            # Сладкое
        add_item("Сливочное масло", 2)  # Масла и жиры
        add_item("Яйца", 3)             # Яйца
        add_item("Ванилин", 1)          # Сладкое

    def create_receipts(self):
        """
        Формирует и сохраняет пользовательский рецепт (Вафли).
        """
        data = self.__repo.data
        if len(data[reposity.receipts_key()]) > 0:
            return

        rec_my = recipe_model()
        rec_my.name = "Вафли хрустящие в вафельнице"
        rec_my.source = "user"

        ingredients = [
            ("Пшеничная мука", "100 гр"),
            ("Сахар", "80 гр"),
            ("Сливочное масло", "70 гр"),
            ("Яйца", "1 шт"),
            ("Ванилин (щепотка)", "5 гр")
        ]
        for n, a in ingredients:
            ing = ingredient_model()
            ing.name = n
            ing.amount = a
            rec_my.add_ingredient(ing)

        steps = [
            "Растопите масло (на маленьком огне, на водяной бане или в микроволновке).",
            "Добавьте в тёплое масло сахар и перемешайте венчиком до полного растворения.",
            "Добавьте в масло яйцо (убедитесь, что масло не слишком горячее) и перемешайте до однородности.",
            "Всыпьте муку и ванилин, перемешайте до получения гладкого однородного теста.",
            "Разогрейте вафельницу по инструкции. Выкладывайте тесто по столовой ложке.",
            "Пеките до золотистого цвета. Осторожно извлеките вафлю лопаткой."
        ]
        for s in steps:
            st = step_model()
            st.description = s
            rec_my.add_step(st)

        data[reposity.receipts_key()].append(rec_my)

    def create(self):
    
        self.__create_ranges()
        self.__create_groups()
        self.__create_nomenclature()
        self.create_receipts()

    def start(self):
        self.create()

    def data(self):
        return self.__repo.data
