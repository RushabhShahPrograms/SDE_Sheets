'''
Write a program that can check whether a given string is palindrome or not
'''

def is_palindrome(string):
    string = string.replace(" ","").lower()
    return string == string[::-1]

print(is_palindrome("Able was I ere I saw Elba"))