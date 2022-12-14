import datetime


class constraints:

    def spaces(self, user_response):
        """
        check iteratively if there is no space in the user response
        :param user_response:
        :return:
        """
        for i in user_response:
            if ord(i) == 32:
                print("oops! please avoid using spaces")
                return False
        return True

    def length_constraint(self, user_response, leng):
        """
        check the length constraint
        :param user_response:
        :param leng:
        :return:
        """
        if len(user_response) == leng:
            return True
        else:
            print(f"oops! input must be of {leng} length")
            return False

    def integer(self, user_response):
        """
        check if the user response is integer and not
        :param user_response:
        :return:
        """
        for i in user_response:
            if (ord(i) < ord('0')) or (ord(i) > ord('9')):
                print("oops! please respond with a integral values")
                return False

        return True

    def range(self, user_response, greater_than, lesser_than):
        """
        check if the user response is in the given range or not
        :param user_response:
        :param greater_than:
        :param lesser_than:
        :return:
        """
        if (user_response > greater_than) and (user_response < lesser_than):
            return True
        else:
            print("oops, looks like you entered value out of bound")

    def password(self, user_response):
        """
        constraint for password
        :param user_response:
        :return:
        """
        if len(user_response) < 9:
            print('Please enter at least 9 character length of password')
            return False
        else:
            count_numeric = 0
            count_capital = 0
            count_small = 0
            count_special_char = 0
            count_space = 0
            for i in user_response:
                if (ord(i) >= 48) and (ord(i) <= 57):
                    count_numeric = count_numeric + 1
                elif (ord(i) >= 65) and (ord(i) <= 90):
                    count_capital = count_capital + 1
                elif (ord(i) >= 97) and (ord(i) <= 122):
                    count_small = count_small + 1
                elif ord(i) == 32:
                    print("Please avoid using Spaces in password")
                    return False
                else:
                    count_special_char = count_special_char + 1
            if count_numeric == 0:
                print('Please enter at least single numeric value')
                return False
            else:
                if count_special_char == 0:
                    print('Please use at least a special character')
                    return False
                else:
                    if count_small == 0:
                        print('Please use at least a lower case alphabet')
                        return False
                    else:
                        if count_capital == 0:
                            print('Please use at least a  upper case alphabet')
                            return False

                        else:
                            return True

    def Aadhar_card(self, user_response):
        """
        constraint for aadhar card
        :param user_response:
        :return:
        """
        if self.spaces(user_response) and self.integer(user_response) and self.length_constraint(user_response,
                                                                                                 12) and self.range(
            int(user_response), 100010001000, 999999999999):
            return True
        else:
            # print("Invalid Aadhar")
            return False

    def Mobile_no(self, user_response):
        """
        constraint for mobile input
        :param user_response:
        :return:
        """
        if self.spaces(user_response) and self.integer(user_response) and self.length_constraint(user_response,
                                                                                                 10) and self.range(
            int(user_response), 6000000000, 9999999999):
            return True
        else:
            # print("Invalid Mobile No.")
            return False

    def email_id(self, user_response):
        """
        constraint for email input
        :param user_response:
        :return:
        """
        if not self.spaces(user_response):
            return False

        poschar = user_response.find('@')  # position of '@'

        if poschar == 0:
            print("Invalid Email Address #1")
            return False

        poschar2 = user_response.find('.', poschar)  # position of '.'

        Global_domains = [".org", ".com", ".in", ".net"]  # List of top level domains used in email address

        if user_response.count('@') != 1:  # @ count of '@' should be 1
            print("Invalid Email Address #2")
            return False
        else:
            if user_response[poschar + 1] == '.':  # checking if email domain is exist or not
                print("Invalid Email Address #3")
                return False
            else:
                if user_response[poschar::].count('.') != 1:  # Count of '.' after '@' should be 1
                    print("Invalid Email Address #4")
                    return False
                else:
                    Global_domain = user_response[poschar2::]  # Extracting global domain from user input email
                    if Global_domain in Global_domains:  # Checking whether top level domain exists or not
                        return True
                    else:
                        print("Invalid Email Address #5")
                        return False

    def Pan_card(self, user_response):
        """
        constraint for pan card input
        :param user_response:
        :return:
        """
        if not self.spaces(user_response):
            return False
        if not self.length_constraint(user_response, 10):
            return False
        first_string_part = user_response[0:5]

        numeric_part = user_response[5:9]

        end_character = user_response[9]

        for i in first_string_part:
            if (ord(i) < ord('A')) or (ord(i) > ord('Z')):
                print("Invalid Pan Number #1")
                return False

        for i in numeric_part:
            if (ord(i) < ord('0')) or (ord(i) > ord('9')):
                print("Invalid Pan Number #2")
                return False

        if (ord(end_character) < ord('A')) or (ord(end_character) > ord('Z')):
            print("Invalid Pan Number #3")
            return False

        return True

    def is_valid_date(self, year, month, day):
        """
        to check if the date is valid or not
        :param year:
        :param month:
        :param day:
        :return:
        """
        isValidDate = True
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            print("Date does not exist")
            isValidDate = False
        return isValidDate

    def Age_constraint(self, birthDate):
        """
        To check the eligibility from birthdate(age>18).
        :param birthDate:
        :return:
        """
        today = datetime.date.today()
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
        if age >= 18:
            return True
        else:
            print(f"You are {18 - age} year younger than the age required for being eligible. (Age should be greater "
                  f"than 18 years)")
            return False

    def input_constraint(self, user_response, leng, Range):
        """
        constraint for taking an input inside according to given length and range
        :param user_response:
        :param leng:
        :param Range:
        :return:
        """
        if self.spaces(user_response) and self.integer(user_response) and self.length_constraint(user_response,
                                                                                                 leng) and self.range(
            int(user_response), 0, Range + 1):
            return True
            # if self.range(int(user_response[4:6:1]), 0, 13) and self.range(int(user_response[6::]), 0, 31):
            #     return True
            # else:
            #     print("Invalid date")
            #     return False
        else:
            # print("Invalid Date Of Birth")
            return False

    def input_constraintWoutl(self, user_response, Range):
        """
        constraint for user response in the given range.
        :param user_response:
        :param Range:
        :return:
        """
        if self.spaces(user_response) and self.integer(user_response) and self.range(int(user_response), 0, Range + 1):
            return True
            # if self.range(int(user_response[4:6:1]), 0, 13) and self.range(int(user_response[6::]), 0, 31):
            #     return True
            # else:
            #     print("Invalid date")
            #     return False
        else:
            # print("Invalid Date Of Birth")
            return False

    # def input_constraint(self, user_response, leng, Range):
    #     if self.spaces(user_response) and self.integer(user_response) and self.length_constraint(user_response, leng) and self.range(int(user_response), 0, Range + 1):
    #         return True
    #     else:
    #         return False

    def only_alphabet(self, user_response):
        """
        constraints for taking only alphabetical input
        :param user_response:
        :return:
        """
        for i in user_response:
            if ((ord(i) >= (ord('A'))) and (ord(i) <= (ord('Z')))) or (
                    (ord(i) >= (ord('a'))) and (ord(i) <= (ord('z')))):
                return True
            else:
                print("Please use only Alphabets")
                return False

    def name_check(self, user_response):
        """
        Constraint for name
        :param user_response:
        :return:
        """
        if self.spaces(user_response) and self.only_alphabet(user_response):
            return True
        else:
            # print("Invalid input")
            return False

# obj = constraints()
# print(obj.is_valid_date(2021, 4, 20))
