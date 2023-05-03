import unittest
import app
from models import StoreModel
from http import HTTPStatus



class StoreTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test Flask application
        self.app = app.create_app('sqlite:///:memory:')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        app.db.create_all()

    def tearDown(self):
        app.db.session.remove()
        app.db.drop_all()
        self.app_context.pop()

    # Test get a store
    def test_get_store(self):
        store = StoreModel(name="Test Store")
        app.db.session.add(store)
        app.db.session.commit()

        response = self.client.get(f"/store/{store.id}")
        self.assertEqual(response.status_code, HTTPStatus.OK)