import Src
from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model, Settings
import unittest
import tempfile
import json
import os


class test_models(unittest.TestCase):

    def test_empty_name_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.name = "   "  # пустое имя не допускается

    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()
        model.name = "test"
        assert model.name == "test"

    def test_invalid_inn_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.inn = 123  # слишком короткий

    def test_invalid_account_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.account = 123456  # слишком короткий

    def test_invalid_bik_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.bik = 111  # слишком короткий

    def test_invalid_corr_account_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.corr_account = 1  # слишком короткий

    def test_invalid_ownership_raises(self):
        s = Settings()
        with self.assertRaises(ValueError):
            s.ownership = "OO"  # слишком короткий

    def test_load_createmodel_companymodel(self):
        data = {
            "company": {
                "name": "Фирма А",
                "inn": 123456789012,
                "account": 11111111111,
                "corr_account": 22222222222,
                "bik": 333333333,
                "ownership": "OOO12"
            }
        }

        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json", encoding="utf-8") as tmp:
            json.dump(data, tmp, ensure_ascii=False)
            tmp_path = tmp.name

        try:
            manager = settings_manager()
            manager.file_name = tmp_path
            result = manager.load()
            assert result is True
            assert manager.company.name == "Фирма А"
            assert manager.company.inn == 123456789012
            assert manager.settings.ownership == "OOO12"
        finally:
            os.remove(tmp_path)

    def test_loadCombo_createmodel_companymodel(self):
        data = {
            "company": {
                "name": "Фирма Б",
                "inn": 987654321098,
                "account": 33333333333,
                "corr_account": 44444444444,
                "bik": 555555555,
                "ownership": "ZAO34"
            }
        }

        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json", encoding="utf-8") as tmp:
            json.dump(data, tmp, ensure_ascii=False)
            tmp_path = tmp.name

        try:
            manager1 = settings_manager()
            manager1.file_name = tmp_path
            manager2 = settings_manager()
            manager1.load()
            assert manager1.company == manager2.company
        finally:
            os.remove(tmp_path)

    def test_load_from_other_directory(self):
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, "custom_settings.json")

        data = {
            "company": {
                "name": "Другая фирма",
                "inn": 987654321098,
                "account": 44444444444,
                "corr_account": 55555555555,
                "bik": 666666666,
                "ownership": "ZAO34"
            }
        }

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)

        try:
            manager = settings_manager()
            manager.file_name = file_path
            result = manager.load()
            assert result is True
            assert manager.company.name == "Другая фирма"
            assert manager.company.inn == 987654321098
            assert manager.settings.ownership == "ZAO34"
        finally:
            os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
    