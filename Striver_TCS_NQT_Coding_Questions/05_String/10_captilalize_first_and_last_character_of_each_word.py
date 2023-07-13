'''
Problem Statement: Given a string, write a program to Capitalize the first and last character of each word of that string.

Examples:

Example 1:
Input: String str = "take u forward is awesome"
Output: “TakE U ForwarD IS AwesomE”
Explanation: We get the result after capitalizing the first and last character of each word of a string

Example 2:
Input: String str = "Take u Forward is Awesome"
Output: “TakE U ForwarD IS AwesomE”
Explanation: Characters T, F, A are initially in uppercase , so they remain as they are in the result.
'''

def capitalize(str):
    str = str.split()
    for i in range(len(str)):
        str[i] = str[i][0].upper() + str[i][1:-1] + str[i][-1].upper()
    return ' '.join(str)

str = "take u forward is awesome"
print("String after capitalizing the first and last letter of each word of the string:")
print(capitalize(str))