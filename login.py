from Data_Queries import Data_queries
from Output_Schema import *


class login:
    # print("Bahut Jald hi Login sevayein chalu ho jayengi meanwhile register to kar hi dijiye")
    # input("Waps jane ke liye enter dabao: ")
    # return

    def __init__(self, user_name):
        self.username = user_name
        self.query_pd = Data_queries(f"personal_details_{user_name}", "BANKING")
        self.query_ad = Data_queries(f"account_details_{user_name}", "BANKING")
        self.query_bd = Data_queries(f"Benifeciary_{user_name}", "BANKING")
        self.query_reg = Data_queries("Registeration", " BANKING")
        self.view_schema = Output_schema()

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


obj = login('6264672891')
obj.show_personal_details()
print("")
obj.show_account_details()
print("")
obj.show_list_of_beneficiary()
