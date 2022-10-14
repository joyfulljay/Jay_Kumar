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

    def map_value(self, to_map_column, to_map_on_value, map_with_column, value_to_be_checked):
        print("will complete later")
