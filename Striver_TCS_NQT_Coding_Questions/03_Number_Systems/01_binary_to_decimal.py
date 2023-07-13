'''
Problem Statement: Convert a binary number to a decimal number.

Examples:

Example 1:
Input: N = 1011
Output: 11
Explanation: 1011 when converted to decimal number is “11”.

Example 2:
Input: 100
Output: 4
Explanation: 100 when converted to decimal number is “4”.
'''
s = input("Enter the binary number: ")
n = len(s)
base,ans = 1,0
for i in range(n-1,-1,-1):
    if s[i] == '1':
        ans += base
    base *= 2
print(ans)