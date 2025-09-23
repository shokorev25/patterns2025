import Src
from Src.settings_manager import settings_manager
from Src.Models.company_model import company_model, Settings
import unittest
import tempfile
import json
import os


class test_models(unittest.TestCase):

    
    def test_empty_createmodel_companymodel(self):
        model = company_model()
        assert model.name == ""

    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()
        model.name = "test"
        assert model.name != ""

    
    def test_load_createmodel_companymodel(self):
        data = {
            "company": {
                "name": "Фирма А",
                "inn": "123456789012",
                "account": "11111111111",
                "corr_account": "22222222222",
                "bik": "333333333",
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
            assert manager.settings.name == "Фирма А"
            assert manager.settings.inn == "123456789012"
        finally:
            os.remove(tmp_path)

    
    def test_loadCombo_createmodel_companymodel(self):
        data = {
            "company": {
                "name": "Фирма Б",
                "inn": "987654321098",
                "account": "33333333333",
                "corr_account": "44444444444",
                "bik": "555555555",
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
            assert manager1.settings == manager2.settings
        finally:
            os.remove(tmp_path)

    
    def test_convert_to_settings(self):
        data = {
            "name": "Тестовая фирма",
            "inn": "123456789012",
            "account": "11111111111",
            "corr_account": "22222222222",
            "bik": "333333333",
            "ownership": "OOO12"
        }
        manager = settings_manager()
        manager.convert(data)
        s = manager.settings
        assert isinstance(s, Settings)
        assert s.name == "Тестовая фирма"
        assert s.inn == "123456789012"
        assert s.account == "11111111111"
        assert s.corr_account == "22222222222"
        assert s.bik == "333333333"
        assert s.ownership == "OOO12"

    
    def test_load_from_other_directory(self):
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, "custom_settings.json")

        data = {
            "company": {
                "name": "Другая фирма",
                "inn": "987654321098",
                "account": "44444444444",
                "corr_account": "55555555555",
                "bik": "666666666",
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
            s = manager.settings
            assert s.name == "Другая фирма"
            assert s.inn == "987654321098"
            assert s.account == "44444444444"
            assert s.corr_account == "55555555555"
            assert s.bik == "666666666"
            assert s.ownership == "ZAO34"
        finally:
            os.remove(file_path)


if __name__ == '__main__':
    unittest.main()
