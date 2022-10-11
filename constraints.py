class constraints:
    def integer(self, user_response):
        if isinstance(user_response, int):
            return True
        else:
            print("oops, looks like you entered non integral value")
            return False

    def range(self, user_response, greater_than, lesser_than):
        if (user_response > greater_than) and (user_response < lesser_than):
            return True
        else:
            print("oops, looks like you entered value out of bound")

    def password(self, user_response):
        print("check1")
        print(ord('s'))
        if len(user_response) < 9:
            print('Please enter atleast 9 character length of password')
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
                print('Please enter atleast 1 numeric value')
                return False
            else:
                if count_special_char == 0:
                    print('Please use atleast a special character')
                    return False
                else:
                    if count_small == 0:
                        print('Please use atleast a lower case alphabet')
                        return False
                    else:
                        if count_capital == 0:
                            print('Please use atleast a  upper case alphabet')
                            return False

                        else:
                            return True
