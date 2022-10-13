from constraints import *
from Additional_Query_functions import *
from login import *
from homepage import *
from Data_Queries import *


class Registeration:
    def __init__(self):
        self.constraint_obj = constraints()
        self.query_obj = helper_query("BANKING", "Registeration")
        self.query_obj_pincode = helper_query("BANKING", "PincodeDB")
        self.data_query_obj = Data_queries("PincodeDB", "BANKING")

    def Enter_mobile_no(self):
        print("Step 1")
        t = 0
        response = input("Enter Valid Mobile no. : +91 ")

        if self.constraint_obj.Mobile_no(response):

            if self.query_obj.CheckInFunction("Mobile_no", response):
                print("Aap is no. se pehele se hi registered ho login karo ho jayega....")
                user_input = input("press ENTER to go on login page to retry with another mobile no. press any: ")
                if bool(user_input):
                    self.Mobile_input()
                else:
                    login()
            elif t > 3:
                print("{: ^100}".format("\U0001F60C \U0001F60C \U0001F60C "))
                print("{: ^100}".format("Finally! you did it"))
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
                print("jab ho jaye tab batadena, mein thoda so leta hun")
            else:
                print("try again")
                print("{: ^100}".format(" \U0001F634 \U0001F634 \U0001F634 \U0001F62A "))

    def Enter_Aadhar_no(self):
        response = input("Please enter the 12 digits valid Aadhar no: ")
        if self.query_obj.CheckInFunction("Aadhar_card", response):
            print("You are already registered")
            user_input = input("press ENTER to go on login page or press anything to go on homepage")
            if bool(user_input):
                Homepage()
                return
            else:
                login()
                return

        if self.constraint_obj.Aadhar_card(response):
            return response
        else:
            print(
                "Oops! please Try Again, Your Aadhar No. should be of 12 digits and should not have spaces in between")
            user_input = input("press ENTER to continue with Aadhar details or enter anything to go on homepage")
            if bool(user_input):
                Homepage()
                return
            else:
                self.Enter_Aadhar_no()

    def Enter_Your_first_name(self):
        response = input("Please Enter your First Name without spaces")
        if self.constraint_obj.name_check(response):
            return response
        else:
            print("Try Again")
            self.Enter_Your_first_name()

    def Enter_Your_Last_name(self):
        response = input("Please Enter your Last Name without spaces")
        if self.constraint_obj.name_check(response):
            return response
        else:
            print("Try Again")
            self.Enter_Your_Last_name()

    def Enter_D_O_B(self):
        response = input("Please Enter Date Of Birth in format YYYYMMDD")
        if self.constraint_obj.D_O_B(response):
            date_formatted = "'" + response[:4:] + "-" + response[4:6:] + "-" + response[6::] + "'"
            return date_formatted
        else:
            print(
                "Oops! please Try Again, Your input format should be 8 digits in format YYYYMMD")
            user_input = input("press ENTER to continue with D-O-B or enter anything to go on homepage")
            if bool(user_input):
                Homepage()
                return
            else:
                self.Enter_D_O_B()

    def Enter_Email(self):
        response = input("Please Enter a valid Email address: ")
        if self.constraint_obj.email_id(response):
            return response
        else:
            print("Oops! try again with a valid Email address")
            self.Enter_Email()

    def Enter_pan_card(self):
        response = input("Please Enter a valid Pan Card without using spaces. For Eg:- 'ABCDE123F': ")
        if self.constraint_obj.Pan_card(response):
            return response
        else:
            print("Oops! try again with a valid Pan Card without using spaces. For Eg:- 'ABCDE123F'")
            self.Enter_pan_card()

    def Enter_password(self):
        response = input(
            "Please Enter a valid password with atleast 1 each upper and lower case alphabet and a special character as well as a numeric value : ")
        if self.constraint_obj.password(response):
            return response
        else:
            print("Oops! Please Try again")
            self.Enter_password()

    def storing_a_response(self, Question):
        response = input(Question)
        if len(response) == 0:
            print('User Response is mandatory for this field')
            self.storing_a_response()
        else:
            return response

    def Enter_Security_questions(self):
        A1 = self.storing_a_response("Q.1) What is your first crush name.")
        A2 = self.storing_a_response("Q.2) What is the last 4 digits of mobile no. you first learned.")
        A3 = self.storing_a_response("Q.3) What is Your favourite movie.")
        Answer = (A1, A2, A3)
        return Answer

    def Enter_pincode(self, per_or_temp):
        response = input(f"Enter the {per_or_temp} Address pincode")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            self.Enter_pincode()
            return
        if not self.query_obj_pincode.CheckInFunction("Pincode", response):
            print("Invalid Pincode! please try again")
            self.Enter_pincode()
        else:
            office_names = self.data_query_obj.find_values_1arg("pincode", response, "Office_Name")
