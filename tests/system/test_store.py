from tests.test_base import TestBase
from http import HTTPStatus


class TestStores(TestBase):
    def test_get_stores_empty(self):
        response = self.app.get('/stores')
        self.assertEqual(response.status_code, 200)
        #self.assertDictEqual(response.json, {'stores': []})

    def test_post_store(self):
        data = {'name': 'Test Store'}
        response = self.app.post('/stores', json=data)
        self.assertEqual(response.status_code, 201)
        #self.assertDictEqual(response.json, {'name': 'Test Store', 'items': []})

    def test_get_stores(self):
        data = {'name': 'Test Store'}
        self.app.post('/stores', json=data)
        response = self.app.get('/stores')
        self.assertEqual(response.status_code, 200)
        #self.assertDictEqual(response.json, {'stores': [{'name': 'Test Store', 'items': []}]})