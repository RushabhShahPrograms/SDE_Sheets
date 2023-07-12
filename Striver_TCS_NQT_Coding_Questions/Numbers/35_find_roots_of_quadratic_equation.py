'''
Problem Statement: The standard form of a quadratic equation is:

ax2 + bx + c = 0, where a, b and c are real numbers and a != 0

You have given a, b, c of the equation, you have found the roots of the equation.

Examples:

Example 1:
Input: a = 1, b = -3, c = -10
Output: Roots are real and different, i.e(5 , -2).

Example2:

Input: a = 1, b = 1, c = 1
Output: Roots are complex, i.e-(-0.5+i1.732 , -0.5-i1.732).
'''

import cmath

def Roots(a, b, c):
    d = b * b - 4 * a * c
    sqrt_val = cmath.sqrt(abs(d))
 
    if d > 0:
        print("Roots are real and different")
        root1 = (-b + sqrt_val) / (2 * a)
        root2 = (-b - sqrt_val) / (2 * a)
        print(root1)
        print(root2)
    elif d == 0:
        print("Roots are real and same")
        root1 = -(b) / (2 * a)
        root2 = -(b) / (2 * a)
        print(root1)
        print(root2)
    else:
        print("Roots are complex")
        root1 = (-b) / (2 * a) + sqrt_val / (2 * a) * 1j
        root2 = (-b) / (2 * a) - sqrt_val / (2 * a) * 1j
        print(root1)
        print(root2)

a = 1
b = -3
c = -10
Roots(a, b, c)
