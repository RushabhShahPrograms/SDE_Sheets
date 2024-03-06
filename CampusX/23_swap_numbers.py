'''
Write a program that will swap numbers

'''

n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
print(f"Before swapping: num1 = {n1}, num2 = {n2}")

n1,n2 = n2,n1
print(f"After swapping: num1 = {n1}, num2 = {n2}")