from constraints import *
from Additional_Query_functions import *
from login import *
from Data_Queries import *
from Output_Schema import *
from mysqlconnector import *


class Registeration:
    def __init__(self):
        self.run_query_obj = mySQLcon("BANKING")
        self.constraint_obj = constraints()
        self.query_obj = helper_query("BANKING", "Registeration")
        self.query_obj_pincode = helper_query("BANKING", "PincodeDB")
        self.data_query_obj = Data_queries("PincodeDB", "BANKING")
        self.schema_obj = Output_schema()

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
            user_input = input("press ENTER to go on login page or press anything to Continue with another Aadhar card")
            if bool(user_input):
                self.Enter_Aadhar_no()
                return
            else:
                login()
                return

        if self.constraint_obj.Aadhar_card(response):
            return response
        else:
            print(
                "Oops! please Try Again, Your Aadhar No. should be of 12 digits and should not have spaces in between")
            user_input = input("press ENTER to try again with Aadhar details")
            if bool(user_input):
                self.Enter_Aadhar_no()
                return
            else:
                self.Enter_Aadhar_no()

    def Enter_Your_first_name(self):
        response = input("Please Enter your First Name without spaces")
        if self.constraint_obj.name_check(response):
            s = """(")"""
            response (s[1] + response + s[1])
            return response
        else:
            print("Try Again")
            self.Enter_Your_first_name()

    def Enter_Your_Last_name(self):
        response = input("Please Enter your Last Name without spaces")
        if self.constraint_obj.name_check(response):
            s = """(")"""
            response(s[1] + response + s[1])
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
            user_input = input("press ENTER to try agin with D-O-B or enter anything to go on homepage")
            if bool(user_input):
                Homepage()
                return
            else:
                self.Enter_D_O_B()

    def Enter_Email(self):
        response = input("Please Enter a valid Email address: ")
        if self.constraint_obj.email_id(response):
            s = """(")"""
            response(s[1] + response + s[1])
            return response
        else:
            print("Oops! try again with a valid Email address")
            self.Enter_Email()

    def Enter_pan_card(self):
        response = input("Please Enter a valid Pan Card without using spaces. For Eg:- 'ABCDE123F': ")
        if self.constraint_obj.Pan_card(response):
            s = """(")"""
            response(s[1] + response + s[1])
            return response
        else:
            print("Oops! try again with a valid Pan Card without using spaces. For Eg:- 'ABCDE123F'")
            self.Enter_pan_card()

    def Enter_password(self):
        response = input(
            "Please Enter a valid password with atleast 1 each upper and lower case alphabet and a special character as well as a numeric value : ")
        if self.constraint_obj.password(response):
            s = """(")"""
            response(s[1] + response + s[1])
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
            index = [i + 1 for i in range(len(office_names))]
            header_list = ["Options", "Near By Office Names"]
            self.schema_obj.table_with_lists(header_list, index)
            print("")
            ind = input("Please select near by location: ")
            return response, office_names[ind]

    def register_user(self):
        Mobile_no = self.Enter_mobile_no()
        Aadhar_no = self.Enter_Aadhar_no()
        First_name = self.Enter_Your_first_name()
        Last_name = self.Enter_Your_Last_name()
        D_O_B = self.Enter_D_O_B()
        Email = self.Enter_Email()
        Pan_card = self.Enter_pan_card()
        password = self.Enter_password()
        security_answers = self.Enter_Security_questions()
        per_pincode, per_office_name = self.Enter_pincode("Permanent")
        temp_pincode, temp_office_name = self.Enter_pincode("Temporary")
        permanent_address = self.data_query_obj.find_values_2arg("pincode", per_pincode, "Office_name", per_office_name, "*")
        Temporary_address = self.data_query_obj.find_values_2arg("pincode", temp_pincode, "Office_name", temp_office_name, "*")

        self.run_query_obj.run_query(f"insert into Registeration (First_name, Last_name, D_O_B, Permanent_address_pincode, Current_address_pincode, Aadhar_card, Mobile_no, Email , Pan_card, Account_status) values ({First_name},{Last_name},{D_O_B},{per_pincode},{temp_pincode},{Aadhar_no},{Mobile_no},{Email},{Pan_card},'Active')")
        # f"create table personal_details_{Mobile_no} (Firstname varchar(100), Last_name varchar(100) D_O_B date, Mobile_no bigint, Email varchar(100), Office_name varchar(50), District varchar(50), State varchar(50))"
        # f"create table benifeciary_{Mobile_no} (Benificiary_name varchar(100), Benificiary_Account_no varchar(100)"
        # f"create table account_details_{Mobile_no} (Account_no bigint, Name varchar(50), account_balance bigint)"
        # f"insert into personal_details_{Mobile_no} (Firstname, D_O_B , Mobile_no, Email, Office_name, District, State) values ({})"