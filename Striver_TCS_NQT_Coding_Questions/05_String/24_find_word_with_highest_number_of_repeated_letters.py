'''
Problem Statement: Write a program to find a word in a given string that has the highest number of repeated letters. If not found, return -1.

Examples:

Example 1:
Input: string=”abcdefghij google microsoft”
Output: google
Explanation: In “google” g appears 2 times, o appears 2 times which is highest among all words

Example 2:
Input: string = “cameron blue”
Output: -1
Explanation: No word has more than 1 letter.
'''

class Solution:
    def HighestRepeatedLetters(self, str):
        lent = len(str)
        maximumword = 0
        curr_maximumword = 0
        result = ""

        left = 0
        while left < lent:
            right = left + 1
            while right < lent and str[right] != ' ':
                right += 1

            frequency = [0] * 26
            curr_maximumword = 0

            for index in range(left, right):
                frequency[ord(str[index]) - ord('a')] += 1

            for index in range(26):
                if frequency[index] > 1:
                    curr_maximumword += 1

            if curr_maximumword > maximumword:
                maximumword = curr_maximumword
                result = str[left:right]

            left = right + 1

        if not result:
            print("-1")
        else:
            print("Word with highest number of repeated letters : ", result)

str = "abcdefg google microsoft"
obj = Solution()
obj.HighestRepeatedLetters(str)
