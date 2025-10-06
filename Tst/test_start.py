import unittest
from Src.start_service import start_service
from Src.reposity import reposity

class test_start(unittest.TestCase):

    def test_data_generation_keys_exist(self):
        svc = start_service()
        svc.start()
        data = svc.data()
        assert reposity.range_key() in data
        assert reposity.group_key() in data
        assert reposity.nomenclature_key() in data
        assert reposity.receipts_key() in data

    def test_data_generation_non_empty(self):
        svc = start_service()
        svc.start()
        data = svc.data()
        assert len(data[reposity.range_key()]) > 0
        assert len(data[reposity.group_key()]) > 0
        assert len(data[reposity.nomenclature_key()]) > 0
        assert len(data[reposity.receipts_key()]) > 0

    def test_receipt_contents(self):
        svc = start_service()
        svc.start()
        data = svc.data()
        receipts = data[reposity.receipts_key()]
        assert len(receipts) >= 2
        found = any(r.name == "Вафли хрустящие в вафельнице" for r in receipts)
        assert found

if __name__ == '__main__':
    unittest.main()
