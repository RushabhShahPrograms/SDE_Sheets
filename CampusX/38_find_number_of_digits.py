'''
Take a number from the user and find the number of digits in it
'''

num = int(input("Enter a number: "))
num_digits = len(str(abs(num)))
print(f"The number {num} has {num_digits} digits")