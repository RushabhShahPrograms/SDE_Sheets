'''
Write a program that can count the number of words in a given string
'''

def count_words(string):
    words = string.split(' ')
    return len(words)

print(count_words("Hello how are you"))