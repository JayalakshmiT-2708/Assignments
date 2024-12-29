num=int(input('Enter an integer:'))
reversed_n=0
for digit in str(num)[::-1]:
    reversed_n=int(digit)+reversed_n*10
print('Reversed number:',reversed_n)