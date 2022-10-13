from mysqlconnector import *

d = mySQLcon("BANKING")
feedback = "create table feedback (session_id int AUTO_INCREMENT PRIMARY KEY, Login_timestamp datetime NOT NULL, Logout_timestamp datetime NOT NULL, Rating int NOT NULL, Additional_Comments varchar(100) NOT NULL)"
feedback_row1_manual_input = """insert into feedback (session_id, Login_timestamp, Logout_timestamp, Rating, Additional_Comments) values(100001,now(),now(),4,"Good night")"""
global_transactions = """create table global_transactions (transaction_id varchar(20) PRIMARY KEY,transaction_time_stamp datetime not null default now(),Transaction_type enum("Debit","Credit"),Transaction_status enum("Succes","Failed"),Ammount bigint not null)"""
Registeration = """create table Registeration (Account_no BIGINT PRIMARY KEY AUTO_INCREMENT, First_name varchar(20) NOT NULL,Last_name varchar(20) NOT NULL, D_O_B DATE NOT NULL,Permanent_address_pincode BIGINT NOT NULL,Current_address_pincode BIGINT NOT NULL,Aadhar_card BIGINT NOT NULL,Mobile_no BIGINT NOT NULL,Email VARCHAR(20) NOT NULL, Pan_card VARCHAR(10))"""
set_initial_account_no = "ALTER TABLE Registeration AUTO_INCREMENT=12092022111111"
login_details = "CREATE TABLE Login_Details (Login_Username BIGINT NOT NULL PRIMARY KEY, Password VARCHAR(50) NOT NULL, Secret_Q1 VARCHAR(50) NOT NULL, Secret_Q2 VARCHAR(50) NOT NULL,Secret_Q3 VARCHAR(50) NOT NULL)"
# What is your first crush name.
# What is the last 4 digits of mobile no. you first learned.
# What is Your favourite movie.
d.run_query()