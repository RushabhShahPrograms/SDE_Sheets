'''
Problem Statement: Given a String remove all the duplicate characters from the given String.

Examples:

Example 1:
Input: s = "bcabc"
Output: “bca"

Explanation: Duplicate Characters are removed
Example 2:
Input: s = "cbacdcbc"
Output: "cbad" 
Explanation: Duplicate Characters are removed
'''

def removeDuplicatesLetters(s):
    ans = ""
    map = [False]*26
    for i in range(len(s)):
        if not map[ord(s[i]) - ord('a')]:
            ans += s[i]
            map[ord(s[i]) - ord('a')] = True
    return ans

#Driver Code
str = "cbacdcbc"
print("Original String: ",str)
print("After removing duplicates:",removeDuplicatesLetters(str))