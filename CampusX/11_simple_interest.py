'''
Write a program to find the simple interest when the value of
principle,rate of interest and time period is given
'''

def calculate_SI(principal,rate,time):
    SI = (principal*rate*time)/100
    return SI

p = float(input("Enter principal amount:"))
r = float(input("Enter the rate of interest:"))
t = float(input("Enter time period:"))

interest = calculate_SI(p,r,t)
print("The simple interest is:",interest)
