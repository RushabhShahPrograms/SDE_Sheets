'''
Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it 
Eg if the num = 5, den = 15 the answer should be ⅓
Eg if the num = 6, den = 9 the answer should be ⅔
'''

from math import gcd

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

g = gcd(numerator, denominator)

numerator /= g
denominator /= g

print(f"The simplified fraction is {int(numerator)}/{int(denominator)}")