from Additional_Query_functions import *
from Register import Registeration
from login import login
from exit import exitpage


def run_process(option):
    obj = helper_query("BANKING", "")
    try:
        if int(option) == 1:

            obj = login("1235")
            print("1")
            obj.run_login()
            Homepage()
        elif int(option) == 2:
            print("{:-^100}".format("Welcome to our Leap bank, Press enter to Continue with Registeration"))
            print("\n")
            i = input("Press anything to Continue--> ")
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
