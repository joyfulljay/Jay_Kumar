from mysqlconnector import *

d = mySQLcon()
feedback = "create table feedback (session_id int AUTO_INCREMENT PRIMARY KEY, Login_timestamp datetime NOT NULL, Logout_timestamp datetime NOT NULL, Rating int NOT NULL, Additional_Comments varchar(100) NOT NULL)"
feedback_row1_manual_input = """insert into feedback (session_id, Login_timestamp, Logout_timestamp, Rating, Additional_Comments) values(100001,now(),now(),4,"Good night")"""

d.run_query()