'''
Write a program that will check whether the number is armstrong number or not.
'''

def is_armstrong(num):
    n_str = str(num)
    n_digits = len(n_str)
    sum_of_powers = sum(int(digit)**n_digits for digit in n_str)
    return sum_of_powers == num

user = int(input("Enter a number: "))
if is_armstrong(user):
    print(f"{user} is an Armstrong number")
else:
    print(f"{user} is not an Armstrong number")