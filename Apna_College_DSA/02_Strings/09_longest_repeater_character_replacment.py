'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

def character_replacement(s,k):
    count = [0]*26
    max_count = max_len = start = 0

    for end in range(len(s)):
        count[ord(s[end]) - ord('A')] += 1
        max_count = max(max_count, count[ord(s[end]) - ord('A')])
        if end - start + 1 - max_count > k:
            count[ord(s[start]) - ord('A')] -= 1
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

print(character_replacement("ABAB", 2))  # Output: 4
print(character_replacement("AABABBA", 1))  # Output: 4