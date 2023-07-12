'''
Problem Statement: Given three numbers. Find the greatest of three numbers.

Examples:

Example 1:
Input: 1 3 5
Output: 5
Explanation: Answer is 5.Since 5 is greater than 1 and 3.

Example 2:
Input: 1.123  1.124 1.125
Output: 1.125
Explanation: Answer is 1.125. Since 1.125 is greater than 1.123 and 1.124
'''

num1,num2,num3 = map(int,input("Enter the three numbers: ").split())
print("The Greatest number from the three numbers is",max(num1,num2,num3))