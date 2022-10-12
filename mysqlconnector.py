import mysql.connector as mysql


class mySQLcon:
    def __init__(self, db):
        self.checkcur = False
        self.new_curser = None
        self.mydb = None
        self.checkcon = False
        self.database = db

    def dql_query(self, query):
        self.connect_server()
        out_put = self.row_from_queries(query)
        self.Commit()
        self.close_curser()
        self.close_connection()
        return out_put

    def run_query(self, query):
        self.connect_server()
        self.Exec(query)
        self.Commit()
        self.close_curser()
        self.close_connection()

    def connect_server(self):
        if self.checkcon:
            print("Connection already created ")
        else:
            self.mydb = mysql.Connect(host="localhost", user="root", password="Password@123", database=self.database)
            self.mydb.autocommit = False
            self.checkcon = True
            # print("Great! Your Connection is Done")
            self.new_curser = self.mydb.cursor()
            self.checkcur = True
            # print("New cursor created")

    def connect_server_manually(self):
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
        if self.checkcur:
            print("Curser already created")
        else:
            self.new_curser = self.mydb.cursor()
            self.checkcur = True
            print("new cursor created")

    def Exec(self, query):
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
        if self.checkcur:
            self.new_curser.close()
            self.checkcur = False
            # print("Curser is Closed")
        else:
            print("Inactive Cursor")

    def close_connection(self):
        if self.checkcon:
            self.mydb.close()
            self.checkcon = False
            # print("Connection is Closed")
        else:
            print("Inactive Connection")

    def row_from_queries(self, query):
        self.Exec(query)
        return self.new_curser.fetchall()



