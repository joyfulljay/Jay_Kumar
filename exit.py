from constraints import *
import datetime as dt


def feedback(rating, comment, login_timestamp):
    logout_time = dt.datetime.now() + dt.timedelta(hours=5, minutes=30)


def logout(login_timestamp):
    rating = input("Hey! How did we serve. Please Rate us on 0 to 5 :")
    cons = constraints()
    if cons.integer(rating):
        if cons.range(rating, 0, 9):
            comment = input("Additional Comments: ")
            if len(comment) == 0:
                comment = "No Valuable Comments"
            feedback(rating, comment, login_timestamp)
    print("{:-^100}".format("Thank you for visiting"))


def exitpage():
    print("{:-^100}".format("Thank you for visiting"))
