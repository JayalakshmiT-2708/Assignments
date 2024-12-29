def calculate_average(*args):
    if len(args)==0:
        return "No numbers provided."
    total=sum(args)
    count=len(args)
    return total/count
print(calculate_average(4,8,15,16,23,42))
print(calculate_average())