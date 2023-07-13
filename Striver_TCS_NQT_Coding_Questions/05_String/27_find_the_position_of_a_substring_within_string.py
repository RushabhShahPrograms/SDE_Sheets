'''
Problem statement: “Given two strings text and pattern find the first occurrence of str1 in str2 if found print it’s index if not found print -1.”

Examples:

Example 1:
Input: str1 = "takeuforward"
       str2 = “forward”
Output: 5
Explanation: "Forward" is present in the 5th index in "takeuforward"

Example 2:
Input: str1 = “hello”
       str2 = “az”
Output: -1
Explanation: "az" is not a substring of "hello"
'''

text = "takeuforward"
pattern = "forward"

foundIdx = text.find(pattern)

print("The substring starts from the index: ", foundIdx)