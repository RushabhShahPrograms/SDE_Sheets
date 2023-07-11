'''
Problem Statement: Given a range of numbers, find all the palindrome numbers in the range.

Note: A palindromic number is a number that remains the same when its digits are reversed.OR  a palindrome is a number that reads the same forward and backward Eg: 121,1221, 2552

Examples:

Example 1:
Input: min = 10 , max = 50
Output: 11 22 33 44 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.

Example2:
Input: min = 100 , max = 150
Output: 101 111 121 131 141 
Explanation: 11, 22, 33, 44 will remain the same when they read from forward or backward.
'''

def isPalindrome(n):
    reverse = 0
    temp = n
    while temp > 0:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
    if n == reverse:
        return True
    return False

min = 100
max = 150
for i in range(min, max+1):
    if isPalindrome(i):
        print(i, end=" ")
