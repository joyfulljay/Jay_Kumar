from constraints import *
import datetime as dt
from mysqlconnector import *


def feedback(rating, comment, login_timestamp):
    logout_time = dt.datetime.now()
    con = mySQLcon("BANKING")
    con.run_query(
        f"""insert into feedback (Login_timestamp, Logout_timestamp, Rating, Additional_Comments) values("{login_timestamp}", "{logout_time}", {rating},"{comment}")""")
    if rating == 5:
        print("Thank you for your valuable feedback")
    elif rating == 4:
        print("Thank you for your valuable feedback. We would serve you better next time.")
    elif rating == 3:
        print("Thank you for your valuable feedback. We would serve you better next time.")
    elif rating == 2:
        print(
            "Thank you for your valuable feedback. Our service team is constantly working for betterment of user experience.")
    elif rating == 1:
        print("Thank you for your valuable feedback. We will look into the issue and serve you better next time.")
    else:
        print("Thank you for your valuable feedback. We will look into the issue and serve you better next time.")


def logout(login_timestamp):
    rating = input("Hey! How did we serve. Please Rate us on 0 to 5 :")
    cons = constraints()
    if cons.integer(rating):
        if cons.range(rating, 0, 9):
            comment = input("Additional Comments: ")
            if len(comment) == 0:
                comment = "No Valuable Comments"
            feedback(rating, comment, login_timestamp)
    print("{:-^100}".format("logout"))


def exitpage():
    print("{:-^100}".format("Thank you for visiting"))
