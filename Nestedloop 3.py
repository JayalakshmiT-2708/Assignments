# Pattern a
n = 5
num = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
        if num > i:
            num = 1
    print()



# pattern b
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()