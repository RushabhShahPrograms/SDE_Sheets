'''
Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not
'''

def count_digits(n):
    return len(str(n))

def is_narcissistic(n):
    l = count_digits(n)
    dup = n
    total_sum = 0
    while dup:
        total_sum += (dup % 10) ** l
        dup //= 10
    return n == total_sum

# Example usage:
user_input = int(input("Enter a 4-digit number: "))
if is_narcissistic(user_input):
    print("Yes, it's a Narcissistic number!")
else:
    print("No, it's not a Narcissistic number.")
