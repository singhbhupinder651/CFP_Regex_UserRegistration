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

    # Country code followed by 10 digit phone number
    def test_to_validate_phone_number(self):
        self.assertTrue(user_obj.get_phone_number('91 8618199770'))
        self.assertFalse(user_obj.get_phone_number('8618199770'))
        self.assertTrue(user_obj.get_phone_number('91 6350789669'))
        self.assertFalse(user_obj.get_phone_number('861819'))
        self.assertFalse(user_obj.get_phone_number('91 4789267892'))   

    # Password should be minimum 8 char, at least 1 upper char , at least 1 digit, exactly one special character
        self.assertTrue(user_obj.get_password('Bhupinder123@'))
        self.assertFalse(user_obj.get_password('bhupinder'))
        self.assertFalse(user_obj.get_password('Bhupinder'))
        self.assertFalse(user_obj.get_password('bhupinder12'))
        self.assertFalse(user_obj.get_password('Bhupinder123@!'))
        self.assertFalse(user_obj.get_password('Sin123@'))     

    # Valid email samples
    def test_to_validate_valid_email_samples(self):
        self.assertTrue(user_obj.get_email_samples('abc@yahoo.com'))
        self.assertTrue(user_obj.get_email_samples('abc-100@yahoo.com'))
        self.assertTrue(user_obj.get_email_samples('abc.100@yahoo.com'))
        self.assertTrue(user_obj.get_email_samples('abc111@abc.com'))
        self.assertTrue(user_obj.get_email_samples('abc100@abc.com'))
        self.assertTrue(user_obj.get_email_samples('abc.100@abc.com.au'))
        self.assertTrue(user_obj.get_email_samples('abc@1.com'))
        self.assertTrue(user_obj.get_email_samples('abc@gmail.com.com'))
        self.assertTrue(user_obj.get_email_samples('abc+100@gmail.com'))

    # Invalid email samples
    def test_to_validate_invalid_email_samples(self):
        self.assertFalse(user_obj.get_email_samples('abc'))
        self.assertFalse(user_obj.get_email_samples('abc@.com.my'))
        self.assertFalse(user_obj.get_email_samples('abc123@gmail.a'))
        self.assertFalse(user_obj.get_email_samples('abc123@.com'))
        self.assertFalse(user_obj.get_email_samples('abc123@.com.com'))
        self.assertFalse(user_obj.get_email_samples('.abc@abc.com'))
        self.assertFalse(user_obj.get_email_samples('abc()\* @gmail.com'))
        self.assertFalse(user_obj.get_email_samples('abc@%\*.com'))
        self.assertFalse(user_obj.get_email_samples('abc.@gmail.com'))
        self.assertFalse(user_obj.get_email_samples('abc@abc@gmail.com'))
        self.assertFalse(user_obj.get_email_samples('abc@gmail.com.1a'))
        self.assertFalse(user_obj.get_email_samples('abc@gmail.com.aa.au'))    
            
if __name__ == '__main__':
    unittest.main()
