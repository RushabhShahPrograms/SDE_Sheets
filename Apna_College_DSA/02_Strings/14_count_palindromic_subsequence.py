'''
Given a string str of length N, you have to find number of palindromic subsequence (need not necessarily be distinct) present in the string str.
Note: You have to return the answer module 109+7;
 

Example 1:

Input: 
Str = "abcd"
Output: 
4
Explanation:
palindromic subsequence are : "a" ,"b", "c" ,"d"
 

Example 2:

Input: 
Str = "aab"
Output: 
4
Explanation:
palindromic subsequence are :"a", "a", "b", "aa"
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function countPs() which takes a string str as input parameter and returns the number of palindromic subsequence.
 

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(N*N)


Constraints:
1<=length of string str <=1000
'''

def countPs(s):
    n = len(s)
    MOD = 10**9 + 7

    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for cl in range(2, n+1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if (s[i] == s[j] and cl == 2):
                dp[i][j] = 2
            elif (s[i] == s[j]):
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]) % MOD

    return dp[0][n - 1]



print(countPs("abcd"))
print(countPs("aab"))