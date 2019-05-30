import os
import unittest
from app import create_app



class BasicTests(unittest.TestCase):
    def setup(self):
        app = create_app()
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
        db.drop_all()
        db.create_al()
        print(app)

if __name__ == '__main__':
    unittest.main()
