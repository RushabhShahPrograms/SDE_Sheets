'''
Problem Statement: Given a string of characters from a to z. Print the duplicate characters(which are occurring more than once) in the given string with their occurrences count.

Examples:

Example 1:
Input:
 str= "sinstriiintng"
Output:
i - 4
n - 3
s - 2
t - 2
Explanation:
In the above example, 's' occurs twice, 'i' occurs four times, 't' occurs twice and 'n' occurs thrice. 'r' and 'g' occur only one time and hence are not considered.

Example 2:
Input:
 str= "abcdefg"
Output:
< -- No Output -- >
Explanation:

In the above example, every character occurs only once(no duplicates), therefore nothing to print.
'''

str = "sinstriiintng"
counts =[0]*26

for i in range(len(str)):
    counts[ord(str[i]) - ord('a')] += 1
for i in range(26):
    if counts[i]>1:
        print(chr(i+ord('a')),"-",counts[i])