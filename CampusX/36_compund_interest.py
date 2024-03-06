'''
Write a program to find the compound interest
'''

def compound_interest(P,r,n,t):
    A = P *(1 + r/n)**(n*t)
    return A

P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in decimal): "))
n = int(input("Enter the number of times that interest is compounded per year: "))
t = int(input("Enter the number of years the money is invested for: "))

A = compound_interest(P, r, n, t)

print(f"The amount of money accumulated after {t} years is {A}")