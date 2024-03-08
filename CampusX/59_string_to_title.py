'''
Write a python program to convert a string to title case without using
the title()
'''

def to_title_case(string):
    words = string.split(' ')
    title_case_words = [word[0].upper() + word[1:].lower() for word in words if word]
    return ' '.join(title_case_words)

print(to_title_case("hello world"))