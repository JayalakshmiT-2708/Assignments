class ArithmeticOperations:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        else:
            return a / b
    def display_result(self, operation, a, b):
        if operation == "add":
            print(f"The result of {a} + {b} = {self.add(a, b)}")
        elif operation == "subtract":
            print(f"The result of {a} - {b} = {self.subtract(a, b)}")
        elif operation == "multiply":
            print(f"The result of {a} * {b} = {self.multiply(a, b)}")
        elif operation == "divide":
            print(f"The result of {a} / {b} = {self.divide(a, b)}")
        else:
            print("Invalid operation!")
if __name__ == "__main__":
    calc = ArithmeticOperations()
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    calc.display_result(operation, num1, num2)