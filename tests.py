import unittest
import json
import api

from models import Item


class TestCase(unittest.TestCase):

    GET_ITEMS = '/items'
    POST_ITEMS_PURCHASE = '/items/{}/purchase'

    def setUp(self):
        api.app.config['TESTING'] = True
        self.app = api.app.test_client()

    def test_inventory_length(self):
        data = self._get_inventory_data()
        assert len(data) == len(Item.get_all())

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

    def test_unauthorized_purchase(self):
        rv = self.app.post(self.POST_ITEMS_PURCHASE.format(self._get_valid_item_id()))
        assert rv.status_code == 401

    def test_authorized_purchase(self):
        rv = self._post_authorized_purchase(self._get_valid_item_id())
        assert rv.status_code == 200

        data = self._get_data(rv)

        assert 'success' in data
        assert data['success']

    def test_invalid_purchase(self):
        id = 99999
        assert id not in Item.get_all()

        rv = self._post_authorized_purchase(id)

        assert rv.status_code == 404

    def _get_inventory_data(self):
        rv = self.app.get(self.GET_ITEMS)
        return self._get_data(rv)

    def _get_data(self, rv):
        data = json.loads(rv.data)
        return data

    def _get_valid_item_id(self):
        items = Item.get_all()
        return items.keys()[0]

    def _post_authorized_purchase(self, id):
        token = list(api.valid_tokens)[0]
        return self.app.post(self.POST_ITEMS_PURCHASE.format(id), headers={'Authorization': 'Token {}'.format(token)})


if __name__ == '__main__':
    unittest.main()