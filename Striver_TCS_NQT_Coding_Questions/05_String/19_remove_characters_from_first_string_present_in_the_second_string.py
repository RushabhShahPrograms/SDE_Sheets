'''
Problem Statement: Given two strings, write a program to remove characters from the first string which are present in the second string.

Examples:

Example 1:
Input: String str1 = “abcdef”
       String str2 = “cefz”
Output: abd
Explanation: The common characters in both strings are c, e, f.
So after removing these characters from string 1 we get string resulting string as abd.


Example 2:
Input: String str1 = “xyzpw”
       String str2 = “lmno”
Output: xyzpw
Explanation: As there is no common character in both the strings, string 1 remains unchanged.
'''

def solve(str1,str2):
    mp = {}
    ans = ""
    for i in range(len(str2)):
        mp[str2[i]] = 1
    for i in range(len(str1)):
        if not mp.get(str1[i]):
            ans += str1[i]
    return ans

#Driver code
str1 = "abcdef"
str2 = "cefz"
print("Final String 1:",solve(str1,str2))