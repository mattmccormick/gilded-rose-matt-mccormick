import unittest
import json
import api


class TestCase(unittest.TestCase):
    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def test_inventory_length(self):
        data = self._get_inventory_data()
        assert len(data) == 5  # would not be hardcoded in a real test suite

    def test_inventory_items(self):
        for item in self._get_inventory_data():
            assert 'id' in item
            assert 'name' in item
            assert 'price' in item
            assert 'description' in item

            assert isinstance(item['id'], int)
            assert isinstance(item['name'], unicode)
            assert isinstance(item['price'], int)
            assert isinstance(item['description'], unicode)

    def _get_inventory_data(self):
        rv = self.app.get('/items')
        data = json.loads(rv.data)
        return data


if __name__ == '__main__':
    unittest.main()