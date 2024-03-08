'''
Write a program that can reverse words of a given string.
Eg if the input is Hello how are you
Output should be you are how Hello
'''

def reverse_words(string):
    words = string.split(' ')
    reversed_words = ' '.join(reversed(words))
    return reversed_words

print(reverse_words("Hello how are you"))