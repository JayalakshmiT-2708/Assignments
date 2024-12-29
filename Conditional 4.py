def grade_marks(marks):
    if 90<=marks<=100:
        return "A+"
    elif 80<=marks<=89:
        return "A"
    elif 60<=marks<=79:
        return "B"
    elif 40<=marks<=59:
        return "C"
    else:
        return "F"
for i in range(1,6):
    marks=float(input('Enter Mathematics marks of Student{i}:'))
    while marks<0 or marks>100:
        print('Invalid marks! Please enter marks between 0 and 100.')
        marks=float(input(f'Enter Mathematics marks of Student{i}:'))
    print(f'Grade of Student{i}:{grade_marks(marks)}')
    print()