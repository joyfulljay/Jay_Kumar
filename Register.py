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
        self.pointer = 0
        self.t = 0

    def Enter_mobile_no(self):
        print("Step 1")
        response = input("Enter Valid Mobile no. : +91 ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            self.Enter_mobile_no()

        if self.constraint_obj.Mobile_no(response):

            if self.query_obj.CheckInFunction("Mobile_no", response):
                print("Aap is no. se pehele se hi registered ho login karo ho jayega....")
                user_input = input("press ENTER to go on login page to retry with another mobile no. press any: ")
                if bool(user_input):
                    self.Enter_mobile_no()
                    return
                else:
                    login()
                    self.Enter_mobile_no()
                    return
            elif self.t > 3:
                print("{: ^100}".format("\U0001F60C \U0001F60C \U0001F60C "))
                print("{: ^100}".format("Finally! you did it"))
            return response
        else:
            if self.t == 0:
                print("kripya! 10 ankon ka sahi mobile no. darj kijiye.........")
            elif self.t == 1:
                print("Ye no. bhi sahi nahi hai, kripya! 10 ankon ka sahi mobile no. darj kijiye.........")
            elif self.t == 2:
                print("Kya kar rahe ho bhai, kripya! 10 ankon ka sahi mobile no. darj kijiye.........")
            elif self.t == 3:
                print("jab ho jaye tab batadena, mein thoda so leta hun")
            else:
                print("try again")
                print("{: ^100}".format(" \U0001F634 \U0001F634 \U0001F634 \U0001F62A "))
            self.t = self.t + 1
            self.Enter_mobile_no()

    def Enter_Aadhar_no(self):
        response = input("Please enter the 12 digits valid Aadhar no: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            self.Enter_Aadhar_no()
            return

        if self.constraint_obj.Aadhar_card(response):
            if self.query_obj.CheckInFunction("Aadhar_card", response):
                print("You are already registered with this Aadhar")
                user_input = input(
                    "press ENTER to go on login page or press anything to Continue with another Aadhar card")
                if bool(user_input):
                    self.Enter_Aadhar_no()
                    return
                else:
                    login()
                    self.Enter_Aadhar_no()
                    return
            else:
                return response

        if self.query_obj.CheckInFunction("Aadhar_card", response):
            print("You are already registered with this Aadhar")
            user_input = input("press ENTER to go on login page or press anything to Continue with another Aadhar card")
            if bool(user_input):
                self.Enter_Aadhar_no()
                return
            else:
                login()
                return
        else:
            print(
                "Oops! please Try Again, Your Aadhar No. should be of 12 digits and should not have spaces in between")
            user_input = input("press ENTER to try again with Aadhar details")
            if bool(user_input):
                self.Enter_Aadhar_no()
                return
            else:
                self.Enter_Aadhar_no()
                return

    def Enter_Your_first_name(self):
        response = input("Please Enter your First Name without spaces: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            self.Enter_Your_first_name()
            return

        if self.constraint_obj.name_check(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            return response
        else:
            print("Try Again")
            self.Enter_Your_first_name()

    def Enter_Your_Last_name(self):
        response = input("Please Enter your Last Name without spaces: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            self.Enter_Your_Last_name()
            return

        if self.constraint_obj.name_check(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            return response
        else:
            print("Try Again")
            self.Enter_Your_Last_name()

    def Enter_D_O_B(self):
        response = input("Please Enter Date Of Birth in format YYYYMMDD: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.Enter_D_O_B()
            return out
        if self.constraint_obj.D_O_B(response):
            date_formatted = "'" + response[:4:] + "-" + response[4:6:] + "-" + response[6::] + "'"
            print(response) # check
            print(date_formatted) # check
            return date_formatted
        else:
            # print(
            #     "Oops! please Try Again, Your input format should be 8 digits in format YYYYMMD")
            # user_input = input("press ENTER to try agin with D-O-B")
            # if bool(user_input):
            #     self.Enter_D_O_B()
            # else:
            #     self.Enter_D_O_B()
            print("Try Again")
            out = self.Enter_D_O_B()
            return out

    def Enter_Email(self):
        response = input("Please Enter a valid Email address: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.Enter_Email()
            return out
        if self.constraint_obj.email_id(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            return response
        else:
            print("Oops! try again with a valid Email address")
            out = self.Enter_Email()
            return out

    def Enter_pan_card(self):
        response = input("Please Enter a valid Pan Card without using spaces. For Eg:- 'ABCDE123F': ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.Enter_pan_card()
            return out
        if self.constraint_obj.Pan_card(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            return response
        else:
            print("Oops! try again with a valid Pan Card without using spaces. For Eg:- 'ABCDE123F'")
            out = self.Enter_pan_card()
            return out

    def Enter_password(self):
        response = input(
            "Please Enter a valid password with atleast 1 each upper and lower case alphabet and a special character as well as a numeric value : ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.Enter_password()
            return out
        if self.constraint_obj.password(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            return response
        else:
            print("Oops! Please Try again")
            out = self.Enter_password()
            return out

    def storing_a_response(self, Question):
        response = input(Question)
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.storing_a_response(Question)
            return out
        else:
            return response

    def Enter_Security_questions(self):
        A1 = self.storing_a_response("Q.1) What is your first crush name: ")
        A2 = self.storing_a_response("Q.2) What is the last 4 digits of mobile no. you first learned: ")
        A3 = self.storing_a_response("Q.3) What is Your favourite movie: ")
        Answer = (A1, A2, A3)
        return Answer

    def Enter_pincode(self, per_or_temp):
        response = input(f"Enter the {per_or_temp} Address pincode: ")
        if self.constraint_obj.integer(response) and self.constraint_obj.spaces(response):
            if len(response) == 0:
                print('User Response is mandatory for this field')
                out = self.Enter_pincode(per_or_temp)
                return out
            if not self.query_obj_pincode.CheckInFunction("Pincode", response):
                print("Invalid Pincode! please try again")
                out = self.Enter_pincode(per_or_temp)
                return out
            else:
                office_names = self.data_query_obj.find_values_1arg("pincode", response, "Office_Name")
                index = [i + 1 for i in range(len(office_names))]
                header_list = ["Options", "Near By Office Names"]
                self.schema_obj.table_with_lists(header_list, index, office_names)
                print("")
                ind = int(input("Please select near by location: "))
                return response, office_names[ind - 1]
        else:
            print("Try Again")
            out = self.Enter_pincode(per_or_temp)
            return out

    def register_user(self):
        print("{:-^100}".format("Welcome to our Leap bank, Press enter to Continue with Registeration"))
        print("\n")
        i = input()
        if self.pointer == 0:
            self.Mobile_no = self.Enter_mobile_no()  # done
        elif self.pointer == 1:
            self.Aadhar_no = self.Enter_Aadhar_no()
        elif self.pointer == 2:
            self.First_name = self.Enter_Your_first_name()
        elif self.pointer == 3:
            self.Last_name = self.Enter_Your_Last_name()
        elif self.pointer == 4:
            self.D_O_B = self.Enter_D_O_B()
        elif self.pointer == 5:
            self.Email = self.Enter_Email()
        elif self.pointer == 6:
            self.Pan_card = self.Enter_pan_card()
        elif self.pointer == 7:
            self.password = self.Enter_password()
        elif self.pointer == 8:
            self.security_answers = self.Enter_Security_questions()
        elif self.pointer == 9:
            self.per_pincode, self.per_office_name = self.Enter_pincode("Permanent")
        elif self.pointer == 10:
            self.temp_pincode, self.temp_office_name = self.Enter_pincode("Temporary")
        elif self.pointer == 11:
            self.permanent_address = self.data_query_obj.find_values_2arg("pincode", self.per_pincode, "Office_name", self.per_office_name, "*")
        elif self.pointer == 12:
            self.Temporary_address = self.data_query_obj.find_values_2arg("pincode", self.temp_pincode, "Office_name",
                                                                     self.temp_office_name, "*")
        elif self.pointer == 13:
            return
        else:
            print("Error in register user")












        Temporary_address = self.data_query_obj.find_values_2arg("pincode", temp_pincode, "Office_name", temp_office_name, "*")

        print(
            f"insert into Registeration (First_name, Last_name, D_O_B, Permanent_address_pincode, Current_address_pincode, Aadhar_card, Mobile_no, Email , Pan_card, Account_status) values ({First_name},{Last_name},{D_O_B},{per_pincode},{temp_pincode},{Aadhar_no},{Mobile_no},{Email},{Pan_card},'Active')")
        # self.run_query_obj.run_query(f"insert into Registeration (First_name, Last_name, D_O_B, Permanent_address_pincode, Current_address_pincode, Aadhar_card, Mobile_no, Email , Pan_card, Account_status) values ({First_name},{Last_name},{D_O_B},{per_pincode},{temp_pincode},{Aadhar_no},{Mobile_no},{Email},{Pan_card},'Active')")
        # f"create table personal_details_{Mobile_no} (Firstname varchar(100), Last_name varchar(100) D_O_B date, Mobile_no bigint, Email varchar(100), Office_name varchar(50), District varchar(50), State varchar(50))"
        # f"create table benifeciary_{Mobile_no} (Benificiary_name varchar(100), Benificiary_Account_no varchar(100)"
        # f"create table account_details_{Mobile_no} (Account_no bigint, Name varchar(50), account_balance bigint)"
        # f"insert into personal_details_{Mobile_no} (Firstname, D_O_B , Mobile_no, Email, Office_name, District, State) values ({})"


obj = Registeration()

print(obj.Enter_D_O_B())
