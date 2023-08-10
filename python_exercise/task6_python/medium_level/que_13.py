'''Create a login page backend to ask users to enter the username and password. Make sure to ask for
a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be
more than 3 times.
'''
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_database = {
        "lakshita": "laksh@123",
        "nav": "12345",
        "harsh": "123456"
    }
    if username in user_database:
        
        retry_count = 0
        while retry_count < 3:
            if user_database[username] == password:
                print("Login successful!")
                break
            else:
                retry_count += 1
                print("Incorrect password. Please try again.")
                password = input("Enter your password: ")
        else:
            print("Too many incorrect attempts. Login failed.")
    else:
        print("Username not found in the database.")


login()
