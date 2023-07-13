'''
Problem Statement: Given a string, write a program to change every letter in the given string with the letter following it in the alphabet (ie. a becomes b, p becomes q, z becomes a)

Examples:

Example 1:
Input: string str = “abcdxyz”
Output: bcdeyza

Example 2:
Input: string str = “Java”
Output: Kbwb
'''

def solve(str, length):
    for i in range(length):
        ascii = ord(str[i])
        if ascii == 90:
            str[i] = chr(65)
        elif ascii == 122:
            str[i] = chr(97)
        elif (ascii >= 65 and ascii < 90) or (ascii >= 97 and ascii < 122):
            str[i] = chr(ascii + 1)
    return str

str = "abcdxyz"
length = len(str)
print("Original String:")
print(str)
print("New string:")
print(solve(list(str), length))