'''
Write a program that can multiply 2 numbers provided by the user without using the * operator
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = 0

for _ in range(abs(num2)):
    result += abs(num1)

if (num1<0 and num2>0) or (num1>0 and num2<0):
    result  = -result

print(f"The product of {num1} and {num2} is {result}")