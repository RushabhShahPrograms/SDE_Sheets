'''
Given two strings wild and pattern. Determine if the given two strings can be matched given that, wild string may contain * and ? but string pattern will not. * and ? can be converted to another character according to the following rules:

* --> This character in string wild can be replaced by any sequence of characters, it can also be replaced by an empty string.
? --> This character in string wild can be replaced by any one character.
Example 1:

Input: 
wild = ge*ks
pattern = geeks
Output: Yes
Explanation: Replace the '*' in wild string 
with 'e' to obtain pattern "geeks".
Example 2:

Input: 
wild = ge?ks*
pattern = geeksforgeeks
Output: Yes
Explanation: Replace '?' and '*' in wild string with
'e' and 'forgeeks' respectively to obtain pattern 
"geeksforgeeks"
Your Task:
You don't need to read input or print anything. Your task is to complete the function match() which takes the string wild and pattern as input parameters and returns true if the string wild can be made equal to the string pattern, otherwise, returns false.

Expected Time Complexity: O(length of wild string * length of pattern string)
Expected Auxiliary Space: O(length of wild string * length of pattern string)

Constraints:
1 <= length of the two string <= 10^3 
'''

def match(wild, pattern):
    len1 = len(wild)
    len2 = len(pattern)

    if len1 < len2:
        return False

    lookup = [[False] * (len2 + 1) for _ in range(len1 + 1)]

    lookup[0][0] = True

    for j in range(1, len1 + 1):
        if wild[j - 1] == '*':
            lookup[j][0] = lookup[j - 1][0]

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if wild[i - 1] == '?' or wild[i - 1] == pattern[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]
            elif wild[i - 1] == '*':
                lookup[i][j] = lookup[i - 1][j] or lookup[i][j - 1]

    return lookup[len1][len2]


print(match("ge*ks", "geeks"))
print(match("ge?ks*", "geeksforgeeks"))