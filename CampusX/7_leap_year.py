'''
Write a program that will tell whether the given year is a leap year or not.
'''

def leap_year(year):
    if (year%4 == 0) and ((year%100 != 0) or (year%400 == 0)):
        return True
    else:
        return False

try:
    user_input = int(input("Enter a year: "))
    if leap_year(user_input):
        print(f"{user_input} is a leap year.")
    else:
        print(f"{user_input} is not a leap year.")
except ValueError:
    print("Please enter a valid year (integer).")