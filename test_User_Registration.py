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


if __name__ == '__main__':
    unittest.main()
