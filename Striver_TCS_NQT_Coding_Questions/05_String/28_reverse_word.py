'''
Problem Statement: Given a string s, reverse the words of the string.

Examples:

Example 1:
Input: s=”this is an amazing program”
Output: “program amazing an is this”

Example 2:
Input: s=”This is decent”
Output: “decent is This”
'''

def result(s):
    words = s.split()
    words = list(reversed(words))
    return " ".join(words)

st = "TUF is great for interview preparation"
print("Before reversing words: ",st)
print("After reversing words: ",result(st))