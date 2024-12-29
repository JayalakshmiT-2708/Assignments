class Student:
    def __init__(self, roll_number, name, college, department):
        self.roll_number = roll_number
        self.name = name
        self.college = college
        self.department = department

    def print_details(self):
        print(f"Student Details:")
        print(f"Roll Number: {self.roll_number}")
        print(f"Name: {self.name}")
        print(f"College: {self.college}")
        print(f"Department: {self.department}")
student1 = Student(101, "John Doe", "ABC University", "Computer Science")
student1.print_details()