class Student:
    def __init__(self):
        self.rollno = None
        self.name = None
    def set_details(self, rollno, name):
        self.rollno = rollno
        self.name = name
    def input_details(self):
        self.rollno = input("Enter Roll Number: ")
        self.name = input("Enter Name: ")
    def display_details(self):
        print(f"Roll Number: {self.rollno}")
        print(f"Name: {self.name}")
student1 = Student()
student1.set_details(101, "Alice")
print("Details of  set using parameters:")
student1.display_details()
print("\nEnter new details:")
student1.input_details()
print("\nDetails of set using input:")
student1.display_details()