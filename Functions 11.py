nums = [1, 2, 3, 4, 5, 6] 
doubled_sum = sum(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))

print(f"The sum of doubled even numbers is: {doubled_sum}")