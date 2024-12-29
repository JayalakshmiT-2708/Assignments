numbers=[]
numinput=int(input('Enter the integers:'))
for i in range(numinput):
    num=int(input('Enter integer:'))
    numbers.append(num)
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
    elif num<smallest:
        smallest=num
print('Largest number:',largest)
print('Smallest number:',smallest)