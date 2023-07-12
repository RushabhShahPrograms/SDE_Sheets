'''
Problem Statement: Adding two fractional numbers.

Examples:

Example 1:
Input: 3/4 + 1/7 
Output: 25/28
Explanation: Since 3/4 + 1/7 = 25/28

Example 2:
Input: 5/2 +1/2
Output: 3/1
Explanation: Since 5/2 + 1/2 = 3/1
'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def simple(num3, den3):
    gcd_val = gcd(num3, den3)
    #dividing num and den by gcd to get the fraction
    #in the simplest form.
    num3 //= gcd_val
    den3 //= gcd_val

num1 = 3
den1 = 4
num2 = 1
den2 = 7
num3 = 0
den3 = 0

lcm = (den1 * den2) // gcd(den1, den2)
#answer's denominator will be lcm of den1 and den2
den3 = lcm
#changing numerators to have same denominator and then adding
num3 = num1 * (den3 // den1) + num2 * (den3 // den2)
simple(num3, den3)
print(f"{num1}/{den1} + {num2}/{den2} = {num3}/{den3}")