'''
Problem Statement: Write a  program to change the case (lower to upper and upper to lower cases) of each character of a given string.

Examples:

Example 1:
Input: String str = “javA”
Output: JAVa
Explanation:
 Changed the lower case characters to uppercase and vice versa.

Example 2:
Input: String str = “take u forward IS Awesome”
Output: TAKE U FORWARD is aWESOME
Explanation: Changed the lower case characters to uppercase and vice versa.
'''

def solve(str, n):
    for i in range(n):
        ascii = ord(str[i])
        if ascii >= 65 and ascii <= 90:
            str[i] = str[i].lower()
        elif ascii >= 97 and ascii <= 122:
            str[i] = str[i].upper()

    print("Resultant string: ")
    print(str)

str = "take u forward IS Awesome"
n = len(str)
solve(list(str), n)
