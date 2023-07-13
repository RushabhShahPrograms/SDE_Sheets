'''
Problem Statement: You are given an integer. Your task is to replace all the zeros in the integer with ones.

Examples:

Example 1:
Input: N = 102003
Output: 112113
Explanation: The 2nd,4th and 5th position from left contain 0.The resultant integer has replaced the 0’s in those  positions with 1.

Example 2:
Input:  204
Output: 214
Explanation: The 2nd position from left contain 0. The resultant integer has replaced the 0 in that position with 1.
'''

def replaceZerosWithOnes(num):
    if num == 0:
        return 1
    ans = 0
    tmp = 1
    while num > 0:
        d = num % 10
        if d == 0:
            d = 1
        ans = d * tmp + ans
        num //= 10
        tmp *= 10
    return ans

n = 204
result = replaceZerosWithOnes(n)
print(f"After replacing zeros with ones {n} becomes {result}")
