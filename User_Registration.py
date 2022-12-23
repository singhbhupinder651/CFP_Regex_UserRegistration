'''
    @Author: Bhupinder Singh
    @Date: 21-12-2022
    @Last Modified by: Bhupinder Singh
    @Last Modified date: 21-12-2022
    @Title: Should clear all email samples provided separately
'''

import re
from data_log import get_logger

lg = get_logger(name="(Validate email samples)", file_name="data_log.log")


class UserRegistration:
    def __init__(self):
        self.regex_name = '^[A-Z][a-z]{2,}$'

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


if __name__ == "__main__":
    try:
        user_object = UserRegistration()

        while True:
            choice = int(input("Enter the choice: \n1.Validate first-name\n0.Exit"))
            if choice == 1:
                first_name = input("Enter the first name: ")
                user_object.get_first_name(first_name)
            
            else:
                break
    except Exception as e:
        lg.exception(e)
