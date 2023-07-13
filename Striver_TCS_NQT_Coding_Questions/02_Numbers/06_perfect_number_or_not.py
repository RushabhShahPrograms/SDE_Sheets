'''
Problem Statement: Perfect Number. Write a program to find whether a number is a perfect number or not.

A perfect number is defined as a number that is the sum of its proper divisors ( all its positive divisors excluding itself). 

Examples:

Example 1:
Input: n=6
Output: 6 is a perfect number

Example 2:
Input: n=15
Output: 15 is not a perfect number

Example 3:
Input: n=28
Output: 28 is a perfect number
Reason:
For 6 and 28 , the sum of their proper divisors (1+2+3) and (1+4+7+14) is equal to the respective numbers and for 15 it is not.
'''

def isPerfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

ex1 = isPerfect(6)
ex2 = isPerfect(15)
ex3 = isPerfect(28)

if ex1 == True:
    print("6 is a perfect number")
else:
    print("6 is not a perfect number")

if ex2 == True:
    print("15 is a perfect number")
else:
    print("15 is not a perfect number")

if ex3 == True:
    print("28 is a perfect number")
else:
    print("28 is not a perfect number")
