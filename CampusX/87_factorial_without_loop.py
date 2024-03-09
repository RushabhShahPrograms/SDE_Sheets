'''
Write a function that accepts a number and returns it’s factorial. You can not use any loop
'''

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))