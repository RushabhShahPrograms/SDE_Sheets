'''
Problem: Given a String, find the largest word in the string.

Examples:

Example 1:
Input: string s=”Google Doc”
Output: “Google”

Explanation: Google is the largest word in the given string.

Example 2:
Input: string s=”Microsoft Teams”
Output: “Microsoft”
Explanation: Microsoft is the largest word in the given string
'''

def MaxLengthWords(str, maxWord):
    lent = len(str)
    i = 0
    j = 0
    min_length = lent
    max_length = 0
    max_start = 0

    while j <= lent:
        if j < lent and str[j] != ' ':
            j += 1
        else:
            curr_length = j - i

            if curr_length > max_length:
                max_length = curr_length
                max_start = i

            j += 1
            i = j

    maxWord.append(str[max_start:max_start + max_length])

str = "Google Docs"
maxWord = []
MaxLengthWords(str, maxWord)

print("Largest Word is: ", maxWord[0])