'''
You are given a string A and you have to find the number of different sub-strings of the string A which are fake palindromes. 

Note: 

1. Palindrome: A string is called a palindrome if you reverse the string yet the order of letters remains the same. For example, MADAM. 

2. Fake Palindrome: A string is called as a fake palindrome if any of its permutations is a palindrome. For example, AAC is fake palindrome, but ACD is not. 

3. Sub-string: A sub-string is a contiguous sequence (non-empty) of characters within a string. 

4. Two sub-strings are considered same if their starting indices and ending indices are equal. 

Input Format: 
First line contains a string S 

Output Format: 
Print a single integer (number of fake palindrome sub-strings). 

Constraints: 
1 <= |S| <= 2 * 105 
The string will contain only Upper case 'A' to 'Z' 

Sample Input 1: 
ABAB 

Sample Output 1: 
7 

Explanation: 
The fake palindrome for the string ABAB are A, B, A, B, ABA, BAB, ABAB. 

Sample Input 2: 
AAA 

Sample output 2: 
6 

Explanation: 
The fake palindrome for the string AAA are A, A, A, AA, AA, AAA 
'''

def countSubstring(s):
    res = 0
    for i in range(len(s)):
        x = 0
        for j in range(i, len(s)):
            if s[j].islower():
                temp = 1 << (ord(s[j]) - ord('a'))
                x ^= temp
                if (x & (x - 1)) == 0:
                    res += 1

    print(res)

str = input()
countSubstring(str)

