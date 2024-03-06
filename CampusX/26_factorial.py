'''
Write a program that can find the factorial of a given number provided by the user.
'''
def factorial(n):
    if n==0:
        return 1
    
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number: "))
fact = factorial(n)
print("The factorial is: ",fact)