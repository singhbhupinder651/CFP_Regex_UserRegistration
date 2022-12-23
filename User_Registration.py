'''
    @Author: Bhupinder Singh
    @Date: 21-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 21-12-2022
    @Title: Should clear all email samples provided separately
'''

import re
from data_log import get_logger

lg = get_logger(name="(Validate password rule 2)", file_name="data_log.log")


class UserRegistration:
    def __init__(self):
        self.regex_name = '^[A-Z][a-z]{2,}$'
        self.regex_email_id = '^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$'
        self.regex_phone_no = '^[0-9]{2}\s+[6-9][0-9]{9}$'
        self.regex_password = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=[^!@#$%_]*[!@#$%_][^!@#$%_]*$)[a-zA-Z0-9!@#$%_]{8,}$'

    def get_first_name(self, first_name):
        """
        Description:
            This function is used to check whether the first name starts with Cap and has minimum 3 characters
        Parameter:
            first_name: The first_name to be checked
        Return:
            None
        """
        try:
            matches = re.search(self.regex_name, first_name)
            if matches:
                lg.info(f'First name validated successfully: {first_name}')
                return True
            else:
                lg.info(
                    "Please re-enter the first name with name starts with capital and has minimum 3 characters")
                return False    
        except Exception as e:
            lg.exception(e)


    def get_last_name(self, last_name):
        """
        Description:
            This function is used to check whether the last name starts with Cap and has minimum 3 characters
        Parameter:
            last_name: The last_name to be checked
        Return:
            None
        """
        try:
            matches = re.search(self.regex_name, last_name)
            if matches:
                lg.info(f'last name validated successfully: {last_name}')
                return last_name
            else:
                lg.info(
                    "Please re-enter the last name with name starts with capital and has minimum 3 characters")
                return False    
        except Exception as e:
            lg.exception(e)

    def get_email(self, email):
        """
        Description:
            This function is used to check for valid email
        Parameter:
            email: The email to be checked
        Return:
            None
        """
        try:
            matches = re.search(self.regex_email_id, email)
            if matches:
                lg.info(f'email validated successfully: {email}')
                return True
            else:
                lg.info(
                    "Please re-enter the valid email")
                return False    
        except Exception as e:
            lg.exception(e)    

    def get_phone_number(self, phone_num):
        """
        Description:
            This function is used to check for valid phone number
        Parameter:
            phone_num: The phone_num to be checked
        Return:
            None
        """
        try:
            matches = re.search(self.regex_phone_no, phone_num)
            if matches:
                lg.info(f'Phone number validated successfully: {phone_num}')
                return True
            else:
                lg.info(
                    "Please re-enter the valid phone number")
                return False    
        except Exception as e:
            lg.exception(e) 

    def get_password(self, password):
        """
        Description:
            This function is used to check for valid password
        Parameter:
            password: The password to be checked
        Return:
            None
        """
        try:
            matches = re.search(self.regex_password, password)
            if matches:
                lg.info(f'Password validated successfully: {password}')
                return True
            else:
                lg.info(
                    "Please re-enter the valid password")
                return False    
        except Exception as e:
            lg.exception(e)                   


if __name__ == "__main__":
    try:
        user_object = UserRegistration()

        while True:

            choice = int(input("Enter the choice: \n1.Validate first-name\n2.Validate last-name\n3.Validate email-id\n4.Validate "
                  "Phone number\n5.Validate password\n0.Exit"))
            if choice == 1:
                first_name = input("Enter the first name: ")
                user_object.get_first_name(first_name)
            elif choice == 2:
                last_name = input("Enter the last name: ")
                user_object.get_last_name(last_name)
            elif choice == 3:
                email = input("Enter the email id: ")
                user_object.get_email(email)
            elif choice == 4:
                phone_num = input("Enter the phone number: ")
                user_object.get_phone_number(phone_num) 
            elif choice == 5:
                password = input("Enter the password: ")
                user_object.get_password(password)           
            else:
                break
    except Exception as e:
        lg.exception(e)
