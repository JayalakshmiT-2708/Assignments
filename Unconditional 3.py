i=1
while True:
    j=1
    while True:
        if i==1:
            print(f'{i}' if j==1 else f'{i}{j}')
        elif i==2 and j==1:
            print(f'{i}{j}')
        elif i==3:
            print(f'{i}{j}')
        j+=1
        if j>3:
            break
    i+=1
    if i>3:
       break