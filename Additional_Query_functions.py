from Data_Queries import *


class helper_query:
    def __init__(self, database, table_name):
        self.database = database
        self.table_name = table_name
        self.obj = Data_queries(table_name, database)

    def CheckInFunction(self, column_name, value):
        values = self.obj.column(column_name)
        if int(value) in values:
            return True
        else:
            return False

    def password_check(self, to_map_column, to_map_on_value, map_with_column, value_to_be_checked):
        t = True
        try:
            val = self.obj.find_values_2arg(to_map_column, to_map_on_value, map_with_column, value_to_be_checked, "*")
        except:
            t = False

        return t

# obj = helper_query("BANKING", "Login_Details")
# print(obj.password_check("Login_Username", 626424277, "Password", "HelloJay@123"))
