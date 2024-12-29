import math
class MathOperations:
    def __init__(self, numbers, number):
        self.numbers = numbers
        self.number = number

    @staticmethod
    def find_max_min(numbers):
        return max(numbers), min(numbers)

    def calculate_square_root_and_cube(self):
        square_root = math.sqrt(self.number)
        cube = self.number ** 3
        return square_root, cube
numbers = [10, 25, 3, 72, 8]
number = 16
math_operations = MathOperations(numbers, number)
max_num, min_num = MathOperations.find_max_min(numbers)
print(f"Maximum Number: {max_num}, Minimum Number: {min_num}")
square_root, cube = math_operations.calculate_square_root_and_cube()
print(f"Square Root of {number}: {square_root}")
print(f"Cube of {number}: {cube}")