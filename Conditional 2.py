weekdays={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
number=int(input('Enter a number:'))
if number in weekdays:
    print(weekdays[number])
else:
    print('Invalid number.Enter a number between 1 and 7:')