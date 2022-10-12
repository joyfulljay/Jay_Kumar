from constraints import *
from Additional_Query_functions import *
from login import *


class Registeration:
    def __init__(self):
        self.constraint_obj = constraints()
        self.query_obj = helper_query("BANKING", "Registeration")

    def Mobile_input(self, user_response):
        t = 0
        response = input("Enter Valid Mobile no. : +91 ")

        if self.constraint_obj.Mobile_no(response):

            if self.query_obj.CheckInFunction("Mobile_no"):
                print("Aap is no. se pehele se hi registered ho login karo ho jayega....")
                user_input = input("press ENTER to go on login page to retry with another mobile no. press any: ")
                if bool(user_input):
                    self.Mobile_input()
                else:
                    login()
            elif t > 3:
                print("{: ^100}".format("\U0001F60C \U0001F60C \U0001F60C "))
                print("{: ^100}".format("Mujhe pata tha bhai tu karlega"))
            return response
        else:
            t = t + 1
            if t == 0:
                print("kripya! 10 ankon ka sahi mobile no. darj kijiye.........")
            elif t == 1:
                print("Ye no. bhi sahi nahi hai, kripya! 10 ankon ka sahi mobile no. darj kijiye.........")
            elif t == 2:
                print("Kya kar rahe ho bhai, kripya! 10 ankon ka sahi mobile no. darj kijiye.........")
            elif t == 3:
                print("jab ho jaye tab batadena, mein sone jaa raha")
            else:
                print("try again")
                print("{: ^100}".format(" \U0001F634 \U0001F634 \U0001F634 \U0001F62A "))
