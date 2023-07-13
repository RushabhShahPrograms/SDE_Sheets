'''
Problem Statement: Find lcm of two numbers.

Examples:

Example 1:
Input: num1 = 4,num2 = 8
Output: 8


Example 2:
Input: num1 = 3,num2 = 6
Output: 6
'''

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
g = gcd(a,b)
lcm = (a*b)/g
print("The LCM of two numbers is",int(lcm))