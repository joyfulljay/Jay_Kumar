class mandatory:

    def is_mandatory(self, user_response, arg):
        if len(user_response) == 0:
            if arg:
                print("This field is mandatory please enter a valid input.")
                return False
            else:
                return True
        else:
            return True
