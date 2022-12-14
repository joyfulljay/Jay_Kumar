from Data_Queries import Data_queries
from Output_Schema import *
from constraints import *
from mysqlconnector import mySQLcon
from Additional_Query_functions import helper_query
from Additional_functions import mandatory
import datetime as dt
from Register import *
import time
import random


class login:
    # print("Bahut Jald hi Login sevayein chalu ho jayengi meanwhile register to kar hi dijiye")
    # input("Waps jane ke liye enter dabao: ")
    # return

    def __init__(self, user_name):
        self.lo = False
        self.login_timestamp = dt.datetime.now()
        self._is_mandatory = mandatory()
        self.wrong_pin_count = 0
        self.update_reg = Registeration()
        self.username = user_name
        self.checkinBenificiary = helper_query("BANKING", f"Benifeciary_{user_name}")
        self.checkin = helper_query("BANKING", "Registeration")
        self.query_pd = Data_queries(f"personal_details_{user_name}", "BANKING")
        self.query_ad = Data_queries(f"account_details_{user_name}", "BANKING")
        self.query_bd = Data_queries(f"Benifeciary_{user_name}", "BANKING")
        self.query_cd = Data_queries(f"CARD_DETAILS_{user_name}", "BANKING")
        self.query_reg = Data_queries("Registeration", " BANKING")
        self.query_Pd = Data_queries("PincodeDB", " BANKING")
        self.sqlCon = mySQLcon("BANKING")
        self.view_schema = Output_schema()
        self.constraint_obj = constraints()

    def show_personal_details(self):
        personal_details = self.query_pd.find_values_1arg("Mobile_no", self.username, "*")
        template = ["1.)Name", "2.)Date of Birth", "3.)Mobile number", "4.)Email", "5.)Nearest Office location",
                    "6.)District", "7.)State"]
        self.view_schema.table_with_row_wise_input(template, personal_details)

    def show_account_details(self):
        account_no = self.query_reg.find_values_1arg("Mobile_no", self.username, "Account_no")
        account_details = self.query_ad.find_values_1arg("Account_no", account_no[0], "*")
        template = ["Account number", "Account holder name", "Account balance"]
        self.view_schema.table_with_row_wise_input(template, account_details)

    def show_list_of_beneficiary(self):
        ben_details = self.query_bd.find_values_1arg('1', '1', "*")
        template = ["Serial no.", "Benificiary Name", "Benificiary Account No"]
        self.view_schema.table_with_row_wise_input(template, ben_details)

    def show_card_details(self):
        card_details = self.query_cd.find_values_1arg('1', '1', "*")
        extract_details = []
        for j in card_details:
            extract_row = []
            for i in range(len(j) - 1):
                extract_row.append(j[i])
            extract_details.append(extract_row)
        template = ["Serial no.", "Card Number", "Type of Card", "Status of card", "CVV", "Card Balance"]
        self.view_schema.table_with_row_wise_input(template, extract_details)

    def taking_input(self, parameter, Range):
        out1 = input(parameter)
        if not self._is_mandatory.is_mandatory(out1, True):
            out = self.taking_input(parameter, Range)
            return out
        if not self.constraint_obj.input_constraintWoutl(out1, Range):
            out = self.taking_input(parameter, Range)
            return out
        else:
            return out1

    def taking_inputl(self, parameter, leng, Range):
        out1 = input(parameter)
        if not self._is_mandatory.is_mandatory(out1, True):
            out = self.taking_inputl(parameter, leng, Range)
            return out
        if not self.constraint_obj.input_constraint(out1, leng, Range):
            out = self.taking_inputl(parameter, leng, Range)
            return out
        else:
            return out1

    def insert_card_details(self, type_):
        card_no = int("202201" + str(int(time.time())))
        cvv = int(1000 * (random.random() + 0.1))
        pin = self.taking_inputl("Enter a valid 4 digit pin: ", 4, 9999)
        self.sqlCon.run_query(
            f"INSERT INTO CARD_DETAILS_{self.username} (CARD_NO, TYPE_OF_CARD , CVV , PIN) VALUES ({card_no}, {type_} ,{cvv}, {pin})")
        return card_no, cvv

    def add_new_card(self):
        print("Please select a card to add \n")

        type_of_card = self.taking_input("1.) Debit Card \n2.) Credit Card \nPlease response with a valid argument "
                                         "according to your choice: ", 2)
        if int(type_of_card) == 1:
            type = "DEBIT CARD"
        elif int(type_of_card) == 2:
            type = "CREDIT CARD"
        card_no, cvv = self.insert_card_details(type_of_card)
        print(f"{type} generated with with card number ({card_no}) and cvv ({cvv})")

    def change_MPIN(self):
        self.show_card_details()
        card_details = self.query_cd.find_values_1arg("1", "1", "*")
        range = len(card_details)
        S_no = self.taking_input("Enter the serial no of card you want to change MPIN : ", range)
        self.change_MPINhf(S_no)

    def change_MPINhf(self, S_no):
        if self.wrong_pin_count == 3:
            print("You exhausted your all attempt please re-login and then try")
            return
        else:
            verify = self.taking_inputl("Enter current MPIN: ", 4, 9999)
            checkmpin = helper_query("BANKING", f"CARD_DETAILS_{self.username}")
            if not checkmpin.password_check("S_No", S_no, "PIN", verify):
                self.wrong_pin_count += 1
                print(f"Incorrect pin, Only {3 - self.wrong_pin_count} trials left")
                temp = self.taking_input("1.) Back to homepage\n2.) Retry Pin\nSelect your desired field: ", 2)
                if int(temp) == 2:
                    self.change_MPINhf(S_no)
                else:
                    return
            else:
                self.wrong_pin_count = 0
                new_pin = self.taking_inputl("Enter new MPIN: ", 4, 9999)
                self.query_cd.update_value("S_no", S_no, "PIN", new_pin)
                print("Pin Changed!\n")

    def add_beneficiary(self):
        self.B = True
        account_no = self.query_reg.find_values_1arg("Mobile_no", self.username, "Account_no")
        print("Note:- There are only internal transaction service available currently. We can add only our bank users")
        self.acc_no = self.taking_input("Enter The Account no. of Recipient: ", 9999999999)
        print(self.acc_no)
        try:
            if self.checkinBenificiary.CheckInFunction("Benificiary_Account_no", self.acc_no):
                print("Benificiary Already Created with this account no")
                inp = input("Press Enter to go back to Home or other key to retry: ")
                if len(inp) == 0:
                    self.B = False
                    return
                else:
                    self.add_beneficiary()

            if account_no[0] == int(self.acc_no) and self.B:
                i = input(
                    "You can not add your own account in your own Beneficiary. Press enter to re-enter or press other key to exit")
                if len(i) == 0:
                    self.add_beneficiary()
                else:
                    print(i)
                    return

            elif not self.checkin.CheckInFunction("Account_no", self.acc_no) and self.B:
                print("This Account is not belong to our bank, Try with appropriate one ")
                self.add_beneficiary()
            elif self.B:
                name = self.query_reg.find_values_1arg("Account_no", self.acc_no, "First_name")
                self.view_schema.table_with_tupple_list(["Name", "Account Number"], [(name[0], self.acc_no)])
                inp = input("Press Enter to Continue or other key to edit: ")
                if len(inp) == 0:
                    self.sqlCon.run_query(
                        f"""insert into Benifeciary_{self.username} (Benificiary_name, Benificiary_Account_no) values ("{name[0]}",{self.acc_no}) """)
                    self.show_list_of_beneficiary()
                    print("Benificiary added to your profile!")
                else:
                    self.add_beneficiary()
        except Exception as e:
            print(e)

    def edit_personal_details(self):
        print("1.) Name\n2.) Date of Birth \n3.) Permanent Address\n4.) Temporary Address \n5.) Email ")
        val = self.taking_input("Select field to edit: ", 5)
        val = int(val)
        if val == 1:
            # print("1")
            first_name_new = self.update_reg.Enter_Your_first_name()
            first_name_new = first_name_new[1:-1:]
            # print("2")
            last_name_new = self.update_reg.Enter_Your_Last_name()
            last_name_new = last_name_new[1:-1:]
            # print("3")
            name = first_name_new + " " + last_name_new
            # print("4")
            self.query_reg.update_value("Mobile_no", self.username, "First_name", first_name_new)
            # print("5")
            self.query_reg.update_value("Mobile_no", self.username, "Last_name", last_name_new)
            # print("6")
            self.query_pd.update_value("Mobile_no", self.username, "Fullname", name)
            # print("7")
            self.show_personal_details()
            # print("8")
        elif val == 2:
            D_O_B = self.update_reg.Enter_D_O_B()
            D_O_B = D_O_B[1:-1:]
            self.query_reg.update_value("Mobile_no", self.username, "D_O_B", D_O_B)
            self.query_pd.update_value("Mobile_no", self.username, "D_O_B", D_O_B)
            self.show_personal_details()
        elif val == 3:
            per_pin_code, per_office_name = self.update_reg.Enter_pincode("permanent")
            permanent_address = self.query_Pd.find_values_2arg("pincode", per_pin_code, "Office_name", per_office_name,
                                                               "*")
            District = permanent_address[7]
            State = permanent_address[8]
            self.query_reg.update_value("Mobile_no", self.username, "Permanent_address_pincode", per_pin_code)
            self.query_pd.update_value("Mobile_no", self.username, "Office_name", per_office_name)
            self.query_pd.update_value("Mobile_no", self.username, "District", District)
            self.query_pd.update_value("Mobile_no", self.username, "State", State)
            self.show_personal_details()
        elif val == 4:
            per_pin_code, per_office_name = self.update_reg.Enter_pincode("Temporary")
            self.query_reg.update_value("Mobile_no", self.username, "Current_address_pincode", per_pin_code)
            self.show_personal_details()
        elif val == 5:
            Email = self.update_reg.Enter_Email()
            Email = Email[1:-1:]
            self.query_reg.update_value("Mobile_no", self.username, "Email", Email)
            self.query_pd.update_value("Mobile_no", self.username, "Email", Email)
            self.show_personal_details()
        print("Details_Updated")

    def transfer_funds(self):
        extract_balance = self.query_ad.find_values_1arg("1", "1", "account_balance")
        # print(extract_balance)
        senders_account_no = self.query_ad.find_values_1arg("1", "1", "Account_no")
        # print(senders_account_no)
        balance = int(extract_balance[0])
        # print(balance)
        self.show_list_of_beneficiary()
        ben_details = self.query_bd.find_values_1arg("1", "1", "*")
        # print(ben_details)
        range = len(ben_details)
        to_send = self.taking_input("Please Select Beneficiary to fund transfer: ", range)
        recievers_acc_no = ben_details[int(to_send) - 1][2]
        # print(recievers_acc_no, type(recievers_acc_no))
        ru = self.query_reg.find_values_1arg("Account_no", recievers_acc_no, "Mobile_no")
        # print(ru)
        self.show_account_details()
        print("")
        self.transfer_ammount = self.taking_input("Enter Amount to transfer: ", balance)
        # if self.constraint_obj.integer(self.transfer_ammount):
        #     if int(self.transfer_ammount) > balance:
        #         print("Insufficient Funds")
        #         return
        #     else:
        self.sqlCon.run_query(
            f"""insert into global_transactions (Senders_Account_no, Recievers_account_no, Ammount) values ({senders_account_no[0]}, {recievers_acc_no}, {self.transfer_ammount} )""")
        self.query_ad.update_value("Account_no", senders_account_no[0], "account_balance",
                                   (balance - int(self.transfer_ammount)))
        query_ad_u = Data_queries(f"account_details_{ru[0]}", "BANKING")
        rb = query_ad_u.find_values_1arg("1", "1", "account_balance")
        # print(rb)
        query_ad_u.update_value("Account_no", recievers_acc_no, "account_balance", (rb[0] + int(self.transfer_ammount)))
        print("Transaction Successful!")
        print("------------------------------------------------------------")
        temp = input("Press enter to show account info: ")
        print("------------------------------------------------------------")
        self.show_account_details()
        print("------------------------------------------------------------")

        # else:
        #     print("Invalid Argument try again")
        #     self.transfer_ammount()
        #     return

    def logout(self):
        self.rating = self.taking_input("Hey! How did we serve. Please Rate us on 1 to 5 : ", 5)

        comment = input("Additional Comments! or press enter to skip: ")
        if len(comment) == 0:
            comment = "No Valuable Comments"
        else:
            comment1 = comment.replace(" ", "")
            if len(comment1) == 0:
                comment = "No Valuable Comments"

        self.feedback(int(self.rating), comment, self.login_timestamp)
        print("{:-^100}".format("logout"))

    def feedback(self, rating, comment, login_timestamp):
        logout_time = dt.datetime.now()
        # print(logout_time)
        # print(login_timestamp)
        # print(rating)
        # print(comment)
        self.sqlCon.run_query(
            f"""insert into feedback (user_id, Login_timestamp, Logout_timestamp, Rating, Additional_Comments) values({self.username},'{login_timestamp}', '{logout_time}', {rating},"{comment}")""")
        if rating == 5:
            print("Thank you for your valuable feedback")
        elif rating == 4:
            print("Thank you for your valuable feedback. We would serve you better next time. ")
        elif rating == 3:
            print("Thank you for your valuable feedback. We would serve you better next time.")
        elif rating == 2:
            print(
                "Thank you for your valuable feedback. Our service team is constantly working for betterment of user "
                "experience.")
        elif rating == 1:
            print("Thank you for your valuable feedback. We will look into the issue and serve you better next time.")
        else:
            print("Thank you for your valuable feedback. We will look into the issue and serve you better next time.")

    def run_login(self):
        print("1.) Personal Details")
        print("2.) Account Details")
        print("3.) Edit Personal Details")
        print("4.) Beneficiary Details")
        print("5.) Add Beneficiary")
        print("6.) CARD Details")
        print("7.) add a new card")
        print("8.) Change MPIN")
        print("9.) Money Transfer")
        print("10.) Logout")

        user_input = self.taking_input("Please Select the appropriate field: ", 10)
        user_input = int(user_input)

        if user_input == 1:
            self.show_personal_details()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 2:
            self.show_account_details()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 3:
            self.edit_personal_details()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 4:
            self.show_list_of_beneficiary()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 5:
            self.add_beneficiary()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 6:
            self.show_card_details()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 7:
            self.add_new_card()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 8:
            self.change_MPIN()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 9:
            self.transfer_funds()
            temp = input("Press Enter to go back to Homepage ")
        if user_input == 10:
            self.lo = True
            self.logout()
        if not self.lo:
            self.run_login()


# transaction_id, Senders_Account_no, Receivers_account_no, transaction_time_stamp, Transaction_status,
# Amount Fullname, D_O_B, Mobile_no, Email, Office_name, District, State Account_no, First_name, Last_name, D_O_B,
# Permanent_address_pincode, Current_address_pincode, Aadhar_card, Mobile_no, Email, Pan_card,
# Account_created_Timestamp, Account_status


#   OWN BANK ACCOUNT BUG TO BE FIXED. FIXED
#   STEP BUG IS TO BE FIXED IN REGISTRATION. FIXED
#   SAME BENEFICIARY BUG TO BE FIXED. FIXED


# obj = login('6264242775')
# # # # obj.show_personal_details()
# # # # print("")
# # # # obj.show_account_details()
# # # # print("")
# # # # obj.show_list_of_beneficiary()
# # # # print("")
# # # # obj.show_card_details()
# obj.change_MPIN()
# # 6526248324
