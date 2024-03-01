'''
Write a program that will give you the sum of 3 digits
'''

n = input("Enter a three-digit number: ")
n = int(n)

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10

sum_of_digits = d1 + d2 + n
print("Sum of digits of the number:", sum_of_digits)