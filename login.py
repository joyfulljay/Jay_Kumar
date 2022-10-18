from Data_Queries import Data_queries
from Output_Schema import *
from constraints import *
from mysqlconnector import mySQLcon
from Additional_Query_functions import helper_query
from Register import *
import time
import random


class login:
    # print("Bahut Jald hi Login sevayein chalu ho jayengi meanwhile register to kar hi dijiye")
    # input("Waps jane ke liye enter dabao: ")
    # return

    def __init__(self, user_name):
        self.update_reg = Registeration()
        self.username = user_name
        self.checkin = helper_query("BANKING", "Registeration")
        self.query_pd = Data_queries(f"personal_details_{user_name}", "BANKING")
        self.query_ad = Data_queries(f"account_details_{user_name}", "BANKING")
        self.query_bd = Data_queries(f"Benifeciary_{user_name}", "BANKING")
        self.query_cd = Data_queries(f"CARD_DETAILS_{user_name}", "BANKING")
        self.query_reg = Data_queries("Registeration", " BANKING")
        self.sqlCon = mySQLcon("BANKING")
        self.view_schema = Output_schema()
        self.constraint_obj = constraints()

    def show_personal_details(self):
        personal_details = self.query_pd.find_values_1arg("Mobile_no", self.username, "*")
        template = ["1.)Name", "2.)Date of Birth", "3.)Mobile number", "4.)Email", "5.)Nearest Office location",
                    "6.)District", "7.)State"]
        self.view_schema.table_with_row_wise_input(template, personal_details)
        temp_input = input("Press Enter To Go back to Home")

    def show_account_details(self):
        account_no = self.query_reg.find_values_1arg("Mobile_no", self.username, "Account_no")
        account_details = self.query_ad.find_values_1arg("Account_no", account_no[0], "*")
        template = ["Account number", "Account holder name", "Account balance"]
        self.view_schema.table_with_row_wise_input(template, account_details)
        temp_input = input("Press Enter To Go back to Home")

    def show_list_of_beneficiary(self):
        ben_details = self.query_bd.find_values_1arg('1', '1', "*")
        template = ["Benificiary Name", "Benificiary Account No"]
        self.view_schema.table_with_row_wise_input(template, ben_details)
        temp_input = input("Press Enter To Go back to Home")

    def show_card_details(self):
        card_details = self.query_cd.find_values_1arg('1', '1', "*")
        extract_details = []
        for j in card_details:
            extract_row = []
            for i in range(len(j) - 1):
                extract_row.append(j[i])
            extract_details.append(extract_row)
        template = ["Card Number", "Type of Card", "Status of card", "CVV", "Card Balance"]
        self.view_schema.table_with_row_wise_input(template, extract_details)
        temp_input = input("Press Enter To Go back to Home")

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

    def insert_card_details(self, type_):
        card_no = int(time.time())
        cvv = int(1000 * (random.random() + 0.1))
        pin = self.taking_input("Enter a valid 4 digit pin: ", 4, 9999)
        self.sqlCon.run_query(
            f"INSERT INTO CARD_DETAILS_{self.username} (CARD_NO, TYPE_OF_CARD , CVV , PIN) VALUES ({card_no}, {type_} ,{cvv}, {pin})")

    def add_new_card(self):

        type_of_card = self.taking_input("1.) Debit Card \n2.) Credit Card \nPlease response with a valid argument "
                                         "according to your choice: ", 1, 2)
        if type_of_card == 1:
            type_ = "DEBIT CARD"
        elif type_of_card == 1:
            type_ = "CREDIT CARD"
        self.insert_card_details(type_of_card)

    def add_beneficiary(self):
        print("Note:- There are only internal transaction service available currently. We can add only our bank users")
        self.acc_no = self.taking_input("Enter your Account no. of recipient: ", 10, 9999999999)
        if not self.checkin.CheckInFunction("Account_no", self.acc_no):
            print("This Account is not belong to our bank, Try with appropriate one ")
            self.add_beneficiary()
        else:
            name = self.query_reg.find_values_1arg("Account_no", self.acc_no, "First_name")
            print("Beneficiary Added!")
            self.view_schema.table_with_row_wise_input(["Name", "Account Number"], [[name], [self.acc_no]])
            inp = input("Press Enter to Continue or other key to edit")
            if len(inp)==0:
                self.sqlCon.run_query(f"""insert into Benificiary_{self.username} values ("{name}",{self.acc_no}) """)
                print("Benificiary added to your profile!")
                i = input("Press Enter to go back to homepage")
            else:
                self.add_beneficiary()

    def edit_personal_details(self):
        print("1.) Name\n2.) Date of Birth \n3.) Permanent Address\n4.) Temporary Address \n5.) Email ")
        val = self.taking_input("Select field to edit: ", 1, 6)
        if val == 1:
            first_name_new = self.update_reg.First_name()
            last_name_new = self.update_reg.Last_name()
            name = first_name_new[:-1:] + " " + last_name_new[1::]
            self.query_reg.update_value("Mobile_no", self.username, "First_name", first_name_new)
            self.query_reg.update_value("Mobile_no", self.username, "Last_name", last_name_new)
            self.query_pd.update_value("Mobile_no", self.username, "Fullname", name)
        elif val ==2:
            D_O_B =








#Fullname, D_O_B, Mobile_no, Email, Office_name, District, State
#Account_no, First_name, Last_name, D_O_B, Permanent_address_pincode, Current_address_pincode, Aadhar_card, Mobile_no, Email, Pan_card, Account_created_Timestamp, Account_status

obj = login('6264242775')
obj.show_personal_details()
print("")
obj.show_account_details()
print("")
obj.show_list_of_beneficiary()
print("")
obj.show_card_details()
