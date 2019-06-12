import os
import unittest
from app import create_app, db
from app.config import TestingConfig


class BasicTests(unittest.TestCase):


    def register(self, username, email, pwd):
        return self.client.post(
            '/register',
            data = dict(username=username, email=email, password=pwd,
                confirm_passwrod=pwd),
            follow_redirects=True
        )


    def login(self, email, pwd):
        return self.client.post(
            '/login',
            data=dict(email=email, password=pwd),
            follow_redirects=True
        )


    def logout(self):
        return self.client.get('/logout',
             follow_redirects=True
        )


    def setUp(self):
        self.app = create_app() # creating an instance of an app
        self.app.config.from_object(TestingConfig) # applying Testing Configuration
        self.client = self.app.test_client() # instancing a test client(look at flask docs for more info)
        with self.app.app_context(): # since app hasn't been ran, we are creating db withing app context(look at flask docs for more info )
            db.create_all()


    def tearDown(self):
        with self.app.app_context(): # since app hasn't been ran, we are clearing db withing app context(look at flask docs for more info )
            db.drop_all()


        """Error handlers testing"""
    def test_404(self):
        response = self.client.get('/test123123',follow_redirects=True)
        assert response.status_code == 404
        assert b'Page you were looking for is not found.' in response.data


if __name__ == '__main__':
    unittest.main()
