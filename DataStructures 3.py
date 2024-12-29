sampleList=[10,13,12,11,16]
sampleListElement=[]
n=int(input("Enter the number of elements of a list:"))
for i in range(n):
    sampleListElement.append(int(input('Enter the elements:')))
print(sampleListElement)
common_ele=set(sampleList).intersection(set(sampleListElement))
print(common_ele)