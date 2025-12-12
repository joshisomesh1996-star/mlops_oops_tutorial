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
                           5. Press any other key to exit
                           
                           Your choice: """)
        if user_input == '1':
            self.login()  
        elif user_input == '2':
            self.signup()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.send_msg()
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
            print("No user found. Please sign up.")
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

    def write_post(self):
        if self.loggedin:
            post_content = input("Write your post here: ")
            print("Post published successfully!", post_content)
        else:
            print("You need to log in to write a post.")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin:
            friend_name = input("Enter your friend's name: ")
            message = input("Enter your message: ")
            print(f"Message sent to {friend_name}: {message}")
        else:
            print("You need to log in to send messages.")
        print("\n")
        self.menu()

#obj = Chatbook() 