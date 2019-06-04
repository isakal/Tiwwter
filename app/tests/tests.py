import os
import unittest
from app import create_app, db
from app.config import TestingConfig



class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app() #creating an instance of an app
        self.app.config.from_object(TestingConfig) #applying Testing Configuration
        self.client = self.app.test_client() # instancing a test client(look at flask docs for more info)
        with self.app.app_context(): #since app hasn't been ran, we are creating db withing app context(look at flask docs for more info )
            db.create_all()


    def tearDown(self):
        with self.app.app_context(): #since app hasn't been ran, we are clearing db withing app context(look at flask docs for more info )
            db.drop_all()


    def test_main_page(self): #testing a simple get request to a "/" route
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200


    def test_register(self): #TODO: make a register function that makes a profile in a test db 
        pass


if __name__ == '__main__':
    unittest.main()
