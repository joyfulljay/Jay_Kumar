import mysql.connector as mysql


class mySQLcon:
    def __init__(self, ):
        self.new_curser = None
        self.mydb = None
        self.checkcon = False

    def connect_server(self):
        host = input("Enter the name of host: ")
        user = input("Enter the user name: ")
        password = input("Enter your connection Password :")
        database = input("Enter your database :")
        try:
            self.mydb = mysql.Connect(host=host, user=user, password=password, database=database)
            self.mydb.autocommit = False
            print("Great! Your Connection is Done")
            self.checkcon = True
        except ImportError:
            platform_specific_module = None

    def new_cursor(self):
        if self.checkcon:
            self.new_curser = self.mydb.cursor()
            print("new cursor created")
        else:
            print('Seems like you did not have any connection')

    def Exec(self, query):
        if self.checkcon:
            self.new_curser.excecute(query)
        else:
            print('Seems like you did not have any connection')
            self.mydb.rollback()

    def Commit(self):
        self.mydb.commit()

    def Rollback(self):
        self.mydb.rollback()

    def CheckConnection(self):
        if self.mydb.is_connected():
            print("Connected")
        else:
            print("Not Connected")

    def close_curser(self):
        self.new_curser.close()
        print("Curser is Closed")

    def close_connection(self):
        self.mydb.close()
        print("Connection is Closed")

    def row_from_queries(self, query):
        self.Exec(query)
        return self.new_curser.fetchone()


obj1 = mySQLcon()
obj1.connect_server()

