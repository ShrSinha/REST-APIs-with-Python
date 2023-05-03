from unittest import TestCase
from app import create_app
from db import db

class TestBase(TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test Flask application
        app = create_app('sqlite:///:memory:')
        app.config['TESTING'] = True
        cls.app = app.test_client()
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with cls.app.application.app_context():
            db.drop_all()
