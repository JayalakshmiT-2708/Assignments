def fibonacci(n):
    if n <= 0:
        return 0  
    elif n == 1:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  
if __name__ == "__main__":
    n = int(input("Enter the position (n) of the Fibonacci sequence: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")