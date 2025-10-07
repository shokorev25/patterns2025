import unittest
from Src.start_service import start_service
from Src.reposity import reposity

class test_start(unittest.TestCase):

    def test_create_generates_keys(self):
        svc = start_service()
        svc.create()
        data = svc.data()
        assert reposity.range_key() in data
        assert reposity.group_key() in data
        assert reposity.nomenclature_key() in data
        assert reposity.receipts_key() in data

    def test_create_populates_non_empty(self):
        svc = start_service()
        svc.create()
        data = svc.data()
        assert len(data[reposity.range_key()]) > 0
        assert len(data[reposity.group_key()]) > 0
        assert len(data[reposity.nomenclature_key()]) > 0
        assert len(data[reposity.receipts_key()]) > 0

    def test_receipt_is_present_and_has_ingredients(self):
        svc = start_service()
        svc.create()
        data = svc.data()
        receipts = data[reposity.receipts_key()]
        assert len(receipts) >= 1
        found = None
        for r in receipts:
            if r.name == "Вафли хрустящие в вафельнице":
                found = r
                break
        assert found is not None
        assert len(found.ingredients) >= 1
        names = [n.name for n in data[reposity.nomenclature_key()]]
        assert "Пшеничная мука" in names
        assert "Сахар" in names

if __name__ == '__main__':
    unittest.main()
