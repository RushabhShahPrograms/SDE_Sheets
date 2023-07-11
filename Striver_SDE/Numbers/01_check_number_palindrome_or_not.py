'''
Problem Statement:  Given a number check if it is a palindrome.

An integer is considered a palindrome when it reads the same backward as forward.

Examples:

Example 1:
Input: N = 123
Output: Not Palindrome Number
Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

Example 2:
Input: N =  121 
Output: Palindrome Number
Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.
'''

def reverse(x):
    y=0
    while x>0:
        digit = x%10
        y = y*10+digit
        x=x//10
    return y

x=121
dummy=x
y=reverse(x)
if dummy == y:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")