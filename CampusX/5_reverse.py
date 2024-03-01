'''
Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
'''

num = int(input("Enter a four-digit number: "))

reversed_str = str(num)[::-1]
reversed_num = int(reversed_str)

if reversed_num == num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")

print(f"Reversed Number: {reversed_num}")
