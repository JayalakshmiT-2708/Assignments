numbers=[]
i=0
while True:
    num=int(input('Enter the integer:'))
    numbers.append(num)
    print(f'Number{i+1}:{num}')
    if num==11 or i==9:
        break
    i+=1
print('List of numbers:',numbers)