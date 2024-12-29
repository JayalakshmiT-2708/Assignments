class Student:
    def __init__(self, name, department, marks):
        self.name = name
        self.department = department
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


class StudentResult(Student):
    def __init__(self, name, department, marks):
        super().__init__(name, department, marks)

    def display_result(self):
        total_marks = self.calculate_total()
        average_marks = self.calculate_average()
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")
        print("-" * 30)
student1 = StudentResult("Alice", "Computer Science", [85, 90, 88, 92, 78])
student2 = StudentResult("Bob", "Electrical Engineering", [78, 81, 75, 88, 85])
student3 = StudentResult("Charlie", "Mechanical Engineering", [80, 85, 88, 90, 92])
student1.display_result()
student2.display_result()
student3.display_result()