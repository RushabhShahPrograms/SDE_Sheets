'''
Problem Statement: Reverse a String. Write a program that reverses a given string (in-place).

Input: HELLO
Output: OLLEH
'''

def reverse_string(str):
    return str[::-1]

str = "HELLO"
print("The reversed string is- ", reverse_string(str))