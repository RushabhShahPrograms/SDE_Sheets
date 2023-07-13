'''
Problem Statement: Given a string, return the character that occurs the maximum number of times in the string. If the maximum occurrence of two or more characters is the same, return any one of them. 

Examples:

Example 1:
Input: str = “takeuforward”
Output: a
Explanation: The character 'a' and 'r’ have the same  maximum occurrence i.e 2. Hence we can print any one of them

Example 2:
Input: str = “apple”
Output: p
Explanation: The character 'p' have the maximum occurrence i.e 2.
'''

def maxOccuringChar(str):
    ans = str[0]
    curr_freq = max_freq = 0
    n = len(str)
    for i in range(n):
        if str[i] == str[i-1]:
            curr_freq += 1
        else:
            if max_freq < curr_freq:
                max_freq = curr_freq
                ans = str[i-1]
            curr_freq = 0
    
    if max_freq < curr_freq:
        max_freq = curr_freq
        ans = str[i-1]

    return ans

#Driver Code
str = "apple"
str = ''.join(sorted(str))
print("Maximum Occuring Character is",maxOccuringChar(str))