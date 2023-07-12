'''
Problem Statement: Given two numbers. Find the greatest of two numbers.

Examples:

Example 1:
Input: 1 3
Output: 3
Explanation: Answer is 3,since 3 is greater than 1.

Input: 1.123  1.124
Output: 1.124
Explanation: Answer is 1.124,since 1.124 is greater than 1.123.
'''

num1,num2 = map(int,input("Enter the two numbers: ").split())
print("The Greatest number from the 2 numbers is",max(num1,num2))