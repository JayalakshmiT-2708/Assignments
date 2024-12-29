num=int(input('Enter an integer:'))
reversed_n=0
while num>0:
    remainder=num%10
    reversed_n=reversed_n*10+remainder
    num=num//10
print('Reveresed number:',reversed_n)