'''
Problem Statement: Given two strings, check if two strings are anagrams of each other or not.

Examples:

Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.

Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.
'''

def checkAnagrams(str1,str2):
    if len(str1)!= len(str2):
        return False
    
    freq = [0]*26
    for i in range(len(str1)):
        freq[ord(str1[i]) - ord('A')] += 1
    for i in range(len(str2)):
        freq[ord(str2[i]) - ord('A')] -= 1
    for i in range(26):
        if freq[i] != 0:
            return False
    return True

str1 = "ACT"
str2 = "CAT"
if checkAnagrams(str1,str2):
    print("True")
else:
    print("False")