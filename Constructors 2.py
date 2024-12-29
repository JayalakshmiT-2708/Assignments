class Employee:
    def __init__(self, emp_id, emp_name, salary, experience):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
        self.experience = experience

    @staticmethod
    def calculate_salary(salary, experience):
        if experience < 2:
            return salary
        elif 2 <= experience <= 5:
            return salary * 1.5
        else:
            return salary * 2

    def print_details(self):
        updated_salary = Employee.calculate_salary(self.salary, self.experience)
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Updated Salary: {updated_salary}")

emp1 = Employee(101, "Alice", 50000, 3)
emp2 = Employee(102, "Bob", 40000, 1)
emp3 = Employee(103, "Charlie", 60000, 6)
emp1.print_details()
emp2.print_details()
emp3.print_details()