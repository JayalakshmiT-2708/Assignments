def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return"Error!Division by zero is not allowed."
    else:
        return x/y
operators={'+':add,'-':sub,'*':mul,'/':div}
num1=float(input('Enter the 1st number:'))
operator=input('Enter the operator:')
num2=float(input('Enter the 2nd number:'))
if operator in operators:
    print(f'{num1}{operator}{num2}={operators[operator](num1,num2)}')
else:
    print('Invalid operator.')