import time

from constraints import *
from Additional_Query_functions import *
from Data_Queries import *
from Output_Schema import *
from mysqlconnector import *
from Additional_functions import mandatory
import datetime
import random


class Registeration:
    def __init__(self):
        self.run_query_obj = mySQLcon("BANKING")
        self.constraint_obj = constraints()
        self.query_obj = helper_query("BANKING", "Registeration")
        self.Data_query_obj = Data_queries("Registeration", "BANKING")
        self.query_obj_pincode = helper_query("BANKING", "PincodeDB")
        self.data_query_obj = Data_queries("PincodeDB", "BANKING")
        self.schema_obj = Output_schema()
        self.pointer = 0
        self.b = True
        self.mandatory_obj = mandatory()
        self.t = 0

    def Enter_mobile_no(self):
        print("Step 1")
        response = input("Enter Valid Mobile no. : +91 ")
        if not self.mandatory_obj.is_mandatory(response, True):
            out = self.Enter_mobile_no()
            return out
        elif self.constraint_obj.Mobile_no(response):

            if self.query_obj.CheckInFunction("Mobile_no", response):
                print("Already Registered with this Mobile no. Try different or login with the same")
                user_input = input("Press ENTER to retry")
                out = self.Enter_mobile_no()
                return out
            elif self.t > 3:
                print("{: ^100}".format("\U0001F60C \U0001F60C \U0001F60C "))
                print("{: ^100}".format("Finally! you did it"))
            self.pointer = self.pointer + 1
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
        print("Step 2")
        response = input("Please enter the 12 digits valid Aadhar no: ")
        if not self.mandatory_obj.is_mandatory(response, True):
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
                self.pointer = self.pointer + 1
                return response

        else:
            print(
                "Oops! please Try Again, Your Aadhar No. should be of 12 digits and should not have spaces in between")
            user_input = input("press ENTER to try again with Aadhar details")
            if bool(user_input):
                out = self.Enter_Aadhar_no()
                return out
            else:
                out = self.Enter_Aadhar_no()
                return out

    def Enter_Your_first_name(self):
        print("Step 3")
        response = input("Please Enter your First Name without spaces: ")
        if not self.mandatory_obj.is_mandatory(response, True):
            out = self.Enter_Your_first_name()
            return out

        if self.constraint_obj.name_check(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            self.pointer = self.pointer + 1
            return response
        else:
            print("Try Again")
            out = self.Enter_Your_first_name()
            return out

    def Enter_Your_Last_name(self):
        print("Step 4")
        response = input("Please Enter your Last Name without spaces: ")
        if not self.mandatory_obj.is_mandatory(response, True):
            out = self.Enter_Your_Last_name()
            return out

        if self.constraint_obj.name_check(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            self.pointer = self.pointer + 1
            return response
        else:
            print("Try Again")
            out = self.Enter_Your_Last_name()
            return out

    def taking_input(self, parameter, leng, Range):
        out1 = input(parameter)
        if not self.mandatory_obj.is_mandatory(out1, True):
            out = self.taking_input(parameter, leng, Range)
            return out
        if not self.constraint_obj.input_constraint(out1, leng, Range):
            out = self.taking_input(parameter, leng, Range)
            return out
        else:
            return out1

    def Enter_D_O_B(self):
        print("Step 5")
        day = self.taking_input("Enter the day of birth 'dd' : ", 2, 31)
        month = self.taking_input("Enter the month of birth 'mm' : ", 2, 12)
        year = self.taking_input("Enter the year of birth 'yyyy' : ", 4, 2022)
        response = year + month + day
        if self.constraint_obj.is_valid_date(int(year), int(month), int(day)) and self.constraint_obj.Age_constraint(
                datetime.date(int(year), int(month), int(day))):
            date_formatted = "'" + response[:4:] + "-" + response[4:6:] + "-" + response[6::] + "'"
            self.pointer = self.pointer + 1
            return date_formatted
        else:
            # print(
            #     "Oops! please Try Again, Your input format should be 8 digits in format YYYYMMDD")
            # user_input = input("press ENTER to try again with D-O-B")
            # if bool(user_input):
            #     self.Enter_D_O_B()
            # else:
            #     self.Enter_D_O_B()
            print("Try Again")
            out = self.Enter_D_O_B()
            return out

    def Enter_Email(self):
        print("Step 6")
        response = input("Please Enter a valid Email address: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.Enter_Email()
            return out
        if self.constraint_obj.email_id(response):
            s = """(")"""
            response = (s[1] + response + s[1])
            self.pointer = self.pointer + 1
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
            self.pointer = self.pointer + 1
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
            self.pointer = self.pointer + 1
            return response
        else:
            print("Oops! Please Try again")
            out = self.Enter_password()
            return out

    def storing_a_response(self, Question, bo_ol):
        if bo_ol:
            response = input(Question)
        else:
            response = self.taking_input(Question, 4, 10000)
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.storing_a_response(Question)
            return out
        else:
            return response

    def Enter_Security_questions(self):
        print("Security Questions for Password recovery")
        A1 = self.storing_a_response("Q.1) What is your first crush name: ", True)
        A2 = self.storing_a_response("Q.2) What is the last 4 digits of mobile no. you first learned: ", False)
        A3 = self.storing_a_response("Q.3) What was your current/last crush first name: ", True)
        Answer = (A1, A2, A3)
        self.pointer = self.pointer + 1
        return Answer

    def Enter_pincode(self, per_or_temp):
        response = input(f"Enter the {per_or_temp} Address pincode: ")
        if len(response) == 0:
            print('User Response is mandatory for this field')
            out = self.Enter_pincode(per_or_temp)
            return out
        if self.constraint_obj.integer(response) and self.constraint_obj.spaces(response):
            if not self.query_obj_pincode.CheckInFunction("Pincode", response):
                print("Invalid Pincode! please try again")
                out = self.Enter_pincode(per_or_temp)
                return out
            else:

                office_names = self.data_query_obj.find_values_1arg("pincode", response, "Office_Name")

                index = [i + 1 for i in range(len(office_names))]

                header_list = ["Options", "Near By Office Names"]

                self.schema_obj.table_with_column_wise_input(header_list, index, office_names)

                ind = self.taking_input("Select nearby office : ", 1, len(office_names))

                self.pointer = self.pointer + 1
                return response, office_names[int(ind) - 1]
        else:
            print("Try Again")
            out = self.Enter_pincode(per_or_temp)
            return out

    def insert_card_details(self, type_, username):
        card_no = int(time.time())
        cvv = int(1000 * (random.random() + 0.1))
        pin = self.taking_input("Enter a valid 4 digit pin: ", 4, 9999)
        self.run_query_obj.run_query(
            f"""INSERT INTO CARD_DETAILS_{username} (CARD_NO, TYPE_OF_CARD , CVV , PIN) VALUES ({card_no}, "{type_}" ,{cvv}, {pin})""")

    def update_before_finalise(self):
        if self.pointer == 7:
            self.Mobile_no = self.Enter_mobile_no()  # done
        elif self.pointer == 6:
            self.Aadhar_no = self.Enter_Aadhar_no()
        elif self.pointer == 1:
            self.First_name = self.Enter_Your_first_name()
        elif self.pointer == 2:
            self.Last_name = self.Enter_Your_Last_name()
        elif self.pointer == 3:
            self.D_O_B = self.Enter_D_O_B()
        elif self.pointer == 8:
            self.Email = self.Enter_Email()
        elif self.pointer == 9:
            self.Pan_card = self.Enter_pan_card()
        elif self.pointer == 4:
            self.per_pincode, self.per_office_name = self.Enter_pincode("Permanent")
            self.permanent_address = self.data_query_obj.find_values_2arg("pincode", self.per_pincode, "Office_name",
                                                                          self.per_office_name, "*")
        elif self.pointer == 5:
            self.temp_pincode, self.temp_office_name = self.Enter_pincode("Temporary")
            self.Temporary_address = self.data_query_obj.find_values_2arg("pincode", self.temp_pincode, "Office_name",
                                                                          self.temp_office_name, "*")
        self.values = [self.First_name[1:-1:], self.Last_name[1:-1:], self.D_O_B[1:-1:], (
            f"{self.permanent_address[3]}, {self.permanent_address[7]}, {self.permanent_address[8]}, ({self.per_pincode})"),
                       (
                           f"{self.Temporary_address[3]}, {self.Temporary_address[7]}, {self.Temporary_address[8]}, ({self.temp_pincode})"),
                       self.Aadhar_no, self.Mobile_no, self.Email[1:-1:], self.Pan_card[1:-1:]]

    def register_user(self):
        if (self.pointer > 0) and (self.pointer < 11):
            check = input(
                f"1.) Go back on previous step.\n2.) Go back to restart registeration. \n3.) Go back to Home page "
                f"\nPress enter to continue to next step (step {self.pointer + 1})         ")
            try:
                if int(check) == 1:
                    self.pointer = self.pointer - 1
                elif int(check) == 3:
                    self.pointer = 13
                    self.b = False
                elif int(check) == 2:
                    self.register_user()
                    return
            except:
                print("Go on....")

        if self.pointer == 0:
            self.Mobile_no = self.Enter_mobile_no()  # done
            out = self.register_user()
            return out
        elif self.pointer == 1:
            self.Aadhar_no = self.Enter_Aadhar_no()
            out = self.register_user()
            return out
        elif self.pointer == 2:
            self.First_name = self.Enter_Your_first_name()
            out = self.register_user()
            return out
        elif self.pointer == 3:
            self.Last_name = self.Enter_Your_Last_name()
            out = self.register_user()
            return out
        elif self.pointer == 4:
            self.D_O_B = self.Enter_D_O_B()
            out = self.register_user()
            return out
        elif self.pointer == 5:
            self.Email = self.Enter_Email()
            out = self.register_user()
            return out
        elif self.pointer == 6:
            self.Pan_card = self.Enter_pan_card()
            out = self.register_user()
            return out
        elif self.pointer == 7:
            self.password = self.Enter_password()
            out = self.register_user()
            return out
        elif self.pointer == 8:
            self.security_answers = self.Enter_Security_questions()
            out = self.register_user()
            return out
        elif self.pointer == 9:
            self.per_pincode, self.per_office_name = self.Enter_pincode("Permanent")
            out = self.register_user()
            return out
        elif self.pointer == 10:
            self.temp_pincode, self.temp_office_name = self.Enter_pincode("Temporary")
            out = self.register_user()
            return out
        elif self.pointer == 11:
            self.permanent_address = self.data_query_obj.find_values_2arg("pincode", self.per_pincode, "Office_name",
                                                                          self.per_office_name, "*")
            self.pointer += 1
            out = self.register_user()
            return out
        elif self.pointer == 12:
            self.Temporary_address = self.data_query_obj.find_values_2arg("pincode", self.temp_pincode, "Office_name",
                                                                          self.temp_office_name, "*")
            self.pointer += 1
            out = self.register_user()
            return out
        elif self.pointer == 13:
            if self.b:
                self.tempelate = ["1.) First name", "2.) Last Name", "3.) Date of Birth", "4.) Permanent Address",
                                  "5.) Temporary Address", "6.) Aadhar No.", "7.) Mobile No.", "8.) Email",
                                  "9.) Pan Card"]
                self.values = [self.First_name[1:-1:], self.Last_name[1:-1:], self.D_O_B[1:-1:], (
                    f"{self.permanent_address[3]}, {self.permanent_address[7]}, {self.permanent_address[8]}, ({self.per_pincode})"),
                               (
                                   f"{self.Temporary_address[3]}, {self.Temporary_address[7]}, {self.Temporary_address[8]}, ({self.temp_pincode})"),
                               self.Aadhar_no, self.Mobile_no, self.Email[1:-1:], self.Pan_card[1:-1:]]
                return self.b

        else:
            print(f"Register_user function completed without any action so pointer value is {self.pointer}")

    def last_check(self):
        print("Please Verify details")
        self.schema_obj.table_with_column_wise_input(self.tempelate, [self.values[0]], [self.values[1]], [self.values[2]],
                                         [self.values[3]], [self.values[4]], [self.values[5]], [self.values[6]],
                                         [self.values[7]], [self.values[8]])
        arg = input("Press enter to continue with these details or press field no. to update: ")
        if len(arg) == 0:
            return
        elif self.constraint_obj.input_constraint(arg, 1, 9):
            self.pointer = int(arg)
            self.update_before_finalise()
            self.last_check()
            return
        else:
            print("Invalid field, Try again!")
            self.last_check()

    def database_creation(self):
        try:
            self.run_query_obj.run_query(
                f"insert into Registeration (First_name, Last_name, D_O_B, Permanent_address_pincode, Current_address_pincode, Aadhar_card, Mobile_no, Email , Pan_card, Account_status) values ({self.First_name},{self.Last_name},{self.D_O_B},{self.per_pincode},{self.temp_pincode},{self.Aadhar_no},{self.Mobile_no},{self.Email},{self.Pan_card},'Active')")
        except:
            print("two")
        try:
            acc_no = self.Data_query_obj.find_values_1arg("Mobile_no", self.Mobile_no, "Account_no")
        except:
            print("two")
        try:
            name = self.First_name[:-1:] + " " + self.Last_name[1::]
        except:
            print("four")
        try:
            self.run_query_obj.run_query(
                f"create table personal_details_{self.Mobile_no} (Fullname varchar(100), D_O_B date, Mobile_no bigint, Email varchar(100), Office_name varchar(50), District varchar(50), State varchar(50))")
        except:
            print("five")
        try:
            self.run_query_obj.run_query(
                f"create table Benifeciary_{self.Mobile_no} (S_no INT PRIMARY KEY AUTO_INCREMENT, Benificiary_name varchar(100), Benificiary_Account_no BIGINT)")
        except:
            print("six")

        try:
            self.run_query_obj.run_query(
                f"create table account_details_{self.Mobile_no} (Account_no bigint, holders_Name varchar(50), account_balance int)")
        except:
            print("seven")

        try:
            self.run_query_obj.run_query(
                f"""insert into personal_details_{self.Mobile_no} values ({name}, {self.D_O_B} , {self.Mobile_no}, {self.Email}, "{self.permanent_address[3]}", "{self.permanent_address[7]}", "{self.permanent_address[8]}")""")
        except:
            print(
                f"""insert into personal_details_{self.Mobile_no} values ({name}, {self.D_O_B} , {self.Mobile_no}, {self.Email}, "{self.permanent_address[3]}", "{self.permanent_address[7]}", "{self.permanent_address[8]}")""")
        try:
            acc_balance = int(1000 * random.random())
        except:
            print("nine")
        try:
            self.run_query_obj.run_query(
                f"""insert into account_details_{self.Mobile_no} values ({acc_no[0]}, {name}, {acc_balance})""")
        except Exception as inst:
            print(inst)

        try:
            self.run_query_obj.run_query(
                f"""insert into Login_Details values ({self.Mobile_no}, {self.password}, "{self.security_answers[0]}", "{self.security_answers[1]}", "{self.security_answers[2]}")""")
        except:
            print(
                f"""insert into Login_Details values ({self.Mobile_no}, {self.password}, "{self.security_answers[0]}", "{self.security_answers[1]}", "{self.security_answers[2]}")""")

        self.run_query_obj.run_query(
            f"CREATE TABLE CARD_DETAILS_{self.Mobile_no} (S_No INT AUTO_INCREMENT, CARD_NO BIGINT PRIMARY KEY , TYPE_OF_CARD ENUM('DEBIT CARD', 'CREDIT CARD'), STATUS_OF_CARD ENUM('ACTIVATED','DEACTIVATED') DEFAULT 'ACTIVATED', CVV INT NOT NULL,CARD_BALANCE BIGINT NOT NULL DEFAULT 0 ,PIN INT NOT NULL)")

        a = input("Press Enter to registering a Credit Card")
        self.insert_card_details("CREDIT CARD", self.Mobile_no)
        a = input("Press Enter to registering a Debit Card")
        self.insert_card_details("DEBIT CARD", self.Mobile_no)

        print(f"Hey! you got a joining reward of Rs {acc_balance}/-")
        a = input("Press Enter to go to the Homepage")

# obj = Registeration()
# print(obj.Enter_D_O_B())
