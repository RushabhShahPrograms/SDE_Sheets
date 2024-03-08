'''
Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
'''

def calculate_series(n,x):
    sum=1
    for i in range(2,n+1):
        sum += (x**i)/i
    return sum

n = int(input("Enter the value of n: "))
x = float(input("Enter the value of x: "))
print("The sum of the series up to the nth term is:",calculate_series(n,x))