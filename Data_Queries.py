from mysqlconnector import *


class Data_queries:
    def __init__(self, table_name, database): #
        self.table_name = table_name
        self.database = database

    def column(self, column_name):
        con = mySQLcon(self.database)
        column_values = con.dql_query(f"select distinct({column_name}) from {self.table_name}")
        column_values_in_list = [x[0] for x in column_values]
        return column_values_in_list

    def find_non_string_values_1arg(self, column_name, value, column_req):
        con = mySQLcon(self.database)
        column_values = con.dql_query(f"select distinct({column_req}) from {self.table_name} where {column_name} = {value}")
        column_values_in_list = [x[0] for x in column_values]
        return column_values_in_list

    def find_values_1arg(self, column_name, value, column_req):
        con = mySQLcon(self.database)
        if column_req == "*":
            column_values = con.dql_query(
                f"""(select distinct{column_req} from {self.table_name} where {column_name} = "{value}")""")
            column_values_in_list = [x for x in column_values]
            return column_values_in_list
        else:
            column_values = con.dql_query(
                f"""(select distinct({column_req}) from {self.table_name} where {column_name} = "{value}")""")
            column_values_in_list = [x[0] for x in column_values]
            return column_values_in_list

    def find_non_string_values_2arg(self, column1_name, value1, column2_name, value2, column_req):
        con = mySQLcon(self.database)
        if column_req == "*":
            column_values = con.dql_query(
                f"select distinct{column_req} from {self.table_name} where ({column1_name} = {value1}) and ({column2_name} = {value2})")
        else:
            column_values = con.dql_query(
                f"select distinct({column_req}) from {self.table_name} where ({column1_name} = {value1}) and ({column2_name} = {value2})")
        column_values_in_list = [x for x in column_values[0]]
        return column_values_in_list

    def find_values_2arg(self, column1_name, value1, column2_name, value2, column_req):
        con = mySQLcon(self.database)
        if column_req == "*":
            column_values = con.dql_query(
                f"""(select distinct{column_req} from {self.table_name} where ({column1_name} = "{value1}") and ({column2_name} = "{value2}"))""")
        else:
            column_values = con.dql_query(
                f"""(select distinct({column_req}) from {self.table_name} where ({column1_name} = "{value1}") and ({column2_name} = "{value2}"))""")
        column_values_in_list = [x for x in column_values[0]]
        return column_values_in_list

    def find_string_and_nonStringValues_2arg(self, string_column_name, value1, non_string_column_name, value2, column_req):
        con = mySQLcon(self.database)
        if column_req == "*":
            column_values = con.dql_query(
                f"""(select distinct{column_req} from {self.table_name} where ({string_column_name} = "{value1}") and ({non_string_column_name} = {value2}))""")
        else:
            column_values = con.dql_query(
                f"""(select distinct({column_req}) from {self.table_name} where ({string_column_name} = "{value1}") 
                and ({non_string_column_name} = {value2}))""")

        column_values_in_list = [x for x in column_values[0]]
        return column_values_in_list
