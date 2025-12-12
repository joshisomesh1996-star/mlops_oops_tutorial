class Chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()
    
    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
                           1. Press 1 to login
                           2. Press 2 to signup
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        if user_input == '1':
            self.login()  # login functionality to be implemented
        elif user_input == '2':
            self.signup()
        elif user_input == '3':
            pass  # write post functionality to be implemented
        elif user_input == '4':
            pass  # message friend functionality to be implemented
        else:
            print("Exiting Chatbook. Goodbye!")
            exit()     
    
    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("Signup successful!")
        print("\n")
        self.menu()
    
    def login(self):
        if self.username == "" and self.password == "":
            print("No user found. Please sign up first by pressing 1 in main menu.")
            self.menu()
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email == self.username and password == self.password:
                self.loggedin = True
                print("Login successful!")
            else:
                print("Invalid credentials. Please try again.")
            print("\n")
            self.menu()

obj = Chatbook() 