from Data_Queries import Data_queries
from Output_Schema import *
from constraints import *
from mysqlconnector import mySQLcon
import time
import random


class login:
    # print("Bahut Jald hi Login sevayein chalu ho jayengi meanwhile register to kar hi dijiye")
    # input("Waps jane ke liye enter dabao: ")
    # return

    def __init__(self, user_name):
        self.username = user_name
        self.query_pd = Data_queries(f"personal_details_{user_name}", "BANKING")
        self.query_ad = Data_queries(f"account_details_{user_name}", "BANKING")
        self.query_bd = Data_queries(f"Benifeciary_{user_name}", "BANKING")
        self.query_cd = Data_queries(f"CARD_DETAILS_{self.Mobile_no}", "BANKING")
        self.query_reg = Data_queries("Registeration", " BANKING")
        self.sqlCon = mySQLcon()
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

    def show_card_details(self):
        card_details = self.query_bd.find_values_1arg('1', '1', "*")
        extract_details = []
        for j in card_details:
            extract_row = []
            for i in range(len(j) - 1):
                extract_row.append(j[i])
            extract_details.append(extract_row)
        template = ["Card Number", "Type of Card", "Status of card", "CVV", "Card Balance"]
        self.view_schema.table_with_row_wise_input(template, extract_details)

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

# obj = login('6264672891')
# obj.show_personal_details()
# print("")
# obj.show_account_details()
# print("")
# obj.show_list_of_beneficiary()
