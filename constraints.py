class constraints:

    def spaces(self, user_response):
        for i in user_response:
            if ord(i) == 32:
                print("oops! please avoid using spaces")
                return False
        return True

    def length_constraint(self, user_response, leng):
        if len(user_response) == leng:
            return True
        else:
            print(f"oops! input must be of {leng} length")
            return False

    def integer(self, user_response):
        """

        :type user_response: Any
        """
        for i in user_response:
            if (ord(i) < 48) and (ord(i) > 57):
                print("oops! please respond with a integral values")
                return False
        return True

    def range(self, user_response, greater_than, lesser_than):
        if (user_response > greater_than) and (user_response < lesser_than):
            return True
        else:
            print("oops, looks like you entered value out of bound")

    def password(self, user_response):
        print("check1")
        print(ord('s'))
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
        if self.spaces(user_response) and self.integer(user_response) and self.length(user_response, 12):
            return True
        else:
            print("Invalid Aadhar")
            return False

    def Mobile_no(self, user_response):
        if self.spaces(user_response) and self.integer(user_response) and self.length(user_response, 10):
            return True
        else:
            print("Invalid Aadhar")
            return False

    def email_id(self, user_response):
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
            if user_response[poschar + 1] == '.':  #Check whether '.' is not just ahead of '@' or just checking if email domain is exist or not
                print("Invalid Email Address #3")
                return False
            else:
                if user_response[poschar::].count('.') != 1:  #Count of '.' after '@' should be 1
                    print("Invalid Email Address #4")
                    return False
                else:
                    Global_domain = user_response[user_response.find('.', poschar)::]  #Extracting global domain from user input email
                    if Global_domain in Global_domains:  # Checking whether top level domain exists or not
                        return True
                    else:
                        print("Invalid Email Address #5")
                        return False
