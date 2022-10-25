Jay_Kumar

# **Banking Application**
#### *Project Description*
The project centres on creating a banking application that enables users to open accounts and carry out various banking tasks. It serves as a user interface that enables users to sign up for an account and log in to the programme to carry out the operations. Python is used to write the code, and a mysql connector is used to connect to the mysql database.

The equipment Programming is done with Python 3. Database creation is configuered with MySQL Database. Python and MySQL databases are connected using the Python mysql-connector.

#### *Code description*
The programme begins to run once the user chooses from a menu whether to log in or register. If the user chooses the "Register" option, then the register_user method will get call from registration library. The user can enter personal information and account information in this feature. The user will be sent to the home page once registration is complete and then the user can choose to loogin.
After selecting feild for login run_login() method will be called from login library, which then shows the user various banking application functionalities.

The functions mapping the functionalities are:

    1.) show_personal_details - To display personal details details of user
    2.) show_account_details - To display Account details details of user
    3.) add_beneficiary() - Allows users to add beneficiaries
    4.) edit_personal_details - To update account information
    5.) list_beneficiary() - To list out the beneficiaries
    6.) show_card_details() - To show card details
    7.) add_new_card() - Allows users to register new card
    8.) change_MPIN() - Allows users to change pin of existing cards
    9.) transfer_funds() - To transfer funds to registered benificiaries
    10.) Logout() - Take user feed back and get out of that function to the existing homepage.
    
Validation checks There are validation checks implemented on several variables.
I created the constraint library for different validation checks and use them for different inputs like:-
    
    1.) Enter mobile number
    2.) Enter Aadhar number
    3.) Entering name
    4.) Enter password
    5.) Enter pin_code
    6.) Enter security Answers
    7.) Enter your date of birth
    8.) Enter your email id

#### *Database discription*
   
   I created a database as "BANKING" in that databse I created multiple tables.
    
    Bank Accesible Data:-
     
     1.) Registeration Table :- This is the table which keep record of every details of customer provided at the time of registeration along with time of registeration except password and account balance.
     2.) Login Details:- This table keep records of login details of user/customer. It contains password, user id, security questions.
     3.) Transations:- This table keep records of all transactions that have been performed.
     4.) Feedback:- This Table used to record feedback of each customers login session.
    
    Only User Accesible data:-
     
     1.) personal_details_{username} = This is the individual table for individual user Personal details.
     2.) Account_details_{username} = This is the individual table for individual user Account details.
     3.) Beneficiary_details_{username}  = This is the individual table for individual user Beneficiary details.
     4.) CARD_DETAILS_{username} = This is the individual table for individual user card list.
     
#### *Database and tables initialisation*
     
     All requered database files could be created by running DatabaseCreation.py but you have to edit it for safety purpose I removed excecution part to avoid creating redundacy. 
   
#### *To execute the program*  

     Run the single file homepage.py which is the main file onto which all other files are imported.
     
