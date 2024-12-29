class Employee:
    def __init__(self, emp_id, first_name, last_name, year_of_birth, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.salary = salary

class EmployeeDetails(Employee):
    def __init__(self, emp_id, first_name, last_name, year_of_birth, salary):
        super().__init__(emp_id, first_name, last_name, year_of_birth, salary)

    def calculate_annual_salary_and_age(self, current_year):
        age = current_year - self.year_of_birth
        annual_salary = self.salary * 12
        return age, annual_salary

    def display_details(self, current_year):
        age, annual_salary = self.calculate_annual_salary_and_age(current_year)
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Employee ID: {self.emp_id}")
        print(f"Full Name: {full_name}")
        print(f"Age: {age} years")
        print(f"Annual Salary: ${annual_salary}")
emp_id = 101
first_name = "John"
last_name = "Doe"
year_of_birth = 1990
salary = 5000  
employee = EmployeeDetails(emp_id, first_name, last_name, year_of_birth, salary)
employee.display_details(2024)