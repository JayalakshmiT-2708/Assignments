class Login:
    def __init__(self):
        self.username = None
        self.password = None
    def input_details(self):
        self.username = input("Enter Username: ")
        self.password = input("Enter Password: ")
    def validate_details(self):
        if self.username == "admin" and self.password == "password123":
            return True
        else:
            return False
    def display_details(self):
        print(f"Username: {self.username}")
        print("Password: ****")  
if __name__ == "__main__":
    user1 = Login()
    user2 = Login()
    print("User 1 Login:")
    user1.input_details()
    print("User 2 Login:")
    user2.input_details()
    if user1.validate_details():
        print("\nUser 1 Validation Successful!")
        user1.display_details()
    else:
        print("\nUser 1 Validation Failed!")

    if user2.validate_details():
        print("\nUser 2 Validation Successful!")
        user2.display_details()
    else:
        print("\nUser 2 Validation Failed!")