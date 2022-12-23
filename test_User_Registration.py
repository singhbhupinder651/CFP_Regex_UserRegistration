'''
    @Author: Bhupinder Singh
    @Date: 22-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 22-12-2022
    @Title: Unit testing of test cases for user registration
'''

import unittest
from User_Registration import UserRegistration


user_obj = UserRegistration()


class TestUserRegistration(unittest.TestCase):
    # start with capital letter and minimum 3 chars.
    def test_to_validate_first_name(self):
        self.assertTrue(user_obj.get_first_name('Bhupinder'))
        self.assertFalse(user_obj.get_first_name('bhupinder'))
        self.assertTrue(user_obj.get_first_name('Bhu'))
        self.assertFalse(user_obj.get_first_name('Bh'))

        

    # start with capital letter and minimum 3 chars.
    def test_to_validate_last_name(self):
        self.assertTrue(user_obj.get_last_name('Singh'))
        self.assertFalse(user_obj.get_last_name('singh'))
        self.assertTrue(user_obj.get_last_name('Sin'))
        self.assertFalse(user_obj.get_last_name('Si'))

    # Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions
    def test_to_validate_email(self):
        self.assertTrue(user_obj.get_email('abc.xyz@bl.co.in'))
        self.assertFalse(user_obj.get_email('.xyzbl.co.in'))
        self.assertTrue(user_obj.get_email('abc.@bl.co.in'))
        self.assertFalse(user_obj.get_email('abc.xyz@.co.in'))
        self.assertTrue(user_obj.get_email('abc@bl.co'))
        self.assertFalse(user_obj.get_email('abc@bl'))
        
            
if __name__ == '__main__':
    unittest.main()
