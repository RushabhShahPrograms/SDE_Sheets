'''
Problem Statement:  Write a program to sort characters (numbers and punctuation symbols are not included) in a given string.

Examples:

Example 1:
Input: String str = “zxcbg”
Output: bcgxz
Explanation: After sorting we get string as bcgxz

Example 2:
Input: String str = “edcba”
Output: abcde
Explanation: After sorting we get string as abcde
'''

def solve(str):
    return ''.join(sorted(str))

str = "zxcbg"
print("String after sorting:")
print(solve(str))
