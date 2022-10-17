from tabulate import tabulate


class Output_schema:

    def table_with_row_wise_input(self, headerlist, values):
        print(tabulate(values, headerlist))

    def table_with_column_wise_input(self, headerlist, *dataattri):
        columns = []
        table = []
        for arg in dataattri:
            columns.append(arg)
        for i in range(len(columns[0])):
            row = []
            for column in columns:
                row.append(column[i])
            table.append(row)
        print(tabulate(table, headerlist))

    def table_with_tupple_list(self, headerlist, data):
        print(tabulate(data, headerlist))
