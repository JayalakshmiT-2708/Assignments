numbers=input('Enter a set of integers:')
numbers=[int(num)for num in numbers.split()]
even_sum=0
odd_sum=0
for num in numbers:
    if num%2==0:
        even_sum+=num
    else:
        odd_sum+=num
print('Sum of even numbers:',even_sum)
print('Sum of odd numbers:',odd_sum)