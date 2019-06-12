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
            self.logout()


        """User testing"""
    def test_register(self): #  testing registering a user in a db
        response = self.register('test_user', 'test@test.com', 'password123')
        assert response.status_code == 200
        assert b'Join Today' in response.data


    def test_login(self): # testing logging in a user
        #self.register('test_user', 'test@test.com', 'password123')
        response = self.login('test@test.com','password123')
        assert response.status_code == 200
        assert b'Tiwwter' in response.data


    def test_logout(self): # testing logging out and redirecting to "/"
        self.register('test_user', 'test@test.com', 'password123')
        self.login('test@test.com','password123')
        self.logout()
        response = self.client.get('/')
        assert response.status_code == 200
        assert b'Log in' in response.data

    def test_browse_users(self):
        self.register('test_user', 'test@test.com', 'password123')
        self.login('test@test.com','password123')
        response = self.client.get('/user/test_user')
        #assert b'test_user' in response.data
        print(response.status_code) #404 TODO: vidi zasto nemoze dobavit usera
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
