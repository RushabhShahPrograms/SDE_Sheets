'''
Problem Statement: Given a character, Find the ASCII value of the character.

Examples:

Example 1:
Input: c = ‘A’
Output: 65
Explanation: ASCII value of A is 65

Example 2:
Input: c = ‘e’
Output: 101
Explanation: ASCII value of e is 101
'''

c = input("Enter a character to find ASCII value of it: ")
print("The ASCII value of",c,"is",ord(c))