import os
import unittest
from app import create_app, db
from app.config import TestingConfig



class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.from_object(TestingConfig)
        with self.app.app_context():
            db.drop_all()
            db.create_all()
        

    def tearDown(self):
        pass


    def test_main_page(self):
        self.app = create_app()
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
