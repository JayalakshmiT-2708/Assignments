class Employee:
    def __init__(self, emp_id, name, salary_per_day):
        self.emp_id = emp_id
        self.name = name
        self.salary_per_day = salary_per_day

    def calculate_monthly_salary(self, days_worked):
        return self.salary_per_day * days_worked


class EmployeeDetails(Employee):
    def __init__(self, emp_id, name, salary_per_day, leaves, marital_status):
        super().__init__(emp_id, name, salary_per_day)
        self.leaves = leaves
        self.marital_status = marital_status

    def calculate_final_salary(self, days_worked):
        basic_salary = self.calculate_monthly_salary(days_worked)
        if self.marital_status == 'Married':
            basic_salary *= 1.05
        
        return basic_salary


class Employee1(EmployeeDetails):
    def __init__(self, emp_id, name, salary_per_day, leaves, marital_status):
        super().__init__(emp_id, name, salary_per_day, leaves, marital_status)

class Employee2(EmployeeDetails):
    def __init__(self, emp_id, name, salary_per_day, leaves, marital_status):
        super().__init__(emp_id, name, salary_per_day, leaves, marital_status)

class Employee3(EmployeeDetails):
    def __init__(self, emp_id, name, salary_per_day, leaves, marital_status):
        super().__init__(emp_id, name, salary_per_day, leaves, marital_status)
employee1 = Employee1(101, "Alice", 200, 2, "Married")
employee2 = Employee2(102, "Bob", 250, 3, "Single")
employee3 = Employee3(103, "Charlie", 300, 5, "Married")
days_worked = 30 - 2
print(f"Employee ID: {employee1.emp_id}, Name: {employee1.name}, Total Salary: ${employee1.calculate_final_salary(days_worked):.2f}")
print(f"Employee ID: {employee2.emp_id}, Name: {employee2.name}, Total Salary: ${employee2.calculate_final_salary(days_worked):.2f}")
print(f"Employee ID: {employee3.emp_id}, Name: {employee3.name}, Total Salary: ${employee3.calculate_final_salary(days_worked):.2f}")