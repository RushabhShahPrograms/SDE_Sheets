'''
Problem Statement: Convert decimal to binary number.

Examples:

Example 1:
Input: N = 15
Output: 1111
Explanation: 15 in binary is represented as "1111".

Example 2:
Input: 18
Output: 10010
Explanation: 18 in binary is represented as "10010".
'''

n = int(input("Enter the decimal number: "))
flag = 0
for i in range(32, -1, -1):
    if (n >> i) & 1:
        flag = 1
        print(1, end="")
    else:
        if flag == 1:
            print(0, end="")