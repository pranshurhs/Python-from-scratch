#excercise 6 solutions 
#this variant only works in VS code and other compilers, not in the hackerrank compiler
def is_leap(year):         
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    elif year % 4 != 0:
        return False 
    else:
        return False
year = int(input('enter a year of your choice  '))
0 <= year <= 10 ** 5
print(is_leap(year))
