'''
Problem:  Given a string, print non-repeating characters of the string.

Examples:

Example 1:
Input: string = “google”
Output: l,e

Explanation: Non repeating characters are l,e.

Example 2:
Input: string = “yahoo”
Output: y,a,h
Explanation: Non repeating characters are y,a,h
'''

class Solution:
    def nonRepeating(self,st,freq):
        l = len(st)
        for i in range(l):
            if st[i] == ' ':
                continue
            else:
                freq[ord(st[i]) - ord('a')] += 1
        
        for i in range(l):
            if freq[ord(st[i]) - ord('a')] == 1 and st[i] != ' ':
                print(st[i],end=" ")
            
#Driver Code
st= "google"
l = len(st)
freq = [0]*200

obj = Solution()
print("Non-Repeating characters: ",end="")
obj.nonRepeating(st,freq)