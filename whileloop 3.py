even_sum=0
odd_sum=0
user_input=""
while user_input.lower()!='stop':
    user_input=input('Enter an integer:')
    if user_input.lower()=='stop':
        break
    try:
        num=int(user_input)
        if num%2==0:
            even_sum+=num
        else:
            odd_sum+=num
    except ValueError:
        print('Invalid input.Please enter an integer')
print('Sum of even numbers:',even_sum)
print('Sum of odd numbers:',odd_sum)