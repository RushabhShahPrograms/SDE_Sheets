'''
Problem Statement: Given a geometric Progression (G.P) sequence with some inputs as:-

a, first term
r, common ratio
n, number of terms
 Write a program to find the sum of the geometric Progression Series.

Examples:

Example 1:
Input: a=1 , r=0.5 , n=3
Output: 1.75
Explanation: The sum of given GP Series is 1.75

Example 2:
Input: a=3 , r=5 , n=2
Output: 18
Explanation: The sum of the given GP Series is 18
'''
import math
def sumOfGP(a,r,n):
    sum = a*(math.pow(r,n)-1)/(r-1)
    return sum

#Driver code
a = float(input("Enter the value of a: "))
r = float(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))
sumGP = sumOfGP(a,r,n)
print("Sum of GP Series is",sumGP)