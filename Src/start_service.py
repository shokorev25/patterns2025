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

    def __default_create_ranges(self):
        """
        Создаёт базовые единицы измерения: грамм и килограмм
        """
        data = self.__repo.data
        if len(data[reposity.range_key()]) == 0:
            data[reposity.range_key()].append(range_model.create_gramm())
            data[reposity.range_key()].append(range_model.create_kill())

    def __default_create_groups(self):
        """
        Создаёт группы номенклатуры
        """
        data = self.__repo.data
        if len(data[reposity.group_key()]) == 0:
            g1 = group_model()
            g1.name = "Овощи"
            g2 = group_model()
            g2.name = "Мука и крупы"
            g3 = group_model()
            g3.name = "Сладости/Сахар"
            data[reposity.group_key()].extend([g1, g2, g3])

    def __default_create_nomenclature(self):
        """
        Создаёт примеры номенклатуры, связывая с группами и единицами измерения
        """
        data = self.__repo.data
        if len(data[reposity.nomenclature_key()]) == 0:
            grams = None
            veg_group = None
            flour_group = None
            if len(data[reposity.range_key()]) > 0:
                grams = data[reposity.range_key()][0]
            if len(data[reposity.group_key()]) >= 2:
                veg_group = data[reposity.group_key()][0]
                flour_group = data[reposity.group_key()][1]

            if grams is not None and veg_group is not None:
                item = nomenclature_model()
                item.name = "Морковь"
                item.range = grams
                item.group = veg_group
                data[reposity.nomenclature_key()].append(item)

            if grams is not None and flour_group is not None:
                item2 = nomenclature_model()
                item2.name = "Пшеничная мука"
                item2.range = grams
                item2.group = flour_group
                data[reposity.nomenclature_key()].append(item2)

            if grams is not None:
                sugar = nomenclature_model()
                sugar.name = "Сахар"
                sugar.range = grams
                sugar.group = data[reposity.group_key()][2] if len(data[reposity.group_key()]) > 2 else None
                data[reposity.nomenclature_key()].append(sugar)

    def create_receipts(self):
        """
        Формирует и сохраняет два рецепта:
         - рецепт, полученный на занятии (пример с морковью)
         - собственный рецепт (вафли — по заданию)
        """
        data = self.__repo.data
        if len(data[reposity.receipts_key()]) > 0:
            return

        rec_lesson = recipe_model()
        rec_lesson.name = "Примерный овощной рецепт (на занятии)"
        rec_lesson.source = "lesson"

        ing_l1 = ingredient_model()
        ing_l1.name = "Морковь"
        ing_l1.amount = "200 г"
        rec_lesson.add_ingredient(ing_l1)

        st_l1 = step_model()
        st_l1.description = "Почистить и нарезать овощи."
        rec_lesson.add_step(st_l1)

        data[reposity.receipts_key()].append(rec_lesson)

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

        # шаги — краткие
        steps = [
            "Растопите масло (на маленьком огне, на водяной бане или в микроволновке).",
            "Добавьте в тёплое масло сахар и перемешайте венчиком до растворения.",
            "Добавьте в масло яйцо (убедитесь, что масло не слишком горячее), перемешайте до однородности.",
            "Всыпьте муку и ванилин. Перемешайте до получения гладкого теста.",
            "Разогрейте вафельницу согласно инструкции. Выкладывайте тесто по столовой ложке.",
            "Пеките до золотистого цвета. Осторожно откройте, извлеките вафлю лопаткой."
        ]
        for s in steps:
            st = step_model()
            st.description = s
            rec_my.add_step(st)

        data[reposity.receipts_key()].append(rec_my)

    """
    Основной метод для генерации эталонных данных
    """
    def start(self):
        self.__default_create_ranges()
        self.__default_create_groups()
        self.__default_create_nomenclature()
        self.create_receipts()

    def data(self):
        return self.__repo.data
