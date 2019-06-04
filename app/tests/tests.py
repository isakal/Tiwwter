import os
import unittest
from app import create_app, db
from app.config import TestingConfig



class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app() #creating an instance of an app
        self.app.config.from_object(TestingConfig) #applying Testing Configuration
        self.client = self.app.test_client() # instancing a test client(look at flask docs for more info)
        with self.app.app_context(): #since app hasn't been ran, we are clearing app withing app context(look at flask docs for more info )
            db.drop_all()
            db.create_all()


    def tearDown(self):
        pass


    def test_main_page(self):
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
