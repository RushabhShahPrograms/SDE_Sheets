'''
Problem Statement: Given a String, write a program to remove vowels from a given String.

Examples:

Example 1:
Input: Str = “take u forward”
Output: tk  frwrd
Explanation: All vowels are removed from the given String.

Example 2:
Input: Str = “I am very happy today”
Output:  m vry happy tdy
Explanation: All vowels are removed from the given String.
'''

str = input("Enter the string: ")
vowels = "AEIOUaeiou"
for i in str:
    if i in vowels:
        str = str.replace(i, "")
print(str)