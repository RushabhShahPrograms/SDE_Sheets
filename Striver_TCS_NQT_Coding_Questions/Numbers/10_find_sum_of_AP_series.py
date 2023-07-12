'''
Problem Statement: Given an A.P. Series, we need to find the sum of the Series.

a = first term of A.P.

d= common Difference of A.P.

n= Number of Terms in  A.P.

Examples:

Example 1:
Input:
n=4
a=2
d=2
Output: 20
Explanation: 2+4+6+8 = 20

Input:
n=8
a=2
d=5
Output: 124
Explanation: -2 +3 + 8 + 13 + 18 + 23 + 28 + 33 = 124
What is A.P. (Arithmetic Progression)?

A.P. is the series of terms having the first term as a and d, common difference. Every next term in the A.P. is greater than the previous term by d units.

Example – 

-2, 3 , 8 , 13 , 18 , 23 , 28 , 33

First term , a = – 2

Common Difference , d=5

Last term , an=33
'''

a = float(input("Enter the value of a: "))
d = float(input("Enter the value of d: "))
n = int(input("Enter the value of n: "))

sum = (n/2.0)*(2.0*a+(n-1)*d)
print("Sum of given AP series is",sum)