'''
Write a program that will tell whether the number entered by the
user is odd or even.
'''
def check(number):
    if number%2 == 0:
        return f"The number {number} is even"
    else:
        return f"The number {number} is odd"

try:
    user_input = int(input("Enter a number: "))
    result = check(user_input)
    print(result)
except ValueError:
    print("Invalid input, please enter a valid integer")