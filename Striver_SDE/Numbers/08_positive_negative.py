'''
Problem statement: Given a number n check whether it’s positive or negative.

Examples:

Example 1:
Input: n=5
Output: Positive

Example2:
Input: n=-6
Output: Negative
'''

n = int(input("Enter the number: "))
if(n>0):
    print(n,"is positive")
else:
    print(n,"is negative")