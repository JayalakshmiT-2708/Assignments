numbers=[]
num_inputs=int(input('Enter the number of integers:'))
i=0
while i<num_inputs:
    num=int(input('Enter an integer:'))
    numbers.append(num)
    i+=1
largest=numbers[0]
smallest=numbers[0]
i=0
while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    elif numbers[i]<smallest:
        smallest=numbers[i]
    i+=1
print('Largest number:',largest)
print('Smallest number:',smallest)