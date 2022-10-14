from Register import Registeration
from login import *
# from exit import exitpage


def run_process(option):
    try:
        if int(option) == 1:
            login()
            Homepage()
        elif int(option) == 2:
            print("{:-^100}".format("Welcome to our Leap bank, Press enter to Continue with Registeration"))
            print("\n")
            i = input("Press anything to Continue--> ")
            reg = Registeration()
            reg.register_user()
            print("gfwegdekhs")
            Homepage()

    except:
        # exitpage()
        print("")


def Homepage():
    print("{:-^100}".format("Welcome to Leap bank"))
    print("1.) Hey! leaper please LOGIN")
    print("2.) Hey! do you know we create account instantly. Please REGISTER to get welcome bonus upto Rs 1000*")
    print("press Enter or any key to Exit page")
    option = input("Please Select Desired Option : ")
    run_process(option)


Homepage()
