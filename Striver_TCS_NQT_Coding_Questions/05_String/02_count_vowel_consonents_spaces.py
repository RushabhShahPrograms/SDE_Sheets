'''
Problem Statement: Given a string, write a program to count the number of vowels, consonants, and spaces in that string.

Examples:

Example 1:
Input: string str=”Take u forward is Awesome”
Output: 
Vowels: 10
Consonants: 11
White spaces: 4


Example 2:
Input: string str=”India won the cricket match”
Output:
Vowels: 8
Consonants: 15
White spaces: 4
'''
def solve(str):
    vowels = consonants = whitespaces = 0
    str = str.lower()
    for i in range(len(str)):
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
            vowels += 1
        elif str[i] >= 'a' and str[i] <= 'z':
            consonants += 1
        elif str[i] == ' ':
            whitespaces += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("White Spaces:", whitespaces)

str = input("Enter the sentence: ")
solve(str)