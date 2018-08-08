import unittest
from model import User

class UserTestcase(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            '_id' : 1,
            'firstname':'robert',
            'surname' : 'ssebintu',
            'phoneNumber' : '0775222759',
            'email' : 'roxy@gmail.com',
            'password' : '123456'
        }
    def test_add_user(self):
        user = User('robert', 'ssebintu', '0775222759', 'roxy@gmail.com', '12345678')
        self.assertEqual(user.firstname, 'robert')
        self.assertEqual(user.surname, 'ssebintu')
        self.assertEqual(user.phoneNumber, '0775222759')
        

    
    def test_validate_email(self):
        user = User('robert', 'ssebintu', '0775222759', 'roxymail.com', '12345678')
        self.assertEqual("Invalid email entered", "Invalid email entered")
    
