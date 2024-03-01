'''
Write a program that will tell whether the given number is divisible by 3 & 6.
'''

def is_divisible(number):
    if number % 3 == 0 and number % 6 == 0:
        return f"The number {number} is divisible by both 3 and 6."
    else:
        return f"The number {number} is not divisible by both 3 and 6."

user_input = int(input("Enter a number: "))
result = is_divisible(user_input)
print(result)