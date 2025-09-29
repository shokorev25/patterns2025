from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model
from Src.Models.storage_model import storage_model
from Src.Models.range_model import range_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.nomenclature_group_model import nomenclature_group_model
import unittest
import uuid
from Src.Core.validator import argument_exception, operation_exception

class test_models(unittest.TestCase):


    def test_empty_createmodel_companymodel(self):
        model = company_model()
        self.assertEqual(model.name, "")
        self.assertEqual(model.inn, 0)
        self.assertEqual(model.bic, 0)
        self.assertEqual(model.corr_account, 0)
        self.assertEqual(model.account, 0)
        self.assertEqual(model.ownership, "")


    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()
        model.name = "Тестовая компания"
        model.inn = 123456789012
        model.bic = 123456789
        model.corr_account = 12345678901
        model.account = 12345678901
        model.ownership = "ООО"
        self.assertEqual(model.name, "Тестовая компания")
        self.assertEqual(model.inn, 123456789012)
        self.assertEqual(model.bic, 123456789)
        self.assertEqual(model.corr_account, 12345678901)
        self.assertEqual(model.account, 12345678901)
        self.assertEqual(model.ownership, "ООО")

 
    def test_create_from_settings_companymodel(self):
        manager = settings_manager()
        try:
            manager.open("settings.json")
            model = company_model(manager.settings)
            self.assertEqual(model.name, manager.settings.company.name)
            self.assertEqual(model.inn, manager.settings.company.inn)
        except operation_exception:
            self.skipTest("Файл настроек не найден, пропуск теста")

    def test_empty_createmodel_storagemodel(self):
        model = storage_model()
        self.assertEqual(model.name, "")

    def test_notEmpty_createmodel_storagemodel(self):
        model = storage_model("Склад 1")
        self.assertEqual(model.name, "Склад 1")

    def test_empty_createmodel_rangemodel(self):
        model = range_model()
        self.assertEqual(model.name, "")
        self.assertEqual(model.conversion_factor, 1.0)
        self.assertIsNone(model.base_unit)

    def test_notEmpty_createmodel_rangemodel(self):
        base_unit = range_model("грамм", 1.0)
        model = range_model("килограмм", 1000.0, base_unit)
        self.assertEqual(model.name, "килограмм")
        self.assertEqual(model.conversion_factor, 1000.0)
        self.assertEqual(model.base_unit, base_unit)

    def test_range_model_conversion(self):
        base_unit = range_model("грамм", 1.0)
        kg_unit = range_model("килограмм", 1000.0, base_unit)
        self.assertEqual(kg_unit.conversion_factor, 1000.0)
        self.assertEqual(kg_unit.base_unit.name, "грамм")
        with self.assertRaises(argument_exception):
            kg_unit.conversion_factor = -1.0
        with self.assertRaises(argument_exception):
            kg_unit.base_unit = "invalid"

    def test_createmodel_nomenclaturegroupmodel(self):
        model = nomenclature_group_model("Группа 1")
        self.assertEqual(model.name, "Группа 1")

    def test_createmodel_nomenclaturemodel(self):
        group = nomenclature_group_model("Электроника")
        unit = range_model("штука", 1.0)
        model = nomenclature_model("Телефон", "Смартфон XYZ", group, unit)
        self.assertEqual(model.name, "Телефон")
        self.assertEqual(model.full_name, "Смартфон XYZ")
        self.assertEqual(model.group, group)
        self.assertEqual(model.unit, unit)

    def test_name_length_limit(self):
        model = storage_model()
        with self.assertRaises(argument_exception):
            model.name = "А" * 51  

    def test_load_settings_and_create_company(self):
        manager = settings_manager()
        try:
            manager.open("settings.json")
            model = company_model(manager.settings)
            self.assertTrue(isinstance(model, company_model))
            self.assertEqual(model.name, manager.settings.company.name)
        except operation_exception:
            self.skipTest("Файл настроек не найден, пропуск теста")

    def test_equals_storage_model_create(self):
        id = uuid.uuid4().hex
        storage1 = storage_model("Склад 1")
        storage1.unique_code = id
        storage2 = storage_model("Склад 2")
        storage2.unique_code = id
        self.assertTrue(storage1 == storage2)

if __name__ == '__main__':
    unittest.main()