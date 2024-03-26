'''
Given a string s, return the longest 
palindromic
 
substring
 in s. 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

def longest_palindrome(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        palindrome = expand_around_center(s,i,i)
        if len(palindrome) > len(longest):
            longest = palindrome
        
        palindrome = expand_around_center(s,i,i+1)

        if len(palindrome) > len(longest):
            longest = palindrome
    return longest

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))