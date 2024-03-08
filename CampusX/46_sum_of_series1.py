'''
 Write a program to calculate the sum of the following series till the nth term
1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
n will be provided by the user
'''

import math

def calculate_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i / math.factorial(i)
    return sum

n = int(input("Enter the value of n: "))
print("The sum of the series up to the nth term is:", calculate_series(n))
