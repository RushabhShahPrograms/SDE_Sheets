'''
Problem: Given a string, calculate the sum of numbers in a string (multiple consecutive digits are considered one number)

Examples:

Example 1:
Input: string = “123xyz”
Output: 123

Example 2:
Input: string = “1xyz23”
Output: 24
'''

class Solution:
    def sum_of_integers(self, st):
        temp_sum = ""
        sum = 0
        for i in st:
            if i >= '0' and i <= '9':
                temp_sum += i
            else:
                sum += int(temp_sum)
                temp_sum = ""
        return sum + int(temp_sum)

st = "1a30z67"
obj = Solution()
print("Sum: ", obj.sum_of_integers(st))