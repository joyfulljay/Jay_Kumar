from Additional_Query_functions import *
from Register import Registeration
from constraints import *
from login import login
from exit import exitpage

cons = constraints()
check_password = helper_query("BANKING", "Login_Details")
reg = Registeration()


def Username_input():
    username = reg.taking_input("Enter your username: ", 10, 9999999999)
    if check_password.CheckInFunction("Login_Username", username):
        return username
    else:
        print("User name does not exist")
        temp = reg.taking_input("1.) Back to homepage\n2.) Retry Username\nSelect your desired field: ", 1, 2)
        if int(temp) == 2:
            out = Username_input()
            return out
        else:
            print(temp)
            return None


def password_input(username):
    password = input("Enter Password: ")
    if not cons.password(password):
        print("Try Again")
        out = password_input()
        return out
    else:
        if check_password.password_check("Login_Username", username, "Password", password):
            return True
        else:
            print("User name does not exist")
            temp = reg.taking_input("1.) Back to homepage\n2.) Retry Password\nSelect your desired field: ", 1, 2)
            if int(temp) == 2:
                out = Username_input()
                return out
            else:
                return False


def run_process(option):
    try:
        if int(option) == 1:
            username = Username_input()
            if username is None:
                Homepage()
                return
            else:
                if password_input(username):
                    obj = login(username)
                    obj.run_login()
                    Homepage()
                else:
                    return

        elif int(option) == 2:
            print("{:-^100}".format("Welcome to our Leap bank, Press enter to Continue with Registeration"))
            print("\n")
            # i = input("Press anything to Continue--> ")
            reg = Registeration()
            check = reg.register_user()
            if check:
                reg.last_check()
                reg.database_creation()
            Homepage()



    except Exception as e:
        exitpage()


def Homepage():
    print("{:-^100}".format("Welcome to Leap bank"))
    print("1.) Hey! leaper please LOGIN")
    print("2.) Hey! do you know we create account instantly. Please REGISTER to get welcome bonus upto Rs 1000*")
    print("press Enter or any key to Exit page")
    option = input("Please Select Desired Option : ")
    run_process(option)


Homepage()
