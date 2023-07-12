'''
Problem Statement: Given a and b, find prime numbers in a given range [a,b], (a and b are included here).

Examples:

Examples:
Input: 2 10
Output: 2 3 5 7 
Explanation: Prime Numbers b/w 2 and 10 are 2,3,5 and 7.

Example 2:
Input: 10 16
Output: 11 13 
Explanation: Prime Numbers b/w 10 and 16 are 11 and 13.
'''
import math

def checkprime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def PrintPrimesbwrange(a, b):
    for i in range(a, b+1):
        if checkprime(i):
            print(i, end=" ")

a = 11
b = 17
PrintPrimesbwrange(a, b)
