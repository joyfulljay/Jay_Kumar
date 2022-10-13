from Register import Registeration
from login import *
from exit import *


def run_process(option):
    if option == 1:
        login()
    elif option == 2:
        reg = Registeration()
        reg.register_user()
    else:
        exitpage()


def Homepage():
    print("{:-^100}".format("Welcome to Leap bank"))
    print("1.) Hey! leaper please LOGIN")
    print("2.) Hey! do you know we create account instantly. Please REGISTER to get welcome bonus upto Rs 1000*")
    print("press Enter or any key to Exit page")
    option = int(input("Please Select Desired Option : "))
    run_process(option)


Homepage()
