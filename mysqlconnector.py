import mysql.connector as mysql
from myconf import *


class mySQLcon:
    def __init__(self, db):
        """
        Constructor is created to take database as an argument,
        And initialise some object variables.
        :param db:
        """
        self.checkcur = False
        self.new_curser = None
        self.mydb = None
        self.checkcon = False
        self.database = db

    def dql_query(self, query):
        """
        This function do several tasks at a time:-
        1.) create connection and create new cursor
        2.) Execute the query and retrieve data from given database
        3.) close cursor
        4.) close connection
        :param query:
        :return:
        """
        self.connect_server()
        out_put = self.row_from_queries(query)
        self.Commit()
        self.close_curser()
        self.close_connection()
        return out_put

    def run_query(self, query):
        """
        This function do several tasks at a time:-
        1.) create connection and create new cursor
        2.) Execute the query (DDl, DML or TCL queries)
        3.) close cursor
        4.) close connection
        :param query:
        :return:
        """
        self.connect_server()
        self.Exec(query)
        self.Commit()
        self.close_curser()
        self.close_connection()

    def connect_server(self):
        """
        Connecting to the sql server and creating a new cursor for the given data in myconf.py file
        :return:
        """
        if self.checkcon:
            print("Connection already created ")
        else:
            self.mydb = mysql.Connect(host=host, user=user, password=password, database=self.database)
            self.mydb.autocommit = False
            self.checkcon = True
            # print("Great! Your Connection is Done")
            self.new_curser = self.mydb.cursor()
            self.checkcur = True
            # print("New cursor created")

    def connect_server_manually(self):
        """
        Connecting to the sql server and creating a new cursor by entering the server details manually
        :return:
        """
        host = input("Enter the name of host: ")
        user = input("Enter the user name: ")
        password = input("Enter your connection Password :")
        database = input("Enter your database :")
        try:
            self.mydb = mysql.Connect(host=host, user=user, password=password, database=database)
            self.mydb.autocommit = False
            print("Great! Your Connection is Done")
            self.new_curser = self.mydb.cursor()
            print("new cursor created")
            self.checkcon = True
            self.checkcur = True
        except Exception as e:
            print("error", e)

    def new_cursor(self):
        """
        Creating a new cursor for the given connection variable
        :return:
        """
        if self.checkcur:
            print("Curser already created")
        else:
            self.new_curser = self.mydb.cursor()
            self.checkcur = True
            print("new cursor created")

    def Exec(self, query):
        """
        Query Execution for (DDL, DML or TCL) queries.
        :param query:
        :return:
        """
        if self.checkcon and self.checkcur:
            self.new_curser.execute(query)
        else:
            print('Seems like you did not have any connection')
            self.mydb.rollback()

    def Commit(self):
        self.mydb.commit()

    def Rollback(self):
        self.mydb.rollback()

    def close_curser(self):
        """
        close the cursor
        :return:
        """
        if self.checkcur:
            self.new_curser.close()
            self.checkcur = False
            # print("Curser is Closed")
        else:
            print("Inactive Cursor")

    def close_connection(self):
        """
        close the connection
        :return:
        """
        if self.checkcon:
            self.mydb.close()
            self.checkcon = False
            # print("Connection is Closed")
        else:
            print("Inactive Connection")

    def row_from_queries(self, query):
        """
        Query for fetching the data from the given database
        :param query:
        :return:
        """
        self.Exec(query)
        return self.new_curser.fetchall()



